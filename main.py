from math import ceil

race_time = int(input("Enter the race time (minutes): "))

lap_time = str(input("Enter the lap time (mm:ss): ")).split(':')

fuel_per_lap = float(input("Enter the fuel per lap (liters): "))



def calculate_fuel(race_time, lap_time, fuel_per_lap):
    race_time_seconds = race_time * 60
    lap_time_seconds = int(lap_time[0]) * 60 + int(lap_time[1])
    total_laps = ceil(race_time_seconds / lap_time_seconds)
    total_fuel = total_laps * fuel_per_lap
    return ceil(total_fuel)

total_fuel_needed = calculate_fuel(race_time, lap_time, fuel_per_lap)

print(f"Total fuel needed: {total_fuel_needed} liters")