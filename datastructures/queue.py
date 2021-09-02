# queue=[]
# top=0
# n=0
# size=int(input("enter size"))
# def insersion():
#     global top,size
#     if top>size:
#         print("queque is full")
#     else:
#         p=int(input("enter the element to insert"))
#         queue.append(p)
#         top+=1
# def deletion():
#     global top,size
#     if top<=0:
#         print("queue is empty")
#     else:
#         queue.pop(0)
#         top-=1
# def display():
#     print(queue)
# while n!=1:
#     print("enter the equation want to perform")
#     opt=int(input("press1)insertion 2)deletion 3 display"))
#     if(opt==1):
#         insersion()
#     elif opt==2:
#         deletion()
#     elif opt==3:
#         display()
#     n=int(input("do you want to continue press 1 for exit"))
#
#


que= []
size=int(input("enter the size"))
front=0
rear=0
n=0
def insert():
    global front,rear,size,que
    if rear>=size:
        print("queue is full")
    else:
        p=int(input("enter the element want to insert"))
        que.insert(rear,p)
        rear+=1
        for i in range(front,rear):
            print(que[i])
def delete():
    global front,rear,size,que
    if rear==front:
        print("queue is empty")
    else:
        front+=1
        for i in range(front,rear):
            print(que[i])
while n!=1:
    print("-----------------------enter the operatin wnat to perform ----------")
    print("enter the equation want to perform")
    opt=int(input("press1)insertion 2)deletion"))
    if(opt==1):
        insert()
    elif opt==2:
        delete()

