class CreateHTML(object):
	def createHTML(self, word_list, standard=True, test=False):
		output = u"""<head>
					<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
				</head>
				<body>"""
		if standard:
			output+= self._dailyList(word_list)
		if test:
			output+= self._dailyTest(word_list)
		output += u"</body>"
		return output
	
	def _dailyList(self, word_list):
		output = u"""<h2>Words to learn</h2><br/>
			<table border="1">
			<tr>
				<td>Form</td>
				<td>Word</td>
				<td>Translation</td>
			</tr><tr></td><td></td><td></td><td></tr>"""
		for item in word_list:
			output += u"<tr><td>Translations</td><td>%s</td><td></td></tr>" % item["word"]
			for trans in item["translations"]:
				output += u"<tr><td></td><td>%s</td><td>%s</td></tr>" % (trans["original"],trans["translation"])
			if len(item["compound"])>0:
				output += u"<tr><td>Compound Usage</td><td></td><td></td></tr>"
				for trans in item["compound"]:
					output += u"<tr><td></td><td>%s</td><td>%s</td></tr>" % (trans["original"],trans["translation"])
			output+="<tr></td><td></td><td></td><td></tr>"
		output+= u"</table><br/>"
		return output

	def _dailyTest(self, word_list):
		output = u"<h2>Daily Tests</h2><br/>"
		output += u"<h3>Words Only</h3>"
		output = u"""<h2>Words to learn</h2><br/>
			<table border="1">
			<tr>
				<td>Word</td>
				<td>Enter Translation</td>
			</tr>"""
		for item in word_list:
			output+=u"<tr><td>%s</td><td><textbox></textbox></td></tr>"%item["word"]
		output+=u"</table>"
		output+=u"""<br/><h3>Translations Only</h3><br/><table border="1">
			<tr>
				<td>Word</td>
				<td>Enter Translation</td>
			</tr>"""
		for item in word_list:
			try:
				output+=u"<tr><td>%s</td><td><textbox></textbox></td></tr>" % item["translations"][0]["translation"]
			except:
				pass
		return output


