# Créons une autre variable pour décider du fonctionnement ou de l'arret du scrip
FonctionnementScript = 0
# Testons les valeurs saisies par l'utilisateur
while FonctionnementScript == 0:
    surnom = input("Entrez votre surnom : ")
    if not surnom.isalpha():
        print("Vous devez saisir une suite de lettres formant votre surnom")
        FonctionnementScript == 0
    else:
        print("Bonjour", surnom + ",", "merci d'avoir tester mon script")
        FonctionnementScript == 1
        break
