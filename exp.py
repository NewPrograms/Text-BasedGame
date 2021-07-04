# defining a SuperClass
class SuperClass:
  
     # defining __init_subclass__ method
    def __init_subclass__(cls, **kwargs):
        cls.default_name ="Inherited Class"
  
# defining a SubClass
class SubClass(SuperClass):
  
     # an attribute of SubClass
    default_name ="SubClass" 
    print(default_name)
  
subclass = SubClass()
print(subclass.default_name)