from os import system
from json import dumps

system("cls")

bigger_price_2 = [
    {'name': "bread", 'price': 15},
    {'name': "wine", 'price': 138},
    {'name': "meat", 'price': 100},  
    {'name': "water", 'price': 5}
]



bigger_price_2.sort(key=lambda x: x['price'], reverse=True)

print(dumps(bigger_price_2,indent=2))




hisob_raqam = int(input("Pulni kiriting: "))





olingan_tovarlar = {}
for mahsulot in bigger_price_2:
    mahsulot_name = mahsulot['name']
    mahsulot_count = 0


    while mahsulot['price'] <= hisob_raqam: 
         
        if mahsulot_name in olingan_tovarlar:
            olingan_tovarlar[mahsulot_name] += 1
        else:
            olingan_tovarlar[mahsulot_name] = 1
        hisob_raqam -= mahsulot['price']  

print("Olingan tovarlar:", dumps(olingan_tovarlar,indent=2))

print("Qolgan summa:", hisob_raqam)
