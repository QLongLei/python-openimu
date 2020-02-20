import sys
import os
import pkgutil


def is_in_bundle():
    return hasattr(sys, 'frozen') and getattr(sys, 'frozen') and hasattr(sys, '_MEIPASS')


def get_executor_path():
    path = os.path.abspath(os.path.dirname(sys.executable))
    if not is_in_bundle():
        path = sys.path[0]
    print(path,is_in_bundle())
    return path


def get_content_from_bundle(package, path):
    module_name = 'openimu'
    if is_in_bundle():
        content = pkgutil.get_data(package, path)
    else:
        content = pkgutil.get_data(module_name, os.path.join(package, path))

    return content
