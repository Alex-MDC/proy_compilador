class Array:
    def __init__(self):
        self.var_name = ''

        self.stack_dim = []
        self.DIM = 0
        self.dim_list = []
    
    def set_var_name(self, name):
        self.var_name = name
    
    def get_var_name(self):
        return self.var_name
    
    def push_dim(self, dim):
        self.stack_dim.append(dim)
    
    def update_top_dim(self, new_dim):
        self.stack_dim[-1] = new_dim
    
    def reset_dim(self):
        self.DIM = 0

    def get_dim(self):
        return int(self.DIM)

    def update_dim(self):
        self.DIM += 1

    def set_dim_list(self, dim_list):
        self.dim_list = dim_list
    
    def get_dim_in_index(self, index):
        return int(self.dim_list[index])

    def get_dim_list(self):
        return self.dim_list