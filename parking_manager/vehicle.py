class Vehicle:
    """
    Hold the fields associated to Car or any vehicle and it's methods.
    """

    def __init__(self, veh_no, driver_age):
        self.vehicle_number = veh_no
        self.driver_age = driver_age

    # Getter methods for the fields.
    @property
    def vehicle_number(self):
        return self._vehicle_number

    @property
    def driver_age(self):
        return self._driver_age

    # Setter methods for the fields
    @vehicle_number.setter
    def vehicle_number(self, value):
        self._vehicle_number = value

    @driver_age.setter
    def driver_age(self, value):
        self._driver_age = value
