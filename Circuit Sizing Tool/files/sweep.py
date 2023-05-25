import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import os, sys
home_directory = os.path.expanduser( '~' )
sys.path.append(str(home_directory) + '/Circuit Sizing Tool/files')

import main


def sweep(VarMin, VarMax, steps, sweepType, sweepVar, technology, transistorModel, targetName, targetValue, maxError,w, l, nf, m, vgs, vds, vbs, variable):
	actualStep = 0

	if sweepType == 'linear':
		sweep_variable = np.linspace(VarMin, VarMax, steps)
	if sweepType == 'logarithmic':
		sweep_variable = np.logspace(VarMin, VarMax, steps)
	parameter_defined = False
	
	for step in sweep_variable:
		if sweepVar == 'L':
			main.main(technology, transistorModel, target_name=targetName, target_value=targetValue, max_error=maxError, W=w, L=step, NF=nf, M=m, VGS=vgs, VDS=vds, VBS=vbs, parameter_calc_name=variable)
		if sweepVar == 'W':
			main.main(technology, transistorModel, target_name=targetName, target_value=targetValue, max_error=maxError,W=step, L=l, NF=nf, M=m, VGS=vgs, VDS=vds, VBS=vbs, parameter_calc_name=variable)
		if sweepVar == 'VGS':
			main.main(technology, transistorModel, target_name=targetName, target_value=targetValue, max_error=maxError,W=w, L=l, NF=nf, M=m, VGS=step, VDS=vds, VBS=vbs, parameter_calc_name=variable)
		if sweepVar == 'VDS':
			main.main(technology, transistorModel, target_name=targetName, target_value=targetValue, max_error=maxError,W=w, L=l, NF=nf, M=m, VGS=vgs, VDS=step, VBS=vbs, parameter_calc_name=variable)
		if sweepVar == 'VBS':
			main.main(technology, transistorModel, target_name=targetName, target_value=targetValue, max_error=maxError,W=w, L=l, NF=nf, M=m, VGS=vgs, VDS=vds, VBS=step, parameter_calc_name=variable)
		
		outputs = open(str(home_directory) + '/Circuit Sizing Tool/files/outputs/out_sweep.txt', 'r')
		out_txt = outputs.readlines()
		outputs.close()

		parameters = []
		values = []

		if parameter_defined == False:
			for line in out_txt[4:-1]:
				parameters.append(line.split("=")[0])
			parameters = [i for i in parameters if i != '\n']
			dataframe = pd.DataFrame(columns = parameters)
		parameter_defined = True

		for line in out_txt[4:-1]:
			if line.split("=")[0] != '\n':
				values.append(line.split("=")[1][:-1])
		if values != 0:
			dataframe.loc[len(dataframe)] = values
			values = []

		actualStep += 1

	dataframe.to_csv(str(home_directory) + '/Circuit Sizing Tool/files/outputs/out_sweep.csv')

def plot():
	df = pd.read_csv('sweep_output.csv')

	plt.plot(df['vth '], df['gm '])
	plt.show()