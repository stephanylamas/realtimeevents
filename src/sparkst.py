import json
from pyspark.sql.types import *

#reference event schema 
with open('eventschema.json', 'r') as file:
    schema = json.load(file)


