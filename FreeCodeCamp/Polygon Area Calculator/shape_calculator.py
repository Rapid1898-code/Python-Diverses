class Rectangle():
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def __str__(self):
        return("Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")")

    def set_width(self,val):
        self.width = val

    def set_height(self,val):
        self.height = val

    def get_area(self):
        return (self.width * self.height)

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        if self.width > 50 or self.height > 50: return("Too big for picture.")
        erg = ""
        for i in range(self.height):
            erg += "*" * self.width + "\n"
        return(erg)

    def get_amount_inside(self,shape):
        area = self.get_area()
        area2 = shape.get_area()
        return(int(area/area2))


class Square(Rectangle):
    def __init__(self,length):
        self.width = self.height = length

    def __str__(self):
        return("Square(side=" + str(self.width) + ")")

    def set_side(self,length):
        self.width = self.height = length

    def set_width(self,val):
        self.width = self.height = val

    def set_height(self,val):
        self.width = self.height = val
