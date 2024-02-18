from datetime import datetime

# Define two datetime objects
date1 = datetime(2024, 2, 10, 12, 0, 0)
date2 = datetime(2024, 2, 15, 12, 0, 0)

# Calculate the difference in seconds
difference_seconds = abs((date2 - date1).total_seconds())

print("Difference between the two dates in seconds:", difference_seconds)
