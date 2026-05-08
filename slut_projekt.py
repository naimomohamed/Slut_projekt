import random
import time
import requests
import json
import html


# =====================
# FILHANTERING (JSON)
# =====================
def skapa_fil_om_den_inte_finns():
    try:
        with open("highscore.json", "r", encoding="utf-8") as fil:
            json.load(fil)
    except:
        with open("highscore.json", "w", encoding="utf-8") as fil:
            json.dump([], fil)


def spara_score(namn, poang):
    try:
        with open("highscore.json", "r", encoding="utf-8") as fil:
            data = json.load(fil)
    except:
        data = []

    data.append({"name": namn, "score": poang})

    with open("highscore.json", "w", encoding="utf-8") as fil:
        json.dump(data, fil, indent=4, ensure_ascii=False)


def visa_highscore():
    try:
        with open("highscore.json", "r", encoding="utf-8") as fil:
            data = json.load(fil)

        if not data:
            print("Ingen highscore än.")
            return

        data.sort(key=lambda x: x["score"], reverse=True)

        print("\n--- TOP HIGH SCORES ---")
        for item in data[:5]:
            print(f"{item['name']} | {item['score']}")

    except:
        print("Fel vid läsning av highscore.")


def rensa_highscore():
    with open("highscore.json", "w", encoding="utf-8") as fil:
        json.dump([], fil)
    print("Highscore rensad!")


# =====================
# KLASSER (OOP + POLYMORFI)
# =====================
class BaseQuestion:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def ask(self):
        pass


class MultipleChoiceQuestion(BaseQuestion):
    def __init__(self, text, options, answer):
        super().__init__(text, answer)
        self.options = options

    def ask(self):
        print("\n" + self.text)

        for i, option in enumerate(self.options, 1):
            print(f"{i}. {option}")

        try:
            choice = int(input("Svar: "))

            if 1 <= choice <= len(self.options):
                if self.options[choice - 1].lower() == self.answer.lower():
                    print("Rätt! ")
                    return True
                else:
                    print("Fel! Rätt svar:", self.answer)
                    return False
            else:
                print("Ogiltigt val!")
                return False

        except ValueError:
            print("Du måste skriva en siffra!")
            return False


# =====================
# API HANDLER
# =====================
class APIHandler:
    def __init__(self):
        self.url = "https://opentdb.com/api.php"

    def get_questions(self, amount=5, difficulty="easy"):
        params = {
            "amount": amount,
            "type": "multiple",
            "difficulty": difficulty
        }

        try:
            response = requests.get(self.url, params=params)
            data = response.json()

            questions = []

            for item in data["results"]:
                options = item["incorrect_answers"] + [item["correct_answer"]]
                random.shuffle(options)

                questions.append(
                    MultipleChoiceQuestion(
                        html.unescape(item["question"]),
                        options,
                        html.unescape(item["correct_answer"])
                    )
                )

            return questions

        except:
            print("Fel vid API-anrop!")
            return []


# =====================
# QUIZ
# =====================
class Quiz:
    def __init__(self, namn):
        self.score = 0
        self.namn = namn

    def start(self, questions):
        self.score = 0
        start_time = time.time()

        for q in questions:
            if q.ask():
                self.score += 1

        end_time = time.time()
        self.show_result(end_time - start_time, len(questions))

    def show_result(self, time_used, total):
        print("\n--- RESULTAT ---")
        print(f"Namn: {self.namn}")
        print(f"Poäng: {self.score}/{total}")
        print(f"Tid: {round(time_used, 2)} sekunder")

        if self.score == total:
            print("Perfekt!")
        elif self.score > total / 2:
            print("Bra jobbat! ")
        else:
            print("Öva mer! ")

        spara_score(self.namn, self.score)


# =====================
# LOKALA FRÅGOR
# =====================
def get_local_questions():
    return [
        MultipleChoiceQuestion(
            "Vad är Sveriges huvudstad?",
            ["Göteborg", "Stockholm", "Malmö", "Uppsala"],
            "Stockholm"
        ),
        MultipleChoiceQuestion(
            "Hur många spelare i fotboll?",
            ["9", "10", "11", "12"],
            "11"
        )
    ]


# =====================
# HUVUDPROGRAM
# =====================
def main():
    skapa_fil_om_den_inte_finns()
    api = APIHandler()

    namn = input("Skriv ditt namn: ")

    print(f"\nHej {namn}!")
    start = input("Vill du starta quizet? (ja/nej): ").lower()

    if start != "ja":
        print(f"Hejdå {namn}!")
        return

    while True:
        print(f"\n=== QUIZ MASTER ({namn}) ===")
        print("1. Lokala frågor")
        print("2. API frågor")
        print("3. Visa highscore")
        print("4. Rensa highscore")
        print("5. Avsluta")

        choice = input("Val: ")

        if choice == "1":
            quiz = Quiz(namn)
            quiz.start(get_local_questions())

        elif choice == "2":
            difficulty = input("Välj svårighet (easy/medium/hard): ").lower()

            if difficulty not in ["easy", "medium", "hard"]:
                print("Ogiltig svårighet!")
                continue

            questions = api.get_questions(5, difficulty)

            if questions:
                quiz = Quiz(namn)
                quiz.start(questions)

        elif choice == "3":
            visa_highscore()

        elif choice == "4":
            rensa_highscore()

        elif choice == "5":
            print(f"Hejdå {namn}! ")
            break

        else:
            print("Ogiltigt val!")


main()