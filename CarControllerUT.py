import unittest
from unittest import mock
from TestData import *
from CarController import CarController
from Engine import Engine
from GearBox import GearBox
from Electronics import Electronics
from StatusPanel import StatusPanel


class ControllerUT(unittest.TestCase):
    def setUp(self):
        self.ctrl = CarController()
        self.panel = StatusPanel()
        self.electronics = Electronics()

    def test_interface_get_ready_to_go(self):
        """
        GIVEN :engine, gearbox, electronics, status_panel
        WHEN  :call get_ready_to_go interface
        THEN  :return true
        """
        self.assertTrue(self.ctrl.get_ready_to_go(Engine(), GearBox(), Electronics(), StatusPanel()))

    def test_interface_go_forward_001(self):
        """
        GIVEN :engine, status_panel,CarController
        GIVEN :CarController call go_forward interface
        WHEN  :electronics.engine_is_running() return True
        WHEN  :status_panel.there_is_enough_fuel() return True
        THEN  :electronics.accelerate will be call
        """
        self.electronics.accelerate = mock.Mock(return_value=None)

        for Data in TestData['GO_FORWARD']:
            self.panel.there_is_enough_fuel = mock.Mock(return_value=Data['FUEL_IS_ENOUGH'])
            self.electronics.engine_is_running = mock.Mock(return_value=Data['ENGINE_IS_RUNNING'])

        self.ctrl.go_forward(self.electronics, self.panel)
        self.assertEqual(Data['CALLED_CNT'], self.electronics.accelerate.call_count)


if __name__ == '__main__':
    unittest.main()
