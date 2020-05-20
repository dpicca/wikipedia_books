from dataclasses import dataclass, asdict
from Character import Character

@dataclass
class Book(Character):
  Title:str
  Author:str
  Characters: list(Character)

assert asdict(Book) 
