import unittest
from unittest import mock
from CarController import CarController
from Engine import Engine
from GearBox import GearBox
from Electronics import Electronics
from StatusPanel import StatusPanel


class ControllerUT(unittest.TestCase):
    def setUp(self):
        self.ctrl = CarController()

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
        panel = StatusPanel()
        electronics = Electronics()

        electronics.accelerate = mock.Mock(return_value=None)
        panel.there_is_enough_fuel = mock.Mock(return_value=True)
        electronics.engine_is_running = mock.Mock(return_value=True)

        self.ctrl.go_forward(electronics, panel)
        electronics.accelerate.assert_called_once()

    def test_interface_go_forward_002(self):
        """
        GIVEN :engine, status_panel,CarController
        GIVEN :CarController call go_forward interface
        WHEN  :electronics.engine_is_running() return flase
        WHEN  :status_panel.there_is_enough_fuel() return True
        THEN  :electronics.accelerate will not be call
        """
        panel = StatusPanel()
        electronics = Electronics()

        electronics.accelerate = mock.Mock(return_value=None)
        panel.there_is_enough_fuel = mock.Mock(return_value=True)
        electronics.engine_is_running = mock.Mock(return_value=False)

        self.ctrl.go_forward(electronics, panel)
        electronics.accelerate.assert_not_called()


if __name__ == '__main__':
    unittest.main()
