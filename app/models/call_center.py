from faker import Faker
import random
import uuid
from datetime import datetime, timedelta

faker = Faker()

# Function to generate a random date within a range
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

# Function to generate CallCenterInteraction dummy data
def generate_call_center_interaction():
    # Generate a single call center interaction instead of two
    interaction = {
        "InteractionID": str(uuid.uuid4()),
        "CustomerID": str(uuid.uuid4()),
        "AgentID": str(uuid.uuid4()),
        "InteractionTime": faker.date_time_this_year().isoformat(),  # Random timestamp this year
        "CallType": random.choice(["Complaint", "Inquiry", "Request"]),
        "Duration": random.randint(1, 60),  # Call duration in minutes
        "SatisfactionRating": random.randint(1, 5),  # Satisfaction rating (1-5)
        "IssueResolved": random.choice(["Yes", "No"])  # Issue resolved (Yes/No)
    }
    return interaction

# Function to generate Customer Complaint dummy data
def generate_customer_complaint():
    # Generate a single customer complaint instead of two
    complaint_date = random_date(datetime.today() - timedelta(days=365), datetime.today())  # Past year complaints
    resolution_start = complaint_date + timedelta(days=random.randint(1, 10))  # Starts resolution after complaint
    resolution_end = resolution_start + timedelta(days=random.randint(1, 20))  # Resolves within 20 days
    resolution_time = (resolution_end - resolution_start).days if resolution_end else None

    complaint = {
        "ComplaintID": str(uuid.uuid4()),
        "CustomerID": str(uuid.uuid4()),  # Unique CustomerID
        "ComplaintDate": complaint_date.strftime('%Y-%m-%d'),
        "ComplaintType": random.choice(["Service", "Product", "Billing"]),
        "ComplaintStatus": random.choice(["Pending", "Resolved"]),
        "ResolutionStartDate": resolution_start.strftime('%Y-%m-%d') if resolution_start else None,
        "ResolutionEndDate": resolution_end.strftime('%Y-%m-%d') if resolution_end else None,
        "ResolutionTime": resolution_time if resolution_end else None,  # Days taken to resolve
        "ResolutionDetails": faker.sentence() if resolution_end else "Resolution in progress"
    }
    return complaint