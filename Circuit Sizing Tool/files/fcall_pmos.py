import simulation as sm

def calc_w(par, ref, max_erro, var_name, var_value, inputs, size, nit, technology):
	erro = 999999999
	w = float(var_value)
	par_ref = ref
	i = 0
	while erro > max_erro and i < nit:
		w_last_it = w

		inputs.update({var_name:w})
		variables, values = sm.simulate(technology, inputs, pmos=True)
		par_index = variables.index(str(par))
		par_value = float(values[par_index])
	
		erro = abs(par_value - par_ref)/abs(par_ref)
		w = par_ref/par_value*w

		if var_name == 'L':
			if float(inputs['L']) <= size[0]:
				w = size[0]
			if float(inputs['L']) >= size[1]:
				w = size[1]
		if var_name == 'W':
			if float(inputs['W']) <= size[2]:
				w = size[2]
			if float(inputs['W']) >= size[3]:
				w = size[3]
	
		if w_last_it == w:
			print("Parameters out of range")
			return variables, values, par_value, w
			break

		i += 1
		print(i)

	return variables, values, par_value, w
