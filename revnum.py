reverse=''
N =input()
for i in range(len(N), 0, -1):
    reverse+=N[i-1]
print(int(reverse))
