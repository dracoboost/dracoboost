#!/usr/bin/env python3
import os
import shutil
import subprocess
import sys
from pathlib import Path


def main():
    """
    Initializes a local Git repository, creates a corresponding repository on GitHub,
    and pushes the initial commit.
    """
    # --- Configuration ---
    # Get the project's root directory (parent of the 'scripts' directory)
    try:
        # Assumes the script is in a 'scripts' directory, and the work_dir is its parent.
        work_dir = Path(__file__).resolve().parent.parent
    except NameError:
        # Fallback for environments where __file__ is not defined (e.g., interactive)
        # This makes the current directory the working directory.
        work_dir = Path.cwd()

    repo_description = ""
    # --- End of configuration ---

    # Ask user whether the repository should be private or public
    choice = (
        input(
            "Do you want the repository to be private or public? [private/public] (default: private) "
        )
        .strip()
        .lower()
    )

    if choice == "public":
        private_or_public_flag = "--public"
    else:
        # Default to private for empty input or "private"
        private_or_public_flag = "--private"

    # GitHub repository name is derived from the working directory's name
    repo_name = work_dir.name

    # Change to working directory
    if not work_dir.is_dir():
        print(
            f"Error: The specified working directory '{work_dir}' was not found.",
            file=sys.stderr,
        )
        sys.exit(1)

    os.chdir(work_dir)
    print(f"Working directory: {os.getcwd()}")

    # Check if Git is initialized
    if not (work_dir / ".git").exists():
        print("Initializing Git repository...")
        result = subprocess.run(["git", "init"], capture_output=True, text=True)
        if result.returncode != 0:
            print("Error: Failed to initialize Git.", file=sys.stderr)
            print(result.stderr, file=sys.stderr)
            sys.exit(1)
    else:
        print("Git repository already initialized.")

    # Stage all files
    print("Staging all changes...")
    result = subprocess.run(["git", "add", "."], capture_output=True, text=True)
    if result.returncode != 0:
        print("Error: git add failed.", file=sys.stderr)
        print(result.stderr, file=sys.stderr)
        sys.exit(1)

    # Commit
    print("Creating initial commit...")
    result = subprocess.run(
        ["git", "commit", "-m", "Initial commit"], capture_output=True, text=True
    )
    if result.returncode != 0:
        print(
            "Warning: git commit failed. There may be no changes to commit.",
            file=sys.stderr,
        )
        status_result = subprocess.run(
            ["git", "status", "--porcelain"], capture_output=True, text=True
        )
        if status_result.stdout:
            print("However, uncommitted changes still exist.", file=sys.stderr)
            sys.exit(1)
        else:
            print("No changes to commit. Continuing...")

    # Create repository on GitHub
    print(f"Creating GitHub repository '{repo_name}' ({private_or_public_flag})...")
    if shutil.which("gh"):
        owner_name_result = subprocess.run(
            ["gh", "api", "user", "-q", ".login"], capture_output=True, text=True
        )
        if owner_name_result.returncode != 0:
            print(
                "Error: Failed to get GitHub username using 'gh api user'.",
                file=sys.stderr,
            )
            print(owner_name_result.stderr, file=sys.stderr)
            sys.exit(1)
        owner_name = owner_name_result.stdout.strip()

        command = [
            "gh",
            "repo",
            "create",
            f"{owner_name}/{repo_name}",
            private_or_public_flag,
            "--source=.",
            f'--description="{repo_description}"',
            "--remote=upstream",
            "--push",
        ]
        # We use shell=True because of the quoted description argument
        result = subprocess.run(
            " ".join(command), shell=True, capture_output=True, text=True
        )
        if result.returncode != 0:
            print(
                "Error: Failed to create repository with gh CLI. Please check authentication.",
                file=sys.stderr,
            )
            print(result.stderr, file=sys.stderr)
            print(
                "\nYou may need to create the repository manually and set the remote URL:"
            )
            print(f"  git remote add origin git@github.com:{owner_name}/{repo_name}.git")
            print("  git branch -M main")
            print("  git push -u origin main")
            sys.exit(1)
        print(f"Repository '{repo_name}' has been created on GitHub and pushed.")
        print(result.stdout)
    else:
        print(
            "Error: GitHub CLI (gh) is not installed or not authenticated.",
            file=sys.stderr,
        )
        print("Please create a repository manually: https://github.com/new")
        print("\nAfter creating it, run the following commands:")
        print(f"  git remote add origin git@github.com:<YOUR_USERNAME>/{repo_name}.git")
        print("  git branch -M main")
        print("  git push -u origin main")
        sys.exit(1)

    print("\nScript completed successfully!")
    # The owner_name is only available if gh is installed.
    if shutil.which("gh"):
        print(f"GitHub repository URL: https://github.com/{owner_name}/{repo_name}")


if __name__ == "__main__":
    main()
