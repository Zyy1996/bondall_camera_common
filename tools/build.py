#!/usr/bin/python3
import getopt
import sys

def func_help():
    print("build.py [option]\n"
          "-h,--help   Help doc\n"
          "-s,--mod_s= Single module compilation\n"
          "-a,--mod_a  Compile all module\n"
          "-l          show the modules that need to be compiled\n")

def func_single_mod():
    print("single compile module")

def func_all_mod():
    print("quiet compile module")

def func_show_mod():
    print("show all module")

def get_params(list):
    opt,args=getopt.getopt(list,"hs:a",["help","mod_s=","mod_a"])
    if(opt==[]):
        func_help()
        return
    if opt[0][0] == '-h':
        func_help()
    elif opt[0][0] == '-s' or opt[0][0] == '-s':
        func_single_mod()
    elif opt[0][0] == '-a' or opt[0][0] == '--mod_a':
        func_all_mod()
    elif opt[0][0] == '-l':
        func_show_mod()
    else:
        func_help()

if __name__=="__main__":
    get_params(sys.argv[1:])
    