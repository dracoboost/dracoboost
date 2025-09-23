import json
import re
from pathlib import Path

def get_project_root() -> Path:
    """Gets the project root directory."""
    return Path(__file__).parent.parent

def get_website_version(project_root: Path) -> str:
    """Reads the version from website/package.json."""
    package_json_path = project_root / "website" / "package.json"
    with open(package_json_path, "r", encoding="utf-8") as f:
        package_data = json.load(f)
    return package_data["version"]

def update_changelog_version(project_root: Path, version: str):
    """Updates the version badge in website/CHANGELOG.md."""
    changelog_path = project_root / "website" / "CHANGELOG.md"
    
    with open(changelog_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Pattern for the version badge
    pattern = r'(<img alt="website version" src="https://img.shields.io/badge/website%20version-)[^->]+(-lightgrey">)'
    replacement = r'\g<1>' + version + r'\g<2>'
    
    new_content = re.sub(pattern, replacement, content)

    if new_content != content:
        with open(changelog_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated website/CHANGELOG.md to version {version}")
    else:
        print("website/CHANGELOG.md version is already up to date.")

if __name__ == "__main__":
    root = get_project_root()
    try:
        current_version = get_website_version(root)
        update_changelog_version(root, current_version)
    except Exception as e:
        print(f"An error occurred: {e}")
