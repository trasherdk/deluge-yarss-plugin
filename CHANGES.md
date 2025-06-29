# YaRSS2 Changes Log

## Version 2.2.0 - Python 3.9+ Modernization (Latest)

> **⚠️ BREAKING CHANGE**: This version drops Python 2.7 support. Python 3.9 or later is now required.

### 🎯 **Objective**
Modernize the YaRSS2 plugin to require Python 3.9 or later (dropping Python 2.7 support), improving build system, CI/CD, and Windows compatibility.

**Version Change**: Updated from 2.1.x to 2.2.0 following semantic versioning - the MAJOR version bump reflects the breaking change of dropping Python 2.7 support.

### 🚀 **Major Changes**

#### Build System Modernization
- **NEW: Comprehensive Makefile** with modern targets and documentation
  - `make all` (default) - Clean and build without version increment
  - `make clean` - Remove all build artifacts (dist/, build/, .tox/, cache files)
  - `make cleanpyc` - Remove Python cache files
  - `make build` - Build with automatic version increment
  - `make build-no-increment` - Build without changing version
  - `make buildegg` - Legacy alias for build-no-increment
  - `make help` - Show help with all available targets

- **NEW: Automated Build Script (`build.py`)**
  - Automatic version incrementing
  - Comprehensive cleanup of build artifacts
  - Python 3.9+ version tagging
  - Build validation and error handling
  - File size reporting

#### Python Version Requirements
- **Added `python_requires=">=3.9"`** in setup.py
- **Added comprehensive Python classifiers** (3.9, 3.10, 3.11, 3.12, 3.13)
- **Added Windows OS classifier**
- **Enhanced package metadata** with better descriptions

#### Code Modernization & Cleanup
- **Removed Python 2/3 compatibility code**:
  - `yarss2/util/http.py` - Simplified to Python 3 only imports
  - `yarss2/util/common.py` - Removed PY2/PY3 compatibility variables
  - `yarss2/gtk3ui/path_combo_chooser.py` - Removed PY2 checks

#### CI/CD Infrastructure
- **NEW: GitHub Actions CI** (`.github/workflows/ci.yml`)
  - Python 3.9-3.13 test matrix
  - Modern actions: checkout@v4.2.2, setup-python@v5
  - Automated testing on Linux

- **NEW: Dependabot Configuration** (`.github/dependabot.yml`)
  - Automatic GitHub Actions updates (weekly)
  - Configured to ignore bundled library dev dependencies
  - Auto-created PRs with proper commit message formatting

- **Deprecated Travis CI** (moved to `.travis.yml.deprecated`)

#### Testing & Quality Assurance
- **Updated tox.ini**:
  - Replaced py36/py37 with py39-py313 test environments
  - Updated testing matrix for Python 3.9+ support

#### Windows Compatibility Fix
- **Fixed missing `six` dependency** for Windows deployment
  - Copied `six.py` to `yarss2/include/`
  - Added `six = yarss2.include.six` to setup.py entry points
  - Ensures proper bundling of all dependencies

#### Documentation & Package Management
- **Complete README.md rewrite**:
  - Clear Python 3.9+ requirements
  - Comprehensive build system documentation
  - Development setup instructions
  - Modern formatting and structure

- **Enhanced MANIFEST.in**:
  - Better exclusion of unnecessary bundled library components
  - Cleaner package builds by excluding dev/test files

- **Improved setup.py**:
  - Better package exclusions
  - Build information printing
  - Enhanced metadata and descriptions

#### Development Tools
- **Enhanced VSCode integration**:
  - Added makefile configuration settings
  - Improved development environment setup

### 🔧 **Technical Details**

#### Build Artifacts
- **Python 2.7: NO LONGER SUPPORTED** (due to `python_requires=">=3.9"` and code modernization)
- Successfully builds with Python 3.9: `YaRSS2-2.2.0-py3.9.egg` (~7MB)
- Compatible with Python 3.9-3.13 as specified in classifiers

#### Dependency Management
- **Bundled libraries remain unchanged** for runtime compatibility
- **Ignored dependabot updates** for bundled urllib3 dev dependencies (tornado, wheel)
- **Maintained backward compatibility** while modernizing build system

### 🎯 **Benefits**

#### For Developers
- ✅ **Modern build system** with comprehensive cleanup and automation
- ✅ **Automated CI/CD** with GitHub Actions and Dependabot
- ✅ **Clear development workflow** with documented build targets
- ✅ **Professional project structure** suitable for community contributions

#### For Users
- ✅ **Clear Python 3.9+ requirement** preventing compatibility issues
- ✅ **Windows deployment fix** resolving import errors
- ✅ **Reliable plugin installation** with proper dependency bundling
- ✅ **Future-proof compatibility** with Python 3.9-3.13

#### For Maintenance
- ✅ **Automated dependency updates** for GitHub Actions
- ✅ **Comprehensive testing matrix** across Python versions
- ✅ **Professional documentation** reducing support overhead
- ✅ **Modern development practices** attracting contributors

### 📋 **Migration Notes**

#### For Existing Users
- **BREAKING CHANGE: Python 2.7 no longer supported** - Users must upgrade to Python 3.9+
- **No breaking changes** for existing Python 3.x installations
- **Improved Windows compatibility** with bundled dependencies
- **Future-proof compatibility** with Python 3.9-3.13

#### For Developers
- **New build targets** available via Makefile
- **Automated version management** via build.py script
- **Modern CI/CD pipeline** for quality assurance
- **Enhanced development documentation** for easier onboarding

### 🏷️ **File Changes Summary**

#### New Files
- `.github/workflows/ci.yml` - GitHub Actions CI
- `.github/dependabot.yml` - Automated dependency management
- `build.py` - Automated build script
- `CHANGES.md` - This changelog
- `.travis.yml.deprecated` - Archived old CI config

#### Modified Files
- `Makefile` - Complete modernization with comprehensive targets
- `README.md` - Complete rewrite with modern documentation
- `setup.py` - Python 3.9+ requirements and enhanced metadata
- `tox.ini` - Updated Python version matrix
- `MANIFEST.in` - Enhanced package exclusions
- `.vscode/settings.json` - Enhanced VSCode integration

#### Code Cleanup
- `yarss2/util/http.py` - Python 3 only imports
- `yarss2/util/common.py` - Removed compatibility variables
- `yarss2/gtk3ui/path_combo_chooser.py` - Simplified signal handling

This modernization brings YaRSS2 up to current Python development standards while maintaining full backward compatibility and improving the development experience.