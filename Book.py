from dataclasses import dataclass, asdict, field
from Character import Character

@dataclass
class Book():
  """
  Dataclass containing the Title and Author of the Book and its list of Characters
  ...
  Attributes
  ----------
  Title : str
    Title of the Book
  Author : str
    Author of the Book
  Characters : list
    List of Character dataclasses of the Book
  """
  Title:str
  Author:str
  Characters: list() = field(default="None")
