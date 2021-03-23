class ParkingSlot(object):
    """
    Hold the attributes related to availability or occupancy of the parking
    spot.
    """

    def __init__(self, slot_no=None, is_available=True):
        self.vehicle = None
        self.slot_no = slot_no
        self.is_available = is_available

    # Getter methods for fields.
    @property
    def vehicle(self):
        return self._vehicle

    @property
    def slot_no(self):
        return self._slot_no

    @property
    def available(self):
        return self._is_available

    # Setter methods for fields
    @slot_no.setter
    def slot_no(self, value):
        self._slot_no = value

    @vehicle.setter
    def vehicle(self, value):
        self._vehicle = value

    @available.setter
    def available(self, value):
        self._is_available = value
