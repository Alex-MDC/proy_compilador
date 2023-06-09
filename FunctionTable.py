from VariableTable import VariableTable

'''
When None is returned, this means an error ocurred!
If an error never occurred, return a confirmation message
'''

class FunctionTable:
    def __init__(self):
        self.functions = {}

    def add_function(self, name, return_type):
        if name in self.functions:
            return None
        
        self.functions[name] = {
            'return_type': return_type,
            'var_table': VariableTable(),
            'params_type': [],
            'params_names': [],
            'dirVir': None,
            'resources': [0] * 8 # [VI, VF, VB, VC, TI, TF, TB, TC]
        }
        return f'Function {name} added!'

    def get_function(self, name):
        return self.functions.get(name)

    def add_var_to_function(self, func_name, var_name, data_type, dirVir):
        func = self.get_function(func_name)

        if func:
            return func['var_table'].add_var(var_name, data_type, dirVir)
        else:
            return None

    def get_var_type_in_function(self, func_name, var_name):
        func = self.get_function(func_name)

        if func:
            return func['var_table'].get_var_type(var_name)
        else:
            return None
    
    def get_var_dirVir_in_function(self, func_name, var_name):
        func = self.get_function(func_name)

        if func:
            return func['var_table'].get_var_dirVir(var_name)
        else:
            return None
    
    def add_dim_to_var_in_function(self, func_name, var_name, dim_size):
        func = self.get_function(func_name)

        if func:
            return func['var_table'].add_dim(var_name, dim_size)
        else:
            return None
    
    def get_dim_of_var_in_function(self, func_name, var_name):
        func = self.get_function(func_name)

        if func:
            return func['var_table'].get_dim_list(var_name)
        else:
            return None
    
    def set_dirVir_of_var_in_function(self, func_name, var_name, dirvir):
        func = self.get_function(func_name)

        if func:
            return func['var_table'].set_var_dirVir(var_name, dirvir)
        else:
            return None
    
    def add_param_types_to_function(self, func_name, param):
        func = self.get_function(func_name)
        func['params_type'].append(param)
    
    def get_params_types_of_function(self, func_name):
        func = self.get_function(func_name)

        if func:
            return func['params_type']
        else:
            return None
        
    def add_param_names_to_function(self, func_name, param_name):
        func = self.get_function(func_name)
        func['params_names'].append(param_name)
    
    def get_params_names_of_function(self, func_name):
        func = self.get_function(func_name)

        if func:
            return func['params_names']
        else:
            return None
        
    def get_returnType_of_function(self, func_name):
        func = self.get_function(func_name)

        if func:
            return func['return_type']
        else:
            return None
    
    def set_dirVir(self, func_name, dir):
        func = self.get_function(func_name)
        func['dirVir'] = dir

    def get_dirVir(self, func_name):
        func = self.get_function(func_name)

        if func:
            return func['dirVir']
        else:
            return None
    
    def set_resources_to_function(self, func_name, resource_name):
        func = self.get_function(func_name)

        if resource_name == 'var int':
            func['resources'][0] += 1
        elif resource_name == 'var float':
            func['resources'][1] += 1
        elif resource_name == 'var bool':
            func['resources'][2] += 1
        elif resource_name == 'var char':
            func['resources'][3] += 1
        elif resource_name == 'temp int':
            func['resources'][4] += 1
        elif resource_name == 'temp float':
            func['resources'][5] += 1
        elif resource_name == 'temp bool':
            func['resources'][6] += 1
        elif resource_name == 'temp char':
            func['resources'][7] += 1

    def get_resources_in_function(self, func_name):
        func = self.get_function(func_name)

        if func:
            return func['resources']
        else:
            return None
            
    def delete_function_table(self):
        self.functions.clear()
    
    def add_var_to_var_in_function(self, func_name, var_name, var, type):
        func = self.get_function(func_name)

        if func:
            func['var_table'].add_var_to_var(var_name, var, type)
        else:
            return None
    
    def get_resources_of_var_in_function(self, func_name, var_name):
        func = self.get_function(func_name)

        if func:
            return func['var_table'].get_resources_of_var(var_name)
        else:
            return None

    def print_function_table(self):
        for func_name, func_data in self.functions.items():
            print(f'Function: {func_name}')
            print(f"Return type: {func_data['return_type']}")
            print(f"Dir Vir: {func_data['dirVir']}")
            print(f"Resources: {func_data['resources']}")
            print(f"Params list: {func_data['params_type']}")
            print(f"Params names: {func_data['params_names']}")
            func_data['var_table'].print_var_table()
            print()

# Testing
# functions = FunctionTable()
# print(functions.add_function('suma','int'))
# print(functions.add_var_to_function('suma','x','int'))
# print(functions.add_var_to_function('suma','y','float'))
# print(functions.get_var_type_in_function('suma', 'z'))