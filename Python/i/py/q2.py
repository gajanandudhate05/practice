
class Hospital:
    def __init__(self):
        self.queue = []

    # 1. Add Patient (Enqueue)
    def add_patient(self, patient_id, name, priority):
        if priority not in [1, 2, 3]:
            print("Invalid priority!")
            return

        patient = (priority, patient_id, name)
        self.queue.append(patient)

        # Sort patients according to priority
        self.queue.sort(key=lambda x: x[0])

        print("Patient added successfully!")

    # 2. Display Next Patient
    def display_next(self):
        if len(self.queue) == 0:
            print("No patients waiting.")
        else:
            priority, patient_id, name = self.queue[0]

            print("\nNext Patient:")
            print("Patient ID:", patient_id)
            print("Patient Name:", name)
            print("Priority:", priority)

    # 3. Remove Patient (Dequeue)
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty.")
        else:
            patient = self.queue.pop(0)

            print("Treated Patient:", patient[2])

    # 4. Display All Patients
    def display_all(self):
        if len(self.queue) == 0:
            print("No waiting patients.")
        else:
            print("\nWaiting Patients:")

            for priority, patient_id, name in self.queue:
                print("ID:", patient_id,
                      "| Name:", name,
                      "| Priority:", priority)


# Main Program
h = Hospital()

while True:
    print("\n--- Hospital Emergency Management ---")
    print("1. Add Patient")
    print("2. Display Next Patient")
    print("3. Remove Patient")
    print("4. Display All Patients")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        patient_id = int(input("Enter Patient ID: "))
        name = input("Enter Patient Name: ")
        priority = int(input("Enter Priority (1-Critical, 2-Serious, 3-Normal): "))

        h.add_patient(patient_id, name, priority)

    elif choice == 2:
        h.display_next()

    elif choice == 3:
        h.dequeue()

    elif choice == 4:
        h.display_all()

    elif choice == 5:
        print("Exiting Hospital Management System.")
        break

    else:
        print("Invalid choice!")
