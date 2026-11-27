# Android release and recovery

Use this for configuring, publishing, or repairing a mobile release. The release tag and the commit it points to identify one release. A run ID, run attempt, or EAS build ID identifies an attempt to produce it.

## Establish the target

1. Confirm publication authorization and record the repository, variant, tag, full source commit, workflow path, required job names, and expected APK and manifest names. Resolve an existing tag to its commit, including annotated tags. Use the requested tag if it already exists.
2. Read the workflow and check that its tag filter, required jobs, conditions, secrets, SDK setup, and publication permissions support this release. If the workflow needs repair, prove the relevant jobs on a safe CI run before tagging. Add an explicit manual path for an existing tag when the project needs one. When fixing competing publishers, coordinate by app and release channel and verify a retry cannot overwrite or promote over a newer release.
3. Check the package name, release version, increasing Android `versionCode`, and signing certificate against the previous public APK. Treat a debug-signed or unsigned APK as a candidate only. Preserve the existing release key and version history.
4. For Expo, check the variant’s EAS project ID, APK profile, signing setup, Actions access to the project through `EXPO_TOKEN`, and any known quota problem. Verify credential configuration without exposing values. A laptop’s authenticated EAS session is distinct from Actions authentication. Use the existing authorized credential source. Adding or changing a remote secret requires authorization for that repository and destination.

After an authorized tag push or dispatch, confirm that the expected run actually appeared. Record the attempt and follow that run through its required jobs. If a tag was created by automation, check whether the originating token can trigger the workflow. GitHub’s built-in `GITHUB_TOKEN` generally suppresses a second workflow on a push it makes. Use the approved dispatch path for the existing tag if needed.

## Recover the same release

Keep the original tag in scope. Read the exact job or trigger failure before choosing a retry.

| What happened | What to do |
| --- | --- |
| The run is queued or a matching EAS build is active. | Follow the recorded run and build IDs. Reuse the matching build and avoid duplicate submissions. Report a timeout as pending or blocked. |
| The tag exists and there is no matching run. | Check the trigger filter, workflow status, tag commit, and token behavior. Dispatch the ready workflow against the existing tag when authorized. Record why the original trigger did not fire if you can establish it. |
| A required job was skipped, including a green run with no APK. | Inspect its condition, credentials, and dependency results. A release workflow should fail clearly when a required input is absent. Check the job and artifact after repair. |
| A transient network, registry, or runner failure happened. | Rerun the failed jobs on the same run when upstream artifacts remain valid. Rerun the full workflow if the affected jobs depend on missing or expired inputs. GitHub reruns reuse the original event’s SHA and ref. |
| Runner setup or workflow logic needs a fix. | Make the authorized workflow fix, then dispatch that workflow with the existing tag as its explicit build input. Verify the checkout resolves to the original tagged commit. Record the workflow SHA and the checked-out app SHA separately. Rerunning an old attempt will still use its original workflow context. |
| App source, lockfiles, or build inputs committed under the tag need a change. | Record the failing tag and source fix. Pause publication and get Russel’s explicit approval for the replacement version and tag. Never move, delete, force-push, or recreate an existing tag to get a green run. |
| A retry already created a different tag or run. | Record both tags, commits, runs, and any published assets. Hold further publication and resolve the intended release with Russel. Leave existing tags and published assets in place. |
| EAS quota, signing, authentication, or access is blocked. | Report the failed stage and exact missing prerequisite. Retry after it is resolved. Keep the build off the laptop and retain the release identity. |
| A release or an incomplete draft already exists. | Verify its tag and the digests of existing assets. Resume only a matching draft. Leave conflicting assets or a published release in place and report the conflict. An older retry must never take over the latest release from a newer version. |

Apply the project’s retry limit or the applicable tagged-release limit. For an identified transient failure, retry once and inspect the result before deciding whether another attempt can help. Stop retrying a deterministic failure while its cause remains unchanged. Use a host-supported watcher when available and follow the host’s rules for the wait.

## Verify before calling it released

- Verify the build, signing, and publication jobs required by the workflow. Include successful upstream jobs and artifacts reused from earlier attempts after a partial rerun. A skipped required job is incomplete even if the run is green.
- [check-release-run.py](../scripts/check-release-run.py) uses read-only GitHub queries to check the tag commit, workflow run, and required jobs in one attempt. Pass the expected tag commit, exact workflow path, and each required job name with `--job`. Check any reused upstream jobs against the previous attempt. For a manual dispatch, verify the app checkout SHA using the run’s checkout evidence or its provenance manifest, even if the workflow itself ran on a different commit.
- For Expo, reuse or start an EAS build scoped to the project, variant, profile, exact source SHA, and version. Wait for completion and verify that its artifact is a release APK from that build.
- Inspect the APK’s package, version name, version code, and signer. Compare its SHA-256 with the exact uploaded asset. Where the repo supports drafts, stage the APK and matching manifest together before promotion. Confirm the public release or authorized private download serves both. Verify an alternate website or app update feed if the project uses one. Keep GitHub credentials out of the app. Use the project’s authenticated HTTPS feed for a private download.
- Exercise the signed update from the previous supported version when applicable. Verify installer permissions, app launch, and preservation of relevant user data, account state, and widgets. Record the target device and any part you could not verify.

GitHub documents how [rerunning workflows](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/re-run-workflows-and-jobs), [workflow dispatch](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow), and [workflow triggers](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow) differ.
