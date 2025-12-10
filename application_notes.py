import csv
import random

FICHIER_ELEVES = "eleves.csv"
FICHIER_QUESTIONS = "questions.csv"

# Paramètres de modification de note
INCREMENT = 1      # +1 si bonne réponse
DECREMENT = 1      # -1 si mauvaise réponse
NOTE_MIN = 0
NOTE_MAX = 20

def charger_eleves(fichier):
    eleves = []
    with open(fichier, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # conversion de la note en entier ou float
            row["note"] = float(row["note"])
            eleves.append(row)
    return eleves

def sauvegarder_eleves(fichier, eleves):
    with open(fichier, "w", newline='', encoding='utf-8') as f:
        champs = ["eleve", "note"]
        writer = csv.DictWriter(f, fieldnames=champs)
        writer.writeheader()
        for e in eleves:
            writer.writerow({"eleve": e["eleve"], "note": e["note"]})

def charger_questions(fichier):
    questions = []
    with open(fichier, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            questions.append(row)
    return questions

def poser_question(eleves, questions):
    # Choix aléatoire d'un élève et d'une question
    eleve = random.choice(eleves)
    question = random.choice(questions)

    print(f"\nÉlève choisi : {eleve['eleve']}")
    print("Question :", question["question"])
    reponse_eleve = input("Réponse : ").strip()

    # Vérification (on peut comparer en minuscules pour être tolérant)
    bonne_reponse = question["reponse"].strip()

    if reponse_eleve.lower() == bonne_reponse.lower():
        print("✅ Bonne réponse !")
        eleve["note"] = min(NOTE_MAX, eleve["note"] + INCREMENT)
    else:
        print(f"❌ Mauvaise réponse. La bonne réponse était : {bonne_reponse}")
        eleve["note"] = max(NOTE_MIN, eleve["note"] - DECREMENT)

    print(f"Nouvelle note de {eleve['eleve']} : {eleve['note']}\n")

def main():
    eleves = charger_eleves(FICHIER_ELEVES)
    questions = charger_questions(FICHIER_QUESTIONS)

    continuer = "o"
    while continuer.lower() == "o":
        poser_question(eleves, questions)
        continuer = input("Poser une nouvelle question ? (o/n) : ")

    # Sauvegarde des notes mises à jour
    sauvegarder_eleves(FICHIER_ELEVES, eleves)
    print("Notes sauvegardées dans", FICHIER_ELEVES)

if __name__ == "__main__":
    main()