blist=['Americano', 'Cafe Latte', 'Cappuccino', 'Oranges', 'CocaCola', 'Grapefruit']
plist=[2500, 3000, 3000, 4000, 1500, 4000]
blistUserChoose=[]
plistUserChoose=[]
print("No.", "Food Name\tPrice")
for i in range (len(blist)):
    print(i+1,'.',blist[i],'\t',plist[i])
print("Please tell me the drink you ordered.")
while True:
    noFoodName=0
    while noFoodName<=0 or noFoodName > len(blist):
        strnoFoodName=input("Please choose the food name(enter number)[{}-{}]):".format(1, len(blist)))
        if strnoFoodName.isdigit():
            noFoodName=int(strnoFoodName)
        else:
            noFoodName=0
    blistUserChoose.append(noFoodName)
    noQuantity=0
    while noQuantity<=0:
        strnoQuantity = input("Please enter quantity[>0]:")
        if strnoQuantity.isdigit():
            noQuantity=int(strnoQuantity)
        else:
            noQuantity=0
    plistUserChoose.append(noQuantity)
    question=input("Do you want to choose another food? (yes/no):")
    if question=='no':
        break
print("The list of ordered food/drink:")
sum=0
print("Food Name\tPrice\tQuantity\tMoney")
for i in range(len(blistUserChoose)):
    foodName=blist[blistUserChoose[i]-1]
    quantity=plistUserChoose[i]
    unitPrice=plist[blistUserChoose[i]-1]
    money=quantity*unitPrice
    sum=sum+money
    print(foodName,'\t',unitPrice,"\t",quantity,"\t\t\t",money)
print("\tThe total amount is:\t",sum,"money")
money=0
while True:
    strmoney=input("Enter the amount to be paid >>")
    if strmoney.isdigit()==False:
        print(strmoney, "is not valid, it should be a digit number")
    else:
        money=int(strmoney)
        if money<0:
            print("is not valid number, it should be positive")
        else:
            if money<sum:
                print("Not enough money, you have to pay", sum, "money")
            else:
                print("Paid is successfully!")
                if money>sum:
                    print("Change is",money-sum,"money")
                break
print("Thank you so much! see you again!")
