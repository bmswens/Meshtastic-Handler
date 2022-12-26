# built in
import os
import importlib

def get_all_modules():
    modules = []
    this_dir = os.path.dirname(os.path.abspath(__file__))
    for file_name in os.listdir(this_dir):
        if '.py' in file_name and file_name != '__init__.py':
            package_name = '.' + file_name.replace('.py', '')
            modules.append(
                importlib.import_module(package_name, "handlers")
            )
    return modules