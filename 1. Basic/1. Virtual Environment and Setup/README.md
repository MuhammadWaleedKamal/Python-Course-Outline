# Virtual Environment and Setup

## What is a Virtual Environment?

A **virtual environment** is an isolated Python installation that allows you to manage project-specific dependencies without affecting the global Python installation. It's like a sandbox where each project can have its own set of packages and versions.

## Why Use Virtual Environments?

1. **Dependency Isolation**: Different projects can use different versions of the same package
2. **Clean Environment**: Keeps system Python clean and manageable
3. **Reproducibility**: Ensures the same code runs consistently across different machines
4. **Conflict Prevention**: Avoids version conflicts between projects
5. **Easy Deployment**: Makes it simple to deploy applications with the exact dependencies

## Types of Python Environments

### 1. System Python
- The default Python installation on your operating system
- Shared across all applications
- Not recommended for development

### 2. Virtual Environment (venv)
- Built-in to Python 3.3+
- Lightweight and fast
- Most commonly used

### 3. Anaconda/Conda
- Package manager with environment support
- Includes pre-installed scientific packages
- Better for data science projects

### 4. pipenv
- Combines pip and virtualenv
- Creates Pipfile for dependency tracking
- Provides deterministic builds

## Basic Commands

```bash
# Create a virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate

# Install packages
pip install package-name

# View installed packages
pip list

# Create requirements file
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt

# Deactivate
deactivate
```

## Best Practices

- ✅ Always use a virtual environment for each project
- ✅ Add venv folder to .gitignore
- ✅ Keep requirements.txt in version control
- ✅ Document Python version requirements
- ❌ Don't commit virtual environment to git
- ❌ Don't modify system Python

## Exercises

1. Create a new virtual environment and activate it
2. Install two packages (e.g., requests and beautifulsoup4) and check versions
3. Create a requirements.txt file and reinstall from it in a new environment
4. Explain the difference between pip and conda
5. Document the steps to set up your project's virtual environment
