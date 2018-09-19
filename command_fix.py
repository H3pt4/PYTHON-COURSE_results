#! /usr/bin/env python3
import sys, getopt

arguments = sys.argv
print(arguments)
try:
    opts, args = getopt.getopt(arguments[1:],"hi:o:",["infile=","outfile="])
except getopt.GetoptError as errorInfo:
    print(errorInfo)
else:
    for opt, arg in opts:
        if (opt == "-h"):
            print("Usage")
            print(arguments[0], "-i input -o output")
            print(arguments[0], "--infile=input --outfile=output")
        else:
            print(opt, arg)
finally:
    print("Programm beendet")
