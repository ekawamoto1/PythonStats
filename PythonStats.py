# PythonStats.py

if __name__ == "__main__":  
    print("PythonStats is being run directly") 
else:  
    print("PythonStats is being imported") 
    


print("Enter 1 for keyboard input, 2 for file input: ")
mode = int(input())
#print("mode = %d" %mode)

if mode == 1:
    numlist = []
    i = 0
    
    print("When no more data is left to enter, simply hit return.")
    while True:
        x = input()
        if x == "":
            break
        else:
            y = float(x)
            #print("You entered %d" %y)
            numlist.append(y)
            
    n = len(numlist)
    if n > 0:
        for y in numlist:
            i += 1
            print("Data point %d: %.2f" %(i, y))

        print("\nFor %d data points, " %n)
        print("The mean (average) is %.2f" %(sum(numlist) / n))
        print("The maximum is %.2f" %max(numlist))
        print("The minimum is %.2f" %min(numlist))
    else:
        print("No data was entered.")
    
elif mode == 2:
    print("mode 2")
else:
    print("Invalid mode; exiting program.")

#  ----jGRASP exec: python3 PythonStats.py
# PythonStats is being run directly
# Enter 1 for keyboard input, 2 for file input: 
# 1
# When no more data is left to enter, simply hit return.
# 32
# 33
# 34
# 
# Data point 1: 32.00
# Data point 2: 33.00
# Data point 3: 34.00
# 
# For 3 data points, 
# The mean (average) is 33.00
# The maximum is 34.00
# The minimum is 32.00
# 
#  ----jGRASP: operation complete.





