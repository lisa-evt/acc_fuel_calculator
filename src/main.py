"""Kivy application entry point for the ACC fuel calculator."""

import os
import sys
import platform

from kivy.app import App  # type: ignore
from calculations import (
    validate_input,
    validate_lap_time,
    validate_fuel_per_lap
    )
from models import SprintRace
from constants import (
    MAX_FUEL_CAPACITY,
    MIN_SPRINT_RACE_DURATION,
    MAX_SPRINT_RACE_DURATION
)

if platform.system() == 'Windows':
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('acc.fuel.calculator')

def resource_path(filename):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, filename)
    return filename

class FuelCalculatorApp(App):
    """Main Kivy application that handles screen switching"""

    def switch_to_endurance(self) -> None:
        """Switch UI to the endurance screen."""
        self.root.current = 'endurance'

    def switch_to_sprint(self) -> None:
        """Switch UI to the sprint screen."""
        self.root.current = 'sprint'

    def calculate(self) -> None:
        """Read user input, validate it, and display calculated fuel values."""

        race_duration = self.root.ids.race_time.text
        lap_time = self.root.ids.lap_time.text
        fuel_per_lap = self.root.ids.fuel_per_lap.text

        try:
            race_duration = validate_input(
                race_duration,
                MIN_SPRINT_RACE_DURATION,
                MAX_SPRINT_RACE_DURATION
                )
            lap_time = validate_lap_time(lap_time)
            fuel_per_lap = validate_fuel_per_lap(fuel_per_lap)

            race = SprintRace(race_duration, lap_time, fuel_per_lap)
            race.calculate()
            self.root.ids.result_label.text = (
                f'Laps: {race.laps}  |'
                f' Fuel: {race.fuel_needed}L  |'
                f' With buffer: {race.fuel_with_one_extra_lap}L'
            )

            if race.exceeds_tank:
                self.root.ids.result_label.text += (
                    f'Warning: fuel exceeds tank capacity'
                    f' ({MAX_FUEL_CAPACITY}L)!'
                )

        except ValueError as e:
            self.root.ids.result_label.text = str(e)

    def build(self):
        """Build the Kivy application and set the window icon."""
        from kivy.resources import resource_add_path
        if platform.system() == 'Windows':
            self.icon = resource_path('app_icon.ico')
        else:
            self.icon = resource_path('icon.icns')
        resource_add_path(resource_path(''))

if __name__ == '__main__':
    FuelCalculatorApp().run()
