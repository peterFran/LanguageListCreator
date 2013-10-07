from controller.DailyList import *
cmd_folder = os.path.realpath(os.path.dirname(inspect.getfile(inspect.currentframe(0)))+'/data/')
if cmd_folder not in sys.path:
	sys.path.insert(0, cmd_folder)
if __name__ == '__main__':
	lista = daily_list(10,"en","es")
	for i in lista:
		print i,"\n",lista[i]["term0"]["PrincipalTranslations"],"\n\n"

