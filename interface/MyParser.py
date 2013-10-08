from optparse import OptionParser
class MyParser(OptionParser):
	def format_epilog(self, formatter):
		return self.epilog

