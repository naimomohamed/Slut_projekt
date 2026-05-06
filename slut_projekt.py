import random

high_scores = []


class Quiz:
    def __init__(self):
        self.score = 0

        self.categories = {
            "1": ("Historia", [
                ("När började första världskriget?", ["1914", "1939", "1900", "1920"], "1914"),
                ("Vem upptäckte Amerika?", ["Columbus", "Newton", "Einstein", "Darwin"], "Columbus"),
                ("När slutade andra världskriget?", ["1945", "1939", "1918", "1960"], "1945")
            ]),

            "2": ("Geografi", [
                ("Vad är Sveriges huvudstad?", ["Göteborg", "Stockholm", "Malmö", "Uppsala"], "Stockholm"),
                ("Vilket är största havet?", ["Atlanten", "Indiska oceanen", "Stilla havet", "Arktiska"], "Stilla havet"),
                ("Vilket land är störst?", ["Sverige", "Ryssland", "USA", "Kina"], "Ryssland")
            ]),

            "3": ("General Knowledge", [
                ("Hur många dagar har ett år?", ["364", "365", "366", "360"], "365"),
                ("Vilket språk talas i Brasilien?", ["Spanska", "Portugisiska", "Engelska", "Franska"], "Portugisiska"),
                ("Hur många ben har en spindel?", ["6", "8", "10", "12"], "8")
            ]),

            "4": ("Sport", [
                ("Hur många spelare i fotboll?", ["9", "10", "11", "12"], "11"),
                ("Vilken sport har puck?", ["Tennis", "Fotboll", "Ishockey", "Basket"], "Ishockey"),
                ("Hur många perioder i hockey?", ["2", "3", "4", "5"], "3")
            ]),

            "5": ("Random", [
                ("Blå + gul blir?", ["Grön", "Röd", "Lila", "Orange"], "Grön"),
                ("Hur många ben har en katt?", ["2", "4", "6", "8"], "4"),
                ("Vad är 2+2?", ["3", "4", "5", "6"], "4")
            ])
        }

    def choose_category(self):
        print("\nVälj kategori:")

        for key, value in self.categories.items():
            print(key + ".", value[0])

        choice = input("Val: ")

        if choice in self.categories:
            return self.categories[choice][1]
        else:
            print("Fel val!")
            return None

    def play(self, questions, name):
        self.score = 0
        random.shuffle(questions)

        print("\n--- Quiz startar ---")

        for i, (text, options, answer) in enumerate(questions[:10], 1):
            print(f"\n{i}. {text}")

            for j in range(len(options)):
                print(f"{j+1}. {options[j]}")

            try:
                user = int(input("Svar: "))

                if 1 <= user <= 4 and options[user - 1].lower() == answer.lower():
                    print("Rätt!")
                    self.score += 1
                else:
                    print("Fel! Rätt svar:", answer)

            except:
                print("Fel inmatning!")

        print("\n--- KLAR ---")
        print(name, "du fick", self.score, "av", len(questions[:10]), "rätt!")

        high_scores.append((name, self.score))


def main():
    while True:
        print("\n=== QUIZ ===")
        print("1. Starta quiz")
        print("2. Avsluta")

        choice = input("Val: ")

        if choice == "1":
            name = input("Skriv ditt namn: ")

            quiz = Quiz()
            questions = quiz.choose_category()

            if questions:
                quiz.play(questions, name)

                again = input("\nVill du spela igen? (ja/nej): ").lower()

                if again != "ja":
                    print("Hejdå!")
                    break

        elif choice == "2":
            print("Hejdå!")
            break

        else:
            print("Ogiltigt val!")


main()