from constants import MAX_FUEL_PER_LAP, MIN_FUEL_PER_LAP, MAX_LAP_TIME_SEC, MIN_LAP_TIME_SEC, MIN_SPRINT_RACE_DURATION, MAX_SPRINT_RACE_DURATION, MAX_FUEL_CAPACITY, SECONDS_IN_MINUTE

from math import ceil


def validate_input(value, min_val, max_val):
    try:
        value = float(value)
    except ValueError:
        raise ValueError('Value must be a number')

    if min_val <= value <= max_val:
        return value
    else:
        raise ValueError(f'Value must be between {min_val} and {max_val}')

def validate_lap_time(lap_time_str):
    lap_time_str = lap_time_str.split(':')
    if len(lap_time_str) != 2:
        raise ValueError(f'Lap time must be mm:ss')

    try:
        lap_time_min = int(lap_time_str[0])
        lap_time_sec = int(lap_time_str[1])
    except ValueError:
        raise ValueError('Lap time must be mm:ss')

    if not (0 <= lap_time_sec < 60):
        raise ValueError('Seconds must be between 0 and 59')

    if lap_time_min <= 0:
        raise ValueError('Minutes must be a positive integer')

    lap_time = lap_time_min * SECONDS_IN_MINUTE + lap_time_sec

    if MIN_LAP_TIME_SEC <= lap_time <= MAX_LAP_TIME_SEC:
        return lap_time
    else:
        raise ValueError(f'Lap time must be between {MIN_LAP_TIME_SEC} and {MAX_LAP_TIME_SEC}')

def validate_fuel_per_lap(fuel_str):
    fuel_per_lap = validate_input(fuel_str, MIN_FUEL_PER_LAP, MAX_FUEL_PER_LAP)
    return fuel_per_lap

def calculate_laps_from_time(race_duration, lap_time):
    total_laps = (race_duration * 60) / lap_time

    return ceil(total_laps)

def calculate_fuel_needed(total_laps, fuel_per_lap):
    fuel_needed = ceil(total_laps * fuel_per_lap)
    fuel_with_one_extra_lap = ceil((total_laps + 1) * fuel_per_lap)
    exceeds_tank = fuel_with_one_extra_lap > MAX_FUEL_CAPACITY

    return fuel_needed, fuel_with_one_extra_lap, exceeds_tank
