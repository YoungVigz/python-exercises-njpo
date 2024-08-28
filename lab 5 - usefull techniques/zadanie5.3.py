import json

def print_menu():
    print("\nMENU:")
    print("1. Dodaj wiersz")
    print("2. Usuń wiersz")
    print("3. Zmień pole wiersza")
    print("4. Wyświetl bazę danych")
    print("5. Wyjście")

def add_row(database):
    print("\nDodaj nowy wiersz:")
    key = input("Podaj klucz: ").strip()
    value = input("Podaj wartość: ").strip()

    if key in database:
        print("Wiersz z tym kluczem już istnieje.")
    else:
        database[key] = value
        print("Wiersz dodany.")

def delete_row(database):
    key = input("\nPodaj klucz wiersza do usunięcia: ").strip()
    
    if key in database:
        del database[key]
        print("Wiersz usunięty.")
    else:
        print("Nie znaleziono wiersza o podanym kluczu.")

def update_row(database):
    key = input("\nPodaj klucz wiersza do zmiany: ").strip()
    
    if key in database:
        new_value = input("Podaj nową wartość: ").strip()
        database[key] = new_value
        print("Wiersz zaktualizowany.")
    else:
        print("Nie znaleziono wiersza o podanym kluczu.")

def display_database(database):
    print("\nBaza danych:")
    if not database:
        print("Baza danych jest pusta.")
    else:
        print(json.dumps(database, indent=4))

def main():
    database = {}
    while True:
        print_menu()
        choice = input("\nWybierz opcję: ").strip()

        if choice == '1':
            add_row(database)
        elif choice == '2':
            delete_row(database)
        elif choice == '3':
            update_row(database)
        elif choice == '4':
            display_database(database)
        elif choice == '5':
            print("Wyjście z programu.")
            break
        else:
            print("Niepoprawny wybór, spróbuj ponownie.")

if __name__ == "__main__":
    main()
