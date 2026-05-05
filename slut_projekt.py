questions = {
    "historia": [
        {
            "question": "Vem var Sveriges kung under 1600-talet?",
            "options": ["Gustav Vasa", "Karl XII", "Olof Palme", "Erik XIV"], 
            "answer": "Karl XII"
        },
        {
            "question": "Vilket år slutade andra världskriget?",
            "options": ["1945", "1918", "1919", "1960"],
            "answer": "1945"
        }
    ],
    "geografi": [
        {
            "question": "Vad heter Sveriges huvudstad?",
            "options": ["Göteborg", "Malmö", "Stockholm", "Uppsala"],
            "answer": "Stockholm"
        },
        {
            "question": "Vilket är världens största hav?",
            "options": ["Atlanten", "Indiska oceanen", "Stilla havet", "Arktiska oceanen"],
            "answer": "Stilla havet"
        }
    ],
     "general knowledge": [
        {
            "question": "Hur många dagar har ett år?",
            "options": ["364", "365", "366", "360"],
            "answer": "365"
        },
        {
            "question": "Vilket språk talas i Brasilien?",
            "options": ["Spanska", "Portugisiska", "Engelska", "Franska"],
            "answer": "Portugisiska"
        }
    ]
}


#Visa kategorier

def show_categories():
    print("Välj kategorier:")
    for category in questions:
        print("-", category)

# Kör quiz
def run_quiz(category):
    score = 0

    for q in questions[category]:
        print("\n" + q["question"])
        
        for option in q["options"]:
            print("-", option)
        try:
            answer = input("Ditt svar: ")

            if answer.lower() == q["answer"].lower():
                print("Rätt!")
                score += 1
            else:
                print("Fel! Rätt svar är:", q["answer"])

        except:
            print("Fel inmatning!")

    print("\nDin poäng:", score, "av", len(questions[category]))

  
  

#Huvudprogram

def main():
     show_categories()
     choice = input("\nSkriv kategori: ").lower()

     if choice in questions:
          run_quiz(choice)

     else:
          print("Ogiltig kategori!")

main()
