# coding=UTF-8

from controller.WordListGenerator import *
from data.db_setup import *
from interface.MyParser import MyParser

cmd_folder = os.path.realpath(os.path.dirname(inspect.getfile(inspect.currentframe(0)))+'/interface/')
if cmd_folder not in sys.path:
	sys.path.insert(0, cmd_folder)

cmd_folder = os.path.realpath(os.path.dirname(inspect.getfile(inspect.currentframe(0)))+'/data/')
if cmd_folder not in sys.path:
	sys.path.insert(0, cmd_folder)


parser = MyParser(epilog="""Language Options:\n\tes - Spanish\n\ten - English\nPairing options (learned -> native):\n\tes -> en\n""")
parser.add_option("-l", "--learning", dest="learned", default="es",
		help="Type the first two letters of the language you want to learn. Default: es")
		  
parser.add_option("-n", "--native", dest="native", default="en",
		help="First two letters of laguage known. Default: en")
parser.add_option("-q", "--quantity", dest="quantity", default=10,
				  help="Number of words to learn today. Default 10")
parser.add_option("-m", "--monthly", action="store_true", dest="monthly",
				  help="Flag for monthly summary")
parser.add_option("-w", "--weekly", action="store_true", dest="weekly",
				  help="Flag for weekly summary")
parser.add_option("-y", "--yearly", action="store_true", dest="yearly",
				  help="Flag for yearly summary")
parser.add_option("-p", "--pdf", action="store_true", dest="pdf",
				  help="Output of lists go to pdf files")
(options, args) = parser.parse_args()

if __name__ == '__main__':
	if not check():
		setup()
	if options.weekly:
		print "Words Learned In The Last Week."
		for word in periodic_revision(weeks=-1):
			print "\t%s" % word
	elif options.monthly:
		print "Words Learned In The Last Month."
		for word in periodic_revision(months=-1):
			print "\t%s" % word
	elif options.yearly:
		print "Words Learned In The Last Year."
		for word in periodic_revision(years=-1):
			print "\t%s" % word
	else:
		for item in daily_list(int(options.quantity),unicode(options.native,sys.stdin.encoding).encode('utf-8'),unicode(options.learned, sys.stdin.encoding).encode('utf-8')):
			output =  "Word: "+item["word"]+"\n\tTranslations:\n"
			for trans in item["translations"]:
				output += "\t\t%s - %s\n" % (trans["original"],trans["translation"])
			if len(item["compound"])>0:
				output+="\tCompound Usage:\n"
				for trans in item["compound"]:
					output += "\t\t%s - %s\n" % (trans["original"],trans["translation"])
			print output
