from datetime import datetime, timedelta

# Get the current date
current_date = datetime.now()

# Subtract five days from the current date
five_days_ago = current_date - timedelta(days=5)

print("Five days ago:", five_days_ago.strftime("%Y-%m-%d"))
