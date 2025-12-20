from pyspark.sql.types import (
    StructType, StructField,
    StringType, LongType, TimestampType, MapType
)

# Schema Layout
#   "event_id": "uuid",
#   "event_type": "view | like | comment | share | save | repost",
#   "user_id": "string",
#   "content_id": "string",
#   "event_timestamp": "ISO-8601",
#   "ingestion_timestamp": "ISO-8601",
#   "device_type": "mobile | web",
#   "platform": "ios | android | web",
#   "country": "US",
#   "session_id": "string"

event_schema = StructType([
    StructField("event_id", StringType(), False),
    StructField("event_type", StringType(), False),
    StructField("user_id", StringType(), False),
    StructField("content_id", StringType(), False),
    StructField("event_ts", TimestampType(), False), 
    StructField("ingestion_ts", TimestampType(), False),
    StructField("device_type", StringType(), False), 
    StructField("platform", StringType(), False),
    StructField("country", StringType(), False),
    StructField("session_id", StringType(), False)
])

#ts is shorthand for timestamp

#test event
from datetime import datetime

data = [
    (
        "evt_001",
        "view",
        "user_123",
        "post_456",
        datetime.utcnow(),
        datetime.utcnow(),
        "mobile",
        "ios",
        "US",
        "sess_789"
    )
]

df = spark.createDataFrame(data, schema=event_schema)
df.printSchema()
df.show(truncate=False)