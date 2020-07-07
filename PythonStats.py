# PythonStats.py
import math

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
        
        avg = sum(numlist) / n
        print("\nFor %d data point(s), " %n)
        print("    the maximum is %.2f" %max(numlist))
        print("    the minimum is %.2f" %min(numlist))
        print("    the mean (average) is %.2f" %avg)
        if n > 1:
            dot_prod = []
            for i in range(0, len(numlist)):
                dot_prod.append((numlist[i] - avg) * (numlist[i] - avg))
            #print(dot_prod)
            #print("sum = %.2f, arg = %.2f, sqrt = %.2f" %(sum(dot_prod), sum(dot_prod)/(n-1), math.sqrt(sum(dot_prod)/(n-1))))
            stdev = math.sqrt(sum(dot_prod) / (n - 1))
            print("    the std dev is %.2f" %stdev)
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
# 6
# 5
# 4
# 3
# 2
# 1
# 
# Data point 1: 6.00
# Data point 2: 5.00
# Data point 3: 4.00
# Data point 4: 3.00
# Data point 5: 2.00
# Data point 6: 1.00
# 
# For 6 data point(s), 
#     the maximum is 6.00
#     the minimum is 1.00
#     the mean (average) is 3.50
#     the std dev is 1.87
# 
#  ----jGRASP: operation complete.
# 
#  ----jGRASP exec: python3 PythonStats.py
# PythonStats is being run directly
# Enter 1 for keyboard input, 2 for file input: 
# 1
# When no more data is left to enter, simply hit return.
# 1
# 
# Data point 1: 1.00
# 
# For 1 data point(s), 
#     the maximum is 1.00
#     the minimum is 1.00
#     the mean (average) is 1.00
# 
#  ----jGRASP: operation complete.
# 
#  ----jGRASP exec: python3 PythonStats.py
# PythonStats is being run directly
# Enter 1 for keyboard input, 2 for file input: 
# 1
# When no more data is left to enter, simply hit return.
# 
# No data was entered.
# 
#  ----jGRASP: operation complete.

