n = 1  

while n <= 10:
    if n % 2 == 0:  
        print(n)  
    n += 1




nom = input("Entrez votre nom : ")
nom = nom.upper() # convvertire une chaine de caractere en maj

age = input("Entrez votre âge : ")
taille = input("Entrez votre taille : ")


fruits = input("Entrez une liste de fruits préférés : ")
#fruits_liste = fruits.split(".")  # Divise la chaîne en une liste



#un message de salutation
# messag = "bonjour"+ " "+ nom + " "+ "vous avez" + age + " "+"ans et musurez " + taille +" " + " cm. Vos fruits préférés sont :"+ fruits_liste
message = f"Bonjour {nom} ! Vous avez {age} ans et mesurez {taille} cm.Vos fruits préférés sont : {fruits}."


# Afficher le message de salutation
print(message)
#print(messag)
