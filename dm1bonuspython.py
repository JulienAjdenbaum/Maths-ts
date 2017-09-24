n = int(input("entrer n :"))
u = int(input("entrer U0 :"))
s = u
for i in range(1,n+1):
    u = s/(s-1)
    s += u
print("U(",n,") = ",round(u,3),sep="")
