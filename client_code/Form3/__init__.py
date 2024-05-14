from ._anvil_designer import Form3Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form3(Form3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.btn_1.set_event_handler("click", self.btn_1_click)
  def btn_1_click(self, **event_args):
    input_numbers = self.txt_nhap.text.split()
    
    numbers = [int(num) for num in input_numbers]
    
    self.insertion_sort(numbers, ascending=True)
    self.txt_sxtang.text = " ".join(map(str, numbers))
    
    self.insertion_sort(numbers, ascending=False)
    self.txt_sxgiam.text = " ".join(map(str, numbers))

  def insertion_sort(self, arr, ascending=True):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and ((arr[j] > key) if ascending else (arr[j] < key)):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

