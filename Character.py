""" Contains the class holding the characters and their description"""
from dataclasses import dataclass, asdict

@dataclass
class Character:
  """
  Dataclass containing the Name and Description of each Character found in each entry of the .json file
  ...
  Attributes
  -----------
  Character : str
    Name of the Character
  Description : str
    Description of the Character
  """
  Character:str
  Description:str
