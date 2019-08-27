"""
Q079-recursion test
08.26.2019
When I'm debugging Q079, it seems calling a class method
recursively will alter the value of the interior variable.
I'm testing the problem here and see what I can do to change
it.

The result of test:
yes, unlike C, python doesn't create a new closed space
every time a class method is called.
I would guess if the method is @staticmethod, it would behave
similar to C.

This must have something to do with the famous saying that
"we are all consenting adults."
And python allows very open access to all the variables within
a class.

The solution I came up with:
I will just use the same variable to work at the recursion.
I just need to adjust the value of the variable every time
a recursion takes place or a recursion is finished.

I could also make the method static. Didn't go for it 'cause
it's gonna be a lot of arguments passed to the funciton.
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








