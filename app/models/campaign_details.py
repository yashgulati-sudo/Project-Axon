from faker import Faker
import random
import uuid
from datetime import datetime, timedelta

faker = Faker()

# Function to generate a random date within a range
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')

# Function to generate dummy data for CampaignDetails table
def generate_campaign_details():
    start_date = datetime.today() - timedelta(days=random.randint(0, 365))  # Random start date within the past year
    end_date = start_date + timedelta(days=random.randint(7, 90))  # Random end date, between 7 and 90 days after start
    campaign = {
        "CampaignID": str(uuid.uuid4()),  # Unique CampaignID
        "CampaignName": f"{faker.company()} Loan Offer",  # Bank-related campaign name
        "StartDate": start_date.strftime('%Y-%m-%d'),
        "EndDate": end_date.strftime('%Y-%m-%d'),
        "Budget": round(random.uniform(10000, 500000), 2),  # Random campaign budget
        "Status": random.choice(["Active", "Completed", "Pending"]),  # Random status
        "Channel": random.choice(["Bank Website", "Email", "SMS", "In-Branch"]),  # Random marketing channel
        "SeasonID": random.randint(1, 4)  # Random season ID (from a possible 4 seasons)
    }
    return campaign

# Function to generate dummy data for CampaignPerformance table
def generate_campaign_performance(campaign):
    performance = {
        "PerformanceID": str(uuid.uuid4()),  # Unique PerformanceID
        "CampaignID": campaign["CampaignID"],  # Foreign key from CampaignDetails table
        "TotalResponses": random.randint(1000, 50000),  # Random number of responses
        "ClickThroughRate": round(random.uniform(1.5, 15.0), 2),  # Random click-through rate in percentage
        "ConversionRate": round(random.uniform(0.5, 10.0), 2),  # Random conversion rate in percentage
        "RevenueGenerated": round(random.uniform(5000, 200000), 2),  # Random revenue generated
        "AverageScore": round(random.uniform(3.0, 9.5), 2),  # Random average NPS score
        "SalesVolume": random.randint(100, 10000)  # Random sales volume
    }
    return performance

# Function to generate dummy data for SalesSeasonality table
def generate_sales_seasonality():
    seasons = ["Summer", "Festive", "Off-Peak", "Winter"]
    season_data = {
        "SeasonID": random.randint(1, 4),
        "SeasonName": random.choice(seasons),
        "RevenueGenerated": round(random.uniform(100000, 5000000), 2),
        "SalesVolume": random.randint(5000, 100000),
        "CustomerRetentionRate": round(random.uniform(50.0, 90.0), 2)  # Random retention rate
    }
    return season_data

# Function to generate dummy data for CustomerCampaign table
def generate_customer_campaign():
    customer_campaign = {
        "customer_campaign_id": random.randint(1000, 9999),  # Random customer campaign ID
        "customer_id": random.randint(1, 99999),  # Random customer ID
        "campaign_id": random.randint(1000, 9999),  # Random campaign ID
        "enrolled_at": faker.date_this_year()  # Random enrollment date within this year
    }
    return customer_campaign
