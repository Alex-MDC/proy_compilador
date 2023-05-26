class VariableTable:
    def __init__(self):
        self.vars = {}

    def add_var(self, name, data_type, dirVir):
        if name in self.vars:
            return None
        
        self.vars[name] = { 
            'data_type': data_type,
            'dirVir': dirVir 
        }

        return f'Variable {name} added!'

    def get_var_type(self, name):
        if name in self.vars:
            return self.vars[name]['data_type']
        
        return None

    def get_var_dirVir(self, name):
        if name in self.vars:
            return self.vars[name]['dirVir']
        
        return None

    def print_var_table(self):
        for var_name, var_data in self.vars.items():
            print(f"{var_name}: {var_data['data_type']} {var_data['dirVir']}")