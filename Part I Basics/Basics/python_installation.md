# Python Installation Guide

This guide provides step-by-step instructions for installing Python on Windows, macOS, and Linux systems, along with verification tests to ensure your installation is working correctly.

## Table of Contents
- [Windows Installation](#windows-installation)
- [macOS Installation](#macos-installation)
- [Linux Installation](#linux-installation)
- [Verification Tests](#verification-tests)
- [Troubleshooting](#troubleshooting)

## Windows Installation

### Method 1: Official Python Installer (Recommended)

1. **Download Python**
   - Visit [python.org/downloads](https://www.python.org/downloads/)
   - Click "Download Python 3.x.x" (latest version)
   - Save the installer file to your computer

2. **Run the Installer**
   - Double-click the downloaded `.exe` file
   - **Important**: Check "Add Python to PATH" at the bottom of the installer window
   - Choose "Install Now" for default installation
   - Wait for installation to complete

3. **Verify Installation**
   - Open Command Prompt (`cmd`) or PowerShell
   - Type `python --version` and press Enter
   - You should see the Python version number

### Method 2: Microsoft Store

1. Open Microsoft Store
2. Search for "Python"
3. Select the latest Python version
4. Click "Install"

### Method 3: Package Manager (Advanced)

Using Chocolatey:
```bash
choco install python
```

Using Scoop:
```bash
scoop install python
```

## macOS Installation

### Method 1: Official Python Installer (Recommended)

1. **Download Python**
   - Visit [python.org/downloads](https://www.python.org/downloads/)
   - Click "Download Python 3.x.x"
   - Download the macOS installer

2. **Install Python**
   - Open the downloaded `.pkg` file
   - Follow the installation wizard
   - Enter your password when prompted

3. **Update PATH (if needed)**
   - Open Terminal
   - If using bash, edit `~/.bash_profile`
   - If using zsh, edit `~/.zshrc`
   - Add: `export PATH="/usr/local/bin/python3:$PATH"`

### Method 2: Homebrew (Recommended for Developers)

1. **Install Homebrew** (if not already installed)
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Python**
   ```bash
   brew install python
   ```

3. **Update PATH**
   ```bash
   echo 'export PATH="/opt/homebrew/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```

### Method 3: pyenv (Version Management)

1. **Install pyenv**
   ```bash
   curl https://pyenv.run | bash
   ```

2. **Add to shell profile**
   ```bash
   echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.zshrc
   echo 'eval "$(pyenv init -)"' >> ~/.zshrc
   source ~/.zshrc
   ```

3. **Install Python**
   ```bash
   pyenv install 3.11.0
   pyenv global 3.11.0
   ```

## Linux Installation

### Ubuntu/Debian

1. **Update package list**
   ```bash
   sudo apt update
   ```

2. **Install Python**
   ```bash
   sudo apt install python3 python3-pip python3-venv
   ```

3. **Create symbolic link (optional)**
   ```bash
   sudo ln -s /usr/bin/python3 /usr/bin/python
   ```

### CentOS/RHEL/Fedora

**For CentOS/RHEL:**
```bash
sudo yum install python3 python3-pip
```

**For Fedora:**
```bash
sudo dnf install python3 python3-pip
```

### Arch Linux

```bash
sudo pacman -S python python-pip
```

### From Source (Advanced)

1. **Install dependencies**
   ```bash
   sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
   ```

2. **Download and compile**
   ```bash
   wget https://www.python.org/ftp/python/3.11.0/Python-3.11.0.tgz
   tar -xf Python-3.11.0.tgz
   cd Python-3.11.0
   ./configure --enable-optimizations
   make -j 8
   sudo make altinstall
   ```

## Verification Tests

### Basic Version Check

Open your terminal/command prompt and run:

```bash
python --version
# or
python3 --version
```

Expected output: `Python 3.x.x`

### Python Interactive Shell Test

1. **Start Python interpreter**
   ```bash
   python
   ```

2. **Run basic commands**
   ```python
   print("Hello, Python!")
   2 + 2
   import sys
   sys.version
   exit()
   ```

### pip Package Manager Test

```bash
pip --version
# or
pip3 --version
```

Expected output: `pip x.x.x from /path/to/pip (python 3.x)`

### Create and Run a Test Script

1. **Create test file**
   ```bash
   # Create test.py file
   echo 'print("Python is working correctly!")' > test.py
   ```

2. **Run the script**
   ```bash
   python test.py
   ```

   Expected output: `Python is working correctly!`

### Virtual Environment Test

```bash
python -m venv test_env
source test_env/bin/activate  # On Windows: test_env\Scripts\activate
pip install requests
python -c "import requests; print('Requests module imported successfully')"
deactivate
```

## Troubleshooting

### Common Issues

**"Python is not recognized as an internal or external command" (Windows)**
- Solution: Add Python to PATH environment variable
- Go to System Properties → Advanced → Environment Variables
- Add Python installation directory to PATH

**"Command not found: python" (macOS/Linux)**
- Try `python3` instead of `python`
- Check if Python is installed: `which python3`
- Add to PATH in shell profile

**Permission denied errors (Linux/macOS)**
- Use `sudo` for system-wide installations
- Consider using virtual environments for project-specific packages

**SSL certificate errors**
- Update certificates: `pip install --upgrade certifi`
- On macOS: Run "Install Certificates.command" in Python folder

### Useful Commands

```bash
# Check Python path
python -c "import sys; print(sys.executable)"

# List installed packages
pip list

# Check pip configuration
pip config list

# Upgrade pip
python -m pip install --upgrade pip
```

## Next Steps

After successful installation:

1. **Learn Python basics** - Try online tutorials or interactive platforms
2. **Set up an IDE** - PyCharm, VS Code, or Sublime Text
3. **Create virtual environments** - Keep projects isolated
4. **Install useful packages** - requests, numpy, pandas, etc.
5. **Join the community** - Python.org, Reddit r/Python, Stack Overflow

## Additional Resources

- [Official Python Documentation](https://docs.python.org/)
- [Python Package Index (PyPI)](https://pypi.org/)
- [Real Python Tutorials](https://realpython.com/)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)

---

*This guide covers Python 3.x installation. Python 2.x reached end-of-life on January 1, 2020, and is no longer recommended for new projects.*
