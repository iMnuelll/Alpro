class Car1 :
    #Constructor
    def __init__(self, name,factory,type) :
        self.name = name
        self.factory = factory
        self.type = type
        self.fuel = 100

    #Mobil Sebelum Terjual
    def print_infostock(self):
        print(f'Car Name : {self.name}')
        print(f'Car Factory : {self.factory}')
        print(f'Car Type : {self.type}')
        print(f'Car Fuel : {self.fuel}')
        print('Car on Stock !')

    #Mobil setelah terjual
    def print_infosold(self):
        print(f'Car Name : {self.name}')
        print(f'Car Factory : {self.factory}')
        print(f'Car Type : {self.type}')
        print(f'Car Fuel : {self.fuel}')
        print('Car is sold')
        
    #Methods for car can running
    def run(self):
        print(f'\nCar is running \nCar fuel : {self.fuel - 10}')

if __name__ == '__main__' :
    car = Car1('Fortuner','Toyota','SUV')
    car.print_infostock()
    car.run()

    answer = input("Do you want to buy this car ? Y/N : ")
    if answer == 'Y' : 
        car = Car1('Fortuner','Toyota','SUV')
        car.print_infosold()
        car.run()
    else : 
        car = Car1('Fortuner','Toyota','SUV')
        car.print_infostock()
        car.run()