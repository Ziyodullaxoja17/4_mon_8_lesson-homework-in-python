from os import system
from json import dumps
system("cls")

number=input("sonni kiriting ")


print(number)

raqamlar={}


for raqam in number:
     if raqam not in raqamlar:
          raqamlar[raqam]=1
     else:
          raqamlar[raqam]+=1


print(raqamlar)
sorted_digit_counts = {key: raqamlar[key] for key in sorted(raqamlar.keys())}
print(dumps(sorted_digit_counts,indent=4))






     

