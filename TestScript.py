#Création de la première variable
surnom = input("Entrez votre surnom : ")

#Testons les valeurs saisies par l'utilisateur
if surnom == "":
    print("Vous devez absolument saisir votre surnom")
elif not surnom.isalpha():
    print("Vous devez saisir une suite de lettres formant votre surnom")
else :
    print("Bonjour",surnom, "merci d'avoir tester mon script")
