# --- LECTURE ---
table_eleves = []

with open("eleves.csv", "r", encoding="utf-8") as f:
    champs1 = f.readline().rstrip().split(";")
    
    for ligne in f:
        liste = ligne.rstrip().split(";")
        table_eleves.append(liste)

# print(table_eleves)

table_questions = []

with open("questions.csv", "r", encoding="utf-8") as f:
    champs2 = f.readline().rstrip().split(";")
    
    for ligne in f:
        liste = ligne.rstrip().split(";")
        table_questions.append(liste)

# print(table_questions)

import random
poursuite=True

def sauvegarde(increment,choix_eleve):
    table_mod = []
    for t in table_eleves:
        if t[0] == choix_eleve:
            if increment=="plus":
                t[1]=str(float(t[1])+1)
            else:
                t[1]=str(float(t[1])-1)
        table_mod.append(t)
    with open("eleves.csv", "w", encoding="utf-8") as f:
        f.write(";".join(champs1) + "\n")
        for ligne in table_mod:
            f.write(";".join(str(x) for x in ligne) + "\n")
            
def lecture(choix_eleve):
    table_eleves = []

    with open("eleves.csv", "r", encoding="utf-8") as f:
        champs1 = f.readline().rstrip().split(";")
        
        for ligne in f:
            liste = ligne.rstrip().split(";")
            table_eleves.append(liste)
    for ligne in table_eleves:
        if ligne[0]==choix_eleve:
            return ligne[1]

while poursuite:
    question=random.choice(table_questions)
    eleve=random.choice(table_eleves)
    choix_question=question[0]
    choix_reponse=question[1]
    choix_eleve=eleve[0]
    choix_note=eleve[1]
    print("Eleve choisi :",choix_eleve)
    print("Question :",choix_question)
    reponse=input("Réponse : ")
    if reponse==choix_reponse:
        print("✅ Bonne réponse !")
        sauvegarde("plus",choix_eleve)
        print("nouvelle note de ",choix_eleve," : ",lecture(choix_eleve))
    else:
        print("❌ Mauvaise réponse")
        print("La réponse était",choix_reponse)
        sauvegarde("moins",choix_eleve)
        print("nouvelle note de ",choix_eleve," : ",lecture(choix_eleve))
        
    


# # --- MODIFICATION D'UN ELEMENT (exemple) ---
# # On change la capitale de l'Autriche
# table_mod = []
# for t in table:
#     if t[0] == "Autriche":
#         t = (t[0], t[1], t[2], t[3], "Capitale modifiée")
#     table_mod.append(t)
# 
# # --- ÉCRITURE ---
# with open("Tableau_capitales.csv", "w", encoding="utf-8") as f:
#     f.write(";".join(champs) + "\n")
#     for ligne in table_mod:
#         f.write(";".join(str(x) for x in ligne) + "\n")
# 
# print("Fichier réécrit.")