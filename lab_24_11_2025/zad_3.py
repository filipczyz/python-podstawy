class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = int(rooms)
        self.price = price
        self.address = address

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = int(plot)

    def __str__(self):
            return (f"--- DOM ---\n"
                    f"Adres: {self.address}\n"
                    f"Powierzchnia: {self.area} m2, Pokoje: {self.rooms}\n"
                    f"Wielkość działki: {self.plot} m2\n"
                    f"Cena: {self.price} PLN")
class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (f"--- MIESZKANIE ---\n"
                f"Adres: {self.address}\n"
                f"Powierzchnia: {self.area} m2, Pokoje: {self.rooms}\n"
                f"Piętro: {self.floor}\n"
                f"Cena: {self.price} PLN")

dom_1 = House(area=150, rooms=5, price=850000, address="ul. Leśna 5, Będzin", plot=600)
mieszkanie_1 = Flat(area=65, rooms=3, price=450000, address="ul. Główna 12/4, Sosnowiec", floor=2)
print(dom_1)
print()
print(mieszkanie_1)

