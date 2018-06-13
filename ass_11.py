#1
from threading import Timer,Thread,Event
class perpetualTimer():
    def __init__(self,t,hFunction):
      self.t=t
      self.hFunction = hFunction
      self.thread = Timer(self.t,self.handle_function)
    def handle_function(self):
      self.hFunction()
      self.thread = Timer(self.t,self.handle_function)
      self.thread.start()
    def start(self):
      self.thread.start()
    def cancel(self):
      self.thread.cancel()
    def printer():
        print('ipsem lorem')
t = perpetualTimer(5,printer)
t.start()

#2

import time
from threading import Thread
def sleepMe(i):
    print("Thread %i." %(i+1))
    time.sleep(1)
for i in range(10):
    th=Thread(target=sleepMe,args=(i,))
    th.start()

#3
import time
from threading import Thread
def sleepMe(i,B):
    time.sleep(B)
    print("Thread %i." %(i))

a=[0,6,8,9]
B=2
for i in a:
    th=Thread(target=sleepMe,args=(i,B,))
    th.start()

#4
def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)
