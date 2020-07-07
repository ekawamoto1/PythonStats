# File1.py 
import sys 
    
print("File1 __name__ = %s" %__name__) 
print(sys.version)
    
if __name__ == "__main__":  
    print("File1 is being run directly") 
else:  
    print("File1 is being imported") 