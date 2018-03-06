import unittest
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


if __name__ == '__main__':
    unittest.main()
