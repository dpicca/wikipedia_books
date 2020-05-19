from dataclasses import dataclass, asdict
from Character import Character

@dataclass
class Book(Character):

  def _init_(self, Title, Author, Characters):
    self.Title = Title
    self.Author = Author
    self.Characters = Characters
 
  def get_Characters(self):
    super()._init_(self, Character, Description)

assert asdict(Book) 
