from os import system
system("clear") 

number=input("sonni kiriting\n")

count=0
for digit in number:
     if digit == '0':
          count=count+1
     
     if digit !='0':
          break;
     

print(count)
