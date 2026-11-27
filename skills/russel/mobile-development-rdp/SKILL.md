---
name: mobile-development-rdp
description: Use for Android app work in Kotlin, Java, Expo, or React Native, including APK and EAS builds, emulator or USB testing, and skipped or failed Android releases.
---

# Mobile development RDP

## When to use it

Apply this from the project context or the request. The user can invoke `$mobile-development-rdp` or ask in their own words.

- “Fix this Android screen” or “add this to my Expo app.”
- “Build me an APK,” “run my EAS build,” or “test this on my phone.”
- “Open the emulator” or “the device says `DEVICE_IN_USE`.”
- “The Android release skipped,” “retry this tag,” or “publish the APK for this version.”

Read [Devices and Android QA](references/devices.md) before reserving or opening a device. Read [Release and recovery](references/releases.md) before tagging, dispatching, or retrying a release. A request to install or preview a build uses the existing CI artifact when it matches the intended commit.

## Build through CI

Use GitHub Actions for every Android build, including debug, preview, and release builds. For Expo, GitHub Actions submits the build to remote EAS. Keep the laptop for editing, installing CI artifacts, and device testing. A failed or unavailable cloud build stays blocked until its cause is fixed. Local Gradle, Android Studio builds, `expo run:android`, and `eas build --local` are outside this workflow.

- Identify the repository, app or variant, package name, and source commit. Read the existing CI and app configuration before choosing a build path.
- For Kotlin, Java, and bare React Native, run the repo’s Gradle wrapper on a GitHub Actions runner with the repo’s Java and Android tooling versions. Run the relevant tests and lint there. A bare React Native APK intended for handoff bundles its JavaScript and must open with Metro stopped.
- For Expo, use the linked EAS project, the app’s Android APK profile, and the authorized Actions credential. Use an EAS development build to test custom native modules. Use a standalone signed APK for release verification.
- For an APK or preview, hand back an Actions artifact or use the project’s existing private preview channel.

## Use a device

Reserve the laptop’s single emulator slot across projects before calling the T3 tool that can boot it. If a device is busy, arrange a handoff or use an available authorized phone. Keep working on CI or code while device testing waits.

Test the APK from the intended CI run. Exercise the changed flow, including relevant launcher, background, permission, or update behavior. For a release, verify an in-place upgrade from the previous compatible public APK when the change calls for it.

## Ship or repair a release

Create a tag or publish only when authorized. Follow the repository’s release checks and use tagged-release when it applies. Pin the intended tag and app commit before any retry. Recover the existing tag if a run is missing, skipped, or failed. When a source fix requires a different commit, get the user’s approval for a replacement version and tag. Verify the required jobs and the actual signed APK on GitHub Releases before calling it published.

## Report the result

Give Russel the commit, the Actions run and APK link, and what passed on an actual device. For a release, include the tag, run attempt, EAS build ID when applicable, and public or private release link. Say which checks are pending or blocked and what would unblock them.
