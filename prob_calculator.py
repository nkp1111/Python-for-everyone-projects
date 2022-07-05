import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **data):
    self.contents = []
    for k, v in data.items():
      for i in range(v):
        self.contents.append(k)

  def draw(self, amount):
    if amount > len(self.contents):
      return self.contents
    else:
      pickup = random.sample(self.contents, amount)
      for item in pickup:
        self.contents.remove(item)
      return pickup
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  failure = False
  success = 0
  
  for i in range(num_experiments):
    container = copy.deepcopy(hat)
    balls = dict()
    pickup = container.draw(num_balls_drawn)
    
    for ball in pickup:
      balls[ball] = balls.get(ball, 0) + 1
      
    for color, number in expected_balls.items():
      if number <= balls.get(color, 0):
        failure = False
      else:
        failure = True
        break
        
    if failure is not True:
      success += 1
      
  return success / num_experiments
      
    
    
  
