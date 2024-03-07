class Rectangle:
    def __init__(self, base: float, height: float) -> None:
        if(base < 0):
            self.__base = 0
        else:       
            self.__base = base
            
        if(height < 0):
            self.__height = 0
        else:
            self.__height = height
        
    def get_height(self) -> float:
        return self.__height
    
    def get_base(self) ->float:
        return self.__base
    
    def get_perimeter(self) -> float:
        return 2 * self.__base + 2 * self.__height
    
    def get_area(self)-> float:
        return 1/2* self.__base*self.__height
 
rectangle1= Rectangle (2,5)
print("Base:", rectangle1.get_base(),"Height:", rectangle1.get_height(), "Area:", rectangle1.get_area(), "Perimeter:", rectangle1. get_perimeter())
 
rectangle2= Rectangle (5,14)
print("Base:", rectangle2.get_base(),"Height:", rectangle2.get_height(), "Area:", rectangle2.get_area(), "Perimeter:", rectangle2. get_perimeter())
print("Yeet")