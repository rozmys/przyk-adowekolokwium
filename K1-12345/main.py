from court import Court

def main():
    court_1 = Court(year_built=1999, address="Słoneczna 10, 10-100 Olsztyn")
    court_2 = Court(100, 500, "Słoneczna 10, 10-100 Olsztyn", 1999)
    print(court_1)
    print(court_2)


if __name__ == '__main__':
    main()
