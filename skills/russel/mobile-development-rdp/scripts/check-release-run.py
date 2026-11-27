#!/usr/bin/env python3
"""Check a GitHub Actions attempt against an Android release tag. Read only."""

import argparse
import json
import re
import subprocess
import sys
from urllib.parse import quote


def github_get(endpoint, *, paginate=False):
    command = ["gh", "api", "--hostname", "github.com", "--method", "GET"]
    if paginate:
        command.extend(["--paginate", "--slurp"])
    result = subprocess.run(
        [*command, endpoint], capture_output=True, text=True, timeout=30
    )
    if result.returncode:
        status = re.search(r"\bHTTP (\d{3})\b", result.stderr)
        detail = f" (HTTP {status.group(1)})" if status else ""
        raise RuntimeError(f"GitHub request failed{detail}: {endpoint}")
    return json.loads(result.stdout)


def check(args):
    repository = f"repos/{args.repo}"
    tag_ref = quote(f"refs/tags/{args.tag}", safe="")
    tag_commit = github_get(f"{repository}/commits/{tag_ref}")["sha"]
    if tag_commit != args.commit:
        print(f"Tag {args.tag} points to {tag_commit}, expected {args.commit}.")
        return 1

    run_path = f"{repository}/actions/runs/{args.run}"
    run = github_get(run_path)
    attempt = run["run_attempt"]
    print(f"Run {args.run}, attempt {attempt}: {run['html_url']}")
    if run["path"] != args.workflow:
        print(f"Workflow is {run['path']}, expected {args.workflow}.")
        return 1

    event, head = run["event"], run["head_sha"]
    if event == "push" and (run["head_branch"] != args.tag or head != tag_commit):
        print(f"Run was for {run['head_branch']} at {head}, not {args.tag} at {tag_commit}.")
        return 1
    if event not in {"push", "workflow_dispatch"}:
        print(f"Run event {event} needs separate verification of the tag checkout.")
        return 1

    if run["status"] != "completed":
        print(f"Run is {run['status']}. Required jobs are not yet verified.")
        return 1

    pages = github_get(
        f"{run_path}/attempts/{attempt}/jobs?per_page=100", paginate=True
    )
    jobs = [job for page in pages for job in page["jobs"]]
    incomplete = run["conclusion"] != "success"
    for name in dict.fromkeys(args.job):
        matching = [job for job in jobs if job["name"] == name]
        if len(matching) != 1:
            print(f"{name}: expected one job, found {len(matching)} in attempt {attempt}.")
            incomplete = True
            continue
        job = matching[0]
        print(f"{name}: {job['conclusion'] or job['status']}")
        if job["status"] != "completed" or job["conclusion"] != "success":
            incomplete = True
    if incomplete:
        print(f"Required checks are incomplete. Run conclusion: {run['conclusion']}.")
        return 1
    if event == "workflow_dispatch":
        print(
            f"Required jobs passed. Dispatch ran at {head}. "
            f"Verify the run checked out {args.tag} at {tag_commit} before using its APK."
        )
        return 3

    print("Required jobs passed on the expected SHA. Verify the tag checkout and APK.")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, help="GitHub owner/repository")
    parser.add_argument("--tag", required=True)
    parser.add_argument("--commit", required=True, help="Expected full tag commit SHA")
    parser.add_argument("--workflow", required=True, help="Path under .github/workflows/")
    parser.add_argument("--run", required=True, type=int, help="GitHub Actions run ID")
    parser.add_argument("--job", required=True, action="append", help="Exact job name. Repeat for each required job.")
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", args.repo):
        parser.error("--repo must be owner/repository")
    if not re.fullmatch(r"[0-9a-f]{40}", args.commit):
        parser.error("--commit must be a full lowercase Git commit SHA")
    if args.run < 1 or not args.workflow.startswith(".github/workflows/"):
        parser.error("provide a positive run ID and a workflow path under .github/workflows/")
    try:
        return check(args)
    except (OSError, RuntimeError, subprocess.TimeoutExpired, ValueError, KeyError, TypeError) as error:
        print(f"Could not verify the run: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
