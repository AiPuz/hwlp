# -- coding: utf-8 --

# 命名、变量、代码、函数

# this one is like your scripts with argv

def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg):
    print "arg: %r" % arg

# this just takes one argument
def print_none():
    print "i got nothin"

print_two("Aed", "shaw")
print_two_again("adf", "dafsa")
print_one("afaf")
print_none()
