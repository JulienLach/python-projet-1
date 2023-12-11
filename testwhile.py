# EXERCICE 2

number = int(input("Donnez un nombre compris entre 10 et 20 : "))

while number < 10 or number > 20:
    if number < 10:
        print("Plus grand!")
    else: 
        print("Plus petit!")
    number = int(input("Donnez un nombre compris entre 10 et 20 : "))
