import re

def log_test_name(fn):
	def wrapper(self):
		outline_header = "=" * 70
		parsed_title = self._testMethodName.replace('_', ' ').upper()
		header_title = f"{' ' * 24}🧪 {parsed_title}"
		header = f"\n\n{outline_header}\n{header_title}\n{outline_header}\n"
		print(header)
		return fn(self)
	return wrapper

