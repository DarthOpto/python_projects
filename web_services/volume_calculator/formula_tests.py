import unittest
import web_services.volume_calculator.formulas as formulas


class FormulaTests(unittest.TestCase):

    def test_cube_volume(self):
        cube_volume_test_values = [
            {'value': 3, 'expected_value': 27},
            {'value': 3.0, 'expected_value': 27.0},
            {'value': 3.5, 'expected_value': 42.88},
            {'value': 2375, 'expected_value': 13396484375},
            {'value': 22.698, 'expected_value': 11693.99}
        ]

        for item in cube_volume_test_values:
            self.assertEqual(formulas.cube_volume(side=item.get('value')),
                             item.get('expected_value'))

    def test_cube_volume_negative(self):
        cube_volume_test_values = [0, -1, -.25, -3.5]
        with self.assertRaises(Exception) as context:
            for item in cube_volume_test_values:
                formulas.cube_volume(side=item)
                self.assertTrue('Side length must be greater than 0' in str(context.exception))

    def test_sphere_volume(self):
        sphere_volume_test_values = [
            {'radius': 3, 'expected_value': 113.1},
            {'radius': 3.0, 'expected_value': 113.1},
            {'radius': 3.5, 'expected_value': 179.59},
            {'radius': 22.698, 'expected_value': 48983.68}
        ]
        for item in sphere_volume_test_values:
            self.assertEqual(formulas.sphere_volume(radius=item.get('radius')),
                             item.get('expected_value'))

    def test_sphere_volume_negative(self):
        sphere_volume_test_values = [0, -1, -.25, -3.25]
        with self.assertRaises(Exception) as context:
            for item in sphere_volume_test_values:
                formulas.sphere_volume(radius=item)
                self.assertTrue('Radius must be greater than 0' in str(context.exception))

    def test_right_square_pyramid_volume(self):
        right_sq_pyramid_volume_test_values = [
            {'base_edge': 3, 'height': 5, 'expected_value': 15},
            {'base_edge': 3.5, 'height': 5.5, 'expected_value': 22.46},
        ]
        for item in right_sq_pyramid_volume_test_values:
            self.assertEqual(formulas.right_square_pyramid(base_edge=item.get('base_edge'), height=item.get('height')),
                             item.get('expected_value'))

    def test_right_square_pyramids_negative(self):
        right_sq_pyramid_volume_test_values = [
            {'base_edge': 0, 'height': 5},
            {'base_edge': 3.5, 'height': 0},
            {'base_edge': 0, 'height': 0},
            {'base_edge': -3, 'height': 5},
            {'base_edge': 3, 'height': -5},
        ]
        with self.assertRaises(Exception) as context:
            for item in right_sq_pyramid_volume_test_values:
                formulas.right_square_pyramid(base_edge=item.get('base_edge'), height=item.get('height'))
                self.assertTrue('Base Edge and/or Height must be greater than 0' in str(context.exception))

    def test_cylinder_volume(self):
        cylinder_volume_test_values = [
            {'radius': 3, 'height': 3, 'expected_value': 84.82},
            {'radius': 3.0, 'height': 3.0, 'expected_value': 84.82},
            {'radius': 3.65, 'height': 3.75, 'expected_value': 156.95},
            {'radius': 10, 'height': 9.67, 'expected_value': 3037.92},
            {'radius': .25, 'height': .75, 'expected_value': .15}
        ]

        for item in cylinder_volume_test_values:
            self.assertEqual(formulas.cylinder_volume(radius=item.get('radius'), height=item.get('height')),
                             item.get('expected_value'))

    def test_cylinder_volume_negative(self):
        cylinder_volume_test_values = [
            {'radius': -3, 'height': 3.0},
            {'radius': 3, 'height': -3},
            {'radius': 0, 'height': 3},
            {'radius': 3, 'height': 0},
        ]
        with self.assertRaises(Exception) as context:
            for item in cylinder_volume_test_values:
                formulas.cylinder_volume(radius=item.get('radius'), height=item.get('height'))
                self.assertTrue('Radius and/or Height must be greater than 0' in str(context.exception))

    def test_dodecahedron_volume(self):
        dodecahedron_test_values = [
            {'side': 3, 'expected_value': 206.9},
            {'side': 10, 'expected_value': 7663.12},
            {'side': .25, 'expected_value': .12},
            {'side': 7.659, 'expected_value': 3442.88}
        ]
        for item in dodecahedron_test_values:
            self.assertEqual(formulas.dodecahedron_volume(item.get('side')), item.get('expected_value'))

    def test_dodecahedron_volume_negative(self):
        dodecahedron_test_values = [0, -.25, -1, -3.25]
        with self.assertRaises(Exception) as context:
            for item in dodecahedron_test_values:
                formulas.dodecahedron_volume(item)
                self.assertTrue('Side length much be greater than 0' in str(context.exception))