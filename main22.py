a=int(input("enter a number"))
temp=a
length=0
while temp >0:
    temp=temp//10
    length=length+1
print("you have entered",length,"digit/s")