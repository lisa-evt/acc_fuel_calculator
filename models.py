from calculations import calculate_laps_from_time, calculate_fuel_needed

class RaceConfig:
    def __init__(self, race_duration_min, lap_time, fuel_per_lap, laps=None, fuel_needed=None, fuel_with_one_extra_lap=None, exceeds_tank=None):
        self.race_duration_min = race_duration_min
        self.lap_time = lap_time
        self.fuel_per_lap = fuel_per_lap
        self.laps = laps
        self.fuel_needed = fuel_needed
        self.fuel_with_one_extra_lap = fuel_with_one_extra_lap
        self.exceeds_tank = exceeds_tank

    def calculate(self):
        self.laps = calculate_laps_from_time(self.race_duration_min, self.lap_time)
        self.fuel_needed, self.fuel_with_one_extra_lap, self.exceeds_tank = calculate_fuel_needed(self.laps, self.fuel_per_lap)

    def __str__(self):
        return f"""
        Race duration: {self.race_duration_min} min
        Lap time: {self.lap_time} sec
        Fuel per lap: {self.fuel_per_lap} L
        Laps: {self.laps}
        Fuel needed: {self.fuel_needed} L
        Fuel with buffer: {self.fuel_with_one_extra_lap} L
        Exceeds tank: {self.exceeds_tank}
        """

class SprintRace(RaceConfig):

    def __str__(self):
        return f"""
        Race type: Sprint
        Race duration: {self.race_duration_min} min
        Lap time: {self.lap_time} sec
        Fuel per lap: {self.fuel_per_lap} L
        Laps: {self.laps}
        Fuel needed: {self.fuel_needed} L
        Fuel with buffer: {self.fuel_with_one_extra_lap} L
        Exceeds tank: {self.exceeds_tank}
        """