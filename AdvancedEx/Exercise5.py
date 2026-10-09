import random
import time

from Chapter5.ex73.libs.my_module import calculate

correctAns=0
wrongAns=0

duplicateListA=[]
duplicateListB=[]

limitTime=45
count=int(input("How many times should I do?"))
while count!=0:
    a=random.randint(3,9)
    b=random.randint(3,9)
    if a==5 or b==5:
        continue
    isDuplicated=False
    for i in range(len(duplicateListA)):
        if duplicateListA[i]==a and duplicateListB[i]==b:
            isDuplicated=True
            break
    if isDuplicated==True:
        continue
    else:
        duplicateListA.append(a)
        duplicateListB.append(b)
    count=count-1
    print("%d X %d?" % (a, b))
    startTime = time.time()
    product = int(input())
    endTime = time.time()
    calculateTime=endTime-startTime
    print("I answered in second %1.f" %calculateTime)
    if calculateTime > limitTime:
        print("You took long time to answer, limit time is", limitTime,
              "second you answered in %1.f second" %calculateTime)
        if product==a*b and calculateTime<=limitTime:
            correctAns=correctAns+1
            print("Right!\n")
        else:
            wrongAns=wrongAns+1
            print("Try again!\n")
print("Total response %d, correct %d times"
      %(correctAns+wrongAns, correctAns))