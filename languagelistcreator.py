from controller.DailyList import *
from data.db_setup import *
cmd_folder = os.path.realpath(os.path.dirname(inspect.getfile(inspect.currentframe(0)))+'/data/')
if cmd_folder not in sys.path:
	sys.path.insert(0, cmd_folder)
if __name__ == '__main__':
	if not check():
		setup()
	for item in daily_list(10,"en","es"):
		output =  "Word: "+item["word"]+"\n\tTranslations:\n"
		for trans in item["translations"]:
			output += "\t\t%s - %s\n" % (trans["original"],trans["translation"])
		if len(item["compound"])>0:
			output+="\tCompound Usage:"
			for trans in item["compound"]:
				output += "\t\t%s - %s\n" % (trans["original"],trans["translation"])
		print output
