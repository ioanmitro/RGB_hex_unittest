'''
1. The class tested is known as the class under test
In this case a class that uses a simplistic RGB to hex code
converter will be used
'''

class RgbhexConverter(object):
	def __init__(self, rgb_hex):
		self.rgb_hex = rgb_hex
		self.rgb_map = {'Black': '#000000', 'White': '#FFFFFF', 'Red': '#FF0000', 'Yellow': '#FFFF00'}

	def convert_to_hex(self):
		hex_val = None
		key = self.rgb_hex
		hex_val = self.rgb_map[key]
		return hex_val 
import unittest
class RgbhexConverterTest(unittest.TestCase):

# we will now create several methods whose names start with test,
# so they are automatically picked up by the test number of unittest

	def test_parsing_black(self):
		value = RgbhexConverter('Black')
		self.assertEqual('#000000', value.convert_to_hex())

	def test_parsing_white(self):
		value = RgbhexConverter('White')
		self.assertEqual('#FFFFFF', value.convert_to_hex())


	def test_parsing_red(self):
		value = RgbhexConverter('Red')
		self.assertEqual('#FF0000', value.convert_to_hex())


	def test_parsing_yellow(self):
		value = RgbhexConverter('Yellow')
		self.assertEqual('#FFFF00', value.convert_to_hex())				


# The next step is making the entire script executable and then 
# use the unittest's runner.

if __name__ == "__main__":
	unittest.main()
