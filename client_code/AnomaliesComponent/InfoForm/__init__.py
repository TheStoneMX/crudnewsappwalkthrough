from ._anvil_designer import InfoFormTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ..Anomalies import *

class InfoForm(InfoFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self._my_string = ''
    # Any code you write here will run before the form opens.
    # Assuming `articles` is the name of the data table
    self.title = None
    self.apariencia = None
    self.relacion = None
    self.implicaciones = None
    self.sintomas = None
    self.pleomorfica = None
    self.medica = None
    self.intervenciones = None
    self.trabajando = None
    self.investigaciones = None
    self.almica = None
    
# define a property to hold the string
  @property
  def my_string(self):
      return self._my_string
  
  @my_string.setter
  def my_string(self, value):
    self._my_string = value
    # do something with the string, e.g. update a label
    # self.label_1.text = value
   
  def button_apariencia_click(self, **event_args):
    # we query DB and fill the Info Form
    article_data = anvil.server.call('get_desequilibrio', self._my_string)
    # row = article_data[1]
    # # Get the list of column names
    #  self.table.get_columns()
  # Loop through the query results and assign the values to the corresponding TextBox components
  for row in article_query:
      title_textbox= row['title'] + "\n"
      appearance_textbox += row['Appearance'] + "\n"
      relevance_textbox.text += row['Relevance'] + "\n"

  # def set_properties( article_data):
    





    
    # Accessing the row's properties
    # title = row['title']  # Assuming there's a `title` column in the table
    # Appearance = row['Appearance']  # Assuming there's a `content` column in the table
    # category = row['category']  # Assuming there's a `date_published` column in the table
    
    # Printing the values
    # print(f"Title: {title}")
    # print(f"Content: {Appearance}")
    # print(f"Category: {category}")
    # print('title', title)
    # print('Appearance', Appearance)
    # print('category', category)







