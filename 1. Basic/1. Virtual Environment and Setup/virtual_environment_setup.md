# Virtual Environment and Setup

A virtual environment keeps project dependencies separate from the system Python installation. It helps avoid conflicts when different projects require different package versions.

Example workflow:
- Create the environment: `python -m venv venv`
- Activate it: `venv\Scripts\activate` on Windows or `source venv/bin/activate` on macOS/Linux
- Install packages inside the environment: `pip install package-name`

Exercises:
1. Write the commands to create and activate a virtual environment for a new project.
2. List three benefits of using a virtual environment.
3. Explain what happens when you install a package outside a virtual environment.
