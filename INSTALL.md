# Installation Guide

## Quick Installation

### From PyPI (Recommended)

```bash
pip install pypm-manager
```

That's it! The `pypm` command is now available globally.

### Verify Installation

```bash
pypm --help
```

You should see the PyPM help menu with all available commands.

## Alternative Installation Methods

### From Source (Development)

If you want to contribute or modify PyPM:

```bash
# Clone the repository
git clone https://github.com/yourusername/pypm.git
cd pypm

# Install in editable mode
pip install -e .

# Or install with development dependencies
pip install -e ".[dev]"
```

### Using pip from GitHub

```bash
pip install git+https://github.com/yourusername/pypm.git
```

## System Requirements

- **Python**: 3.7 or higher
- **Operating System**: Windows, macOS, Linux
- **Dependencies**: None (uses only Python standard library)

## Post-Installation

After installation, PyPM will create two directories when you first use it:

- `~/.pypm_store/` - Central package repository
- `~/.pypm_envs/` - Environment configurations

These are created automatically when needed.

## First Steps

### 1. Check Installation

```bash
pypm --help
```

### 2. View Store Info

```bash
pypm info
```

### 3. Create Your First Environment

```bash
pypm create-env myproject -d "My first PyPM project"
pypm list-envs
```

### 4. Next Steps

Check out:
- [GETTING_STARTED.md](GETTING_STARTED.md) - Beginner's guide
- [USAGE.md](USAGE.md) - Detailed usage examples
- [QUICKREF.md](QUICKREF.md) - Command reference

## Upgrading

```bash
pip install --upgrade pypm-manager
```

## Uninstallation

```bash
# Remove PyPM
pip uninstall pypm-manager

# Optionally remove data directories
rm -rf ~/.pypm_store
rm -rf ~/.pypm_envs
```

## Troubleshooting

### Command not found

If `pypm` command is not found after installation:

1. Check if pip installed it:
   ```bash
   pip show pypm-manager
   ```

2. Ensure pip's script directory is in your PATH:
   ```bash
   python -m pip show pypm-manager
   ```

3. Try running as a module:
   ```bash
   python -m pypm --help
   ```

### Permission Errors

On Linux/macOS, if you get permission errors:

```bash
pip install --user pypm-manager
```

Or use a virtual environment:

```bash
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
pip install pypm-manager
```

## For Developers

### Running Tests

```bash
# Install with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# With coverage
pytest --cov=pypm
```

### Building from Source

```bash
# Install build tools
pip install build

# Build distribution
python -m build

# Install local build
pip install dist/pypm_manager-1.0.0-py3-none-any.whl
```

## Support

- **Documentation**: [README.md](README.md)
- **Issues**: https://github.com/yourusername/pypm/issues
- **Discussions**: https://github.com/yourusername/pypm/discussions

---

**Ready to start?** See [GETTING_STARTED.md](GETTING_STARTED.md)
