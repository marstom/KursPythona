from builder import Builder
from engine import StandardEngine, SportEngine


class Director:
    """
    He knows some car recipes!
    """

    def make_sports_car(self, builder: Builder):
        builder.reset()
        builder.set_seats(2)
        builder.set_engine(SportEngine())
        builder.set_trip_computer()

    def make_suv(self, builder: Builder):
        builder.reset()
        builder.set_seats(5)
        builder.set_engine(StandardEngine())
        builder.set_gps()
        builder.set_trip_computer()
