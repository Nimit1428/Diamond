print("By Nimit Savant!")

h = input("Enter height(even) :")

h = int(h)

for i in range(1,h,2):
    print(" "*(h-int(i/2)),"*"*i)

l = h-3
b = h-1

for i in range(l,0,-2):
    print(" "*(b-int(i/2)+1),"*"*i)
