max_score = int(input("Podaj maksymalna ilosc punktow do zdobycia: "))
score = int(input("Podaj zdobyte punkty: "))
result = int((score * 100) / max_score)

def test_calc(result):
    print(f"Uzyskales:  {result}%")
    print(f"Ocena {mark}")

if result < 30:
    mark = "niedostateczna (1)"
elif result < 50:
    mark = "dopuszczajca (2)"
elif result < 75:
    mark =  "dostateczna (3)"
elif result < 85:
    mark =  "dobra (4)"
elif result < 95:
    mark =  "bardzo dobra (5)"
elif result > 95:
    mark =  "celujaca (6)"
if result > 100:
    print("Podaj poprawne dane!")

test_calc(result)
