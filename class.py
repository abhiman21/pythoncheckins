"""
A simple calss without much blah blah defining a variable and a function
sdome wisdom bytes
The instantiation operation (“calling” a class object) creates an empty object. Many classes like to create objects with instances customized to a specific initial state. Therefore a class may define a special method named __init__(), like this:

def __init__(self):
    self.data = []
When a class defines an __init__() method, class instantiation automatically invokes __init__() for the newly-created class instance. So in this example, a new, initialized instance can be obtained by:

x = MyClass()

Of course, the __init__() method may have arguments for greater flexibility. In that case, arguments given to the class instantiation operator are passed on to __init__(). For example,

>>>
>>> class Complex:
...     def __init__(self, realpart, imagpart):
...         self.r = realpart
...         self.i = imagpart
...
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)i
"""

class no_blah_blah:
    i=123
    def abc(self):
        str="go to heaven hell is full"
        return str 
# Defining an object x to class no_blah_blah
 
x=no_blah_blah()
print (x.i)
a=x.abc()
print (a)

 
