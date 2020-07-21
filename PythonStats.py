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
    

class Dataset:
    numPts = 0
    mean = 0.0
    dList = []
    
    def __init__(self, dList):
        self.numPts = len(self.dList)
        
    def GetNumPts(self):
        return len(self.dList)
        
    def ClearArray(self):
        self.dList.clear()
    
    def AddArray(self, inList):
        self.dList = inList

    def GetArray(self):
        return self.dList

    def AddPoint(self, x):
        self.dList.append(float(x))
        
    def GetPoint(self, i):
        pt = 0.0
        self.numPts = len(self.dList)
        if i >= 0 and i < self.numPts:
            pt = self.dList[i]
        return pt
    
    def ComputeExtremes(self):
        out = []
        max = -float('inf')
        min = float('inf')
        self.numPts = len(self.dList)
        for x in self.dList:
            if x > max:
                max = x
            if x < min:
                min = x
        out = [min, max]
        return out
    
    def ComputeMean(self):
        self.numPts = len(self.dList)
        sum = 0.0
        if self.numPts > 0:
            for term in self.dList:
                sum += term
            self.mean = sum / self.numPts
        return self.mean
        
    def ComputeStdev(self):
        self.numPts = len(self.dList)
        stdev = 0.0
        if self.numPts > 1:
            sum = 0.0
            for x in self.dList:
                term = x - self.mean
                sum += term * term
            stdev = math.sqrt(sum / (self.numPts - 1))
        else:
            stdev = math.nan
        return stdev
   
    def ComputeMedian(self):
        self.numPts = len(self.dList)
        median = 0.0
        if self.numPts > 1:
            self.dList.sort()
            m0 = self.numPts // 2;
            if self.numPts % 2 == 0:
                median = (self.dList[m0 - 1] + self.dList[m0]) / 2
            else:
                median = self.dList[m0]
        return median            


def PrintDataPoints(ds):
    m = ds.GetNumPts()
    outStr = ""
    if m > 0:
        if m < 10:
            i = 0
            for i in range(0, m):
                y = ds.GetPoint(i)
                outStr += "Data point {0:d}: {1:.2f}\n".format(i+1, y)
        else:
            for i in range(0, 5):
                y = ds.GetPoint(i)
                outStr += "Data point {0:d}: {1:.2f}\n".format(i+1, y)
            outStr += "     ...\n"
            for i in range(m - 5, m):
                y = ds.GetPoint(i)
                outStr += "Data point {0:d}: {1:.2f}\n".format(i+1, y)
                
    return outStr
    

def PrintOutStats(ds):
    n = ds.GetNumPts()
    avg = ds.ComputeMean()
    extremes = ds.ComputeExtremes()
    outStr = "\nFor {0:d} data point(s)".format(n)
    outStr += "\n    the maximum is {0:.2f}".format(extremes[1])
    outStr += "\n    the maximum is {0:.2f}".format(extremes[0])
    outStr += "\n    the mean (average) is {0:.2f}".format(avg)
    if n > 1:
        med = ds.ComputeMedian()
        outStr += "\n    the median is {0:.2f}".format(med)
        stdev = ds.ComputeStdev()
        outStr += "\n    the std dev is {0:.2f}".format(stdev)
        
    return outStr


def GetDataPointsFromConsole():
    ds = Dataset([])
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
            ds.AddPoint(y)
    return ds
    

def GetDataPointsFromFile(fName):
    ds = Dataset([]);
    if fName == "":
        print("\nEnter pathname of data file:", end = " ")
        fName = input()
    try:
        f = open(fName, "r")
        for line in f:    # this reads all lines of file (even blank ones) to the very end
            line1 = line.strip('\n')    # each line of f comes with \n, which must be stripped
            if len(line1) > 0:    # blank lines are ignored
                ds.AddPoint(float(line1))
        f.close()

    except IOError:    # if error on attempt to open file (e.g., doesn't exist, etc.)
        print("File %s does not exist." %fName)
        quit()
        
    return ds
    

def PythonStatsGUIApp(arg):
    def OK_cmd():
        x = My_entry.get()
        #print("x = %s, arg = %s" %(x,arg))
        root.withdraw()    # close window after OK button is clicked and text field is read
        if int(arg) == 1:
            #print("process data points")
            if x != "":
                sList = x.split(",")
                ds = Dataset([])
                for xx in sList:
                    ds.AddPoint(float(xx))
                print(ds.dList)
            else:
                print("No data points to be analyzed.")
                quit()
            
        elif int(arg) == 3:
            quit()
            
        n = ds.GetNumPts()
        if n > 0:
            s1 = PrintDataPoints(ds)
            s2 = PrintOutStats(ds)
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
            
        ds = GetDataPointsFromFile(fName)
        n = ds.GetNumPts()
        if n > 0:
            s1 = PrintDataPoints(ds)
            s2 = PrintOutStats(ds)
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
        ds = GetDataPointsFromConsole()
        s = ""
        
    elif mode == 2:    # data read from file
        ds = GetDataPointsFromFile("")
        s = PrintDataPoints(ds)
        
    else:
        print("Invalid mode; exiting program.")
        quit()
        
    n = ds.GetNumPts()
    if n > 0:
        s += PrintOutStats(ds)
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
