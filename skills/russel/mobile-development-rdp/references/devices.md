# Devices and Android QA

## Reserve the laptop’s emulator

Every cooperating local thread uses the same lock across repositories, worktrees, and accounts running as Russel. Acquire it before any T3 call that might boot or attach an emulator. T3 still owns platform discovery and the device session.

Run the following on the laptop in a dedicated PTY command session. Yield after one second so the session can hold the lock while you use T3. Keep the returned shell session ID until cleanup.

```bash
umask 077
android_state_dir="${HOME}/.local/state/mobile-development-rdp"
mkdir -p "$android_state_dir" &&
  flock -n -E 75 "$android_state_dir/emulator.lock" sh -c '
    printf "%s\n" "Emulator slot reserved. Press Enter to release it."
    IFS= read -r unused
  '
```

- Proceed only after the reservation message. Exit 75 means another session holds the slot. Use a free, authorized USB phone or arrange a handoff. If the reservation command is unavailable, coordinate with the other threads before opening any emulator.
- With the reservation held, use T3 `device_list` to verify the laptop’s live devices and host status. Check for an active owner or handoff. T3’s open list is scoped to this thread, so the system-wide reservation is not proof that a device started outside it is free. If discovery is incomplete, resolve it before booting. If any emulator is already running, keep the count at one. Use the existing emulator only when it is this thread’s session or the user explicitly authorizes a handoff.
- Use T3 `device_open` with the exact host and device ID, then its bound `agent-device` command for interaction. If you switch to USB, confirm the phone is unlocked, authorized for USB debugging, and free, then target that exact device. Keep a working phone from another task in its current state.
- After testing, close your T3 panel session and shut down your emulator when you no longer need it. Keep it open if the user requested a live preview and report that it still occupies the slot. Release the shell lock with Enter when you hand back control. If the holder crashes, the OS releases the lock when its process ends. A remaining lock file does not indicate an active holder. Never delete the lock file to bypass a live reservation.

## Recover a stale device session

Treat `DEVICE_IN_USE` as real contention until you can identify the owner. Compare the host, AVD name, and serial with the active task and recent handoff. A serial can be reused after an emulator restart. A device or thread listing alone cannot prove a binding stale.

Quote the exact device-tool error and follow the supported recovery advice once. For a confirmed stale binding owned by this task, close that session, re-list devices, and acquire a fresh binding. If a clean restart is needed, verify the previous emulator stopped before reopening. Close or reuse another session only when the user explicitly authorizes it. Leave unknown owners alone and continue independent work. If the supported retry fails, report the blocker. Avoid global ADB resets, emulator wipes, and changes to another app’s data.

## Verify the installed build

- Install the exact APK from the intended CI run. Confirm package, version code, signer, and target device. Use a clean install when checking first-run behavior and an in-place upgrade when checking release compatibility. Uninstalling the old version defeats an upgrade check.
- Start the app with Metro stopped for a standalone APK. Test the actual native development build when Expo features depend on native modules. Use the intended backend and an isolated test account. Verify the live HTTPS origin when the release depends on it.
- Where touched, test notification permission denial and recovery, delivery while backgrounded, and tap-to-open. For widgets, pin and resize on the launcher, check background refresh with the app closed, and check the destination. Inspect Android system surfaces with T3 screenshots when an app snapshot misses the prompt.
- Capture before and after on the same screen, state, theme, and device when visual evidence is requested. Report emulator, phone, and cloud CI coverage by what each actually exercised.
