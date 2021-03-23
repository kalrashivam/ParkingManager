#!/usr/bin/python
import os, sys
from parking_manager import ParkingManager


class CommandHandler:
    """
    Reads and handles all the commands from a given file.
    """

    def __init__(self):
        self.parking = ParkingManager()

    def process_file(self, given_file):
        if not os.path.exists(given_file):
            print("File does not exist")

        file_obj = open(given_file)
        try:
            while True:
                line = file_obj.next()
                if line.endswith('\n'):
                    line = line[:-1]
                else:
                    continue

                self.get_command(line)
        except Exception as ex:
            file_obj.close()
            print("Error occured while processing file {}".format(ex))

    def get_params(self, params):
        """
        Fetches params at odd number from the given list.
        """

        return [params[i] for i in range(0, len(params), 2)]

    def get_command(self, line):
        line_parts = line.split()
        command = line_parts[0].lower()
        params = self.get_params(line_parts[1:])

        if hasattr(self.parking, command):
            command_function = getattr(self.parking, command)
            command_function(*params)
        else:
            print("Got wrong command.")

    def process_input(self):
        try:
            while True:
                stdin_input = input("Enter command: ")
                self.get_command(stdin_input)
        except (KeyboardInterrupt, SystemExit):
            return
        except Exception as ex:
            print("Error occured while processing input {}".format(ex))


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        pk_command = CommandHandler()
        pk_command.process_input()
    elif len(args) == 2:
        pk_command = CommandHandler()
        pk_command.process_file(args[1])
    else:
        print('Method not called properly')
