import random
import time

correctAns=0
wrongAns=0

count=int(input("How many time should I do?"))
while count!=0:
    a=random.randint(3,9)
    b=random.randint(3,9)
    if a==5 or b==5:
        continue
    count=count-1
    print("%d X %d?" %(a,b))
    startTime=time.time()
    product=int(input())
    endTime=time.time()
    print("I answered in seconds %1.f"%(endTime-startTime))

    if product==a*b:
        correctAns=correctAns+1
        print("Right!\n")
    else:
        wrongAns=wrongAns+1
        print("Try again!\n")
print("Total response %d, correct %d times" %(correctAns+wrongAns, correctAns))