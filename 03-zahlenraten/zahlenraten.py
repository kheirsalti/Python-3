import random

numm = random.randint(1 , 20)

print("Hallo User Enter a nummer between 1 - 20")
user_nummer =int(input("Can you guess the nummber"))
if user_nummer > numm:
    print("Zu gross")
elif user_nummer < numm:
    print("Zu klein")
    
else: 
    print("Richtig geraten!")



