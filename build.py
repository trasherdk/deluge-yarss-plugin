#!/usr/bin/env python3
"""
Auto-build script for YaRSS2
Automatically increments version and builds with proper Python version tags
"""
import subprocess
import sys
import os
import shutil
import re

def increment_version():
    """Increment the patch version in setup.py"""
    with open('setup.py', 'r') as f:
        content = f.read()

    # Find the version line
    version_pattern = r'__version__ = "(\d+)\.(\d+)\.(\d+)"'
    match = re.search(version_pattern, content)

    if not match:
        print("Could not find version string in setup.py")
        return None

    major, minor, patch = match.groups()
    current_version = f"{major}.{minor}.{patch}"

    # Increment patch version
    new_patch = int(patch) + 1
    new_version = f"{major}.{minor}.{new_patch}"

    # Replace in content
    new_content = re.sub(
        version_pattern,
        f'__version__ = "{new_version}"',
        content
    )

    # Write back to file
    with open('setup.py', 'w') as f:
        f.write(new_content)

    print(f"Version incremented: {current_version} -> {new_version}")
    return new_version



def main():
    print("=== YaRSS2 Auto-Build Script ===")

    # Clean previous builds
    print("Cleaning previous builds...")
    for dir_name in ['dist', 'build', 'YaRSS2.egg-info']:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"Removed {dir_name}/")

    # Auto-increment version
    print("\nIncrementing version...")
    new_version = increment_version()
    if not new_version:
        print("Failed to increment version, exiting...")
        sys.exit(1)

    # Build
    print(f"\nBuilding YaRSS2 v{new_version}...")
    print("Running: python3 setup.py bdist_egg")
    result = subprocess.run([sys.executable, 'setup.py', 'bdist_egg'])

    if result.returncode != 0:
        print(f"Build failed with exit code: {result.returncode}")
        sys.exit(1)

    print("Build successful!")

    # Skip renaming - keep the accurate py3.9 tag
    print("\nKeeping accurate Python version tag (py3.9)")

    # Show final results
    print("\n=== Build Complete ===")
    if os.path.exists('dist'):
        files = os.listdir('dist')
        for file in files:
            file_path = os.path.join('dist', file)
            size = os.path.getsize(file_path)
            print(f"Created: dist/{file} ({size:,} bytes)")

if __name__ == "__main__":
    main()