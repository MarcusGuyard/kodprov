import requests


def download_course_data():
    print("Downloading all future course data... ", end='')
    r = requests.get("https://proagile.se/api/publicEvents")
    courses = r.json()
    print("Done.")
    return courses


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
            # TODO (10 p): Allow user entering only part of name.
            # E.g. if the user enters "fredrik", all courses
            # held by "Fredrik Wendt" will be listed.
            trainer_name = input("Name of trainer:")
            print(f"These courses are held by {trainer_name}:")
            matching_courses = [course for course in course_data
                                if course['trainerName'] == trainer_name]
            for num, course in enumerate(matching_courses):
                print(f"{num}. {course['courseName']} ({course['startDate']})")
        if user_answer == '4':
            # TODO (10 p): Print the name of the trainer who
            # holds most courses in the future.
            # TODO (15 p): Also print out the phone number
            # of that trainer.
            # Note: The trainer is an employee of ProAgile,
            # and public data about employees are available
            # from this API endpoint:
            #    https://proagile.se/api/publicEmployees
            print('fix me')
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
    # TODO (10p):
    # 1. First column is always 2 column wide
    # 2. Second column is always 50 columns wide
    # 3. Third column is as small as possible
    # TODO (5p):
    #  - We want next 5, not all courses printed
    # TODO (5p):
    #  - We want the sorted on startDate, not name
    # TODO (5p):
    #  - We want the output numbered from 1, not 0
    print("Next 5 courses sorted by date:")
    course_data = sorted(course_data, key=lambda c: c['name'])
    for num, course in enumerate(course_data):
        print(f"{num}. {course['courseName']} ({course['startDate']})")


if __name__ == '__main__':
    run()
