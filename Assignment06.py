# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Nicole Tsao, 11/25/2024, Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.


class FileProcessor:
    """
        A collection of processing layer functions that work with Json files

        Ntsao, 11/25/2024, Created script
     """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data from JSON file

            Ntsao,11.25.2024,Created function

            :return: list
        """
        try:
            file = open(file_name, "r")

            student_data = json.load(file)

            file.close()
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with reading the file.", e)

        finally:
            if file.closed == False:
                file.close()
        return student_data


    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to JSON file and saves it

            Ntsao,11.25.2024,Created function

            :return: none
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)

            file.close()
            IO.output_student_courses(student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message, e)
        finally:
            if file.closed == False:
                file.close()


class IO:
    """
        A collection of presentation layer functions that manage user input and output

        Ntsao,11.25.2024,Created Class
        Ntsao,11.25.2024,Added menu output and input functions
        Ntsao,11.25.2024,Added a function to display the data
        Ntsao,11.25.2024,Added a function to display custom error messages
     """

    @ staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user

            Ntsao,11.25.2024,Created function

            :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message --")
            print(error, error.__doc__, type(error), sep="\n")


    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

            Ntsao,11.25.2024,Created function

            :return: None
        """
        print()
        print(MENU)
        print()


    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

            Ntsao,11.25.2024,Created function

            :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):
                raise Exception("Please only choose 1,2,3 or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return choice


    @staticmethod
    def output_student_courses(student_data: list):
        """ This function displays current data including student name and course

            Ntsao,11.25.2024,Created function

            :return: none
        """
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)


    @staticmethod
    def input_student_data(student_data: list):
        """ This function collects student information from the user

            Ntsao,11.25.2024,Created function

            :return: list
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student)
            print()
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages("One of the values was not the correct data type!", e)
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with your entered data.", e)
        return student_data


#When the program starts, read the file data into a list of lists (table)
#Extract the data from the file
#Read from JSON file

#Beginning of the main body of this script
students = FileProcessor.read_data_from_file(FILE_NAME, students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME,students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

print("Program Ended")
