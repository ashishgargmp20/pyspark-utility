from pyspark_utility.size_calculator import SizeCalculator
from pyspark.sql import SparkSession

spark = (
    SparkSession
    .builder
    .appName("AshSparkApp")
    .master("local[*]")
    .getOrCreate()
)

number_array = [1, 2, 3, 4]
size_in_bytes = SizeCalculator.get_size_for_machine(number_array)
assert size_in_bytes == 144, True
