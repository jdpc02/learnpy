"""
 Generate a base64 random string
"""
#!/usr/bin/python
__author__ = 'dev'
import sys, os, base64

# defaults
intdeflen = 10

if len(sys.argv) <= 1:
    print("Defaulting to {0}".format(intdeflen))
    print("python {0} <length of random base64 string>".format(sys.argv[0]))
else:
    try:
        intdeflen = int(sys.argv[1])
    except:
        print("The parameter {0} is not an integer".format(sys.argv[1]))
        sys.exit("Invalid parameter")

print("Generating {0} base64 random string".format(intdeflen))
print("{0}".format(base64.b64encode(os.urandom(int(intdeflen)))))
