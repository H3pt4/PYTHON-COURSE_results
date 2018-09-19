#! /usr/bin/env python3
import sys, getopt

arguments = sys.argv
print(arguments)
opts, args = getopt.getopt(arguments[1:],"hi:o:",["infile=","outfile="])
for opt, arg in opts:
    if (opt == "-h"):
        print("Usage")
        print(arguments[0], "-i input -o output")
        print(arguments[0], "--infile=input --outfile=output")
    else:
        print(opt, arg)
