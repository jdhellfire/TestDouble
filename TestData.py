TestData = \
    {

        'GO_FORWARD': (
            {'FUEL_IS_ENOUGH': True, 'ENGINE_IS_RUNNING': True, 'CALLED_CNT': 1},
            {'FUEL_IS_ENOUGH': False, 'ENGINE_IS_RUNNING': True, 'CALLED_CNT': 0},
            {'FUEL_IS_ENOUGH': True, 'ENGINE_IS_RUNNING': False, 'CALLED_CNT': 0},
            {'FUEL_IS_ENOUGH': False, 'ENGINE_IS_RUNNING': False, 'CALLED_CNT': 0},
        ),
        'STOP': (
            {'SPEED': [-1], 'CALLED_CNT': 1},
            {'SPEED': [0], 'CALLED_CNT': 1},
            {'SPEED': [1, 0], 'CALLED_CNT': 2},
        )
    }
