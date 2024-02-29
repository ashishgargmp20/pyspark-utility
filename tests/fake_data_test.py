from pyspark_utility.fake_data import FakeData
from pyspark.sql import DataFrame, SparkSession

spark = (
    SparkSession
    .builder
    .appName("AshSparkApp")
    .master("local[*]")
    .getOrCreate()
)

fakedata_obj = FakeData(spark)
df = fakedata_obj.sales_data(10)
df

