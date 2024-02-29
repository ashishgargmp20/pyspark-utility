# pyspark-utility
Provide utility functions for pyspark

## Example - How to use?
***
 ``` python
 from pyspark_utility.object_size_calculator import ObjectSizeCalculator 
 calc = ObjectSizeCalculator(spark) 
 calc.get_size_for_human(numbers) 
 ```

## Listing here the classes and useful functions (version - 0.4.0)
***
| Class                  | Function| Description|                                                                                                                             
|------------------------|-|-|
| _ObjectSizeCalculator_ | `get_size_for_machine(obj)` | get size in bytes |
| _ObjectSizeCalculator_ | `get_size_for_human(obj)` | get size in KB, MB, GB, and so on |