# PythonStats.py
import math

if __name__ == "__main__":  
    print("PythonStats is being run directly") 
else:  
    print("PythonStats is being imported") 
    

def ComputeExtremes(inList):
    out = []
    out.append(min(inList))
    out.append(max(inList))
    return out

def ComputeMean(inList):
    avg = sum(inList) / len(inList)
    return avg

def ComputeStdev(inList, mean):
    m = len(inList)
    #print("ComputeStdev %d" %n)
    if m > 1:
        dot_prod = []
        for i in range(0, m):
            term = inList[i] - mean
            dot_prod.append(term * term)
        stdev = math.sqrt(sum(dot_prod) / (m - 1))
    else:
        stdev = math.nan
    return stdev


print("Enter 1 for keyboard input, 2 for file input:", end = " ")
mode = int(input())
#print("mode = %d" %mode)

numlist = []
n = 0
if mode == 1:
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
    
elif mode == 2:
    print("Enter pathname of data file:", end = " ")
    fName = input()
    try:
        f = open(fName, "r")
        for line in f:
            line1 = line.strip('\n')
            #ln = len(line1)
            #print("line %d: %s, length %d" %(n, line1, ln))
            if len(line1) > 0:
                numlist.append(float(line1))
        f.close()
        #print(numlist)
        n = len(numlist)
        
    except IOError:
        print("File %s does not exist." %fName)
        quit()
    
else:
    print("Invalid mode; exiting program.")
    quit()

if n > 0:
    if n < 10:
        i = 0
        for y in numlist:
            i += 1
            print("Data point %d: %.2f" %(i, y))
    else:
        for i in range(0, 5):
            print("Data point %d: %.2f" %(i+1, numlist[i]))
        print("    ...")
        for i in range(n - 5, n):
            print("Data point %d: %.2f" %(i+1, numlist[i]))
    
    avg = ComputeMean(numlist)
    extremes = ComputeExtremes(numlist)
    print("\nFor %d data point(s), " %n)
    print("    the maximum is %.2f" %extremes[1])
    print("    the minimum is %.2f" %extremes[0])
    print("    the mean (average) is %.2f" %avg)
    if n > 1:
        stdev = ComputeStdev(numlist, avg)
        print("    the std dev is %.2f" %stdev)
else:
    print("No data points to be analyzed.")




#  ----jGRASP exec: python3 PythonStats.py
# PythonStats is being run directly
# Enter 1 for keyboard input, 2 for file input: 1
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
# Enter 1 for keyboard input, 2 for file input: 1
# When no more data is left to enter, simply hit return.
# 3.5
# 
# Data point 1: 3.50
# 
# For 1 data point(s), 
#     the maximum is 3.50
#     the minimum is 3.50
#     the mean (average) is 3.50
# 
#  ----jGRASP: operation complete.
# 
#  ----jGRASP exec: python3 PythonStats.py
# PythonStats is being run directly
# Enter 1 for keyboard input, 2 for file input: 1
# When no more data is left to enter, simply hit return.
# 
# No data points to be analyzed.
# 
#  ----jGRASP: operation complete.
# 
#  ----jGRASP exec: python3 PythonStats.py
# PythonStats is being run directly
# Enter 1 for keyboard input, 2 for file input: 2
# Enter pathname of data file: testdata1.txt
# Data point 1: 60.00
# Data point 2: 62.00
# Data point 3: 57.00
# Data point 4: 58.00
# Data point 5: 68.00
#     ...
# Data point 6: 65.00
# Data point 7: 63.00
# Data point 8: 59.00
# Data point 9: 60.00
# Data point 10: 58.00
# 
# For 10 data point(s), 
#     the maximum is 68.00
#     the minimum is 57.00
#     the mean (average) is 61.00
#     the std dev is 3.50
# 
#  ----jGRASP: operation complete.
# 
#  ----jGRASP exec: python3 PythonStats.py
# PythonStats is being run directly
# Enter 1 for keyboard input, 2 for file input: 2
# Enter pathname of data file: testdata2.txt
# Data point 1: 23.50
# 
# For 1 data point(s), 
#     the maximum is 23.50
#     the minimum is 23.50
#     the mean (average) is 23.50
# 
#  ----jGRASP: operation complete.
# 
#  ----jGRASP exec: python3 PythonStats.py
# PythonStats is being run directly
# Enter 1 for keyboard input, 2 for file input: 2
# Enter pathname of data file: testdata3.txt
# No data points to be analyzed.
# 
#  ----jGRASP: operation complete.
# 
#  ----jGRASP exec: python3 PythonStats.py
# PythonStats is being run directly
# Enter 1 for keyboard input, 2 for file input: 2
# Enter pathname of data file: testdata4.txt
# File testdata4.txt does not exist.
# 
#  ----jGRASP: operation complete.
# 
