class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (f"Biblioteka: {self.city}, ul. {self.street} {self.zip_code} "
                f"(Czynne: {self.open_hours}, Tel: {self.phone})")


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (f"Pracownik: {self.first_name} {self.last_name} "
                f"(Zatrudniony: {self.hire_date}, Adres: {self.city}, {self.street})")


class Student:
    def __init__(self, first_name, last_name, index_number):
        self.first_name = first_name
        self.last_name = last_name
        self.index_number = index_number

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name} (Indeks: {self.index_number})"


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f"Książka: '{self.author_name} {self.author_surname}' ({self.publication_date}), "
                f"{self.number_of_pages} stron. \n\t-> Własność: {self.library}")


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        opis_ksiazek = ""
        for b in self.books:
            opis_ksiazek += f"\n\t* {b.author_name} {b.author_surname} ({b.publication_date})"

        return (f"--- ZAMÓWIENIE z dnia {self.order_date} ---\n"
                f"Obsługuje: {self.employee}\n"
                f"Dla: {self.student}\n"
                f"Wypożyczone pozycje:{opis_ksiazek}\n"
                f"----------------------------------------")

lib_warszawa = Library("Warszawa", "Marszałkowska 1", "00-001", "8:00-16:00", "22-111-22-33")
lib_krakow = Library("Kraków", "Floriańska 15", "30-002", "10:00-18:00", "12-333-44-55")


emp1 = Employee("Jan", "Kowalski", "2020-01-01", "1990-05-12", "Warszawa", "Złota 5", "00-002", "500-100-100")
emp2 = Employee("Anna", "Nowak", "2021-03-15", "1995-07-20", "Warszawa", "Chmielna 2", "00-003", "500-200-200")
emp3 = Employee("Piotr", "Wiśniewski", "2019-11-01", "1985-12-12", "Kraków", "Długa 10", "30-005", "600-300-300")


stud1 = Student("Kasia", "Kaczyńska", "12345")
stud2 = Student("Tomek", "Cesarz", "67890")
stud3 = Student("Monika", " Kozak", "54321")


book1 = Book(lib_warszawa, "2001", "J.K.", "Rowling", 300)
book2 = Book(lib_warszawa, "1954", "J.R.R.", "Tolkien", 500)
book3 = Book(lib_krakow, "1949", "George", "Orwell", 250)
book4 = Book(lib_krakow, "1890", "Bolesław", "Prus", 800)
book5 = Book(lib_warszawa, "2023", "Remigiusz", "Mróz", 400)

order1 = Order(emp1, stud1, [book1, book2], "2025-06-01")

order2 = Order(emp3, stud2, [book4], "2025-06-02")


print(order1)
print()
print(order2)
