from os import system 
system("cls")


ls=[]

shart=True

while shart:
     num=int(input("son kiriting => "))

     ls.append(num)


     word=input("yana son kiritasizmi ?  ha / yoq   =>  ")
     if word == 'ha' and isinstance(num , int):
          shart=True
     elif word == 'yoq':
          shart=False
     else:
          print("xato buyruq")
          break;


print(ls)


 

for num in ls:
    if num+1 in ls:
        print(num, num+1)


        









