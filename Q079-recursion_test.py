"""
Q079-recursion test
08.26.2019
When I'm debugging Q079, it seems calling a class method
recursively will alter the value of the interior variable.
I'm testing the problem here and see what I can do to change
it.
"""

class RecursionTest():

    a = 0

    def add(self, a):

        if a == 5:
            return 0
        print(a)
        self.add(a+1)


inst = RecursionTest()

inst.add(0)








