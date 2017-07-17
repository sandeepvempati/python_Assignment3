# class Test:
#     pass
#
# t = Test()
# t.x = 10
#
# print  t.x

class Test:
    def __init__(self,x):
        self.x = x

t = Test(10)
print t.x