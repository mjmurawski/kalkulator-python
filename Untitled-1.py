def dodawanie(x, y):
    return x + y

def odejmowanie(x, y):
    return x - y

def mnozenie(x, y):
    return x * y

def dzielenie(x, y):
    if y != 0:
        return x / y
    else:
        return "Nie można dzielić przez zero."

while True:
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Wyjście")

    choice = input("Wpisz numer operacji (1/2/3/4/5): ")

    if choice == '5':
        print("Zakończono program.")
        break

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Wpisz pierwszą liczbę: "))
            num2 = float(input("Wpisz drugą liczbę: "))
        except ValueError:
            print("Wprowadzono nieprawidłową liczbę.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", dodawanie(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", odejmowanie(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", mnozenie(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", dzielenie(num1, num2))
    else:
        print("Nieprawidłowy wybór. Wybierz liczbę od 1 do 5.")
