max_score = int(input("Podaj maksymalna ilosc punktow do zdobycia: "))
score = int(input("Podaj zdobyte punkty: "))
result = int((score * 100) / max_score)

def test_calc(result):
    print(f"Uzyskales:  {result}%")

if result < 30:
    print("Ocena niedostateczna (1)")
elif result < 50:
    print("Ocena dopuszczajca (2)")
elif result < 75:
    print("Ocena dostateczna (3)")
elif result < 85:
    print("Ocena dobra (4)")
elif result < 95:
    print("Ocena bardzo dobra (5)")
elif result > 95:
    print("Ocena celujaca (6)")
    

test_calc(result)
