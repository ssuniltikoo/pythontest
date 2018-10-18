from threading import Thread
import time
__doc__="""implementaion of threading"""


def sum(x,y,z):
    print("started sum thread with delay",z)
    while z > 0:
        print(x+y)
        z-=1
    print("finished sum Thread with starting number",x)


def sub(x,y):
    print("started sub")
    print(x - y)
    time.sleep(2)
    print("finished sub")
def Main():
    t1=Thread(target=sum, args=(1,1,100))
    print("T1 thread started")
    t2=Thread(target=sum, args=(4,1,10))
    print("T2 thread started")
    #t1=Timer(5.0,sum(1,1))
    #t2=Timer(2.0,sub(5,1))
    t1.start()
    t2.start()

    print("program completed")

if __name__ =="__main__":
    print(__doc__)
    Main()


