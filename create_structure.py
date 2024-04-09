import os

# Define the directory structure
directory_structure = {
    'app': {
        'api': ['routers.py'],
        'config': ['__init__.py', 'constants.py', 'settings.py'],
        'db': ['__init__.py', 'repository.py'],
        'models.py': None,
        'services.py': None,
        'utils.py': None
    },
    'main.py': None,
    '.env': None,
    'requirements.txt': None
}

# Function to create the directory structure
def create_directory_structure(root_path, structure):
    for name, contents in structure.items():
        path = os.path.join(root_path, name)
        if contents is None:
            # Create file
            open(path, 'a').close()
            print(f"Created file: {path}")
        else:
            # Create directory
            os.makedirs(path)
            print(f"Created directory: {path}")
            # Recursively create contents
            if isinstance(contents, dict):
                create_directory_structure(path, contents)
            else:
                for filename in contents:
                    filepath = os.path.join(path, filename)
                    open(filepath, 'a').close()
                    print(f"Created file: {filepath}")

# Define root directory
root_directory = './'

# Create directory structure
create_directory_structure(root_directory, directory_structure)
