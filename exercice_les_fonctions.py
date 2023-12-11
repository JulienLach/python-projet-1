# EXERCICE 1

# def function_helloworld():
#     return ("Bonjour tout le monde")    

# print(function_helloworld())    

# def function_helloworld():
#     print("Bonjour tout le monde")    

# var = function_helloworld()
# print(var)



# EXERCICE 2

# def function_helloYou(first_name):
#      print("Bonjour", first_name)

# first_name = input("Quel est votre nom ? ")

# function_helloYou(first_name)


# EXERCICE 3

# def function_average (number_1, number_2):
#     return (number_1 + number_2) / 2

# number_1 = float(input("Entre le premier nombre : "))
# number_2 = float(input("Entre le deuxième nombre : "))

# resultat = function_average(number_1, number_2)

# print("Le calcul est le suivant : ",number_1,"+",number_2,"/ 2. ","le résultat est le suivant",resultat,)
# print(f"le calcul est le suivant : {number_1} + ....." )

# EXERCICE 4

def function_my_calcul(operation, *numbers):
    if operation == "addition":
        result = sum(numbers)
    elif operation == "soustraction":
        result = numbers[0] - sum(numbers[1:])     
    return result

resultat_de_laddition = function_my_calcul("addition", 10, 10, 10, 10)
resultat_de_la_soustraction = function_my_calcul("soustraction", 10, 3, 3)

print(resultat_de_laddition)
print(resultat_de_la_soustraction)
