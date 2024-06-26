class Rectangle:

    def __init__(self, base: float, height: float) -> None:
        if (base < 0):
            self.__base = 0
        else:
            self.__base = base

        if (height < 0):
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
        
    
    def __str__(self) -> str:

        # Rectangle of base:3, height:4
        return "Rectangle of base:" + str (self.__base) + ", height:" + str (self.__height)

Rectangle_1=Rectangle(4,7)
print(Rectangle_1)

Rectangle_2=Rectangle(5, 8)
print(Rectangle_2)