import unittest
from 64_python import FirstSimpleClass, SecondSimpleClass

class TestCaseFirstSimpleClass(unittest.TestCase):
    def setUp(self) -> None:
        self.fsc = FirstSimpleClass({1, 2, 3, 4, 5})

    def tearDown(self) -> None:
        print(f'Test completed perfectly...')

    # TODO def sum_set
    def test_sum_set_res_int(self):
        result = self.fsc.sum_set()
        self.assertEqual(15, result)

    def test_sum_set_res_not_str(self):
        result = self.fsc.sum_set()
        self.assertNotEqual('15', result)

    def test_sum_set_res_not_none(self):
        result = self.fsc.sum_set()
        self.assertIsNotNone(result)

    def test_sum_set_res_type(self):
        result = self.fsc.sum_set()
        self.assertIsInstance(result, int)

    # TODO def avg_set
    def test_avg_set_res_int(self):
        result = self.fsc.avg_set()
        self.assertEqual(3, result)

    def test_avg_set_res_not_str(self):
        result = self.fsc.avg_set()
        self.assertNotEqual('3', result)

    def test_avg_set_res_not_none(self):
        result = self.fsc.avg_set()
        self.assertIsNotNone(result)

    def test_avg_set_res_type(self):
        result = self.fsc.avg_set()
        self.assertIsInstance(result,float)

    # TODO def max_set
    def test_max_set_res_int(self):
        self.assertEqual(5, self.fsc.max_set())

    def test_max_set_res_not_str(self):
        self.assertNotEqual('3', self.fsc.max_set())

    def test_max_set_res_not_none(self):
        result = self.fsc.max_set()
        self.assertIsNotNone(result)

    def test_max_set_res_type(self):
        result = self.fsc.max_set()
        self.assertIsInstance(result, int)

    # TODO def min_set
    def test_min_set_res_int(self):
        result = self.fsc.min_set()
        self.assertEqual(1, result)

    def test_min_set_res_not_str(self):
        result = self.fsc.min_set()
        self.assertNotEqual('3', result)

    def test_min_set_res_not_none(self):
        result = self.fsc.min_set()
        self.assertIsNotNone(result)

    def test_min_set_res_type(self):
        result = self.fsc.min_set()
        self.assertIsInstance(result, int)


class TestCaseSecondSimpleClass(unittest.TestCase):

    def setUp(self) -> None:
        self.ssc = SecondSimpleClass(10)

    def tearDown(self) -> None:
        print(f'Test completed perfectly...')

    # TODO def get value
    def test_get_value_int(self):
        print('test_get_value_int')
        self.ssc.value = 10
        result = self.ssc.value
        self.assertEqual(10,result)

    # TODO def get string value
    def test_get_value_str(self):
        print('test_get_value_str')
        # TODO first type test
        self.assertRaises(TypeError,self.ssc.value,'10')
        # TODO second type test
        # with self.assertRaises(TypeError):
        #     self.ssc.value = '10'


    # TODO def convert_value_to_octal_system
    def test_convert_value_to_octal_system_res_int(self):
        print('test_convert_value_to_octal_system_res_int')
        result = self.ssc.convert_value_to_octal_system()
        self.assertEqual(oct(0o12), result)

    def test_convert_value_to_octal_system_res_not_none(self):
        print('test_convert_value_to_octal_system_res_not_none')
        result = self.ssc.convert_value_to_octal_system()
        self.assertIsNotNone(result)


    # TODO def convert_value_to_hexadecimal_system
    def test_convert_value_to_hexadecimal_system_res_int(self):
        print('test_convert_value_to_hexadecimal_system_res_int')
        result = self.ssc.convert_value_to_hexadecimal_system()
        self.assertEqual(hex(0xa), result)

    def test_convert_value_to_hexadecimal_system_res_none(self):
        print('test_convert_value_to_hexadecimal_system_res_none')
        result = self.ssc.convert_value_to_hexadecimal_system()
        self.assertIsNotNone(result)


    # TODO def convert_value_to_binary_system
    def test_convert_value_to_binary_system_res_int(self):
        print('test_convert_value_to_binary_system_res_int')
        result = self.ssc.convert_value_to_binary_system()
        self.assertEqual(bin(0b1010), result)

    def test_convert_value_to_binary_system_res_none(self):
        print('test_convert_value_to_binary_system_res_none')
        result = self.ssc.convert_value_to_binary_system()
        self.assertIsNotNone(result)