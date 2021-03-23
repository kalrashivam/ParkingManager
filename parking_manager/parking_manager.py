from parking_slot import ParkingSlot
from vehicle import Vehicle


class ParkingManager:
    """
    Performs CRUD and conditional operations on objects related to
    parking_slot and Vehicle class.
    """

    def __init__(self):
        self.parking_slots = {}

    def check_parking_slots(self):
        if len(self.parking_slots) == 0:
            print "Parking not initiated"
            return False

        return True

    def create_parking(self, slots):
        """
        Creates a parking with a given no. of slots as input.

        Input:-
            slots - Integer
        """

        slots = int(slots)

        if len(self.parking_slots.keys()) > 0:
            print "Parking already exists"
            return

        if slots > 0:
            for slot in range(slots):
                self.slots[slot] = ParkingSlot(slot_no=i)

            print('Created Parking of {} slots'.format(slots))

        return

    def park(self, vehicle_number, driver_age):
        """
        Provides a slot for the vehicle and creates the vehicle object.

        Input:-
            Vehicle Number - String
            Driver_age - Integer
        """

        if not self.check_parking_slots:
            return

        available_slots = filter(
            lambda x: x.is_available, self.parking_slots.values()
        )

        if not available_slots:
            return None

        available_slot = sorted(available_slots, key=lambda x: x.slot_no)[0]

        if available_slot:
            # create car object and save in the available slot
            available_slot.vehicle = Vehicle(vehicle_number, driver_age)
            available_slot.is_available = False

            print('Car with vehicle no "{}" has been parked at slot number {}'
                  .format(available_slot.car.vehicle_number,
                          available_slot.slot_no))

            return

        print("Cannot park any more cars")
        return

    def Remove_vehicle(self, slot_no):
        """
        Removes a vehicle from a slot.

        Input:-
            slot_no - Integer
        """

        slot_no = int(slot_no)

        if not self.check_parking_slots:
            return

        if slot_no in self.parking_slots[slot_no]:
            parking_slot = self.parking_slots[slot_no]

            if not parking_slot.is_available and parking_slot.car:
                vehicle = parking_slot.vehicle
                vehicle_number = vehicle.vehicle_number
                driver_age = vehicle.driver_age
                parking_slot.vehicle = None
                parking_slot.is_available = True

                print('Slot number {} vacated, the car with vehicle registration number "{}" left the space, the driver of the car was of age {}'
                      .format(slot_no, vehicle_number, driver_age))
            else:
                print('Slot already vacant')
        else:
            print('No such parking slot')

    def slot_numbers_for_driver_of_age(self, driver_age):
        """
        Returns all slots where vehicles of given driver_age are present.

        Input:-
            driver_age - Integer
        """

        if not self.check_parking_slots:
            return

        slot_nos = []
        for parking_slot in self.parking_slots.values():
            if (not parking_slot.is_available and parking_slot.vehicle and
                parking_slot.vehicle.driver_age == driver_age):
                slot_nos.append(parking_slot.slot_no)

        if slot_nos:
            print(slot_nos.join(','))
        else:
            print(None)

    def slot_number_for_car_with_number(self, vehicle_number):
        """
        Return slot for vehicle with given vehicle_number is present.

        Input:-
            vehicle_number - String
        """

        if not self.check_parking_slots:
            return

        slot_no = ''
        for parking_slot in self.parking_slots.values():
            if (not parking_slot.is_available and parking_slot.vehicle and
                parking_slot.vehicle.vehicle_number == vehicle_number):
                slot_no = parking_slot.slot_no
                break

        if slot_no:
            print(slot_no)
        else:
            print "The given vehicle_number does not exit"

    def vehicle_registration_number_for_driver_of_age(self, driver_age):
        """
        Returns all vehicle_numbers where vehicles of given driver_age are
        present.

        Input:-
            driver_age - Integer
        """

        if not self.check_parking_slots:
            return

        vehicle_numbers = []
        for parking_slot in self.parking_slots.values():
            if (not parking_slot.is_available and parking_slot.vehicle and
                parking_slot.vehicle.driver_age == driver_age):
                slot_nos.append(parking_slot.vehicle.vehicle_number)

        if slot_nos:
            print(vehicle_numbers.join(','))
        else:
            print(None)
