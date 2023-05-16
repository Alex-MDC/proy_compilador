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
            'params_type': []
        }
        return f'Function {name} added!'

    def get_function(self, name):
        return self.functions.get(name)

    def add_var_to_function(self, func_name, var_name, data_type):
        func = self.get_function(func_name)

        if func:
            return func['var_table'].add_var(var_name, data_type)
        else:
            return None

    def get_var_type_in_function(self, func_name, var_name):
        func = self.get_function(func_name)

        if func:
            return func['var_table'].get_var_type(var_name)
        else:
            return None
    
    def add_param_to_function(self, func_name, param):
        func = self.get_function(func_name)
        func['params_type'].append(param)
    
    def get_params_of_function(self, func_name):
        func = self.get_function(func_name)

        if func:
            return func['params_type']
        else:
            return None
    
    def delete_function_table(self):
        self.functions.clear()

    def print_function_table(self):
        for func_name, func_data in self.functions.items():
            print(f'Function: {func_name}')
            print(f"Return type: {func_data['return_type']}")
            print(f"Params list: {func_data['params_type']}")
            func_data['var_table'].print_var_table()
            print()

# Testing
# functions = FunctionTable()
# print(functions.add_function('suma','int'))
# print(functions.add_var_to_function('suma','x','int'))
# print(functions.add_var_to_function('suma','y','float'))
# print(functions.get_var_type_in_function('suma', 'z'))