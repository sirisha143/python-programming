g=int(input("enter a number:"))
temp=g
rev=0
while(g>0):
    dig=g%10
    rev=rev*10+dig
    g=g//10
if(temp==rev):
    print("yes")
else:
    print("no")
