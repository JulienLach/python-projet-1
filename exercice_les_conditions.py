# EXERCICE 1

# user_number = int(input("Nombre d'utilisateurs : "))

# if user_number > 0:
#     print("Le nombre d'utilisateur est positif")

# EXERCICE 2

# first_number = float(input("Premier nombre : "))
# second_number = float(input("Deuxième nombre : "))


# if first_number * second_number > 0:
#     print("Le résultat est positif")

# else : print("Le résultat est négatif")


# EXERCICE 3

# age = int(input("Quel est votre âge ? : "))

# if 8 <= age <= 9:
#     print("Microbe")
# elif 10 <= age <= 11:
#     print("Poussin")
# elif 12 <= age <= 13:
#     print("Benjamine/benjamin")
# elif 14 <= age <= 15:
#     print("Minime")
# elif 16 <= age <= 17:
#     print("Cadette/cadet")
# elif 18 <= age <= 19:
#     print("Junior")
# elif 20 <= age <= 39:
#     print("Sénior")
# elif age >= 40:
#     print("Vétérane/vétéran")


# EXERCICE 4

number_pages = int(input("Nombre de photocopie : "))

if number_pages <= 10:
    price = number_pages * 0.10
    print("Le prix total est de :", price ,"€" )
elif 11 <= number_pages <= 30:
    price = number_pages * 0.09
    print("Le prix total est de :", price ,"€" )
elif number_pages >= 31:
    price = number_pages * 0.08
    print("Le prix total est de :", price ,"€" )
