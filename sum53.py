e=int(input(" "))
total=0
while(e>0):
    dig=e%10
    total=total+dig
    e=e//10
print(" ",total)
