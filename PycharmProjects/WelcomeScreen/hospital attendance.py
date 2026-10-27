import datetime

# predefined list of hospital departments
DEPARTMENTS = [
    "General Outpatient Department (GOPD)",
    "Paediatrics",
    "Maternity",
    "Dental",
    "Eyeclinic",
]

def display_departments():
    """Display available departments with index numbers."""
    print("\n--- Available Departments ---\n")
    for index, department in enumerate(DEPARTMENTS, start=1):
        print(f"{index}. {department}")

def get_department_choice():
    """Prompt the user to select a department."""
    while True:
        display_departments()
        try:
            choice = int(input("\nSelect department number (1-5): "))
            if 1 <= choice <= len(DEPARTMENTS):
                return DEPARTMENTS[choice - 1]
            else:
                print("Invalid selection. Please pick a number from 1 to 5.")

        except ValueError:
            print("Invalid input. Please enter a valid integer number.")

def record_patient_visits(visit_records):
    """Records a new patient visit entry"""
    print("\n--- Record New Patient Visit ---\n")

    patient_name = input("Enter patient name: ").strip()
    while not patient_name:
        patient_name = input("Patient name cannot be empty. Please enter a new name: ").strip()

    patient_id = input("Enter patient id: ").strip().strip()
    department = get_department_choice()

    visit_entry = {
        "id": patient_id,
        "name": patient_name,
        "department": department,
        "time" : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    visit_records.append(visit_entry)
    print(f"\n Visit successfully recorded for {patient_name} in {department}.")

def generate_attendance_report(visit_records):
    """Generates and displays the daily attendance report and departmental statistics"""
    print("\n" + "="*50)
    print("          Hospital Attendance and Visit Report               ")
    print("="*50)

    total_visits = len(visit_records)
    print(f"\nTotal Visits Recorded Today: {total_visits}")

    if total_visits == 0:
        print("No Visits recorded yet.")
        print("="*50)
        return

    department_count = {department: 0 for department in DEPARTMENTS}
    for record in visit_records:
        department_count[record["department"]] += 1

    print("\n--- Attendance Breakdown by Department ---\n")
    for department, count in department_count.items():
        percentage = (count / total_visits) * 100 if total_visits > 0 else 0
        print(f"{department}: {count} visit(s) ({percentage:.1f}%)")


    max_visits = max(department_count.values())
    if max_visits > 0:
        busiest_departments = [department for department, count in department_count.items() if count == max_visits]
        print(f"Busiest Department(s): {', '.join(busiest_departments)} ({max_visits} visit(s))")

    print("\n--- Detailed Visit History Log ---")
    for idx, rec in enumerate(visit_records, start=1):
        print(f"{idx}. [{rec['time']}] ID: {rec['id']} | Name: {rec['name']} | Department: {rec['department']}")

    print("="*50)

def main():
    """Main program execution loop"""
    visit_records = []

    while True:
        print("\n=========================================================================")
        print("                    HEALTH INFORMATION MANAGEMENT TRACKER                  ")
        print("\n=========================================================================")
        print("1. Record New Patient Visit")
        print("2. View Daily Attendance Report")
        print("3. Exit program")

        choice = input("\nEnter your choice (1-3): ").strip()
        match choice:
            case "1":
                record_patient_visits(visit_records)
            case "2":
                generate_attendance_report(visit_records)
            case "3":
                print("\nThank you for using this Visit tracker! Goodbye!.")

            case "_":
                print("Invalid input. Please enter 1, 2, or 3.")



if __name__ == "__main__":
    main()








