from threading import *
def sum(x,y):
    print("started sum")
    print(x+y)
    print("finished sum")

def sub(x,y):
    print("started sub")
    print(x - y)
    print("finished sub")


t1=sum(10,3)
t2=sub(6,1)

t1.start()
t2.start()


from threading import *

class cal():

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def sum(self):
        print("started sum")
        print(self.x+self.y)
        print("finished sum")

    def sub(self):
        print("started sub")
        print(self.x - self.y)
        print("finished sub")

if __name__=="__main__":
    c1=cal(5,1)
    c1.sum()
    c1.sub()
