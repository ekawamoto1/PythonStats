# File2.py
import File1

# formatted print: https://www.geeksforgeeks.org/python-output-formatting/
print("File2 __name__ = %s" %__name__)
print(File1.sys.version)    # print(sys.version) does not work

if __name__ == "__main__": 
    print("File2 is being run directly")
else: 
    print("File2 is being imported")