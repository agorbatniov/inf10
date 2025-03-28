try:
    age = int(input("Įveskite amžių: "))  # Pabandykite konvertuoti įvestį į sveikąjį skaičių
except ValueError:  # Jei įvestis nėra skaičius
    print("Įvestas neteisingas amžius. Įveskite skaičių.")  # Pranešimas klaidos atveju
