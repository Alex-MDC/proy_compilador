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
     
    def get_class_attribute(self,name,attribute):
        currClass = self.get_class(name)

        if currClass:
            return self.classes['attributes'].get_var_dirVir(attribute)
        else:
            return None
        
    #-------------------------------------------

    #------------class attributes setting-------
        
    def add_var_to_class(self,className,var_name,data_type,dirVir):
        currClass = self.get_class(className)

        if currClass:
            return currClass['attributes'].add_var(var_name, data_type, dirVir)
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
    

    #--------------------------------------

    #---free up memory--
    def delete_classes_table(self):
        self.classes.clear()

    


    #-------------------
    