from urllib import robotparser


class Cylinder:
    def init__(self, height, radius = 1):
        self.height = height
        self.radius = radius

    def get_surface_area(self):
        radius = float(input('Enter the radius: '))

        height = float (input('Enter the height: '))

        surface_area = 2 * 3.145 * radius * (radius + height)
        surface_area =round(surface_area,2)
        print(surface_area)

        return surface_area

    def get_volume(self):
        length = float(input('Enter the length: '))

        breadth = float(input('Enter the width: '))

        vol_height = float(input('Enter volume height: '))
        volume = round((length * breadth * vol_height), 2)
        print(volume)

        return volume  





cylinder_obj = Cylinder()

cylinder_obj.get_surface_area()
cylinder_obj.get_volume()


    