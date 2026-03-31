"""Console entry point for interactive sprint fuel calculations."""

from calculations import (
    validate_input,
    validate_lap_time,
    validate_fuel_per_lap
)
from models import SprintRace
from constants import MIN_SPRINT_RACE_DURATION, MAX_SPRINT_RACE_DURATION


def run_console_calculator():
    """Run interactive CLI flow and print sprint fuel calculation results."""
    print('🏎️  ACC Sprint Race Fuel Calculator  🏎️')
    print('Enter your race details below.')

    while True:
        race_duration = input('Race duration (m):')

        try:
            race_duration = validate_input(
                race_duration,
                MIN_SPRINT_RACE_DURATION,
                MAX_SPRINT_RACE_DURATION
                )
            break
        except ValueError as e:
            print(e)

    while True:
        lap_time = input('Lap time (mm:ss):')

        try:
            lap_time = validate_lap_time(lap_time)
            break
        except ValueError as e:
            print(e)

    while True:
        fuel_per_lap = input('Fuel per lap (l):')

        try:
            fuel_per_lap = validate_fuel_per_lap(fuel_per_lap)
            break
        except ValueError as e:
            print(e)

    race = SprintRace(race_duration, lap_time, fuel_per_lap)

    print('=== Results ===')

    race.calculate()

    print(race)


if __name__ == '__main__':
    run_console_calculator()
