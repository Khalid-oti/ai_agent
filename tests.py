from functions.get_files_info import get_files_info
import unittest
import os

def test_files_info_function():
    print(get_files_info("calculator", "."))
    print(get_files_info("calculator", "pkg"))
    print(get_files_info("calculator", "/bin"))
    print(get_files_info("calculator", "../"))

test_files_info_function()


#class FileInfoTest(unittest.TestCase):
    #def test_calculator_info1(self):
        #expected = f"""- pkg: filesize={os.path.getsize("calculator/pkg/")}, is_dir=True\n
        #- main.py: filesize={os.path.getsize("calculator/main.py/")}, is_dir=False\n
        #- tests.py: filesize={os.path.getsize("calculator/tests.py/")}, is_dir=True\n"""
        #get_files_info("calculator", ".") 
        #self.assertEqual(expected, actual)

    #def test_calculator_info2(self):
        #get_files_info("calculator", "pkg")
        #self.assertEqual(expected, actual)

    #def test_calculator_info3(self):
        #get_files_info("calculator", "/bin")
        #self.assertEqual(expected, actual)

    #def test_calculator_info4(self):
        #get_files_info("calculator", "../")
        #self.assertEqual(expected, actual)