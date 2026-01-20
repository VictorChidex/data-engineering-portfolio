Homework 1: Docker, SQL and Terraform for Data Engineering Zoomcamp 2026
https://github.com/DataTalksC…

Due date: 26 January 2026 18:59 (local time)

Questions

Question 1. What's the version of pip in the python:3.13 image? (1 point)
25.3
24.3.1
24.2.1
23.3.1

Answer:
'''bash
sudo docker run -it --rm python:3.13 bash
pip --version
'''

'''bash
root@f865970984e5:/# python --version
Python 3.13.11
root@f865970984e5:/# pip --version
pip 25.3 from /usr/local/lib/python3.13/site-packages/pip (python 3.13)
'''

Question 2. Given the docker-compose.yaml, what is the hostname and port that pgadmin should use to connect to the postgres database? (1 point)
postgres:5433
localhost:5432
db:5433
postgres:5432
db:5432 - Answer


Prepare the Data
Download the green taxi trips data for November 2025:
'''bash
wget https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet
'''
You will also need the dataset with zones:
'''bash
wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv 
'''
Question 3. Counting short trips
For the trips in November 2025 (lpep_pickup_datetime between '2025-11-01' and '2025-12-01', exclusive of the upper bound), how many trips had a trip_distance of less than or equal to 1 mile?
7,853
8,007 - Answer
8,254
8,421

'''bash
SELECT COUNT(*) AS trips_le_1_mile
FROM green_tripdata
WHERE lpep_pickup_datetime >= TIMESTAMP '2025-11-01'
  AND lpep_pickup_datetime <  TIMESTAMP '2025-12-01'
  AND trip_distance <= 1;
'''


Question 4. Which was the pick up day with the longest trip distance? Only consider trips with trip_distance less than 100 miles. (1 point)
2025-11-14
2025-11-20
2025-11-23
2025-11-25

Question 5. Which was the pickup zone with the largest total_amount (sum of all trips) on November 18th, 2025? (1 point)
East Harlem North
East Harlem South
Morningside Heights
Forest Hills

Question 6. For the passengers picked up in the zone named "East Harlem North" in November 2025, which was the drop off zone that had the largest tip? (1 point)
JFK Airport
Yorkville West
East Harlem North
LaGuardia Airport

Question 7. Which of the following sequences describes the Terraform workflow for: 1) Downloading plugins and setting up backend, 2) Generating and executing changes, 3) Removing all resources? (1 point)
terraform import, terraform apply -y, terraform destroy
teraform init, terraform plan -auto-apply, terraform rm
terraform init, terraform run -auto-approve, terraform destroy
terraform init, terraform apply -auto-approve, terraform destroy
terraform import, terraform apply -y, terraform rm

