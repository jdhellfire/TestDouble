import unittest
from unittest import mock
from mock import create_autospec
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
        THEN  :electronics.accelerate will be call otherwise electronics.accelerate will not be call
        """
        self.electronics.accelerate = mock.Mock(return_value=None)

        for Data in TestData['GO_FORWARD']:
            self.panel.there_is_enough_fuel = mock.Mock(return_value=Data['FUEL_IS_ENOUGH'])
            self.electronics.engine_is_running = mock.Mock(return_value=Data['ENGINE_IS_RUNNING'])

        self.ctrl.go_forward(self.electronics, self.panel)
        self.assertEqual(Data['CALLED_CNT'], self.electronics.accelerate.call_count)

    def test_interface_stop_001(self):
        """
        GIVEN :electronics, status_panel
        WHEN  :call stop
        WHEN  :StatusPanel.get_speed() <= 0
        THEN  :stop will be call only once
        """
        """
        GIVEN :electronics, status_panel
        WHEN  :call stop
        WHEN  :StatusPanel.get_speed() > 0
        THEN  :stop will be call 2 ate least
        """

        half_braking_power = 50
        for data in TestData['STOP']:

            self.panel.get_speed = mock.Mock(side_effect=data['SPEED'])
            self.electronics.push_brakes = mock.Mock(return_value=None)

            self.ctrl.stop(half_braking_power, self.electronics, self.panel)
            self.assertEqual(data['CALLED_CNT'], self.panel.get_speed.call_count)


    # def test_interface_stop_002(self):
    #     """
    #     GIVEN :electronics, status_panel
    #     WHEN  :call stop
    #     WHEN  :StatusPanel.get_speed() = 0
    #     THEN  :stop will be call only once
    #     """
    #
    #     half_braking_power = 50
    #     self.panel.get_speed = mock.Mock(return_value=0)
    #     self.electronics.push_brakes = mock.Mock(return_value=None)
    #
    #     self.ctrl.stop(half_braking_power, self.electronics, self.panel)
    #     self.assertEqual(1, self.panel.get_speed.call_count)
    #
    # def test_interface_stop_003(self):
    #     """
    #     GIVEN :electronics, status_panel
    #     WHEN  :call stop
    #     WHEN  :StatusPanel.get_speed() > 0
    #     THEN  :stop will be call 2 ate least
    #     """
    #
    #     half_braking_power = 50
    #     self.panel.get_speed = mock.Mock(side_effect=[1, 0])
    #     self.electronics.push_brakes = mock.Mock(return_value=None)
    #
    #     self.ctrl.stop(half_braking_power, self.electronics, self.panel)
    #     self.assertEqual(2, self.panel.get_speed.call_count)
    #

if __name__ == '__main__':
    unittest.main()
