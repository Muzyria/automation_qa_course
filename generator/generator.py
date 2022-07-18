import os
import random

from gata.data import Person
from faker import Faker

faker_ru = Faker("ru_RU")
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(10, 80),
        salary=random.randrange(10000, 100000, 10000),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile=faker_ru.msisdn(),
        subject=generated_subject()
    )


def generated_file():
    path = rf'{os.getcwd()}\filetest{random.randint(0, 999)}.txt'
    with open(path, "w+") as file:
        file.write(f"Hello Word {random.randint(0, 999)}")
    return file.name, path


def generated_subject():
    data = ["Hindi", "English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science", "Commerce",
            "Accounting", "Economics", "Arts", "Social Studies", "History", "Civics"]
    return data[random.randint(0, len(data) - 1)]
