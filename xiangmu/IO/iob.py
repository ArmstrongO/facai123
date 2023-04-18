import threading
import time
# loop =20000000
# loopp=10000000
# x=0
# y=0
# def sum_1(count):
#     global x
#     for n in range ( count):
#         x+=n
#     print(f"sum_1:{x}")
#
# def sum_2(count):
#     global y
#     for n in range ( count ):
#         y+=n
#     print ( f"sum_2:{y}" )
# def sum_3( ):
#     global y
#     for n in range (1,10000):
#         y+=n
#     print ( f"sum_2:{y}" )
#
# t1=threading.Thread(target=sum_1,args=(loop,))
# t1.start()
#
# t2=threading.Thread(target=sum_2,args=(loopp,))
# t2.start()
# print(y)
# t3=threading.Thread(target=sum_3( ))
# t3.start()
# print(y)
loop=1000000000
x=0
def sum_3( count):
    global x
    for n in range (count):
        x+=n
    print ( f"sum_2:{x}" )
def sum_4( ):
    global y
    while 1:
        y-=1
y=0
def sum_5( ):
    global y
    for n in range (1,1000000000):
        y+=n
    print ( f"sum_2:{y}" )

t1 = threading.Thread(target=sum_3,args = (loop,))
t1.start()
t2 = threading.Thread(target=sum_5)
t2.start()
print(x)
print(y)

time.sleep(2)
print(x)
print(y)

time.sleep(2)
print(x)
print(y)

time.sleep(2)
print(y)
# t1.join()
print(y)

t1.join()

# print(z)
# time.sleep(2)
# print(y)
# print(z)