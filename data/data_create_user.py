from faker import Faker


class RegistrationData:
    fake = Faker()

    name = "Test User"
    email = fake.email()
    password = '123456'

