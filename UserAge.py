def demander_nom():
    nom_reponse = ""
    while nom_reponse == "":
        nom_reponse = input("Quel est votre nom ? ")
    return nom_reponse
def demander_age():
    age_int = 0
    while age_int == 0 :
        age_str = input("Quel est votre âge ? ")
        try:
            age_int = int(age_str) 
        except:
            print("Erreur : Vous devez rentrer un nombre pour l'age")
    return age_int
    

# Demande de nom
nom = demander_nom()
# Demande d'âge
age = demander_age()
#Afficher les résultats
print("Vous êtes donc " + nom + " et vous avez " + str(age) + " ans.")
print("L'année prochaine, vous aurez donc " + str(age+1) + " ans.")
