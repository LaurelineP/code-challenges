import re
def convert_time( time: str):
	''' Toggles the time from one format to the other 
	- either 12h format to 24h
	- either 24h format to 12h
	'''

	# [ Error handling ]: expects 2 digits separated by ":" and potentially a meridiem (am|pm)
	time = time.strip()
	is_valid_input_fmt = True if re.match(r'\d{1,2}:\d{1,2}\s?[am|pm]?', time) else False
	if not is_valid_input_fmt:
		raise Exception("Invalid input")

	# Parsing values and detaigpls about time
	time_details = re.split(r'[:\s]', time)
	time_details_length = len(time_details)


	# Original Time details - value ref
	hours  		= int(time_details[0])
	minutes 	= int(time_details[1])
	meridiem 	= time_details[2] if time_details_length == 3 else None

	# [ Error handling ]: expects input's hours or minutes to not be negative
	if hours < 0 or minutes < 0:
		raise Exception("Invalid time")

	_hours = None
	_meridiem = None
	# Output handling ---------------------------------------------------
	# 12h format input - ex 1:30pm to 13:30
	if meridiem:
		if meridiem == 'pm':
			_hours = 12 if hours == 12 else hours + 12
		if meridiem == 'am':
			_hours = 0 if not hours else hours if hours < 12 else 0

	# 24 format input - ex 13:30 to 1:30pm
	else:
		_hours = hours - 12 if hours > 12 \
			else hours if hours in range(1, 13) else \
				hours + 12

		_meridiem = 'pm' if hours >= 12 else 'am'


	_hours = f"{_hours:02d}" if _hours == 0 else _hours
	HH_MM = f"{_hours}:{minutes:02d}"
	result = f"{HH_MM} {_meridiem}" if _meridiem else HH_MM
	return result

