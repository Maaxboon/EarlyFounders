#!/usr/bin/env python

# if x == 1:
#   var = 20
#else:
#   var = 30
x = 2
var = (20 if x == 1 else 30)
print("var:", var)

# A if condition else B

print("x has value 1" if x == 1 else "x is unequal to 1")

# Complex Complex conditional expression
a = 4
b = 3
xyz = (a * 2 if (a > 10 and b < 5) else b * 2)
print("xyz = ", xyz)
