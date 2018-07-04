
import random
import sys
# Tworzy losowy kod


sprawdzenie = ["1", "2", "3", "4", "5", "6"]
dupa = True
gra = False

# Przywitanie
print("== Master Mind ==")
print("Zasady gry:\nW miejsce 'Podaj kod' wpisujesz 4 cyfry od 1 do 6.\n☻ oznacza, że pewna liczba jest trafiona i na "
      "odpowiednim miejscu.\nZ kolei ☺ oznacza trafioną cyfrę, ale w złym miejscu.\nKolejność emotikonek jest losowa.")

while dupa:

    proba = 0
    losy = ""
    los = ""
    wybor = ""
    odpowiedz = []

    for d in range(4):
        los = str((random.randrange(1,7)))
        losy += los
    #print(losy)

# Początek
    gra = True
    while gra:
        wybor = input("Podaj kod: ")

# Sprawdzenie poprawnosci kodu
        for litera in wybor:
            if litera not in sprawdzenie: # not in sprawdza cos w czyms
                print(litera)
                print(sprawdzenie)
                print("Zły kod")
                continue
        if len(wybor) != len(losy):
            print("Niepoprawna długość kodu")
            continue

        test = list(losy)

# Dodawanie emotikonek
        for i in range(4):
            if wybor[i] == losy[i]:
                test[i] = ""
                odpowiedz.append("☻")

        for i in range(4):
            if wybor[i] != losy[i] and wybor[i] in test:
                test[i] = ""
                odpowiedz.append("☺")
        random.shuffle(odpowiedz)
        odpowiedzi = ""
        for i in odpowiedz:
            odpowiedzi += i
        print(odpowiedzi)
        print()
        odpowiedz = []
        proba += 1
        if proba < 7:
            print("Pozostało ci", 10 - proba, "prób")
        elif proba == 8 or proba == 7:
            print("Pozostały ci", 10 - proba, "próby")
        elif proba == 9:
            print("Pozostała ci", 10 - proba, "próba")

# Przerwanie gry
        if proba == 10:
            print("Skończyły ci się próby")
            print("Szukany kod to:", losy)
            gra = False
        elif wybor == losy:
            print("Gratulacje! Udało ci się odgadnąć kod w", proba, "próbach")
            gra = False

# Nowa gra/Koniec gry
        if gra == False:
            print()
            koniec = input("Czy chcesz zacząć nową grę? Wpisz 'tak' lub 'nie'")
            if koniec == "tak":
                gra = False
            elif koniec == "nie":
                print("Koniec gry")
                sys.exit()