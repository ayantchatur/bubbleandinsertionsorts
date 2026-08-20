mylist =[12,34,2,5,7,18028308128318238, -1, 67]
n=len(mylist)

for i in range(n):
    print("Pass:",i+1)
    swapped=False
    for j in range(n-1,0,-1):
        if mylist[j] > mylist[j-1]:
            swapped = True
            temp=mylist[j]
            mylist[j]=mylist[j-1]
            mylist[j-1]=temp
            print(mylist)

    if not swapped:
        break

print("*"*20)