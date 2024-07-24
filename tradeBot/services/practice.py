import threading
from typing import Set
set1={1,2,3}

def printName():
    print("Name",threading.current_thread().name)

Threads=[]
for i in range(6):
    thread=threading.Thread(target=printName())
    Threads.append(thread)
    thread.start()

for item in Threads:
    item.join()

