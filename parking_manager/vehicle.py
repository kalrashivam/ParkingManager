class Vehicle:
    """
    Hold the fields associated to Car or any vehicle and it's methods.
    """

    def __init__(self, veh_no, driver_age):
        self._vehicle_number = veh_no
        self._driver_age = driver_age

    # Getter methods for the fields.
    @property
    def vehicle_number(self):
        return self.vehicle_number

    @property
    def driver_age(self):
        return self.driver_age

    # Setter methods for the fields
    @vehicle_number.setter
    def vehicle_number(self, value):
        self._reg_no = value

    @driver_age.setter
    def driver_age(self, value):
        self._colour = value
