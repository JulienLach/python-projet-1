print("-- algo 1  --")

a = 5
b = 3
c = a + b

print(c)

a = 2
c = b - 4

print(c)

print("-- algo 2  --")

a = 5
b = a + 4
a = a + 1
b = a - 4

print(b)

print("-- algo 3  --")

a = 3
b = 10
c = a + b
b = a + b
a = c

print(a)

print("-- algo 4  --")

a = 5
b = 2
a = b
b = a

print(b)


print("-- algo échange de variables avec 2 variables  --")
a = 1
b = 2

a = b
b = a

print (a, b)



print("-- algo échange de variables avec 3 variables  --")

a = 1
b = 2
c = 3

b = a
c = b
a = c

print(a ,b ,c)


print("-- algo Calcul du carré  --")

Valeur = input("Entez la valeur : ")

Valeur = int(Valeur)

Carré_de_la_valeur = Valeur * Valeur

print(Carré_de_la_valeur)


print("-- Prix du panier  --")

prix_article_hors_taxes = input("Prix hors taxes de l'article : ")
quantité_article = input("Nombre d'articles : ")
TVA_article = input("TVA : ")

prix_article_hors_taxes = int(prix_article_hors_taxes)
quantité_article = int(quantité_article)
TVA_article = float(TVA_article)

Prix_TTC = (prix_article_hors_taxes * TVA_article + prix_article_hors_taxes) * quantité_article

print(f"Prix TTC : ", Prix_TTC)