from FunctionTable import *
from VariableTable import *

class Classes:
    def __init__ (self):
        self.classes = {}

    def add_class(self,name):
        if name in self.classes:
            return None
        
        self.classes[name] = {
            'attributes': VariableTable(),
            'methods':FunctionTable(),
            'dirVir':None,
            'resources': [0] * 8 # [VI, VF, VB, VC, TI, TF, TB, TC]
        }
        return f'Class {name} added!'
    
    def get_class(self,name):
        return self.classes.get(name)
    
    def set_class_dirVir(self,className,dir):
        currClass = self.get_class(className)
        currClass['dirVir'] = dir

    def get_class_dirVir(self,className):
        currClass = self.get_class(className)
        if currClass:
            return currClass['dirVir']
        else:
            return None
        
    def set_resources_to_class(self, class_name, resource_name):
        currClass = self.get_class(class_name)

        if resource_name == 'var int':
            currClass['resources'][0] += 1
        elif resource_name == 'var float':
            currClass['resources'][1] += 1
        elif resource_name == 'var bool':
            currClass['resources'][2] += 1
        elif resource_name == 'var char':
            currClass['resources'][3] += 1
        elif resource_name == 'temp int':
            currClass['resources'][4] += 1
        elif resource_name == 'temp float':
            currClass['resources'][5] += 1
        elif resource_name == 'temp bool':
            currClass['resources'][6] += 1
        elif resource_name == 'temp char':
            currClass['resources'][7] += 1

    def get_class_resources(self, class_name):
        currClass = self.get_class(class_name)
        if currClass:
            return currClass['resources']
        else:
            return None

    #TODO NOTE: THE DIR VIR of classes will require updates to ERA and GOSUB 
    # REMEMBER TO POP on the FLAG of in a class scope!!!

    #------------class method getters--------------
    def get_class_function(self,className,method):
     currClass = self.get_class(className)

     if currClass:
         return self.classes['methods'].get_function(method)
     else:
         return None
     
    def get_method_dirVir(self,className,func_name):
        currClass = self.get_class(className)

        if currClass:
            return currClass['methods'].get_dirVir(func_name)
        else:
            return None
     
    def get_var_type_in_method(self,className, func_name, var_name):
        currClass = self.get_class(className)

        if currClass:
            return currClass['methods'].get_var_type_in_function(func_name, var_name)
        else:
            return None
        
    def get_var_dirVir_in_method(self,className, func_name, var_name):
        currClass = self.get_class(className)

        if currClass:
            return currClass['methods'].get_var_dirVir_in_function(func_name, var_name)
        else:
            return None
        
    def get_dim_of_var_in_method(self,className, func_name, var_name):
        currClass = self.get_class(className)

        if currClass:
            return currClass['methods'].get_dim_of_var_in_function(func_name, var_name)
        else:
            return None

    def get_params_types_of_method(self,className, func_name):
        currClass = self.get_class(className)

        if currClass:
            return currClass['methods'].get_params_types_of_function(func_name)
        else:
            return None
        
    def get_params_names_of_method(self,className, func_name):
        currClass = self.get_class(className)

        if currClass:
            return currClass['methods'].get_params_names_of_function(func_name)
        else:
            return None     

    def get_returnType_of_method(self,className, func_name):
        currClass = self.get_class(className)

        if currClass:
            return currClass['methods'].get_returnType_of_function(func_name)
        else:
            return None  
        
    def get_resources_in_method(self,className, func_name):
        currClass = self.get_class(className)

        if currClass:
            return currClass['methods'].get_resources_in_function(func_name)
        else:
            return None 
    
    #--------------------------------------------

    #-------class atributes getters------------
     
    def get_class_attribute_dirVir(self,name,attribute):
        currClass = self.get_class(name)

        if currClass:
            return currClass['attributes'].get_var_dirVir(attribute)
        else:
            return None
        
    def get_attribute_type_in_class(self,name,attribute):
        currClass = self.get_class(name)
        # currClass['attributes'].print_var_table()
        if currClass:
            return currClass['attributes'].get_var_type(attribute)
        else:
            return None
        
    def get_dim_of_attribute_in_class(self,className,attribute):
        currClass = self.get_class(className)

        if currClass:
            return currClass['attributes'].get_dim_list(attribute)
        else:
            return None
    
    #-------------------------------------------

    #------------class attributes setting-------
        
    def add_attribute_to_class(self,className,var_name,data_type,dirVir):
        currClass = self.get_class(className)

        if currClass:
            return currClass['attributes'].add_var(var_name, data_type, dirVir)
        else:
            return None
        
    def set_dirVir_of_attribute_in_class(self,className,var_name,dirVir):
        currClass = self.get_class(className)

        if currClass:
            return currClass['attributes'].set_var_dirVir(var_name, dirVir)
        else:
            return None
    #---------------------------------------

    #----------------class methods setting-----------
        
    def add_function_to_class(self,className,funcName,return_type):
        currClass = self.get_class(className)

        if currClass:
            return currClass['methods'].add_function(funcName,return_type)
        else:
            return None
        
    def add_var_to_class_method(self,className,funcName,var_name,data_type, dirVir):
        currClass = self.get_class(className)
        #print(currClass['methods'].print_function_table())
        if currClass:
            return currClass['methods'].add_var_to_function(funcName,var_name,data_type, dirVir)
        else:
            return None
        
    def set_method_dirVir(self,className,func_name,dir):
        currClass = self.get_class(className)
        currClass['methods'].set_dirVir(func_name,dir)
        
    def set_dirVir_of_var_in_method(self,className,func_name, var_name, dirvir):
        currClass = self.get_class(className)

        if currClass:
            return currClass['methods'].set_dirVir_of_var_in_function(func_name, var_name, dirvir)
        else:
            return None
        
    def add_dim_to_var_in_method(self,className,func_name, var_name, dirvir):
        currClass = self.get_class(className)

        if currClass:
            return currClass['methods'].add_dim_to_var_in_function(func_name, var_name, dirvir)
        else:
            return None
        
    def add_param_types_to_method(self,className,func_name,param):
        currClass = self.get_class(className)
        currClass['methods'].add_param_types_to_function(func_name,param)

    def add_param_names_to_method(self,className,func_name,param_name):
        currClass = self.get_class(className)
        currClass['methods'].add_param_names_to_function(func_name,param_name)

    def set_resources_to_method(self,className,func_name,resource_name):
        currClass = self.get_class(className)
        currClass['methods'].set_resources_to_function(func_name,resource_name)
        #we must also UPDATE class resources
        self.set_resources_to_class(className,resource_name)

    #--------------------------------------

    #---free up memory--
    def delete_classes_table(self):
        self.classes.clear()

    def print_Classes_Table(self):
        for class_name, class_data in self.classes.items():
            print(f'Class: {class_name}')
            print("Attributes")
            class_data['attributes'].print_var_table()
            print("Methods")
            class_data['methods'].print_function_table()
            print(f"Class Dir Vir: {class_data['dirVir']}")
            print(f"Class Resources: {class_data['resources']}")
            print()


    #-------------------
    