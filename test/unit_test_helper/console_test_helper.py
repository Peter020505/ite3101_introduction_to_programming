import sys
from io import StringIO
import contextlib
from typing import Tuple, Union, Dict

from unit_test_helper import is_answer


@contextlib.contextmanager
def stdout_io(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


def get_script_output(file_relative_path: str) -> str:
    test_file_path_name = get_path_name(file_relative_path)

    print("Testing file: ", test_file_path_name)
    with stdout_io() as s:
        try:
            with open(test_file_path_name, "r") as f:
                exec(f.read())
        except:
            print("File " + test_file_path_name + " not found!")
            return ""
    return str(s.getvalue())


def exec_script(file_relative_path: str):
    test_file_path_name = get_path_name(file_relative_path)
    try:
        with open(test_file_path_name, "r") as f:
            exec(f.read())
    except:
        print("File " + test_file_path_name + " not found!")


def get_path_name(file_relative_path: str) -> str:
    import os
    dirname, filename = os.path.split(os.path.abspath(__file__))
    test_file_path_name = dirname + "/../../lab/" + file_relative_path
    if is_answer:
        test_file_path_name = test_file_path_name.replace(".py", "_ans.py")
    return test_file_path_name


def execfile(file_relative_path: str, temp_globals: dict = None, temp_locals: dict = None) -> \
        Tuple[Union[Dict[str, str], dict], Union[dict, dict], str, str]:
    test_file_path_name = get_path_name(file_relative_path)
    if temp_globals is None:
        temp_globals = {}
    temp_globals.update({
        "__file__": test_file_path_name,
        "__name__": "__main__",
    })

    if temp_locals is None:
        temp_locals = {}
    content = ""
    with stdout_io() as s:
        try:
            with open(test_file_path_name, 'rb') as file:
                content = file.read()
                exec(compile(content, test_file_path_name, 'exec'), temp_globals, temp_locals)
        except FileNotFoundError:
            print("File " + test_file_path_name + " not found!")

    return temp_globals, temp_locals, str(content), str(s.getvalue())
