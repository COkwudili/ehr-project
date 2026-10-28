patient_names = ["Omisore Martins", "Abdulraheem Basto", "Tinubu Ebun", "Azeez Idris", "Okwudili Chinedu"]

patient_database = [{"id": "HOSP001", "name": "Omisore Martins", "age": 19, "department": "emergency"},
                    {"id": "HOSP002", "name": "Abdulraheem Basit", "age": 20, "department": "GOPD"},
                    {"id": "HOSP003", "name": "Tinubu Ebun", "age": 21, "department": "COPD"},
                    {"id": "HOSP004", "name": "Azeez Idris", "age": 22, "department": "NHIS"},
                    {"id": "HOSP005", "name": "Okwudili Chinedu", "age": 20, "department": "radiology"}
                    ]


def display_welcome():
    print("===========================================================================")
    print("                      HOSPITAL ELECTRONIC HEALTH                           ")
    print("                          RECORD (EHR) SYSTEM                              ")
    print("===========================================================================")


def main():
    display_welcome()

    while True:
        print("\n--main menu--")
        print("1. View all patient names")
        print("2. Search patient record (Name & Department)")
        print("3. Add a new patient")
        print("4.Exit the system")

        choice = input("Select an option (1-4): ")
        match choice:
            case "1":
                print("\n----Current Patient Directory----")
                for index, name in enumerate(patient_names, start=1):
                    print(f"{index}. {name}")

            case "2":
                search_name = input("Enter patient name: ").strip()
                found = False

                for patient in patient_database:
                    if patient["name"].lower() == search_name.lower():
                        print("\n-----Patient Record Found-----")
                        print(f"ID: {patient['id']}")
                        print(f"Name: {patient['name']}")
                        print(f"Department: {patient['department']}")
                        found = True
                        break

                if not found:
                    print(f"No record found for {search_name}")

            case "3":
                new_name = input("Enter name of the new patient: ").strip()
                new_age = input("Enter the age of the new patient: ").strip()
                new_department = input("Enter the department of the new patient: ").strip()

                new_id = f"HOSP00{len(patient_database) + 1}"
                new_record = {
                    "id": new_id,
                    "name": new_name,
                    "age": int(new_age) if new_age.isdigit() else 0,
                    "department": new_department
                }
                patient_database.append(new_record)
                print(f"\nSuccessful! {new_name} has been added to the EHR system")

            case "4":
                print("Goodbye, Stay Safe!")
                break

            case "_":
                print("Invalid Choice, Please select a number between 1 and 4")


if __name__ == "__main__":
    main()














