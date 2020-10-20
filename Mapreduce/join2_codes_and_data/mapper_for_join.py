#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip() #strip is a method,with string variable, it will strip the carriage return (by defautl)
    key_value = line.split(",")
    key_in = key_value[0]
    value_in = key_value[1]
    if value_in == "ABC" or value_in.isdigit():
        print('%s\t%s'%(key_in, value_in))
