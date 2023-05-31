class Array:
    def __init__(self):
        self.var_name = []

        self.stack_dim = []
        self.DIM = []
        self.dim_list = []
    
    def set_var_name(self, name):
        self.var_name.append(name)
    
    def get_var_name(self):
        return self.var_name[-1]
    
    def pop_var_name(self):
        self.var_name.pop()
    
    # stack_dim
    def push_to_stack_dim(self, dim):
        self.stack_dim.append(dim)
    
    def update_top_dim_stack(self, new_dim):
        self.stack_dim[-1] = new_dim
    
    def pop_from_dim_stack(self):
        self.stack_dim.pop()
    
    # DIM
    def push_dim(self):
        self.DIM.append(0)

    def get_dim(self):
        return int(self.DIM[-1])

    def update_dim(self):
        self.DIM[-1] += 1
    
    def pop_dim(self):
        self.DIM.pop()

    # Dim List
    def set_dim_list(self, dim_list):
        self.dim_list.append(dim_list)
    
    def get_dim_in_index(self, index):
        return int(self.dim_list[-1][index])

    def get_dim_list(self):
        return self.dim_list[-1]
    
    def pop_dim_list(self):
        self.dim_list.pop()
    