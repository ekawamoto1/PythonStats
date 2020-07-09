# PythonStats.py
import sys
import math
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
print(sys.version)
if __name__ == "__main__":  
    print("PythonStats is being run directly") 
else:  
    print("PythonStats is being imported")
print("")
    

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
    outStr = ""
    if m > 0:
        if m < 10:
            i = 0
            for y in inList:
                i += 1
                outStr += "Data point {0:d}: {1:.2f}\n".format(i, y)
        else:
            for i in range(0, 5):
                outStr += "Data point {0:d}: {1:.2f}\n".format(i+1, inList[i])
            outStr += "     ...\n"
            for i in range(m - 5, m):
                outStr += "Data point {0:d}: {1:.2f}\n".format(i+1, inList[i])
                
    return outStr
    

def PrintOutStats(inList):
    n = len(inList)
    avg = ComputeMean(inList)
    extremes = ComputeExtremes(inList)
    outStr = "\nFor {0:d} data point(s)".format(n)
    outStr += "\n    the maximum is {0:.2f}".format(extremes[1])
    outStr += "\n    the maximum is {0:.2f}".format(extremes[0])
    outStr += "\n    the mean (average) is {0:.2f}".format(avg)
    if n > 1:
        med = ComputeMedian(inList)
        outStr += "\n    the median is {0:.2f}".format(med)
        stdev = ComputeStdev(inList, avg)
        outStr += "\n    the std dev is {0:.2f}".format(stdev)
        
    return outStr


def GetDataPointsFromConsole():
    numlist = []
    i = 0
    while True:
        i += 1
        outStr = "Data point {0:d}:".format(i)
        print(outStr, end = " ")
        x = input()
        if x == "":
            break
        else:
            y = float(x)
            #print("You entered %d" %y)
            numlist.append(y)
    return numlist
    

def GetDataPointsFromFile(fName):
    numlist = []
    if fName == "":
        print("\nEnter pathname of data file:", end = " ")
        fName = input()
    try:
        f = open(fName, "r")
        for line in f:    # this reads all lines of file (even blank ones) to the very end
            line1 = line.strip('\n')    # each line of f comes with \n, which must be stripped
            if len(line1) > 0:    # blank lines are ignored
                numlist.append(float(line1))
        f.close()

    except IOError:    # if error on attempt to open file (e.g., doesn't exist, etc.)
        print("File %s does not exist." %fName)
        quit()
        
    return numlist
    

def PythonStatsGUIApp(arg):
    def OK_cmd():
        x = My_entry.get()
        #print("x = %s, arg = %s" %(x,arg))
        root.withdraw()    # close window after OK button is clicked and text field is read
        if int(arg) == 1:
            #print("process data points")
            if x != "":
                sList = x.split(",")
                numlist = []
                for xx in sList:
                    numlist.append(float(xx))
                print(numlist)
            else:
                print("No data points to be analyzed.")
                quit()
            
        elif int(arg) == 3:
            quit()
            
        n = len(numlist)
        if n > 0:
            s1 = PrintDataPoints(numlist)
            s2 = PrintOutStats(numlist)
            s3 = s1 + "\n" + s2
            w2 = 250
            h2 = 360
            geom_str2 = "{}x{}+{}+{}".format(w2,h2,xp,yp)
            root2 = tk.Toplevel()
            root2.geometry(geom_str2)
            root2.title("Stats")
            My_label = tk.Label(root2,text=s3)
            My_label.place(x=0.5*w2/10,y=0)
            OK_button = tk.Button(root2,text="OK",command=OK_cmd2)
            OK_button.place(x=w2/2-35,y=8.7*h2/10)
            root2.bind('<Return>', lambda event: OK_cmd2())
            root2.mainloop()
            #print(s3)
        else:
            print("No data points to be analyzed.")
        quit()
                
    def Cancel_cmd():
        quit()
        
    def OK_cmd2():
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
        My_entry = tk.Entry(root)    
        OK_button = tk.Button(root,text="OK",command=OK_cmd)
        Cancel_button = tk.Button(root,text="Cancel",command=Cancel_cmd)
    
        My_label.place(x=0.5*w/10,y=2*h/8)
        My_entry.place(x=4.5*w/10,y=2*h/8,height=30,width=5*w/10)
        OK_button.place(x=w/2-100,y=5*h/8)
        Cancel_button.place(x=w/2+50,y=5*h/8)
        root.bind('<Return>', lambda event: OK_cmd())
        root.mainloop()

    elif int(arg) == 2:    # read data points from file
        root.overrideredirect(True)
        root.geometry('0x0+0+0')    # these two lines hide the root window
        root.focus_force()    # this forces AskOpenFilename dialog to have focus
        fName = fd.askopenfilename(initialdir=".",title="Select file",filetypes=(("txt files","*.txt"),("all files","*.*")))
        #print(fName)
        if fName == "":
            quit()
            
        numlist = GetDataPointsFromFile(fName)
        n = len(numlist)
        if n > 0:
            s1 = PrintDataPoints(numlist)
            s2 = PrintOutStats(numlist)
            s3 = s1 + "\n" + s2
            w2 = 250
            h2 = 360
            geom_str2 = "{}x{}+{}+{}".format(w2,h2,xp,yp)
            root2 = tk.Toplevel()
            root2.geometry(geom_str2)
            root2.title("Stats")
            My_label = tk.Label(root2,text=s3)
            My_label.place(x=0.5*w2/10,y=0)
            OK_button = tk.Button(root2,text="OK",command=OK_cmd2)
            OK_button.place(x=w2/2-35,y=8.7*h2/10)
            root2.bind('<Return>', lambda event: OK_cmd2())
            root2.mainloop()
            #print(s3)
        else:
            print("No data points to be analyzed.")
        quit()
        
    else:    # invalid command-line argument
        root.title("Error")
        Cancel_button = tk.Button(root,text="Cancel",command=Cancel_cmd)
        My_label = tk.Label(root,text="invalid command-line argument")
        My_label.place(x=0.5*w/10,y=2*h/8)
        Cancel_button.place(x=w/2-40,y=5*h/8)
        root.bind('<Return>', lambda event: Cancel_cmd())
        root.mainloop()


def PythonStatsConsoleApp():
    print("Enter 1 for keyboard input, 2 for file input:", end = " ")
    mode = int(input())
    
    if mode == 1:    # data entered from keyboard
        print("\nWhen no more data is left to enter, simply hit return.")
        numlist = GetDataPointsFromConsole()
        s = ""
        
    elif mode == 2:    # data read from file
        numlist = GetDataPointsFromFile("")
        s = PrintDataPoints(numlist)
        
    else:
        print("Invalid mode; exiting program.")
        quit()
        
    n = len(numlist)
    if n > 0:
        s += PrintOutStats(numlist)
        print(s)
    else:
        print("No data points to be analyzed.")


# --------------------------------------------------
# main body of PythonStats.py
# must define functions above before this is executed

# get command-line arguments, if any
nArgs = len(sys.argv)
#print("nArgs = %d, sys.argv[0] = %s" %(nArgs, sys.argv[0]))

# if command-line arg is supplied, run GUI version
if nArgs > 1:
    #print("sys.argv[1] = %s" %(sys.argv[1]))
    PythonStatsGUIApp(sys.argv[1])
# otherwise, run console version
else:
    PythonStatsConsoleApp()
    
# end main body of PythonStats.py    
# --------------------------------------------------




#  ----jGRASP exec: python3 PythonStats.py
# 3.8.3 (default, Jul  7 2020, 02:06:50) 
# [Clang 11.0.3 (clang-1103.0.32.62)]
# PythonStats is being run directly
# 
# Enter 1 for keyboard input, 2 for file input: 1
# 
# When no more data is left to enter, simply hit return.
# Data point 1: 6
# Data point 2: 1
# Data point 3: 5
# Data point 4: 2
# Data point 5: 4
# Data point 6: 3
# Data point 7: 
# 
# For 6 data point(s)
#     the maximum is 6.00
#     the maximum is 1.00
#     the mean (average) is 3.50
#     the median is 3.50
#     the std dev is 1.87
# 
#  ----jGRASP: operation complete.
# 
#  ----jGRASP exec: python3 PythonStats.py
# 3.8.3 (default, Jul  7 2020, 02:06:50) 
# [Clang 11.0.3 (clang-1103.0.32.62)]
# PythonStats is being run directly
# 
# Enter 1 for keyboard input, 2 for file input: 1
# 
# When no more data is left to enter, simply hit return.
# Data point 1: 7
# Data point 2: 6
# Data point 3: 5
# Data point 4: 4
# Data point 5: 3
# Data point 6: 2
# Data point 7: 1
# Data point 8: 
# 
# For 7 data point(s)
#     the maximum is 7.00
#     the maximum is 1.00
#     the mean (average) is 4.00
#     the median is 4.00
#     the std dev is 2.16
# 
#  ----jGRASP: operation complete.
# 
#  ----jGRASP exec: python3 PythonStats.py
# 3.8.3 (default, Jul  7 2020, 02:06:50) 
# [Clang 11.0.3 (clang-1103.0.32.62)]
# PythonStats is being run directly
# 
# Enter 1 for keyboard input, 2 for file input: 1
# 
# When no more data is left to enter, simply hit return.
# Data point 1: 3.4
# Data point 2: 
# 
# For 1 data point(s)
#     the maximum is 3.40
#     the maximum is 3.40
#     the mean (average) is 3.40
# 
#  ----jGRASP: operation complete.
# 
#  ----jGRASP exec: python3 PythonStats.py
# 3.8.3 (default, Jul  7 2020, 02:06:50) 
# [Clang 11.0.3 (clang-1103.0.32.62)]
# PythonStats is being run directly
# 
# Enter 1 for keyboard input, 2 for file input: 1
# 
# When no more data is left to enter, simply hit return.
# Data point 1: 
# No data points to be analyzed.
# 
#  ----jGRASP: operation complete.
# 
#  ----jGRASP exec: python3 PythonStats.py
# 3.8.3 (default, Jul  7 2020, 02:06:50) 
# [Clang 11.0.3 (clang-1103.0.32.62)]
# PythonStats is being run directly
# 
# Enter 1 for keyboard input, 2 for file input: 2
# 
# Enter pathname of data file: testdata1.txt
# Data point 1: 60.00
# Data point 2: 62.00
# Data point 3: 57.00
# Data point 4: 58.00
# Data point 5: 68.00
#      ...
# Data point 6: 65.00
# Data point 7: 63.00
# Data point 8: 59.00
# Data point 9: 60.00
# Data point 10: 58.00
# 
# For 10 data point(s)
#     the maximum is 68.00
#     the maximum is 57.00
#     the mean (average) is 61.00
#     the median is 60.00
#     the std dev is 3.50
# 
#  ----jGRASP: operation complete.
# 
#  ----jGRASP exec: python3 PythonStats.py
# 3.8.3 (default, Jul  7 2020, 02:06:50) 
# [Clang 11.0.3 (clang-1103.0.32.62)]
# PythonStats is being run directly
# 
# Enter 1 for keyboard input, 2 for file input: 2
# 
# Enter pathname of data file: testdata2.txt
# Data point 1: 23.50
# 
# For 1 data point(s)
#     the maximum is 23.50
#     the maximum is 23.50
#     the mean (average) is 23.50
# 
#  ----jGRASP: operation complete.
# 
#  ----jGRASP exec: python3 PythonStats.py
# 3.8.3 (default, Jul  7 2020, 02:06:50) 
# [Clang 11.0.3 (clang-1103.0.32.62)]
# PythonStats is being run directly
# 
# Enter 1 for keyboard input, 2 for file input: 2
# 
# Enter pathname of data file: testdata3.txt
# No data points to be analyzed.
# 
#  ----jGRASP: operation complete.
# 
#  ----jGRASP exec: python3 PythonStats.py
# 3.8.3 (default, Jul  7 2020, 02:06:50) 
# [Clang 11.0.3 (clang-1103.0.32.62)]
# PythonStats is being run directly
# 
# Enter 1 for keyboard input, 2 for file input: 2
# 
# Enter pathname of data file: testdata4.txt
# File testdata4.txt does not exist.
# 
#  ----jGRASP: operation complete.
# 
