# PythonStats.py
import sys
import math
import tkinter as tk
from tkinter import *
#from tkinter import messagebox

print(sys.version)
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


def ComputeMedian(inList):
    m = len(inList)
    if m > 1:
        inList.sort()
        #print(inList)
        m0 = m // 2
        if m % 2 == 0:
            median = (inList[m0 - 1] + inList[m0]) / 2
        else:
            median = inList[m0]
    return median


def PrintDataPoints(inList):
    m = len(inList)
    if m > 0:
        if m < 10:
            i = 0
            for y in inList:
                i += 1
                print("Data point %d: %.2f" %(i, y))
        else:
            for i in range(0, 5):
                print("Data point %d: %.2f" %(i+1, inList[i]))
            print("    ...")
            for i in range(m - 5, m):
                print("Data point %d: %.2f" %(i+1, inList[i]))


def PrintOutStats(inList):
    n = len(inList)
    avg = ComputeMean(inList)
    extremes = ComputeExtremes(inList)
    print("\nFor %d data point(s), " %n)
    print("    the maximum is %.2f" %extremes[1])
    print("    the minimum is %.2f" %extremes[0])
    print("    the mean (average) is %.2f" %avg)
    if n > 1:
        med = ComputeMedian(inList)
        print("    the median is %.2f" %med)
        stdev = ComputeStdev(inList, avg)
        print("    the std dev is %.2f" %stdev)


def GetDataPointsFromConsole():
    numlist = []
    while True:
        x = input()
        if x == "":
            break
        else:
            y = float(x)
            #print("You entered %d" %y)
            numlist.append(y)
    return numlist
    

def GetDataPointsFromFile():
    numlist = []
    print("Enter pathname of data file:", end = " ")
    fName = input()
    try:
        f = open(fName, "r")
        for line in f:
            line1 = line.strip('\n')
            if len(line1) > 0:
                numlist.append(float(line1))
        f.close()

    except IOError:
        print("File %s does not exist." %fName)
        quit()
        
    return numlist
    

def PythonStatsGUIApp(arg):
    def OK_cmd():
        x = My_entry.get()
        print("x = %s, arg = %s" %(x,arg))
        root.withdraw()
        if int(arg) == 1:
            #print("process data points")
            sList = x.split(",")
            numlist = []
            for xx in sList:
                numlist.append(float(xx))
            print(numlist)
        elif int(arg) == 2:
            #print("process file name")
            fName = x
            print("file name is %s" %fName)
        quit()
        
    def Cancel_cmd():
        quit()
        
    w = 500
    h = 100
    xp = 300
    yp = 300
    geom_str = "{}x{}+{}+{}".format(w,h,xp,yp)
    #print(geom_str)
    root = tk.Tk()
    root.geometry(geom_str)
    
    if int(arg) == 1:    # input data points in text field
        root.title("Data entry")
        My_label = tk.Label(root,text="Enter data points:")

    elif int(arg) == 2:    # read data points from file
        root.title("File name entry")
        My_label = tk.Label(root,text="Enter path name of data file:")
        
    else:    # invalid command-line argument
        root.title("Error")
        My_label = tk.Label(root,text="invalid CL argument")
    
    My_entry = tk.Entry(root)    
    OK_button = tk.Button(root,text="OK",command=OK_cmd)
    Cancel_button = tk.Button(root,text="Cancel",command=Cancel_cmd)

    My_label.place(x=0.5*w/10,y=2*h/8)
    My_entry.place(x=4.5*w/10,y=2*h/8,height=30,width=5*w/10)
    OK_button.place(x=w/2-100,y=5*h/8)
    Cancel_button.place(x=w/2+50,y=5*h/8)
    root.mainloop()
    
    
    

def PythonStatsConsoleApp():
    print("Enter 1 for keyboard input, 2 for file input:", end = " ")
    mode = int(input())
    
    if mode == 1:    # data entered from keyboard
        print("When no more data is left to enter, simply hit return.")
        numlist = GetDataPointsFromConsole()
        
    elif mode == 2:    # data read from file
        numlist = GetDataPointsFromFile()
    
    else:
        print("Invalid mode; exiting program.")
        quit()
        
    n = len(numlist)
    if n > 0:
        PrintDataPoints(numlist)
        PrintOutStats(numlist)
    else:
        print("No data points to be analyzed.")


# --------------------------------------------------
# main body of PythonStats.py
# must define functions above before this is executed
nArgs = len(sys.argv)
#print("nArgs = %d, sys.argv[0] = %s" %(nArgs, sys.argv[0]))
if nArgs > 1:
    #print("sys.argv[1] = %s" %(sys.argv[1]))
    PythonStatsGUIApp(sys.argv[1])
else:
    PythonStatsConsoleApp()
    
# end main body of PythonStats.py    
# --------------------------------------------------



#  ----jGRASP exec: python3 PythonStats.py
# PythonStats is being run directly
# Enter 1 for keyboard input, 2 for file input: 1
# When no more data is left to enter, simply hit return.
# 6
# 1
# 5
# 2
# 4
# 3
# 
# Data point 1: 6.00
# Data point 2: 1.00
# Data point 3: 5.00
# Data point 4: 2.00
# Data point 5: 4.00
# Data point 6: 3.00
# 
# For 6 data point(s), 
#     the maximum is 6.00
#     the minimum is 1.00
#     the mean (average) is 3.50
#     the median is 3.50
#     the std dev is 1.87
# 
#  ----jGRASP: operation complete.
# 
#  ----jGRASP exec: python3 PythonStats.py
# PythonStats is being run directly
# Enter 1 for keyboard input, 2 for file input: 1
# When no more data is left to enter, simply hit return.
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 
# Data point 1: 7.00
# Data point 2: 6.00
# Data point 3: 5.00
# Data point 4: 4.00
# Data point 5: 3.00
# Data point 6: 2.00
# Data point 7: 1.00
# 
# For 7 data point(s), 
#     the maximum is 7.00
#     the minimum is 1.00
#     the mean (average) is 4.00
#     the median is 4.00
#     the std dev is 2.16
# 
#  ----jGRASP: operation complete.
# 
#  ----jGRASP exec: python3 PythonStats.py
# PythonStats is being run directly
# Enter 1 for keyboard input, 2 for file input: 1
# When no more data is left to enter, simply hit return.
# 3.4
# 
# Data point 1: 3.40
# 
# For 1 data point(s), 
#     the maximum is 3.40
#     the minimum is 3.40
#     the mean (average) is 3.40
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
#     the median is 60.00
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
