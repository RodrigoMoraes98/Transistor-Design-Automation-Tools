import os
import sys

home_directory = os.path.expanduser( '~' )

def simulate(technology, kwargs, pmos=False):
	if pmos == False:
		fileTxt_n = open(str(home_directory) + "/Circuit Sizing Tool/files/parametros_n.txt", 'w')

		var = []

		for key, value in zip(kwargs.keys(),kwargs.values()):
			var.append(str(key) + "=" + str(value))
	
		sys.stdout = fileTxt_n
		print("//parametros da simulacao")
		print("simulator lang=spectre")
		print("parameters", end=" ")
		print(*var)
		sys.stdout = sys.__stdout__
		fileTxt_n.close()

		if technology == '180nm':
			os.system('spectre -64 ' + str(home_directory) + '/Circuit\ Sizing\ Tool/netlist/tsmc180/nmos_dc180.scs -format psfascii')
			arq = open(str(home_directory) + '/Circuit Sizing Tool/netlist/tsmc180/nmos_dc180.raw/dcOpInfo.info', 'r')
		elif technology == '65nm':
			os.system('spectre -64 ' + str(home_directory) + '/Circuit\ Sizing\ Tool/netlist/tsmc65/nmos_dc65.scs -format psfascii')
			arq = open(str(home_directory) + '/Circuit Sizing Tool/netlist/tsmc65/nmos_dc65.raw/dcOpInfo.info', 'r')

	if pmos == True:
		fileTxt_p = open(str(home_directory) + "/Circuit Sizing Tool/files/parametros_p.txt", 'w')

		var = []

		for key, value in zip(kwargs.keys(),kwargs.values()):
			var.append(str(key) + "=" + str(value))
	
		sys.stdout = fileTxt_p
		print("//parametros da simulacao")
		print("simulator lang=spectre")
		print("parameters", end=" ")
		print(*var)
		sys.stdout = sys.__stdout__
		fileTxt_p.close()

		if technology == '180nm':
			os.system('spectre -64 ' + str(home_directory) + '/Circuit\ Sizing\ Tool/netlist/tsmc180/pmos_dc180.scs -format psfascii')
			arq = open(str(home_directory) + '/Circuit Sizing Tool/netlist/tsmc180/pmos_dc180.raw/dcOpInfo.info', 'r')
		elif technology == '65nm':
			os.system('spectre -64 ' + str(home_directory) + '/Circuit\ Sizing\ Tool/netlist/tsmc65/pmos_dc65.scs -format psfascii')
			arq = open(str(home_directory) + '/Circuit Sizing Tool/netlist/tsmc65/pmos_dc65.raw/dcOpInfo.info', 'r')


	variables = []
	values = []
	index = 0


	text = arq.readlines()
	for line in text:
		for word in line.split():
			index = word.find("FLOAT")
			index2 = word.find("INT")
			if index != -1:
				variables.append(line.split()[0])
			if index2 != -1:
				variables.append(line.split()[0])
	for i in range(442, 544):
		values.append(text[i])
	variables = [i.replace('"', '') for i in variables]

	return variables, values

