from controller.DailyList import *
from data.db_setup import *
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-l", "--learning", dest="learned", default="es"
                  help="Type the first two letters of the language you want to learn. Default Spanish")
parser.add_option("-n", "--native", dest="native", default="en",
                  help="First two letters of laguage known. default English")
parser.add_option("-q", "--quantity", dest="quantity", default=10,
				  help="Number of words to learn today. Default 10")
parser.add_option("-m", "--monthly", action="store_true", dest="monthly",
				  help="Flag for monthly summary")
parser.add_option("-w", "--weekly", action="store_true", dest="weekly",
				  help="Flag for weekly summary")
parser.add_option("-m", "--yearly", action="store_true", dest="yearly",
				  help="Flag for yearly summary")

(options, args) = parser.parse_args()

cmd_folder = os.path.realpath(os.path.dirname(inspect.getfile(inspect.currentframe(0)))+'/data/')
if cmd_folder not in sys.path:
	sys.path.insert(0, cmd_folder)
if __name__ == '__main__':
	if not check():
		setup()
	for item in daily_list(options.quantity,options.native,options.learned):
		output =  "Word: "+item["word"]+"\n\tTranslations:\n"
		for trans in item["translations"]:
			output += "\t\t%s - %s\n" % (trans["original"],trans["translation"])
		if len(item["compound"])>0:
			output+="\tCompound Usage:"
			for trans in item["compound"]:
				output += "\t\t%s - %s\n" % (trans["original"],trans["translation"])
		print output
