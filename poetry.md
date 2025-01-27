```sh
     mkdir my_project
     cd my_project
```
   - Initialize a new Poetry project:
     
```sh
    poetry init
```
- Follow the prompts to set up your project.

`NOTE`: To get the environment path we use:
```bash
    poetry env info --path
```

### **Add dependencies using Poetry**:
   - To add a dependency, use the following command:
     
```sh
    poetry add <package_name>
```
- For example, to add `requests`:
     
```sh
    poetry add requests
```

To delete a dependency
```sh
    poetry remove <package_name>
```

### **Install dependencies**:
   - To install all dependencies listed in the `pyproject.toml` file, run:
     
```sh
    poetry install
```

### **Activate the virtual environment**:
   - Poetry automatically creates a virtual environment for your project. To activate it, run:
     
```sh
    poetry shell
```