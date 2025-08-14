from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

DIRECTIONS = ["Entry", "Exit"]
EVENT_TYPES = ["Footfall", "MotionDetected", "Unknown"]
SENSOR_LOCATIONS = ["Entrance", "Lobby", "BackDoor", "Staircase"]
DATA_SOURCES = ["InfraRed", "Thermal", "Video", "Ultrasonic"]
SENSORS = [f"S{str(i).zfill(4)}" for i in range(1, 101)]

def get_random_date():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2025, 12, 31)
    delta = end_date - start_date
    return start_date + timedelta(days=random.randint(0, delta.days))

def get_random_branch_id():
    return random.randint(1, 40)


def get_random_datetime():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2025, 12, 31, 23, 59, 59)
    delta_seconds = int((end_date - start_date).total_seconds())
    random_dt = start_date + timedelta(seconds=random.randint(0, delta_seconds))
    return random_dt

def generate_footfall_sensor_record():
    dt = get_random_datetime()
    is_covid_year = dt.year in [2020, 2021]

    return {
        "SensorID": random.choice(SENSORS),
        "BranchID": get_random_branch_id(),
        "Record_Date": dt.date().isoformat(),
        "RTimeStamp": dt.time().isoformat(timespec="seconds"),
        "Direction": random.choice(DIRECTIONS),
        "RCount": random.randint(0, 2) if is_covid_year else random.randint(1, 5),
        "SensorLocation": random.choice(SENSOR_LOCATIONS),
        "DataSource": random.choice(DATA_SOURCES),
        "EventType": random.choice(EVENT_TYPES),
    }


# Global set to track generated summary dates
generated_dates_set = set()

# Full date range for summary records
start_summary_date = datetime(2020, 1, 1).date()
end_summary_date = datetime(2025, 12, 31).date()
all_possible_dates = [start_summary_date + timedelta(days=i)
                      for i in range((end_summary_date - start_summary_date).days + 1)]

def get_next_available_date():
    for date in all_possible_dates:
        if date not in generated_dates_set:
            return date
    return None  # All dates used

def get_random_branch_id():
    return random.randint(1, 40)

def generate_footfall_summary_record():
    dt = get_next_available_date()
    if dt is None:
        return None  # No more unique dates left

    generated_dates_set.add(dt)
    is_covid_year = dt.year in [2020, 2021]

    # Define bank hours
    bank_hours = list(range(10, 17))  # 10 AM to 4 PM
    peak_hours_range = list(range(11, 14))  # 11 AM to 1 PM

    # Initialize hourly list with zeros
    hourly = [0 for _ in range(24)]

    for hour in bank_hours:
        if is_covid_year:
            hourly[hour] = random.randint(0, 3)
        else:
            if hour in peak_hours_range:
                hourly[hour] = random.randint(30, 60)
            else:
                hourly[hour] = random.randint(5, 30)

    total_entry = sum(hourly)
    anomaly_factor = random.uniform(0.95, 1.05)
    total_exit = max(0, int(total_entry * anomaly_factor))

    peak = hourly.index(max(hourly))
    offpeak = hourly.index(min(hour for hour in hourly if hour > 0)) if any(hourly) else 0

    return {
        "SummaryID": random.randint(100000, 999999),
        "BranchID": get_random_branch_id(),
        "Record_Date": dt.isoformat(),
        "TotalFootfall": total_entry,
        "TotalExit": total_exit,
        "NetFootfall": total_entry - total_exit,
        "PeakHour": f"{peak}:00",
        "OffPeakHour": f"{offpeak}:00"
    }
