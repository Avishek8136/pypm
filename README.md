# PyPM - Python Package Manager

**Production-ready package manager with true multi-version support** - Tested with TensorFlow, handles complex dependencies perfectly!

## 🚀 Quick Start

```bash
# Install PyPM
pip install pypm-manager

# Create environment  
pypm create myproject

# Activate it
pypm activate myproject  # Shows activation command
# Run the activation command shown

# Install packages with version isolation
pypm install pandas numpy scikit-learn

# Deactivate when done
deactivate
```

## ✨ The Problem PyPM Solves

**Problem 1 - Duplication:**
```
project1/venv/ → pandas 1.5.0 (100 MB)
project2/venv/ → pandas 1.5.0 (100 MB)  [DUPLICATE!]
project3/venv/ → pandas 1.5.0 (100 MB)  [DUPLICATE!]
Total: 300 MB wasted
```

**Problem 2 - Version Conflicts:**
```
project1 needs requests 2.28.0
project2 needs requests 2.31.0
❌ Can't have both with venv/conda!
```

**With PyPM v2.2:**
```
~/.pypm_central/packages/
  ├── tensorflow/2.20.0/cp313/  [TensorFlow for Python 3.13]
  ├── matplotlib/3.10.8/cp313/  [Latest matplotlib]
  ├── matplotlib/3.9.0/cp313/   [Older matplotlib - both coexist!]
  └── numpy/2.4.0/cp313/        [Shared by all - stored once!]

✅ Multiple package versions coexist
✅ Python version tagging (cp313) for binary compatibility
✅ Each environment uses specific versions
✅ Shared dependencies stored once
✅ Complex packages like TensorFlow work perfectly!
```

## 🎯 How It Works

1. **Create**: `pypm create myenv` - Creates lightweight environment
2. **Activate**: `pypm activate myenv` - Shows activation command
3. **Install**: `pypm install pandas==1.5.0` - Stores in version-specific directory
4. **Isolation**: Each environment's PYTHONPATH points to its specific package versions

## 📦 Installation

```bash
pip install pypm-manager
```

## 🆕 What's New in v2.2.0

**Production-Ready Release** - Tested with TensorFlow 2.20.0 and complex packages!

- **RECORD-based File Migration**: Accurately captures all package files by parsing RECORD metadata
  - Handles packages where module name ≠ package name (e.g., `absl-py` → `absl`)
  - Discovers modules via RECORD file analysis
  - Fallback to top_level.txt for compatibility

- **Python Version Tagging**: Automatic binary compatibility
  - Adds Python tags (cp313, cp311, etc.) to storage paths
  - Prevents mixing incompatible binary packages
  - Works seamlessly with packages compiled for specific Python versions

- **Complete File Capture**: Enhanced migration captures everything
  - Module directories (e.g., `tensorflow/`, `absl/`)
  - DLL dependencies and .libs folders
  - dist-info metadata
  - All package components migrated correctly

- **Verified with Complex Packages**:
  - TensorFlow 2.20.0 with 38 dependencies ✅
  - Keras 3.13.0 ✅
  - matplotlib (multiple versions) ✅
  - All imports work perfectly!

## 🔧 Commands

```bash
# Environment Management
pypm create <name>         # Create environment
pypm activate <name>       # Show activation command
pypm install <package>     # Install with version isolation
deactivate                 # Deactivate current environment
pypm delete <name>         # Delete environment
pypm list                  # List all environments
pypm info <name>           # Show environment details

# Central Store
pypm store-info            # View central store stats
```

## 💡 Complete Example

```bash
# Create data science environment
pypm create datascience
pypm activate datascience
# Run activation command shown (e.g., C:\...\datascience\Scripts\Activate.ps1)

# Install packages with specific versions
pypm install pandas==2.1.0 numpy scikit-learn

# Work on your project...
python my_analysis.py

# Deactivate
deactivate

# Create another project with different pandas version
pypm create ml-project
pypm activate ml-project
# Activate...

pypm install pandas==2.3.0 tensorflow
# ✅ Both pandas 2.1.0 and 2.3.0 coexist!
# ✅ numpy/scikit-learn shared between projects
```

## 🌟 Features

- ✅ **Production Ready** - Tested with TensorFlow, Keras, and complex dependency trees
- ✅ **Python Version Tagging** - Binary compatibility with cp313, cp311 tags
- ✅ **RECORD-based Migration** - Accurate module discovery (handles absl-py → absl)
- ✅ **True Version Isolation** - Multiple package versions coexist perfectly
- ✅ **Environment-specific Versions** - Each env uses its own package versions
- ✅ **Zero Duplication** - Shared dependencies stored once, reused everywhere
- ✅ **Complete File Capture** - DLLs, .libs, all package components migrated
- ✅ **Familiar Workflow** - Similar to venv activation
- ✅ **Cross-platform** - Windows, macOS, Linux
- ✅ **No Dependencies** - Pure Python stdlib

## 🆚 vs Other Tools

| | venv | conda | PyPM v2.2 |
|---|---|---|---|
| **Multiple versions** | No | Limited | Yes ✅ |
| **Python version tagging** | No | Yes | Yes ✅ |
| **Binary compatibility** | Manual | Yes | Auto ✅ |
| **Duplication** | Yes | Yes | No ✅ |
| **TensorFlow tested** | - | Yes | Yes ✅ |
| **Workflow** | activate + pip | activate + conda | activate + pypm |
| **Storage Efficiency** | Low | Low | High ✅ |

## 📁 Storage Locations

- Environments: `~/.pypm_envs/`
- Versioned packages: `~/.pypm_central/packages/{name}/{version}/{python_tag}/`
  - Example: `numpy/2.4.0/cp313/` (Python 3.13)
  - Example: `tensorflow/2.20.0/cp313/`
- Environment configs: `{env}/pypm_requirements.json`

## 🤝 Contributing

https://github.com/Avishek8136/pypm

## 📜 License

MIT License

---

**PyPM v2.2 - Production-ready with TensorFlow support!** 🎉
