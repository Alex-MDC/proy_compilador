class SemanticCube:
    def __init__(self):
        # Define operators for semantic cube
        self.operators = {
            '+': 'add',
            '-': 'subtract',
            '*': 'multiply',
            '/': 'divide',
            '>': 'greater_than',
            '<': 'less_than',
            '>=': 'greater_than_or_equal_to',
            '<=': 'less_than_or_equal_to',
            '==': 'equal_to',
            '<>': 'not_equal_to'
        }

        # Define data types for semantic cube
        self.data_types = ['int', 'float', 'char', 'bool']

        # Define semantic cube as a dictionary
        self.cube = {}
        for op in self.operators:
            self.cube[op] = {}
            for dt1 in self.data_types:
                self.cube[op][dt1] = {}
                for dt2 in self.data_types:
                    self.cube[op][dt1][dt2] = None

        # Set semantic rules for arithmetic operations
        self.cube['+']['int']['int'] = 'int'
        self.cube['+']['int']['float'] = 'float'
        self.cube['+']['float']['int'] = 'float'
        self.cube['+']['float']['float'] = 'float'

        self.cube['-']['int']['int'] = 'int'
        self.cube['-']['int']['float'] = 'float'
        self.cube['-']['float']['int'] = 'float'
        self.cube['-']['float']['float'] = 'float'

        self.cube['*']['int']['int'] = 'int'
        self.cube['*']['int']['float'] = 'float'
        self.cube['*']['float']['int'] = 'float'
        self.cube['*']['float']['float'] = 'float'

        self.cube['/']['int']['int'] = 'int'
        self.cube['/']['int']['float'] = 'float'
        self.cube['/']['float']['int'] = 'float'
        self.cube['/']['float']['float'] = 'float'

        # Set semantic rules for relational operations
        for op in ['>', '<', '>=', '<=', '==', '<>']:
            self.cube[op]['int']['int'] = 'bool'
            self.cube[op]['float']['float'] = 'bool'
            self.cube[op]['int']['float'] = 'bool'
            self.cube[op]['float']['int'] = 'bool'
        
        self.cube['==']['char']['char'] = 'bool'
        self.cube['<>']['char']['char'] = 'bool'
        self.cube['==']['bool']['bool'] = 'bool'
        self.cube['<>']['bool']['bool'] = 'bool'

        # Set semantic rules for logical operations
        # for op in ['&&', '||']:
        #     self.cube[op]['bool']['bool'] = 'bool'

    # If None is returned, an error occured
    def get_result_type(self, operator, operand1_type, operand2_type):
        return self.cube[operator][operand1_type][operand2_type]


# Testing
cube = SemanticCube()
result_type = cube.get_result_type('*', 'char','float')
print(cube.cube['*']['int']['int'])

if result_type is None:
    print(f'Invalid operation')
else:
    print(f'Result type: {result_type}')