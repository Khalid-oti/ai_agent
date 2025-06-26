from functions.get_file_content import get_file_content

def test():
    print(get_file_content("calculator", "main.py"))
    print("---------------------------------------")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print("---------------------------------------")
    print(get_file_content("calculator", "/bin/cat"))

test()