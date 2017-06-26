import unittest
from web_services.volume_calculator.formulas import Formulas as formulas


class FormulaTests(unittest.TestCase):

    def test_cube_volume(self):
        cube_volume_test_values = [
            {'value': 3, 'expected_value': 27},
            {'value': -3, 'expected_value': -27},
            {'value': 3.0, 'expected_value': 27.0},
            {'value': 3.5, 'expected_value': 42.875},
            {'value': 2375, 'expected_value': 13396484375},
            {'value': 22.698, 'expected_value': 11693.991532392001}
        ]

        for item in cube_volume_test_values:
            self.assertEqual(formulas.cube_volume(side=item.get('value')),
                             item.get('expected_value'))

    def test_sphere_volume(self):
        sphere_volume_test_values = [
            {'value': 3, 'expected_value': 113.09733552923254},
            {'value': 3.0, 'expected_value': 113.09733552923254},
            {'value': 3.5, 'expected_value': 179.5943800302165},
            {'value': 22.698, 'expected_value': 48983.67718573861}
        ]
        for item in sphere_volume_test_values:
            self.assertEqual(formulas.sphere_volume(radius=item.get('value')),
                             item.get('expected_value'))

    def test_right_square_pyramid_volume(self):
        right_sq_pyramid_volume_test_values = [
            {'base_edge': 3, 'height': 5, 'expected_value': 15},
            {'base_edge': 3.5, 'height': 5.5, 'expected_value': 22.458333333333332},
            {'base_edge': -3, 'height': -5, 'expected_value': -15},
        ]
        for item in right_sq_pyramid_volume_test_values:
            self.assertEqual(formulas.right_square_pyramid(base_edge=item.get('base_edge'), height=item.get('height')),
                             item.get('expected_value'))