class Circle:

    def __init__(self, centre, radius):
        self.x = centre[0]
        self.y = centre[1]
        self.radius = radius
    
    def __contains__(self,coord):
        if ((self.x - coord[0])**2 + (self.y - coord[1])**2) < self.radius ** 2:
            return True
        else:
            return False
        