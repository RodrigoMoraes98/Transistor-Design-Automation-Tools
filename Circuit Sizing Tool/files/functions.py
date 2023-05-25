import sys
import os
import shutil

home_directory = os.path.expanduser( '~' )

def results(technology, target_name, par_ref, par_calc_name, w, variables, values, pmos=False):

	if technology == '180nm':
		if pmos == False:
			out_file_name = str(home_directory) + "/Circuit Sizing Tool/files/outputs/output_nmos180.txt"
		elif pmos == True:
			out_file_name = str(home_directory) + "/Circuit Sizing Tool/files/outputs/output_pmos180.txt"
	elif technology == '65nm':
		if pmos == False:
			out_file_name = str(home_directory) + "/Circuit Sizing Tool/files/outputs/output_nmos65.txt"
		elif pmos == True:
			out_file_name = str(home_directory) + "/Circuit Sizing Tool/files/outputs/output_pmos65.txt"

	output = open(out_file_name, 'w')
	sys.stdout = output

	print("#############################################")
	print(str(target_name) + " = " + str(par_ref))
	print(str(par_calc_name) + " = " + str(w))
	print("################ Parameters #################")
	for key, value in zip(variables, values):
		print(str(key) + " = " + str(value))
	print("#############################################")

	sys.stdout = sys.__stdout__
	output.close()

	shutil.copy(out_file_name, str(home_directory) + "/Circuit Sizing Tool/files/outputs/out_sweep.txt")

def search(par_to_search, input_list):
	for line in input_list:
		for word in line.split():
			if word == par_to_search:
				ids = float(line.split()[2])
	return search_value

def search_index(par_to_search, input_list):
	index = input_list.index(par_to_search)
	return index

def inputs(input_file):
	file = open(input_file, 'r')

	inputs = []
	for line in file.readlines():
		if line != '\n':
			inputs.append(line)
	file.close()

	inputs = [i.replace('\n', ',') for i in inputs]

	target_name = inputs[0][:-1].split('=')[1]
	target_value = float(inputs[1][:-1].split('=')[1])

	max_error = float(inputs[2][:-1].split('=')[1])
	par_calc_name = inputs[3][:-1].split('=')[1]
	nit = float(inputs[4][:-1].split('=')[1])

	Lmin = float(inputs[5][:-1].split('=')[1])
	Lmax = float(inputs[6][:-1].split('=')[1])
	Wmin = float(inputs[7][:-1].split('=')[1])
	Wmax = float(inputs[8][:-1].split('=')[1])

	size = [Lmin, round(Lmax,6), round(Wmin,8), Wmax]

	input_dict = {}
	for item in inputs[9:]:
		key, value = item.split("=")
		input_dict[str(key)] = value[:-1]
	par_calc_val = input_dict[par_calc_name]

	return input_dict, target_name, target_value, max_error, par_calc_name, par_calc_val, nit, size

def edit_input(input_file, kwargs):

	standard_parameters = ["target_name", "target_value", "max_error", "parameter_calc_name", "nit", "Lmin", "Lmax", "Wmin", "Wmax", "L", "M", "NF", "W", "VBS", "VGS", "VDS"]
	standard_values = ["ids", 100e-9, 0.01, "W", 30, Lmin, Lmax, Wmin, Wmax, 1e-6, 1, 1, 1e-6, 0, 0.25, 0.25]

	for key, value in zip(kwargs.keys(), kwargs.values()):
		for name in standard_parameters:
			if key == name:
				index = search_index(name, standard_parameters)
				standard_values[index] = value

	file = open(input_file, 'w')
	sys.stdout = file

	for par, val in zip(standard_parameters, standard_values):
		print(str(par) + "=" + str(val))

	sys.stdout = sys.__stdout__
	file.close()

def out_parameter(out_par, variables, values):
	for var, val in zip(variables, values):
		if out_par == var:
			out_val = val
	return out_val

def model(technology, model_name):

	if technology == '180nm':
		models_file = open(str(home_directory) + '/Circuit Sizing Tool/models/models180.txt', 'r')
	elif technology == '65nm':
		models_file = open(str(home_directory) + '/Circuit Sizing Tool/models/models65.txt', 'r')
	else:
		print(technology)
		print("Not available")
		exit()

	filetxt = []

	for line in models_file.readlines():
		filetxt.append(line)
	models_file.close()

	for i in range(len(filetxt)):
		if model_name in filetxt[i]:
			break

	global Lmin, Lmax, Wmin, Wmax

	model_name = filetxt[i].split()[0]
	Lmin = float(filetxt[i].split()[1])*float(filetxt[i].split()[5])
	Lmax = float(filetxt[i].split()[2])*float(filetxt[i].split()[5])
	Wmin = float(filetxt[i].split()[3])*float(filetxt[i].split()[5])
	Wmax = float(filetxt[i].split()[4])*float(filetxt[i].split()[5])

	if model_name == 'pch' or model_name == 'pch3' or model_name == 'mepch':
		pmos = True
		nmos = False

		if technology == '180nm':
			netlist_file = open(str(home_directory) + '/Circuit Sizing Tool/netlist/tsmc180/pmos_dc180.scs', 'r')
		elif technology == '65nm':
			netlist_file = open(str(home_directory) + '/Circuit Sizing Tool/netlist/tsmc65/pmos_dc65.scs', 'r')
		netlist_file_txt = netlist_file.readlines()
		netlist_file.close()

		if technology == '180nm':
			netlist_file_txt[46] = netlist_file_txt[46].replace(netlist_file_txt[46].split()[5], model_name)
		elif technology == '65nm':
			netlist_file_txt[14] = netlist_file_txt[14].replace(netlist_file_txt[14].split()[5], model_name)

		if technology == '180nm':
			netlist_out = open(str(home_directory) + '/Circuit Sizing Tool/netlist/tsmc180/pmos_dc180.scs', 'w')
		elif technology == '65nm':
			netlist_out = open(str(home_directory) + '/Circuit Sizing Tool/netlist/tsmc65/pmos_dc65.scs', 'w')
		netlist_out.writelines(netlist_file_txt)
		netlist_out.close()

	else:
		pmos = False
		nmos = True

		if technology == '180nm':
			netlist_file = open(str(home_directory) + '/Circuit Sizing Tool/netlist/tsmc180/nmos_dc180.scs', 'r')
		elif technology == '65nm':
			netlist_file = open(str(home_directory) + '/Circuit Sizing Tool/netlist/tsmc65/nmos_dc65.scs', 'r')
		netlist_file_txt = netlist_file.readlines()
		netlist_file.close()

		if technology == '180nm':
			netlist_file_txt[46] = netlist_file_txt[46].replace(netlist_file_txt[46].split()[5], model_name)
		elif technology == '65nm':
			netlist_file_txt[14] = netlist_file_txt[14].replace(netlist_file_txt[14].split()[5], model_name)

		if technology == '180nm':
			netlist_out = open(str(home_directory) + '/Circuit Sizing Tool/netlist/tsmc180/nmos_dc180.scs', 'w')
		elif technology == '65nm':
			netlist_out = open(str(home_directory) + '/Circuit Sizing Tool/netlist/tsmc65/nmos_dc65.scs', 'w')
		netlist_out.writelines(netlist_file_txt)
		netlist_out.close()

	return pmos, nmos
