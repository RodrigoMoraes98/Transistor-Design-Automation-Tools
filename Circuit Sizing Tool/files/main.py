import fcall_nmos
import fcall_pmos
import simulation
import functions
import os

home_directory = os.path.expanduser( '~' )

def main(technology, model_name, no_op = False, out_param=None, **kwargs):

	pmos, nmos = functions.model(technology, model_name)

	if nmos == True:
		functions.edit_input(str(home_directory) + '/Circuit Sizing Tool/files/inputs/input_nmos.txt', kwargs)
		input_dict, target_name, target_value, max_error, par_calc_name, par_calc_val, nit, size = functions.inputs(str(home_directory) + '/Circuit Sizing Tool/files/inputs/input_nmos.txt')

		if no_op == False:
			variables, values, par_ref, w = fcall_nmos.calc_w(target_name, target_value, max_error, par_calc_name, par_calc_val, input_dict, size, nit, technology)
			functions.results(technology, target_name, par_ref, par_calc_name, w, variables, values)

		elif no_op == True:
			variables, values = simulation.simulate(technology, input_dict)
			target_index = functions.search_index(target_name, variables)
			par_ref = values[target_index]
			functions.results(technology, target_name, par_ref, par_calc_name, par_calc_val, variables, values)

		if out_param != None:
			out_n = functions.out_parameter(out_param, variables, values)
			return out_n

	if pmos == True:
		functions.edit_input(str(home_directory) + '/Circuit Sizing Tool/files/inputs/input_pmos.txt', kwargs)
		input_dict, target_name, target_value, max_error, par_calc_name, par_calc_val, nit, size = functions.inputs(str(home_directory) + '/Circuit Sizing Tool/files/inputs/input_pmos.txt')

		if no_op ==  False:
			if target_name == 'ids':
				target_value = -target_value
			#input_dict.update({'VGS':-float(input_dict['VGS'])})
			#input_dict.update({'VDS':-float(input_dict['VDS'])})

			variables, values, par_ref, w = fcall_pmos.calc_w(target_name, target_value, max_error, par_calc_name, par_calc_val, input_dict, size, nit, technology)
			functions.results(technology, target_name, par_ref, par_calc_name, w, variables, values, pmos=True)

		elif no_op == True:
			variables, values = simulation.simulate(technology, input_dict, pmos=True)
			target_index = functions.search_index(target_name, variables)
			par_ref = values[target_index]
			functions.results(technology, target_name, par_ref, par_calc_name, par_calc_val, variables, values, pmos=True)

		if out_param != None:
			out_p = functions.out_parameter(out_param, variables, values)
			return out_p
