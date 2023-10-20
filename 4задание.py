class Airline:
    def __init__(self, name, fuel_consumption, cargo_capacity):
        self.name = name
        self.fuel_consumption = fuel_consumption
        self.cargo_capacity = cargo_capacity

    def get_name(self):
        return self.name

    def get_fuel_consumption(self):
        return self.fuel_consumption

    def get_cargo_capacity(self):
        return self.cargo_capacity


#Создаем объекты-самолеты и помещаем их в список
airplanes = [
    Airline("Boeing 747", 50, 10000),
    Airline("Airbus A380", 60, 15000),
    Airline("Boeing 737", 40, 8000),
    Airline("Embraer E190", 30, 5000),
]

#Подсчитываем общую грузоподъемность
total_cargo_capacity = sum(airplane.get_cargo_capacity() for airplane in airplanes)
print("Общая грузоподъемность:", total_cargo_capacity)

#Находим самолеты, соответствующие заданному диапазону потребления горючего
min_fuel_consumption = 40
max_fuel_consumption = 60

matching_airplanes = [
    airplane.get_name()
    for airplane in airplanes
    if min_fuel_consumption <= airplane.get_fuel_consumption() <= max_fuel_consumption
]
print("Самолеты с потреблением горючего от", min_fuel_consumption, "до", max_fuel_consumption, "л/км:")
for airplane in matching_airplanes:
    print("-", airplane)