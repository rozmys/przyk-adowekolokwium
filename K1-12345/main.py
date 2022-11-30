from court import Court
from stadium import Stadium
def main():
    court_1 = Court(year_built=1999, address="Słoneczna 10, 10-100 Olsztyn")
    court_2 = Court(100, 500, "Słoneczna 10, 10-100 Olsztyn", 1999)
    print(court_1)
    print(court_2)
    court_3 = Court(50, 100, "Słoneczna 10, 10-100 Olsztyn", 1999)
    print(court_3)
    print(court_1.length)
    court_1.year_built = 1990
    print(court_1)
    print(court_1.area())
    court_1.year_built = 2030
    print(court_1)
    Court.validate(court_1)
    print(court_1)
    stadium_1 = Stadium(50, 100, "Słoneczna 10, 10-100 Olsztyn", 1999, "Słoneczny stadion", "Słoneczko", 10000)
    print(stadium_1)
    stadium_2 = Stadium(width = 50, length=100, address="Słoneczna 10, 10-100 Olsztyn", year_built=1999, name="Słoneczny stadion", capacity=10000)
    print(stadium_2)
    stadium_1.year_built = 2030
    print(stadium_1)
    Court.validate(stadium_1)
    print(stadium_1)
    print(stadium_1 == stadium_2)
    stadium_1.width = 50
    stadium_1.length = 100
    print(stadium_1 == stadium_2)
    print(stadium_1 != stadium_2)
    stadium_1.capacity = 500
    print(stadium_1 == stadium_2)

if __name__ == '__main__':
    main()
