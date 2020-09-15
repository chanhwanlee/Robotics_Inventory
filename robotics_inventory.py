import List

class BaseRecord:
  def __init__(self, id: int):
    self.created_at = datetime.datetime.now()
    self.updated_at = datetime.datetime.now()
    self.id = id
    
class Bin(BaseRecord):
  num_bins = 0
  def __init__(self, location:str, part_id:str, qty_in_bin:int):
    id = num_bins
    super().__init__(id)
    self._location = location
    self._part_id = part_id
    self._qty_in_bin = qty_in_bin
    num_bins += 1

  def get_location(self):
    return self._location
  
  def set_location(self,value:str):
    assert type(value) is str, "The location must be a string."
    self._location = value
    self.updated_at = date.datetime.now()

  def get_part_id(self):
    return self._part_id
  
  def set_part_id(self,value:str):
    assert type(value) is str, "The part id must be a string."
    self._part_id = value
    self.updated_at = date.datetime.now()
    
  def get_qty_in_bin(self):
    return self._qty_in_bin
  
  def set_qty_in_bin(self,value:int):
    assert type(value) is int, "The quantity in the bin must be an integer."
    assert value>=0, "The quantity in the bin must be 0 or more".
    self._qty_in_bin = value
    self.updated_at = date.datetime.now()
    
class Part(BaseRecord):
  num_parts = 0
  def __init__(self, name:str, quantity:int, bin_id: int):
    part_id = num_parts
    super().__init__(part_id)
    self._name = name
    self._quantity = quantity
    self._bin_id = bin_id
    num_parts +=1
    
  def get_name(self):
    return self._name
  
  def set_name(self,value:str):
    assert type(value) is str, "The part name must be a string."
    self._name = value
    self.updated_at = date.datetime.now()
    
  def get_quantity(self):
    return self._quantity
  
  def set_quantity(self,value:int):
    assert type(value) is int, "The part quantity must be an integer."
    assert value>=0, "The quantity must be 0 or more."
    self._quantity = value
    self.updated_at = date.datetime.now()
   
  def get_bin_id(self):
    return self._bin_id
  
  def set_bin_id(self,value:int):
    assert type(value) is int, "The bin id must be an integer."
    self._bin_id = value
    self.updated_at = date.datetime.now()

    
class User(BaseRecord):
  num_users = 0
  def __init__(self, email:str):
    id = num_users
    super().__init__(id)
    self._email = email
    num_users +=1
    
  def get_email(self):
    return self._email
  
  def set_email(self, value:str):
    assert type(value) is str, "The user's email must be a string."
    self._email = value
    self.updated_at = date.datetime.now()

class Log(BaseRecord):
  num_logs = 0
  def __init__(self, part_id:int, quantity:int):
    log_id = num_logs
    super().__init__(log_id)
    self._part_id = part_id
    self._quantity = quantity
    num_logs +=1
    
  def get_part_id(self):
    return self._part_id
  
  def set_part_id(self,value:int):
    assert type(value) is int, "The part id must be an integer."
    self._part_id = value
    self.updated_at = date.datetime.now()
    
  def get_quantity(self):
    return self._quantity
  
  def set_quantity(self,value:int):
    assert type(value) is int, "The quantity must be an integer."
    assert value>=0, "The quantity must be 0 or more."
    self._quantity = value
    self.updated_at = date.datetime.now()
    
class InventoryManager:
  def __init__(self, parts:List[Part], bins:List[Bin], logs:List[Log], users:List[User]):
    self.parts = parts
    self.bins = bins
    self.logs = logs
    self.users = users
    
  def create_user(email: str, student_num: int) -> Student:
    student_num = User(student_num, email)
    append.student_num(User)
    
  def find_bin_by_location(location: str) -> Bin:
    for bin in bins:
      if location == bins[location]
        return bin
    
  def find_user_by_student_num(num: int) -> Student:
    for student in users:
      if num == users[num]:
        return student
    
  def add_part(name: str, quantity: int, bin_location: str):
    name = Part(name, quantity, bin_location)
    for bin in bins:
      if name == part_id:
        find_bin_by_location(name)
