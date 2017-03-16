# Answer: 278
path = "L1, R3, R1, L5, L2, L5, R4, L2, R2, R2, L2, R1, L5, R3, L4, L1, L2, R3, R5, L2, R5, L1, R2, L5, R4, R2, R2, L1, L1, R1, L3, L1, R1, L3, R5, R3, R3, L4, R4, L2, L4, R1, R1, L193, R2, L1, R54, R1, L1, R71, L4, R3, R191, R3, R2, L4, R3, R2, L2, L4, L5, R4, R1, L2, L2, L3, L2, L1, R4, R1, R5, R3, L5, R3, R4, L2, R3, L1, L3, L3, L5, L1, L3, L3, L1, R3, L3, L2, R1, L3, L1, R5, R4, R3, R2, R3, L1, L2, R4, L3, R1, L1, L1, R5, R2, R4, R5, L1, L1, R1, L2, L4, R3, L1, L3, R5, R4, R3, R3, L2, R2, L1, R4, R2, L3, L4, L2, R2, R2, L4, R3, R5, L2, R2, R4, R5, L2, L3, L2, R5, L4, L2, R3, L5, R2, L1, R1, R3, R3, L5, L2, L2, R5"

class Coords(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y
      
class Direction(object):
  def __init__(self, coords):
    self.coords = Coords(*coords)
    self.startCoords = Coords(*coords)
    self.side = North
    
  def walk(self, path):
    for data in path.split(','):
      d = data.strip()
      side, step = d[0], int(d[1:])
      if side == 'L':
        self.side.turn_left(self, step)
      else:
        self.side.turn_right(self, step)
      
    
    
class North(Direction):
  def turn_left(self, steps):
    self.coords.y -= steps
    self.side = West
    
  def turn_right(self, steps):
    self.coords.y += steps
    self.side = East
    
class East(Direction):
  def turn_left(self, steps):
    self.coords.x -= steps
    self.side = North
  
  def turn_right(self, steps):
    self.coords.x += steps
    self.side = South
    
class West(Direction):
  def turn_left(self, steps):
    self.coords.x += steps
    self.side = South
    
  def turn_right(self, steps):
    self.coords.x -= steps
    self.side = North
    
class South(Direction):
  def turn_left(self, steps):
    self.coords.y += steps
    self.side = East
  def turn_right(self, steps):
    self.coords.y -= steps
    self.side = West

d = Direction((0, 0))
d.walk(path)
print(abs(d.coords.x + d.coords.y))
