# coding=UTF-8

from controller.WordListGenerator import *
from data.db_setup import *
from interface.MyParser import MyParser
from output.TerminalPrinter import TerminalPrinter
import arrow
import output.doc_create.CreateHTML as CreateHTML
from output.SendEmail import *

cmd_folder = os.path.realpath(os.path.dirname(inspect.getfile(inspect.currentframe(0)))+'/interface/')
if cmd_folder not in sys.path:
	sys.path.insert(0, cmd_folder)

cmd_folder = os.path.realpath(os.path.dirname(inspect.getfile(inspect.currentframe(0)))+'/data/')
if cmd_folder not in sys.path:
	sys.path.insert(0, cmd_folder)


parser = MyParser(epilog="""Language Options:\n\tes - Spanish\n\ten - English\n\tit - Italian\nPairing options (learned -> native):\n\tes -> en\n\tit -> en\n""")

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
parser.add_option("-e", "--email", action="store_true", dest="email",
				  help="Send to email")

(options, args) = parser.parse_args()

if __name__ == '__main__':
	if not check(options.learned):
		setup(options.learned)
	term_print = TerminalPrinter()
	if options.weekly:
		print "Words Learned In The Last Week.\n"
		print term_print.periodic_list_printout(periodic_revision(options.learned, weeks=-1))
	elif options.monthly:
		print "Words Learned In The Last Month.\n"
		print term_print.periodic_list_printout(periodic_revision(options.learned,months=-1))
	elif options.yearly:
		print "Words Learned In The Last Year.\n"
		print term_print.periodic_list_printout(periodic_revision(options.learned,years=-1))
	else:
		word_list = daily_list(int(options.quantity),unicode(options.native,sys.stdin.encoding).encode('utf-8'),unicode(options.learned, sys.stdin.encoding).encode('utf-8'))
		term_print = TerminalPrinter()
		print term_print.std_printout(word_list)
		print term_print.test_printout(word_list)
		if options.email:
			address = "peterf.meckiffe@gmail.com"
			HTMLCreator = CreateHTML.CreateHTML()
			html = HTMLCreator.createHTML(word_list,test=True)
			sendMail(address, html)

