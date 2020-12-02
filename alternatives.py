from api_handlers import download_employee_data


def print_trainer_with_most_courses(course_data):
    """Find the trainer with most planned courses
       in future and print his/her name and phone number"""
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
    employees = download_employee_data()
    for employee in employees:
        if employee["name"] == most_courses_trainer:
            phone_number = employee["phone"]
    print(f"""Trainer with most courses is {most_courses_trainer}
he/she has {max_course_count} courses planned in future.
Phone number: {phone_number}""")


def find_course_by_trainer(course_data):
    """Let user search for courses using part of trainers name"""
    trainer_name = input("Name of trainer:")
    print(f"Courses matching trainer {trainer_name}:")
    matching_courses = [course for course in course_data
                        if trainer_name.lower() in course['trainerName'].lower()]
    for num, course in enumerate(matching_courses):
        print(f"{num}. {course['trainerName']} {course['courseName']} ({course['startDate']})")


def list_trainers(courses):
    """Print list of ProAgile trainers"""
    print("The trainers at ProAgile are:")
    trainers = []
    for course in courses:
        trainer = course['trainerName']
        if trainer not in trainers:
            trainers.append(trainer)
    for trainer in sorted(trainers):
        print(f'  {trainer}')


def list_next_five(course_data):
    """List next 5 upcoming courses"""
    print("Next 5 courses sorted by date:")
    course_data = sorted(course_data, key=lambda c: c['startDate'])
    for num, course in enumerate(course_data[:5], start=1):
        print(f"{num:2}. {course['courseName']:50} ({course['startDate']})")