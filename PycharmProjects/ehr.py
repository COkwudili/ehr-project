# create a list containing four patients name
# create a dictionary for one patient with an ID, name, age and department
# print the patient name and department
# use a for loop to display all four names
# add a fifth name using append

patient_names = ["Martins Eniola", "Azeez Idris", "Abdulraheem Basto", "Okwudili Chinedu"]

patient_database = [{"id": "HOSP001", "name": "Martins Eniola", "age": 20, "department": "emergency"},
                    {"id": "HOSP002", "name": "Azeez Idris", "age": 21, "department": "COPD"},
                    {"id": "HOSP003", "name": "Abdulraheem Basto", "age": 20, "department": "NHIS"},
                    {"id": "HOSP004", "name": "Okwudili Chinedu", "age": 20, "department": "RADIOLOGY"}
]

def display_welcome():
    print("=====================================================")
    print("          HOSPITAL ELECTRONIC HEALTH                 ")
    print("            RECORD (EHR) SYSTEM                      ")
    print("=====================================================")

def main():
    display_welcome()

    while True:
        print("\n--Main Menu--")
        print("1. View all patient names")
        print("2. Search patient record (Name & Department)")
        print("3. Add a new patient")
        print("4. Exit the system")

        choice = input("Select an option(1-4): ")
        match choice:
            case"1":
                print("\n---Current Patient Directory---")
                for index, name in enumerate(patient_names, start=1):
                    print(f"{index}. {name}")

            case"2":
                search_name = input("Enter patient name: ").strip()
                found = False

                for patient in patient_database:
                    if patient["name"].lower()== search_name.lower():
                        print(f"\n--- Patient Record Found ---")
                        print(f"ID :{patient['id']}")
                        print(f"Name :{patient['name']}")
                        print(f"Age :{patient['age']}")
                        print(f"Department :{patient['department']}")
                        found = True
                        break

                if not found:
                    print(f"No record found for '{search_name}'.")

            case"3":
                new_name = input("Enter new patient's full name: ").strip()
                new_age = input("Enter new patient's age: ").strip()
                new_department = input("Enter new patient's department: ").strip()

                new_id = f"HOSP00{len(patient_database)+1}"
                new_record = {
                    "id": new_id,
                    "name": new_name,
                    "age": int(new_age) if new_age.isdigit() else 0,
                    "department": new_department
                }
                patient_database.append(new_record)

                print(f"\nSuccess! {new_name} has been added to the EHR system.")

            case"4":
                print("Goodbye, Stay Safe! ")

            case "_":
                print("Invaid choice, Please select a number between 1 and 4.")


if __name__ == "__main__":
    main()