from pyspark.sql import DataFrame, SparkSession
from pyspark_utility.fake_data import FakeData

spark = (
    SparkSession
    .builder
    .appName("AshSparkApp")
    .master("local[*]")
    .getOrCreate()
)

print(FakeData.fake_user())
print(FakeData.fake_users(spark))
