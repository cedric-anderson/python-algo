numbers = []
    
while True:
    try:
        users = int(input("Saisissez un nombre entre 0 et 20 (ou -1 pour quitter): "))
        if users == -1:
            if not numbers:
                print("Aucun nombre n'a été saisi.")
            else:
                min_number = min(numbers)
                max_number = max(numbers)
                
                occurrences = {}
                for i in range(21):
                    occurrences[i] = numbers.count(i)

                print(f"Nombre minimal: {min_number}")
                print(f"Nombre maximal: {max_number}")
                print("Occurrences de chaque nombre:")
                for number, count in occurrences.items():
                    if count > 0:
                        print(f"{number}: {count} fois")
            break
        elif 0 <= users <= 20:
            numbers.append(users)
        else:
            print("Veuillez saisir un nombre entre 0 et 20.")
    except ValueError:
        print("Entrée invalide. Veuillez saisir un nombre entier.")

