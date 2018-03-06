import unittest
from CarController import CarController
from Engine import Engine
from GearBox import GearBox
from Electronics import Electronics
from StatusPanel import StatusPanel

class ControllerUT(unittest.TestCase):
    def test_interface_get_ready_to_go(self):
        """
        GIVEN :engine, gearbox, electronics, status_panel
        WHEN  :call get_ready_to_go interface
        THEN  :return true
        """
        ctrl = CarController()
        self.assertTrue(ctrl.get_ready_to_go(Engine(),GearBox(),Electronics(),StatusPanel()))


if __name__ == '__main__':
    unittest.main()
