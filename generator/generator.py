import random

from data.data import Person

from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()

def generated_person():
    yield Person(
        full_name = faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        first_name = faker_ru.first_name(),
        last_name = faker_ru.last_name(),
        age = random.randint(10, 80),
        department = faker_ru.job(),
        salary = random.randint(10000, 100000),
        email = faker_ru.email(),
        current_address = faker_ru.address(),
        permanent_address = faker_ru.address(),

    )

def generated_file():
    path = rf'C:\Users\Админ\Desktop\automation_qa\filetest{random.randint(0, 999)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello{random.randint(0, 999)}')
    file.close()
    return file.name, path