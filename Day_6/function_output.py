#functions with output
def format_name(f_name, l_name):
	 formated_f_name = (f_name.title())
	 formated_l_name = (l_name.title())
	 #print(f'{formated_f_name} {formated_l_name}')
	 return f'{formated_f_name} {formated_l_name}'
	 
#formated_string = format_name('eDgar', 'CanRo')
#print(formated_string)
#print(format_name('eDgar', 'CanRo'))

#output = len('Edgar')
print(format_name(input('What is you firts name?: '), input('What is your last name?: ')))