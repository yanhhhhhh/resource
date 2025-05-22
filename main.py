def get_full_name(first_name:str, last_name:str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age

print(get_full_name("john", "doe"))
print(get_name_with_age("john", 35))


from typing import List
def process_items(items:List[str]):
    for item in items:
        print(item.capitalize())
process_items(["item1", "item2", "item3"])


from typing import Set,Tuple
def process_items(items_t:Tuple[int,int,str], items_s: Set[bytes]):
  return items_t, items_s
print(process_items((1,2,"3"), {b"item1", b"item2"}))


from typing import Dict
def process_items(items:Dict[str, int]):
  for key, value in items.items():
    print(key, value)
process_items({"item1": 1, "item2": 2})
from typing import Union
def process_items(items:Union[str, int]):
  print(items)
process_items("item1")
process_items(1)


# class
class Person:
  def __init__(self,name:str,age:int):
    self.name = name
    self.age = age
  def get_name(self):
    return self.name
  def get_age(self):
    return self.age
person = Person("John", 35)
print(person.get_name())
print(person.get_age())
print(person.name + " " + str(person.age))