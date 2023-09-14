from director import Director
from builder import CarBuilder, CarManualBuilder

if __name__ == '__main__':
    director = Director()
    car_builder = CarBuilder()
    # director.make_sports_car(car_builder)
    director.make_suv(car_builder)
    car = car_builder.get_product()
    print(car)


    car_manual_builder = CarManualBuilder("Man title")
    # director.make_sports_car(car_manual_builder)
    director.make_suv(car_manual_builder)
    manual = car_manual_builder.get_product()
    print(manual)
