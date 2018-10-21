class A:
    def __init__(self,x=0):
        self._var=x

n=A(4)
print(n._var)
x=A()
print(x._var)