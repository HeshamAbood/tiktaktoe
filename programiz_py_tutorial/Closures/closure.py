''' 
what are closures good for?

Closures can avoid the use of global values and provides some form of data hiding. 
It can also provide an object oriented solution to the problem. '''

def print_msg(msg):
    # This is the outer enclosing function

    def printer():
# This is the nested function
        print(msg)

    return printer  # this got changed

# Now let's try calling this function.
# Output: Hello
another = print_msg("Hello")
another()
print (type(another))
print (type(another()))

''' The criteria that must be met to create closure in Python are summarized in the following points.

We must have a nested function (function inside a function).
The nested function must refer to a value defined in the enclosing function.
The enclosing function must return the nested function. '''


