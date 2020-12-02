import requests


def download_course_data():
    print("Downloading all future course data... ", end='')
    r = requests.get("https://proagile.se/api/publicEvents")
    courses = r.json()
    print("Done.")
    return courses


def print_trainer_with_most_courses(course_data):
    # TODO (15 p): Also print out the phone number
    # of that trainer.
    # Note: The trainer is an employee of ProAgile,
    # and public data about employees are available
    # from this API endpoint:
    #    https://proagile.se/api/publicEmployees

    trainer_course_count = {}
    for course in course_data:
        trainer_name = course['trainerName']
        if trainer_name not in trainer_course_count:
            trainer_course_count[trainer_name] = 0
        trainer_course_count[trainer_name] = trainer_course_count[trainer_name] + 1

    max_course_count = max(trainer_course_count.values())
    for trainer_name in trainer_course_count:
        if trainer_course_count[trainer_name] == max_course_count:
            most_courses_trainer = trainer_name

    print(f"""
Trainer with most courses is {most_courses_trainer}
he/she has {max_course_count} courses planned in future.
""")


def run():
    course_data = download_course_data()
    while True:
        print("""
---> MENU <---
1) List all trainers sorted by name
2) List 5 next upcoming courses sorted by date
3) List all courses with a specific trainer
4) List telephone number of most popular trainer
Q) Quit
""")
        user_answer = input("What say you? ").upper().strip()
        if user_answer == '1':
            list_trainers(course_data)
        if user_answer == '2':
            list_next_five(course_data)
        if user_answer == '3':
            trainer_name = input("Name of trainer:")
            print(f"Courses matching trainer {trainer_name}:")
            matching_courses = [course for course in course_data
                                if trainer_name.lower() in course['trainerName'].lower()]
            for num, course in enumerate(matching_courses):
                print(f"{num}. {course['trainerName']} {course['courseName']} ({course['startDate']})")
        if user_answer == '4':
            print_trainer_with_most_courses(course_data)
        if user_answer.upper() == 'Q':
            print("Good-bye and thank you for the fish!")
            return


def list_trainers(courses):
    print("The trainers at ProAgile are:")
    trainers = []
    for course in courses:
        trainer = course['trainerName']
        if trainer not in trainers:
            trainers.append(trainer)
    for trainer in sorted(trainers):
        print(f'  {trainer}')


def list_next_five(course_data):
    print("Next 5 courses sorted by date:")
    course_data = sorted(course_data, key=lambda c: c['startDate'])
    for num, course in enumerate(course_data[:5], start=1):
        print(f"{num:2}. {course['courseName']:50} ({course['startDate']})")


if __name__ == '__main__':
    run()
