class TerminalPrinter(object):
	DEFINITION = False
	def std_printout(self, daily_list):
		output = u"##########################\n##### STANDARD OUTPUT ####\n##########################\n"
		for item in daily_list:
                        output +=  "Word: "+item["word"]+"\n\tTranslations:\n"
                        for trans in item["translations"]:
                                output += "\t\t%s - %s\n" % (trans["original"],trans["translation"])
	                if len(item["compound"])>0:
				output+="\tCompound Usage:\n"
				for trans in item["compound"]:
					output += "\t\t%s - %s\n" % (trans["original"],trans["translation"])
		return output
	def test_printout(self, daily_list):
		output= u"##########################\n####### TEST OUTPUT ######\n##########################\n"
		output+=u"Words:\n"
		for item in daily_list:
			output+=u"\t"+item["word"]+u"\n"
		output+=u"\nTranslations:\n"
		for item in daily_list:
			try:
				output+=u"\t"+item["translations"][0]["translation"]+u"\n"
			except:
				pass
		return output
