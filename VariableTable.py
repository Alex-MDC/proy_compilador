class VariableTable:
    def __init__(self):
        self.vars = {}

    def add_var(self, name, data_type):
        if name in self.vars:
            return None
        
        self.vars[name] = data_type
        return f'Variable {name} added!'

    def get_var_type(self, name):
        if name in self.vars:
            return self.vars.get(name)
        
        return None

    def print_var_table(self):
        for var_name, var_type in self.vars.items():
            print(f"{var_name}: {var_type}")