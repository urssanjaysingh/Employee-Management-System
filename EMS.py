import csv
import os
from tempfile import NamedTemporaryFile

from tabulate import tabulate


def main():
    os.system("cls")
    menu()


def logo():
    print("""
                    ==================================
                        EMPLOYEE MANAGEMENT SYSTEM
                    ==================================
""")


def menu():
    os.system("cls")
    logo()
    while True:
        print(
            """
                    *********** MAIN MENU ************
                     ________________________________
                    |                                |
                    |____ 1) View Employees List ____|
                    |                                |
                    |____ 2) Edit Employees List ____|
                    |                                |
                    |____ 3) Search Record __________|
                    |                                |
                    |____ 4) Exit __________________ |
                    |                                |
                    |________________________________|
            """)
        choice1 = int(input("\n\n\t\tEnter your choice: "))
        if choice1 == 1:
            display()
            os.system("pause")
            menu()
            break
        elif choice1 == 2:
            edit()
            break
        elif choice1 == 3:
            os.system("cls")
            search()
            break
        elif choice1 == 4:
            os._exit(0)
        else:
            print("\n\n\t\tInvalid Input! Please Try Again.\n\n")
            os.system("pause")
            menu()


def display():
    os.system("cls")
    try:
        with open('employees.csv', 'r') as file:
            array = file.readlines()
            array = [row.split(',') for row in array]
            print(tabulate(array, headers="firstrow", tablefmt='fancy_grid'))
    except FileNotFoundError:
        print("\nFile Not Found!!")
        


def edit():
    os.system("cls")
    while True:
        print("""
                ***EDIT EMPLOYEE LIST***
                 ______________________
                |                      |
                |____ 1) Add __________|
                |                      |
                |____ 2) Modify _______|
                |                      |
                |____ 3) Remove _______|
                |                      |
                |____ 4) Main Menu ____|
                |                      |
                |______________________|
        """)
        choice2 = int(input("\n\n\t\tSelect any option: "))
        if choice2 == 1:
            add()
            break
        elif choice2 == 2:
            modify()
            break
        elif choice2 == 3:
            remove()
            break
        elif choice2 == 4:
            return menu()
        else:
            print("\n\n\t\tInvalid Input! Please Try Again.\n\n")
            os.system("pause")
            edit()


def add():
    os.system("cls")
    try:
        file = open("employees.csv", "r")
        file.close()
    except FileNotFoundError:
        header = ['Employee ID', 'First Name', 'Last Name', 'Age', 'Salary', 'Phone NO', 'Address']
        with open('employees.csv', 'w', newline="") as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(header)
    print("\n\t\t *** Add Employee Details ***\n")
    empId = input("\n\t\tEmployee ID: ")
    with open("employees.csv", "r") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            if row["Employee ID"] == empId:
                print("\n\t\tThis Employee ID already in use!\n")
                os.system("pause")
                edit()
        else:
            with open("employees.csv", "a", newline="") as file:
                w = csv.writer(file)
                ans = 'Y'
                while ans.lower() == 'y':
                    fName = input("\n\t\tFirst Name: ")
                    lName = input("\n\t\tLast Name: ")
                    age = input("\n\t\tAge: ")
                    salary = input("\n\t\tSalary: ")
                    phoneNo = input("\n\t\tPhone NO: ")
                    address = input("\n\t\tAddress: ")
                    w.writerow([empId, fName, lName, age, salary, phoneNo, address])
                    print("\n\t\tRecord Added!!")
                    ans = input("\nDo you want add more employee?\nEnter[Y/N]: ")
    os.system("cls")
    edit()


def modify():
    os.system("cls")
    display()
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    fields = ['Employee ID', 'First Name', 'Last Name', 'Age', 'Salary', 'Phone NO', 'Address']
    with open("employees.csv", 'r') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=fields)
        writer = csv.DictWriter(tempfile, fieldnames=fields)
        emp_id = input("\n\tEnter Employee ID: ")
        for row in reader:
            if row['Employee ID'] == str(emp_id):
                os.system("cls")
                print("\n\t\t *** Enter New Details for Employee ID:", row['Employee ID'], "***")
                fName = input("\n\t\tFirst Name: ")
                lName = input("\n\t\tLast Name: ")
                age = input("\n\t\tAge: ")
                salary = input("\n\t\tSalary: ")
                phoneNo = input("\n\t\tPhone NO: ")
                address = input("\n\t\tAddress: ")
                row['First Name'], row['Last Name'], row['Age'], row['Salary'], row['Phone NO'], row[
                    'Address'] = fName, lName, age, salary, phoneNo, address
            row = {'Employee ID': row['Employee ID'], 'First Name': row['First Name'], 'Last Name': row['Last Name'],
                   'Age': row['Age'], 'Salary': row['Salary'], 'Phone NO': row['Phone NO'], 'Address': row['Address']}
            writer.writerow(row)
    with open(tempfile.name, newline='') as in_file:
        with open("employees.csv", 'w', newline='') as out_file:
            writer = csv.writer(out_file)
            for row in csv.reader(in_file):
                if row:
                    writer.writerow(row)
    print("\n\t\tRecord Updated!!\n\n")
    os.system("pause")
    edit()


def remove():
    os.system("cls")
    display()
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    fields = ['Employee ID', 'First Name', 'Last Name', 'Age', 'Salary', 'Phone NO', 'Address']
    with open("employees.csv", 'r') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=fields)
        writer = csv.DictWriter(tempfile, fieldnames=fields)
        emp_id = input("\n\tEnter Employee ID: ")
        for row in reader:
            if row['Employee ID'] != str(emp_id):
                writer.writerow(row)
    with open(tempfile.name, newline='') as in_file:
        with open("employees.csv", 'w', newline='') as out_file:
            writer = csv.writer(out_file)
            for row in csv.reader(in_file):
                if row:
                    writer.writerow(row)
    print("\n\tRecord Removed!!\n\n")
    os.system("pause")
    edit()


def search():
    print("\n*** Search Record in Employees List ***\n")
    keyword = input("Enter any detail of the employee to search: ")
    fields = ['Employee ID', 'First Name', 'Last Name', 'Age', 'Salary', 'Phone NO', 'Address']
    with open("employees.csv", 'r') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=fields)
        for row in reader:
            if row['Employee ID'] == str(keyword) or row['First Name'] == str(keyword) or row['Last Name'] == str(keyword) or row['Age'] == str(keyword) or row['Salary'] == str(keyword) or row['Phone NO'] == str(keyword) or row['Address'] == str(keyword):
                print("\n")
                print(tabulate(row.items(), headers="firstrow", tablefmt='fancy_grid'))
    print("\n\n")
    os.system("pause")
    menu()


main()
