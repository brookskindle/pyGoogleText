"""
	Brooks Kindle
	brooks.kindle@wsu.edu

	ParseError.py - a custom exception class that should be raised whenever 
			you are unable to parse a given text for a desired 
			value.
"""

class ParseError:
	"""Basic exception associated with parse failures"""

	def __init__(self):
		"""constructor"""

def main():
	"""starting point for the program"""
	test() #test ParseError

def test():
	"""tests the ParseError exception class"""
	try:
		print "Raising ParseErrror."
		raise ParseError
	except ParseError:
		print "Caught ParseError."

if __name__ == "__main__":
	main()
