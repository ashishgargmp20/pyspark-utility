from faker import Faker
from pydantic import BaseModel
from pydantic.dataclasses import dataclass
import uuid
import datetime

faker = Faker()


# @dataclass
# class UserModel(BaseModel):
#     username: str = faker.user_name()
#     email: str = faker.email()
#     full_name: str = faker.name()
#     password: str = faker.password()
#
#
# @dataclass
# class ProductModel(BaseModel):
#     product_name: str = faker.word()
#     price: float = faker.random_number(digits=2)
#     description: str = faker.text()
#
#
# @dataclass
# class OrderModel(BaseModel):
#     order_id: str = str(uuid.uuid4())
#     order_date: datetime.datetime = faker.date_time_between(start_date='-2y')
#     user: UserModel = UserModel()
#     product: ProductModel = ProductModel()
#     quantity: int = faker.random_int(min=1, max=10)
#
#
# @dataclass
# class AddressModel(BaseModel):
#     street_address: str = faker.street_address()
#     zip_code: str = faker.zipcode()
#     state_abrv: str = faker.state_abbr()
#
#
# @dataclass
# class PersonModel(BaseModel):
#     first_name: str = faker.first_name()
#     last_name: str = faker.last_name()
#     address: AddressModel = AddressModel()
#     phone_number: str = faker.phone_number()


class UserModel:
    username: str = faker.user_name()
    email: str = faker.email()
    full_name: str = faker.name()
    password: str = faker.password()


class ProductModel:
    product_name: str = faker.word()
    price: float = faker.random_number(digits=2)
    description: str = faker.text()


class OrderModel:
    order_id: str = str(uuid.uuid4())
    order_date: datetime.datetime = faker.date_time_between(start_date='-2y')
    user: UserModel = UserModel()
    product: ProductModel = ProductModel()
    quantity: int = faker.random_int(min=1, max=10)


class AddressModel:
    street_address: str = faker.street_address()
    zip_code: str = faker.zipcode()
    state_abrv: str = faker.state_abbr()


class PersonModel:
    first_name: str = faker.first_name()
    last_name: str = faker.last_name()
    address: AddressModel = AddressModel()
    phone_number: str = faker.phone_number()
