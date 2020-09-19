NumList = []
Num=int(input("Please enter the total number of elements present in the list:"))
for i in range(0,Num):
    val=int(input("Please enter the value of the %d Element: "%i))
    NumList.append(val)

print("Positive Numbers in the list are : ")
for j in range (Num):
    if(NumList[j] > 0):
        print(NumList[j],end=' ')
