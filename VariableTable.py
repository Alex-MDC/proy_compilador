from MemoryMap import MemoryMap

class VariableTable:
    def __init__(self):
        self.vars = {}

    def add_var(self, name, data_type, dirVir):
        if name in self.vars:
            raise TypeError(f"Variable {name} already declared!")
        
        self.vars[name] = { 
            'data_type': data_type,
            'dirVir': dirVir,
            'dim_list': [],
            'memory_map': MemoryMap(1000, 2000, 3000, 4000, 5000)
        }

        return f'Variable {name} added!'

    def get_var_type(self, name):
        if name in self.vars:
            return self.vars[name]['data_type']
        
        return None

    def set_var_dirVir(self, name, dirvir):
        self.vars[name]['dirVir'] = dirvir

    def get_var_dirVir(self, name):
        if name in self.vars:
            return self.vars[name]['dirVir']
        
        return None

    def add_dim(self, var_name, dim_size):
        self.vars[var_name]['dim_list'].append(dim_size)

    def get_dim_list(self, var_name):
        if var_name in self.vars:
            return self.vars[var_name]['dim_list']
        
        return None

    def print_var_table(self):
        for var_name, var_data in self.vars.items():
            print(f"{var_name}: {var_data['data_type']} {var_data['dirVir']} {var_data['dim_list']}")
            
            memory = var_data['memory_map'].printMemoryMap()
            if memory is not None:
                print(f"inside var table {var_data['memory_map'].printMemoryMap()}")
    
    def add_var_to_var(self, var_name, var, type):
        return self.vars[var_name]['memory_map'].addVar(var, type)
    
    def get_resources_of_var(self, var_name):
        return self.vars[var_name]['memory_map']

    def clear(self):
        self.vars.clear()