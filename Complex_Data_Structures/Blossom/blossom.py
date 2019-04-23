from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

class HashMap:
  def __init__(self, size):
    self.size = size
    self.array = [LinkedList() for i in range(self.size)]
    
  def hash(self, key):
    return sum(key.encode())
  
  def compressor(self, hash_code):
    return hash_code % self.size
  
  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    for element in list_at_array:
      if element[0] == key:
        element[1] = value
    list_at_array.insert(payload)
        
    
    
  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    list_at_index = self.array[array_index]
    for item in list_at_index:
      if item[0] == key:
        return item[1]
    return None
        
    payload = self.array[array_index]
    if payload:
      if payload[0] == key:
        return payload
    else:
      return None
    
blossom = HashMap(len(flower_definitions))

for each_flower in flower_definitions:
  blossom.assign(each_flower[0], each_flower[1])
  
print(blossom.retrieve('daisy'))
  