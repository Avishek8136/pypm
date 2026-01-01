# Publishing PyPM to PyPI

## Prerequisites

1. **PyPI Account**: Create accounts on:
   - Test PyPI: https://test.pypi.org/account/register/
   - PyPI: https://pypi.org/account/register/

2. **Install Build Tools**:
   ```bash
   pip install --upgrade build twine
   ```

## Build the Package

```bash
# Clean previous builds
rm -rf dist/ build/ *.egg-info

# Build distribution
python -m build
```

This creates:
- `dist/pypm_manager-1.0.0-py3-none-any.whl` (wheel)
- `dist/pypm-manager-1.0.0.tar.gz` (source)

## Test on Test PyPI First

### Upload to Test PyPI

```bash
python -m twine upload --repository testpypi dist/*
```

Enter your Test PyPI credentials when prompted.

### Install from Test PyPI

```bash
pip install --index-url https://test.pypi.org/simple/ pypm-manager
```

### Test the Installation

```bash
pypm --help
pypm info
```

If everything works, proceed to production PyPI.

## Publish to Production PyPI

### Upload to PyPI

```bash
python -m twine upload dist/*
```

Enter your PyPI credentials when prompted.

### Verify Publication

Visit: https://pypi.org/project/pypm-manager/

### Install from PyPI

```bash
pip install pypm-manager
```

## Using API Tokens (Recommended)

### Create API Token

1. Go to PyPI Account Settings
2. Create a new API token
3. Save the token securely

### Create `.pypirc` File

Create `~/.pypirc`:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-your-api-token-here

[testpypi]
username = __token__
password = pypi-your-test-api-token-here
```

Now you can upload without entering credentials:

```bash
python -m twine upload dist/*
```

## Version Management

### Update Version

Edit `pypm/__init__.py` and `pyproject.toml`:

```python
__version__ = "1.0.1"  # or 1.1.0, 2.0.0, etc.
```

### Version Naming

Follow Semantic Versioning (SemVer):
- **MAJOR**: Incompatible API changes (2.0.0)
- **MINOR**: New features, backwards compatible (1.1.0)
- **PATCH**: Bug fixes, backwards compatible (1.0.1)

## Release Checklist

Before each release:

- [ ] Update version in `pypm/__init__.py`
- [ ] Update version in `pyproject.toml`
- [ ] Update version in `setup.py`
- [ ] Update CHANGELOG.md (if you have one)
- [ ] Run tests: `pytest`
- [ ] Build: `python -m build`
- [ ] Test on Test PyPI
- [ ] Tag release: `git tag v1.0.0`
- [ ] Push tag: `git push origin v1.0.0`
- [ ] Upload to PyPI
- [ ] Create GitHub release

## Automation with GitHub Actions

Create `.github/workflows/publish.yml`:

```yaml
name: Publish to PyPI

on:
  release:
    types: [published]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install build twine
    - name: Build package
      run: python -m build
    - name: Publish to PyPI
      env:
        TWINE_USERNAME: __token__
        TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
      run: twine upload dist/*
```

Add `PYPI_API_TOKEN` to GitHub repository secrets.

## Quick Reference

```bash
# Build
python -m build

# Test PyPI
twine upload -r testpypi dist/*
pip install -i https://test.pypi.org/simple/ pypm-manager

# Production PyPI
twine upload dist/*
pip install pypm-manager

# Check distribution
twine check dist/*
```

## Troubleshooting

### "File already exists" Error

- Increment version number
- Can't re-upload same version

### Import Errors After Install

- Check package structure
- Verify `__init__.py` exports
- Test with `python -c "import pypm"`

### Command Not Found

- Check entry points in `setup.py`
- Verify console_scripts configuration
- Reinstall: `pip install --force-reinstall pypm-manager`

## Resources

- PyPI: https://pypi.org/
- Test PyPI: https://test.pypi.org/
- Packaging Guide: https://packaging.python.org/
- Twine: https://twine.readthedocs.io/

---

**Good luck with your publication!** 🚀
