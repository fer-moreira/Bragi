from importlib import import_module
from src.base import BaseCommand

def find_class (path, classname) -> BaseCommand:
    return getattr(import_module(path), classname)()
    

def find_class_by_path (path) -> BaseCommand:
    file_path = ".".join(path.split(".")[:-1])
    file_class = path.split('.')[-1]
    
    return find_class(file_path, file_class)