"""
Centralized configuration constants for race limits,
fuel usage, and time-related calculations.
"""

# Sprint race duration bounds, in minutes.
MIN_SPRINT_RACE_DURATION = 5
MAX_SPRINT_RACE_DURATION = 60

# Allowed lap time bounds, in seconds.
MIN_LAP_TIME_SEC = 80
MAX_LAP_TIME_SEC = 840  # 14:00

# Allowed fuel consumption bounds, liters per lap.
MIN_FUEL_PER_LAP = 0.5
MAX_FUEL_PER_LAP = 15

# Upper fuel tank limit in liters.
MAX_FUEL_CAPACITY = 120

# Time conversion helper.
SECONDS_IN_MINUTE = 60
