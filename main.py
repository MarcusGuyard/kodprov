from alternatives import (print_trainer_with_most_courses,
                          find_course_by_trainer,
                          list_trainers,
                          list_next_five)
from api_handlers import download_course_data


def run():
    """Main program"""
    course_data = download_course_data()
    while True:
        print_main_menu()
        user_answer = input("What say you? ").upper().strip()
        if user_answer == '1':
            list_trainers(course_data)
        if user_answer == '2':
            list_next_five(course_data)
        if user_answer == '3':
            find_course_by_trainer(course_data)
        if user_answer == '4':
            print_trainer_with_most_courses(course_data)
        if user_answer.upper() == 'Q':
            print("Good-bye and thank you for the fish!eoghEWGOIWHEo")
            return


def print_main_menu():
    """Print the main menu"""
    print("""
---> MENU <---
1) List all trainers sorted by name
2) List 5 next upcoming courses sorted by date
3) List all courses with a specific trainer
4) List telephone number of most popular trainer
Q) Quit
""")


if __name__ == '__main__':
    run()
