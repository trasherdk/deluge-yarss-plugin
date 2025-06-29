# YaRSS2 - Yet Another RSS 2

Yet another RSS 2, a simple RSS plugin for Deluge, based on YaRSS written by Camillo Dell'mour.

## Requirements

- **Python 3.9 or later**
- Deluge 2.0+
- GTK 3.0+

## Installation

Download the latest release from the [releases page](../../releases) and install it via the Deluge plugin manager.

## Development

### Prerequisites

- Python 3.9 or later
- Deluge development environment
- GTK development libraries

### Setup

1. Clone the repository
2. Install development dependencies: `pip install tox`
3. Run tests: `tox`
4. Run specific Python version tests: `tox -e py39` (or py310, py311, py312, py313)

### Building

This project includes a modern build system with multiple options:

#### Using Make (Recommended)

```bash
# Quick build (clean + build without version increment)
make

# Build with automatic version increment
make build

# Clean all build artifacts
make clean

# Show all available targets
make help
```

#### Using the Automated Build Script

```bash
# Full automated build with version increment
python3 build.py
```

#### Manual Building

```bash
# Direct setup.py build
python3 setup.py bdist_egg
```

#### Available Make Targets

- `make all` (default) - Clean and build without version increment
- `make clean` - Remove all build artifacts (dist/, build/, .tox/, cache files)
- `make cleanpyc` - Remove only Python cache files
- `make build` - Build with automatic version increment
- `make build-no-increment` - Build without changing version
- `make buildegg` - Legacy alias for build-no-increment
- `make help` - Show help with all available targets

The built .egg file will be located in the `dist/` directory.

## Compatibility

This plugin requires **Python 3.9 or later**. It has been tested with:

- Python 3.9+
- Deluge 2.0+
- Both Linux and Windows environments

## Changelog

See [CHANGES.md](CHANGES.md) for detailed information about recent improvements and changes.

## License

This project is licensed under the GNU General Public License v3.0 or later. See the LICENSE file for details.

## Running the tests ##
The directory containing yarss2 must be on the PYTHONPATH

e.g.

```
#!bash

yarss2$ export PYTHONPATH=$PYTHONPATH:$PWD/..
```


Run the tests with:

```
#!bash

yarss2$ trial tests
```
