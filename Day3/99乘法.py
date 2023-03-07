c=[]
for i in range ( 1, 10 ):
    for ii in range ( 1, 10 ):
        c.append ( i*ii )
        # print(i*ii)
    pass
print(c)

for i in range(1, 10):
    for j in range(1, 1+i):
        print(f"{j}*{i}={j * i}",end='  ')
    print()
