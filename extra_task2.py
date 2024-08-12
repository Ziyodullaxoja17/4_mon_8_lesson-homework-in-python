from os import system 
from json import dumps

system("cls")

ls = []

number = int(input("Ishtirokchilar soni kiriting => "))

for i in range(number):
    odam = {}
    odam["ism"] = input("Ismni kiriting => ")
    odam["vote"] = int(input("Ovozlar sonini kiriting => "))
    ls.append(odam)

print("Ishtirokchilar va ovozlar ro'yxati:")
print(dumps(ls, indent=2))


max_vote = ls[0]["vote"]
winners = [ls[0]["ism"]]


for person in ls[1:]:
    if person['vote'] > max_vote:
        max_vote = person['vote']
        winners = [person['ism']]  

    elif person['vote'] == max_vote:
        winners.append(person['ism'])  




if len(winners) > 1:
    print("Maksimal ovoz yutgan kishilar:")
    for winner in winners:
        print(f"Name: {winner} \nVote: {max_vote}")
    print("\nTeng natija qayd etildi!")
else:
    print("Maksimal ovoz yutgan kishi:")
    print(f"Name: {winners[0]} \nVote: {max_vote}")
