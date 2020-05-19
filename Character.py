from dataclasses import dataclass, asdict

@dataclass
class Character:
  def _init_(self, Character, Description):
    self.Character = Character
    self.Description = Description

  def get_Character(self):
      return self.Character
  
  def get_Description(self):
      return self.Description
  
assert asdict(Character)

