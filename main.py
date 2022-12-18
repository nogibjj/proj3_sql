import os
from google.cloud import bigquery

os.environ[
    "GOOGLE_APPLICATION_CREDENTIALS"
] = "/Users/kristivanmeter/Downloads/proj3-gc-clientcred-key.json"

client = bigquery.Client()

sql_query = """
SELECT 
*
FROM `proj3-368706.proj3_population.world_population` 

WHERE Total BETWEEN 10000000 AND 100000000

ORDER BY Total DESC
"""

query_job = client.query(sql_query)

# to print out results
# for row in query_job.result():
#     print(row)
