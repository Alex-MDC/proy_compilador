class Quadruples:
    def __init__(self):
        self.stack_operators = []
        self.stack_operands = []
        self.stack_types = []
        self.stack_jumps = []
        
        self.quadruples = []
        self.temporals_counter = 1
    
    def print_stacks(self):
        print(f"Operators: {self.stack_operators}")
        print(f"Operands: {self.stack_operands}")
        print(f"Types: {self.stack_types}")
        print(f"Jumps: {self.stack_jumps}")
        print(f"Quadruples: ")
        for index, quad in enumerate(self.quadruples):
            print(index, quad)
    
    def get_temporal_counter(self):
        return self.temporals_counter

    def increment_counter(self):
        self.temporals_counter += 1
    