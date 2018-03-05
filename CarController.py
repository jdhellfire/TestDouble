from mock import *

class CarController:
    def get_ready_to_go(self, engine, gearbox, electronics, status_panel):
        return True

    def go_forward(self, electronics, status_panel):
        if electronics.engine_is_running() and status_panel.there_is_enough_fuel():
            electronics.accelerate()

    def stop(self, half_braking_power, electronics, status_panel):
        electronics.push_brakes(half_braking_power)
        if status_panel.get_speed() > 0:
            self.stop(half_braking_power, electronics, status_panel)
