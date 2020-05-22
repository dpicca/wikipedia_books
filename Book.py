from dataclasses import dataclass, asdict, field
from Character import Character

@dataclass
class Book():
  Title:str
  Author:str
  Characters: list() = field(default="None")
