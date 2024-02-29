from pyspark.sql import SparkSession, DataFrame
from pyspark_utility.fake_data.data_models import (
    PersonModel,
    OrderModel
)


class FakeData:
    def __init__(self, spark: SparkSession):
        self.__spark = spark

    def sales_data(self, count: int = 10) -> DataFrame:
        sales_data = []
        for i in range(0, count):
            sales_data.append(OrderModel())

        df = self.__spark.crateDataFrame(sales_data)
        return df

    def person_data(self, count: int = 10) -> DataFrame:
        person_data = []
        for i in range(0, count):
            person_data.append(PersonModel())

        df = self.__spark.crateDataFrame(person_data)
        return df
