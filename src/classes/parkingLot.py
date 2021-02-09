class ParkingLot:
    # Creating this as Singleton as only ParkingLot can be created
    initialized = False

    def __new__(klaas, *args, **kwargs):
        if not hasattr(klaas, "instance"):
            # print("created object")
            klaas.instance = super(ParkingLot, klaas).__new__(klaas)

        return klaas.instance

    def __init__(self, max_slots=10):
        if ParkingLot.initialized:
            return
        # print("init crossed")
        self.__max_slots = max_slots
        self.__slots_filled = 0
        # python 3.8 ensures the insertion order
        self.__parking_slots_dict = dict.fromkeys(range(1, max_slots + 1))
        ParkingLot.initialized = True

    def get_slots_filled(self):
        return self.__slots_filled

    def update_slots_filled(self, update_diff):
        self.__slots_filled += update_diff

    def get_max_slots(self):
        return self.__max_slots

    def get_parking_slots_dict(self):
        return self.__parking_slots_dict

    def update_parking_slots_dict(self, k, v):
        self.__parking_slots_dict[k] = v

    def get_available_slot(self):
        return self.get_max_slots() - self.get_slots_filled()

    def park_vehicle(self, vehicle_registration_number, driver_age):

        if self.get_available_slot() <= 0:
            return

        for k, v in self.get_parking_slots_dict().items():
            if v is None:
                self.update_slots_filled(1)
                self.update_parking_slots_dict(k, {"vehicle_registration_number": vehicle_registration_number,
                                                   "driver_age": driver_age
                                                   })
                return k

    def get_slot_number_for_vehicle_with_registration_number(self, vehicle_registration_number):
        for k, v in self.get_parking_slots_dict().items():
            if v is not None and v["vehicle_registration_number"] == vehicle_registration_number:
                return k

    def get_slot_numbers_where_cars_of_drivers_of_age_parked(self, driver_age):
        result = []
        for k, v in self.get_parking_slots_dict().items():
            if v is not None and v["driver_age"] == driver_age:
                result.append(k)
        return tuple(result)

    def get_registration_numbers_of_cars_of_drivers_of_age_parked(self, driver_age):
        result = []
        for k, v in self.get_parking_slots_dict().items():
            if v is not None and v["driver_age"] == driver_age:
                result.append(v["vehicle_registration_number"])
        return tuple(result)

    def leave_vehicle_process(self, slot_number):
        for k, v in self.get_parking_slots_dict().items():
            # import pdb
            # pdb.set_trace()
            if k == slot_number and v is not None:
                return v["vehicle_registration_number"], v["driver_age"]

        return (None,None)

    def __del__(self):
        del self
