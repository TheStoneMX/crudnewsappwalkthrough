from ._anvil_designer import Add_DesequilibrioComponentTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from .Apariencia import Apariencia
from .Implicaciones import Implicaciones
from .intervenciones import intervenciones
# from investigacion import investigacion
from .medica import medica
from .pleomorfica import pleomorfica
from .Relacion import Relacion
from .sintomas import sintomas
from .trabajando import trabajando

# Return a list of rows from the 'categories' Data Table
categories = [(cat['name'], cat) for cat in app_tables.categories.search()]

class Add_DesequilibrioComponent(Add_DesequilibrioComponentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.new_row = None
 
    # Any code you write here will run when the form opens.
    self.category_box.items = categories

  def image_uploader_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    # When a new file is loaded, add the image to self.item
    self.item['image'] = file
    
  def clear_text_controls(self):
    text_areas = [c for c in self.get_components() if isinstance(c, anvil.TextArea)]
    for text_area in text_areas:
      text_area.text = ''   

  def primary_color_save_click(self, **event_args): 
  # def primary_color_save_click(self, **event_args):
  #   # Create a dictionary to store the values
  #   new_row = {}
  #   # Iterate over each TextArea control in the Form
  #   for text_area in self.get_components(anvil.TextArea): 
  #     # Get the name of the TextArea control (i.e. the column name in the database)
  #     column_name = text_area.name
  #     # Get the value of the TextArea control
  #     value = text_area.text 
  #     # Add the column name and value to the new_row dictionary
  #     new_row[column_name] = value
      
  #   # Add the article to the Data Table is the user clicks 'Save'
  #     print(new_row)
    server.call('add_article', self.new_row)
    self.clear_text_controls()

  def primary_color_cancel_click(self, **event_args):
    self.clear_text_controls()

  def form_show(self, **event_args):
    self.new_row = self.item

  def button_Apariencia_click(self, **event_args):
    cmpt = Apariencia()
    add_component(cmpt)
    
  def add_component(self, cmpt):
      # self.link_list_anomalies.role = 'selected'
    self.column_panel_tabcontent.clear()
    self.column_panel_tabcontent.add_component(cmpt)  










