

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 17:15:43 2025

@author: tejavathi teju
"""

from supervisor import Supervisor
from exceptions import LineNotFoundError, InvalidOperationError

def main():
    supervisor = Supervisor()

    while True:
        print("\n--- Production Line Menu ---")
        print("1. Add Production Line")
        print("2. Remove Line")
        print("3. Start Line")
        print("4. Stop Line")
        print("5. Log Output")
        print("6. Generate Reports")
        print("7. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                name = input("Enter line name: ")
                item = input("Enter item produced: ")
                capacity = int(input("Enter line capacity: "))
                supervisor.add_line(name, item, capacity)
                print(f"Production line '{name}' added successfully.")

            elif choice == "2":
                line_id = input("Enter line ID to remove: ")

                supervisor.remove_line(line_id)
                print(f"Line {line_id} removed successfully.")

            elif choice == "3":
                line_id = input("Enter line ID to start: ")
                supervisor.start_line(line_id)
                print(f"Line {line_id} started.")

            elif choice == "4":
                line_id = input("Enter line ID to stop: ")
                supervisor.stop_line(line_id)
                print(f"Line {line_id} stopped.")

            elif choice == "5":
                line_id = input("Enter line ID to log output: ")
                amount = int(input("Enter output amount: "))
                supervisor.log_output(line_id, amount)
                print(f"Logged {amount} units for line {line_id}.")

            elif choice == "6":
                print("\n--- Reports ---")
                print("1. Total Output")
                print("2. Efficiency")
                print("3. Downtime")
                report_choice = input("Select report type: ")
                if report_choice == "1":
                    supervisor.output_report()
                elif report_choice == "2":
                    supervisor.efficiency_report()
                elif report_choice == "3":
                    supervisor.downtime_report()
                else:
                    print("Invalid report choice.")

            elif choice == "7":
                print("Exiting program. Goodbye!")
                break

            else:
                print("Invalid choice, try again.")

        except (LineNotFoundError, InvalidOperationError, ValueError) as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()