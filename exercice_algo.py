# Définition de la fonction de tri

def function_tri_bulle(list): #en paramètre le tableau à trier
    nombres = len(list) #la fonction prend tous les nombres de la liste à parcourir

    for x in range(nombres): #deuxième nombre à attraper dans le tableau
        for y in range(0, nombres-x-1): #premier nombre à attraper dans le tableau = (x) - 1 dans la range  du premier au suivant
    
            if list[y] > list[y+1] :
                list[y], list[y+1] = list[y+1], list[y]


#EXEMPLE DE TABLEAU

list = [56, 5, 2, 1, 8, 22, 15, 32, 74, 6, 7, 4]

function_tri_bulle(list)

print("ok")
for y in range(len(list)):
    print (list[y])
