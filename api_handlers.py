import requests


def download_course_data():
    """Fetch JSON data for ProAgile future courses and convert to
    Python list"""
    print("Downloading all future course data... ", end='')
    r = requests.get("https://proagile.se/api/publicEvents")
    courses = r.json()
    print("Done.")
    return courses


def download_employee_data():
    """Fetch JSON data for ProAgile employees and convert to
    Python list"""
    print("Downloading all future course data... ", end='')
    r = requests.get("https://proagile.se/api/publicEmployees")
    employees = r.json()
    print("Done.")
    return employees