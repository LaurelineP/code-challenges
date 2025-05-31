import unittest
from convert_time.index import convert_time
from __utils.test_utilities import log_test_name

regular_tests_24h = [
	("13:40", "1:40 pm"),
	("9:30", "9:30 am")
]

tricky_tests_24h = [
	("12:00", "12:00 pm"),
	("00:00", "12:00 am")
]

regular_test_12h = [
	("15:29", "3:29 pm"),
	("11:55", "11:55 am")
]

tricky_test_12h = [
	("1:12 am ", "1:12"),
	("1:12 pm ", "13:12"),
	("12:07 am", "00:07"),
	("12:31 pm", "12:31"),
]

def log_details(input_str, output_str):
	print( f"[ {convert_time.__name__.upper()} ]: {input_str} > {output_str}")
class TestConvertTime( unittest.TestCase ):
	'''Test Suite for convert time function '''
	@log_test_name
	def test_regular_24h_inputs(self):
		for (test_arg, expected_arg) in regular_tests_24h:
			log_details(test_arg, expected_arg)
			self.assertEqual(convert_time(test_arg), expected_arg)


	@log_test_name
	def test_tricky_24h_inputs(self):
		for (test_arg, expected_arg) in tricky_tests_24h:
			log_details(test_arg, expected_arg)
			self.assertEqual(convert_time(test_arg), expected_arg)

	@log_test_name
	def test_regular_12h_inputs(self):
		for (test_arg, expected_arg) in regular_test_12h:
			log_details(test_arg, expected_arg)
			self.assertEqual(convert_time(test_arg), expected_arg)

	@log_test_name
	def test_tricky_12h_inputs(self):
		for (test_arg, expected_arg) in tricky_test_12h:
			log_details(test_arg, expected_arg)
			self.assertEqual(convert_time(test_arg), expected_arg)

if __name__ == '__main__':
    unittest.main()