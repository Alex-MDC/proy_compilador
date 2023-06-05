from VariableTable import VariableTable
from FunctionTable import FunctionTable

class ClassTable:
    def __init__(self):
        self.classes = {}

    def add_class(self, name):
        if name in self.classes:
            raise TypeError(f"Class {name} already declared!")
        
        self.classes[name] = {
            'var_table': VariableTable(),
            'function_table': FunctionTable(),
            'resources': [0] * 8 # [VI, VF, VB, VC, TI, TF, TB, TC]
        }
        return f'Class {name} added!'

    def get_class(self, name):
        return self.classes.get(name)
    
    def add_var_to_class(self, class_name, var_name, var_type):
        classes = self.get_class(class_name)

        if classes:
            return classes['var_table'].add_var(var_name, var_type, 0)
        else:
            raise TypeError(f"Class {class_name} does not exist!")
        
    def set_resources_to_class(self, class_name, resource_name):
        classes = self.get_class(class_name)

        if resource_name == 'var int':
            classes['resources'][0] += 1
        elif resource_name == 'var float':
            classes['resources'][1] += 1
        elif resource_name == 'var bool':
            classes['resources'][2] += 1
        elif resource_name == 'var char':
            classes['resources'][3] += 1
        elif resource_name == 'temp int':
            classes['resources'][4] += 1
        elif resource_name == 'temp float':
            classes['resources'][5] += 1
        elif resource_name == 'temp bool':
            classes['resources'][6] += 1
        elif resource_name == 'temp char':
            classes['resources'][7] += 1

    def get_resources_in_class(self, class_name):
        classes = self.get_class(class_name)

        if classes:
            return classes['resources']
        else:
            return None
    
    def get_resources_of_function_in_class(self, class_name, func_name):
        classes = self.get_class(class_name)

        if classes:
            return classes['function_table'].get_resources_in_function(func_name)
        else:
            return None
    
    def set_dirvir_to_var_in_class(self, class_name, var_name, dirvir):
        classes = self.get_class(class_name)

        if classes:
            return classes['var_table'].set_var_dirVir(var_name, dirvir)
        else:
            return None
    
    def add_function_to_class(self, class_name, func_name, return_type):
        classes = self.get_class(class_name)

        if classes:
            return classes['function_table'].add_function(func_name, return_type)
        else:
            return None
    
    def add_var_to_function_in_class(self, class_name, func_name, var_name, var_type, dirvir):
        classes = self.get_class(class_name)

        if classes:
            return classes['function_table'].add_var_to_function(func_name, var_name, var_type, dirvir)
        else:
            return None
        
    def set_resources_to_function_in_class(self, class_name, func_name, resource_name):
        classes = self.get_class(class_name)

        if classes:
            return classes['function_table'].set_resources_to_function(func_name, resource_name)
        else:
            return None
    
    def set_dirVir_in_function(self, class_name, dir, func_name):
        classes = self.get_class(class_name)
        classes['function_table'].set_dirVir(func_name, dir)

    def get_dirVir_in_function(self, class_name, func_name):
        classes = self.get_class(class_name)
        return classes['function_table'].get_dirVir(func_name)
    
    def add_param_types_to_function_in_class(self, class_name, func_name, type):
        classes = self.get_class(class_name)

        if classes:
            return classes['function_table'].add_param_types_to_function(func_name, type)
        else:
            return None
    
    def add_param_names_to_function_in_class(self, class_name, func_name, name):
        classes = self.get_class(class_name)

        if classes:
            return classes['function_table'].add_param_names_to_function(func_name, name)
        else:
            return None
    
    def get_param_types_to_function_in_class(self, class_name, func_name):
        classes = self.get_class(class_name)

        if classes:
            return classes['function_table'].get_params_types_of_function(func_name)
        else:
            return None
    
    def get_param_names_to_function_in_class(self, class_name, func_name):
        classes = self.get_class(class_name)

        if classes:
            return classes['function_table'].get_params_names_of_function(func_name)
        else:
            return None
    
    def get_dim_of_var_in_function_in_class(self, class_name, func_name, var_name):
        classes = self.get_class(class_name)

        if classes:
            return classes['function_table'].get_dim_of_var_in_function(func_name, var_name)
        else:
            return None
    
    def set_dirVir_of_var_in_function_in_class(self, class_name, func_name, var_name, dirvir):
        classes = self.get_class(class_name)

        if classes:
            return classes['function_table'].set_dirVir_of_var_in_function(func_name, var_name, dirvir)
        else:
            return None
        
    def add_dim_to_var_in_function_in_class(self, class_name, func_name, var_name, dim_size):
        classes = self.get_class(class_name)

        if classes:
            return classes['function_table'].add_dim_to_var_in_function(func_name, var_name, dim_size)
        else:
            return None
        
    def get_var_dirVir_in_function_in_class(self, class_name, func_name, var_name):
        classes = self.get_class(class_name)

        if classes:
            return classes['function_table'].get_var_dirVir_in_function(func_name, var_name)
        else:
            return None
    
    def get_var_dirVir(self, class_name, var_name):
        classes = self.get_class(class_name)

        if classes:
            return classes['var_table'].get_var_dirVir(var_name)
        else:
            return None
    
    def get_var_type(self, class_name, var_name):
        classes = self.get_class(class_name)

        if classes:
            return classes['var_table'].get_var_type(var_name)
        else:
            return None
    
    def get_var_type_in_function(self, class_name, func_name, var_name):
        classes = self.get_class(class_name)

        if classes:
            return classes['function_table'].get_var_type_in_function(func_name, var_name)
        else:
            return None
    
    def get_returnType_of_function(self, class_name, func_name):
        classes = self.get_class(class_name)

        if classes:
            return classes['function_table'].get_returnType_of_function(func_name)
        else:
            return None

    def get_function(self, class_name, func_name):
        classes = self.get_class(class_name)

        if classes:
            return classes['function_table'].get_function(func_name)
        else:
            return None
        
    def print_class_table(self):
        for class_name, class_data in self.classes.items():
            print(f'Class: {class_name}')
            print(f"Resources: {class_data['resources']}")
            class_data['var_table'].print_var_table()
            class_data['function_table'].print_function_table()
            print()
        