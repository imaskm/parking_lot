import os, sys
from src.classes import parkingLot
from src.settings import INPUT_TYPES


def check_if_file_can_be_read(file_path):
    if not os.path.exists(file_path):
        print("This file doesn't exist, try absolute path of file")
        return False
    if not os.path.isfile(file_path):
        print("Provided is not a file")
        return False
    if not os.access(file_path, os.R_OK):
        print("You don't have read permission for the file")
        return False

    return True


def check_if_parking_lot_already_exists():
    return hasattr(parkingLot.ParkingLot, "instance")


def create_parking_lot(slots):
    return parkingLot.ParkingLot(slots)


def get_parking_lot():
    return parkingLot.ParkingLot()


def get_file_input():
    while True:
        try:
            print("Please provide a file with inputs for the application (ctrl+c to exit):")
            file_path = input()

            if not check_if_file_can_be_read(file_path):
                continue
            else:
                with open(file_path) as fp:

                    for original_line in fp.readlines():
                        line = original_line
                        line.rstrip("\n")
                        line = line.lower()
                        try:
                            if line.lower().startswith(INPUT_TYPES[1]):
                                if check_if_parking_lot_already_exists():
                                    print("ERROR: Parking Lot Already Exists!!")
                                    break
                                else:
                                    max_slots = int(line.split()[1])
                                    parking_lot = create_parking_lot(max_slots)
                                    if parking_lot:
                                        print(f"Created parking of {max_slots} slots")
                                        continue
                            else:
                                if not check_if_parking_lot_already_exists():
                                    print("ERROR: No Parking Lot Here, Create One First")
                                    break
                                parking_lot = get_parking_lot()

                                if line.lower().startswith(INPUT_TYPES[2]):
                                    line = line.split()
                                    vehicle_registration_number, driver_age = line[1], int(line[3])
                                    slot_number = parking_lot.park_vehicle(
                                        vehicle_registration_number=vehicle_registration_number,
                                        driver_age=driver_age
                                    )
                                    if slot_number:
                                        print(f"Car with vehicle registration number \"{vehicle_registration_number.upper()}\" "
                                              f"has been parked at slot number {slot_number}")
                                    else:
                                        print("Parking is full")
                                        continue

                                elif line.lower().startswith(INPUT_TYPES[3]):

                                    driver_age = int(line.split()[1])
                                    slot_numbers = parking_lot.get_slot_numbers_where_cars_of_drivers_of_age_parked(
                                        driver_age)
                                    print(*slot_numbers if slot_numbers else "No such car found", sep=",")

                                elif line.lower().startswith(INPUT_TYPES[4]):
                                    vehicle_registration_number = line.split()[1]
                                    slot_number = parking_lot.get_slot_number_for_vehicle_with_registration_number(
                                        vehicle_registration_number)
                                    print(slot_number if slot_number else "Vehicle registration number not found")

                                elif line.lower().startswith(INPUT_TYPES[5]):
                                    slot_number = int(line.split()[1])
                                    vehicle_registration_number, driver_age = parking_lot.leave_vehicle_process(
                                        slot_number)
                                    if vehicle_registration_number:
                                        print(f"Slot number {slot_number} vacated, the car with vehicle registration "
                                              f"number {vehicle_registration_number} left the space, the driver of the"
                                              f" car was of age {driver_age}")

                                elif line.lower().startswith(INPUT_TYPES[6]):

                                    driver_age = int(line.split()[1])
                                    vehicle_registration_numbers = parking_lot.get_registration_numbers_of_cars_of_drivers_of_age_parked(
                                        driver_age)

                                    if vehicle_registration_numbers:
                                        print(*vehicle_registration_numbers , sep=",")
                                    else:
                                        print("No Such Vehicle")

                                else:
                                    print("WARNING: Invalid Input, Ignoring: ", line)
                        except KeyboardInterrupt:
                            sys.exit("Exiting...")
                        except Exception as e:
                            print(e)
                            print("WARNING: Invalid Input, Ignoring: ", line)
                    else:
                        break

                sys.exit()
        except KeyboardInterrupt:
            sys.exit("Exiting...")
        except Exception as e:
            print("Invalid Input!!", e)
