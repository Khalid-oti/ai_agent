#from functions.write_file import write_file
from functions.run_python import run_python_file

def test():
    tests = [
        run_python_file("calculator", "main.py"),
        run_python_file("calculator", "tests.py"),
        run_python_file("calculator", "../main.py"),
        run_python_file("calculator", "nonexistent.py")
    ]
    for test in tests:
        print(test)


test()