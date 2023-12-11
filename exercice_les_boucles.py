# EXERCICE 1

# while True:
#     number = int(input("Donnez un chiffre entre 1 & 3 : "))

#     if 1 <= number <=3:
#         print("Vous avez saisi un chiffre valide :", number)
#         break
#     else:
#         print("Le chiffre doit être entre 1 et 3. Veuillez réessayer.")



# EXERCICE 2

# while True:
#      number = int(input("Donnez un nombre compris entre 10 et 20 : "))

#      if 10 <= number <= 20:
#          print("Le nombre saisi est valide")
#          break

#      elif number < 10:
#          print("Plus grand !")

#      elif number > 20:
#          print("Plus petit !")



# EXERCICE 3 avec WHILE

# number = int(input("Donnez un nombre de départ : "))
# suite_number = number  #Je stock la valeur de number dans suite_number pour avoir ma condition de sortie de la boucle

# while number <= suite_number + 10:
#     print(number)
#     number = number + 1


# EXERCICE 3 avec FOR

# number = int(input("Donnez un nombre de départ : "))

# for number in range(number + 1, number + 11):
#     print (number)
#     number + 1



# EXERCICE 4

languages =  ["Python", "Javascript", "Java", "PHP", "C++", "Cobol"]

for index in range(0,5):
    print (languages[index])