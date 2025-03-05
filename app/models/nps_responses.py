from faker import Faker
import random, json
import uuid
from datetime import datetime, timedelta
import os

faker = Faker()

# File path to store generated IDs
file_path = 'generated_ids.json'

# Function to load the generated IDs from the JSON file
def load_generated_ids():
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    else:
        return {"ResponseIDs": [], "CustomerIDs": []}

# Function to save the updated IDs to the JSON file
def save_generated_ids(ids):
    with open(file_path, 'w') as f:
        json.dump(ids, f)

# Function to generate a random date between two dates
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')

# Function to generate dummy data for NPS Responses table
def generate_nps_responses():
    # Load existing IDs
    ids = load_generated_ids()

    # Generate unique ResponseID and CustomerID
    while True:
        response_id = str(uuid.uuid4())
        if response_id not in ids["ResponseIDs"]:
            ids["ResponseIDs"].append(response_id)
            break

    while True:
        customer_id = str(uuid.uuid4())
        if customer_id not in ids["CustomerIDs"]:
            ids["CustomerIDs"].append(customer_id)
            break

    # Save updated IDs to JSON file
    save_generated_ids(ids)

    # Generate a random score
    score = random.randint(0, 10)

    # Generate the response data
    response = {
        "ResponseID": response_id,
        "CustomerID": customer_id,
        "SurveyDate": random_date(datetime.today() - timedelta(days=730), datetime.today()),  # Random survey date
        "Score": score,
        "Comment": faker.sentence(),  # Random comment related to banking services
        "SatisfactionLevel": "Promoter" if score >= 9 else "Passive" if score >= 7 else "Detractor",
        "SurveyChannel": random.choice(["Email", "SMS", "Phone", "Online Banking"])  # Random survey channel
    }

    return response