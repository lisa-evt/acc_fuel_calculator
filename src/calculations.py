
"""Validation and calculation helpers for ACC sprint fuel planning."""

from math import ceil

from constants import (
    MAX_FUEL_PER_LAP,
    MIN_FUEL_PER_LAP,
    MAX_LAP_TIME_SEC,
    MIN_LAP_TIME_SEC,
    MAX_FUEL_CAPACITY,
    SECONDS_IN_MINUTE
)


def validate_input(
    value: str | int | float,
    min_val: int | float,
    max_val: int | float
) -> float:
    """Validate numeric input and check that it lies within a range.

    Args:
        value: User input that should represent a number.
        min_val: Lower inclusive boundary.
        max_val: Upper inclusive boundary.

    Returns:
        float: Parsed numeric value.

    Raises:
        ValueError: If input is not numeric or outside allowed range.
    """
    try:
        value = float(value)
    except ValueError as exc:
        raise ValueError('Value must be a number') from exc

    if min_val <= value <= max_val:
        return value
    else:
        raise ValueError(f'Value must be between {min_val} and {max_val}')


def validate_lap_time(lap_time_str: str) -> int:
    """Validate lap time in ``mm:ss`` format and convert it to seconds.

    Args:
        lap_time_str: Lap time string in minutes and seconds.

    Returns:
        int: Lap time in total seconds.

    Raises:
        ValueError: If format is invalid or value is out of configured range.
    """
    parts = lap_time_str.split(':')
    if len(parts) != 2:
        raise ValueError('Lap time must be mm:ss')

    try:
        lap_time_min = int(parts[0])
        lap_time_sec = int(parts[1])
    except ValueError as exc:
        raise ValueError('Lap time must be mm:ss') from exc

    if not 0 <= lap_time_sec < 60:
        raise ValueError('Seconds must be between 0 and 59')

    if lap_time_min <= 0:
        raise ValueError('Minutes must be a positive integer')

    lap_time = lap_time_min * SECONDS_IN_MINUTE + lap_time_sec

    if MIN_LAP_TIME_SEC <= lap_time <= MAX_LAP_TIME_SEC:
        return lap_time
    else:
        raise ValueError(
            f'Lap time must be between {MIN_LAP_TIME_SEC}'
            f' and {MAX_LAP_TIME_SEC}'
            )


def validate_fuel_per_lap(fuel_str: str | int | float) -> float:
    """Validate fuel consumption per lap.

    Args:
        fuel_str: User input with fuel consumption in liters per lap.

    Returns:
        float: Parsed fuel value.
    """

    return validate_input(fuel_str, MIN_FUEL_PER_LAP, MAX_FUEL_PER_LAP)


def calculate_laps_from_time(
    race_duration: int | float,
    lap_time: int | float
) -> int:
    """Calculate estimated number of laps for a timed race.

    Args:
        race_duration: Race duration in minutes.
        lap_time: Average lap time in seconds.

    Returns:
        int: Number of laps rounded up to ensure completion.
    """
    total_laps = (race_duration * 60) / lap_time

    return ceil(total_laps)


def calculate_fuel_needed(
    total_laps: int,
    fuel_per_lap: int | float
) -> tuple[int, int, bool]:
    """Calculate base fuel, buffered fuel, and tank limit flag.

    Args:
        total_laps: Number of laps to cover.
        fuel_per_lap: Fuel consumption in liters per lap.

    Returns:
        tuple[int, int, bool]: Base fuel, fuel with +1 lap buffer,
        and whether buffered fuel exceeds max tank capacity.
    """
    fuel_needed = ceil(total_laps * fuel_per_lap)
    fuel_with_one_extra_lap = ceil((total_laps + 1) * fuel_per_lap)
    exceeds_tank = fuel_with_one_extra_lap > MAX_FUEL_CAPACITY

    return fuel_needed, fuel_with_one_extra_lap, exceeds_tank
