.PHONY: all clean cleanpyc build build-no-increment help

# Default target - clean and build (no version increment)
all: clean build-no-increment

# Comprehensive clean target
clean: cleanpyc
	@echo "Cleaning build artifacts..."
	-rm -rf build/
	-rm -rf dist/
	-rm -rf *.egg-info/
	-rm -rf .tox/
	@echo "Clean complete."

# Clean Python cache files
cleanpyc:
	@echo "Cleaning Python cache files..."
	-find . -name "*.pyc" -delete
	-find . -name "*.pyo" -delete
	-find . -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	-find . -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true

# Build using build.py (auto-increments version)
build:
	@echo "Building YaRSS2 plugin..."
	python3 build.py

# Build without version increment (direct setup.py call)
build-no-increment: cleanpyc
	@echo "Building YaRSS2 plugin (no version increment)..."
	python3 setup.py bdist_egg

# Legacy target for compatibility
buildegg: build-no-increment

# Help target
help:
	@echo "Available targets:"
	@echo "  all               - Clean and build without version increment (default)"
	@echo "  clean             - Remove all build artifacts"
	@echo "  cleanpyc          - Remove Python cache files"
	@echo "  build             - Build plugin (auto-increments version)"
	@echo "  build-no-increment- Build plugin without incrementing version"
	@echo "  buildegg          - Legacy alias for build-no-increment"
	@echo "  help              - Show this help message"
