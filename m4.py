from os import system
system("cls")

matn=input("matnni kiriting  => ")



left_hand=['q','a','z','w','s','x','e','d','c','r','f','v','t','g','b','1','2','3','4']

right_hand=['6','7','y','u','h','j','m','n','8','i','k',',','9','o','l','.','0','p',';','/','-','=','[',']','"','?' ]

harflar=[]
chap_hand=[]
ong_hand=[]


for harf in matn:

     harf=harf.lower()

     harflar.append(harf)


print("jami harflar : =>" ,harflar)


for letter in harflar:
     if letter in left_hand:
          chap_hand.append(letter)
     elif letter in right_hand :
          ong_hand.append(letter)



print("o'ng barmoqda : => ", ong_hand)
print("chap barmoqda : => ", chap_hand)

print(f"o'ng qolda {len(ong_hand)} \n chap qolda {len(chap_hand)}")


