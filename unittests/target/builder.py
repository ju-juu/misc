class Building:

    def __init__(self):
        self.floor = None
        self.wall = None
        self.door = None

    def set_floor(self, floor_style):
        self.floor = floor_style

    def set_wall(self, wall_style):
        self.wall = wall_style

    def set_door(self, door_style):
        self.door = door_style


class BuildingBuilder:
    def __init__(self):
        self.building = Building()

    def add_floor(self, floor_style):
        self.building.set_floor(floor_style)
        return self

    def add_wall(self, wall_style):
        self.building.set_wall(wall_style)
        return self

    def add_door(self, door_style):
        self.building.set_door(door_style)
        return self

    def build(self):
        return self.building


building = BuildingBuilder().add_floor('tiles').add_wall('brick').add_door('wooden').build()
assert building.door == 'wooden'
