class Pokemon: #Here have some explication
  entry = 0
  name = ''
  types = ['']
  description = ''
  level = 0
  height = 0.0
  is_caught = 0

class Pokemon:  #The Init
  def __init__(self, entry, name, types, description, level, height, is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.level = level
    self.height = height
    self.is_caught = is_caught

  def speak(self): #It Speak, you can change!
    print(self.name + ', ' + self.name + '!')

  def display_details(self): #More details about it
    print('Entry Number: ' + str(self.entry))
    print('Pokemon:' + self.name)
    print('It this the type: ' + str(self.types))
    print('Description: ' + self.description)
    print('Level: ' + self.level)
    print('Height: ' + self.height)

    if self.is_caught:
      print(self.name + ' Has already been Caught!')
    else:
      print(self.name + " Hasn´t been caught yet")
  
Pikachu = Pokemon(1, 'Pikachu', ['Electric', 'Normal'], 'It has small electric sacs oh both its cheeks.', '32', '0.98', True)

Pikachu.speak()
Pikachu.display_details()