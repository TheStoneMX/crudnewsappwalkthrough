from ._anvil_designer import InfoFormTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class InfoForm(InfoFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self._my_string = ''
    # Any code you write here will run before the form opens.
    # Assuming `articles` is the name of the data table
    self.table = app_tables.articles  
    
    ## Propiedades de la forma 
    self.Title = None
    self.Appearance = None
    self.Image = None
    self.Created = None
    self.UpDated = None
    self.Categoty = None
    self.Relevance = None
    self.Implications = None
    self.Symptoms = None
    self.Pleomorphic = None
    self.MedPerspecive = None
    self.Interventions = None
    self.WorkingWith = None
    self.Investigations = None 
    self.Almica = None 
    
# define a property to hold the string
  @property
  def my_string(self):
      return self._my_string
  
  @my_string.setter
  def my_string(self, value):
    self._my_string = value
    # do something with the string, e.g. update a label
    # self.label_1.text = value

    
  def set_form_controls(self, article_data):
    # Set the values of the form controls for each article
    self.Title = article_data['Title']
    self.Appearance = article_data['Appearance']
    self.Image = article_data['Image']
    self.Created = article_data['Created']
    self.UpDated = article_data['UpDated']
    self.Categoty = article_data['Category']
    self.Relevance = article_data['Relevance']
    self.Implications = article_data['Implications']
    self.Symptoms = article_data['Symptoms']
    self.Pleomorphic = article_data['Pleomorphic']
    self.MedPerspecive = article_data['MedPerspective']
    self.Interventions = article_data['Interventions']
    self.WorkingWith = article_data['WorkingWith']
    self.Investigations = article_data['Investigations']
    self.Almica = article_data['Almica']

    
  def button_apariencia_click(self, **event_args):
      try:
          # we query DB and fill the Info Form
          article_data = anvil.server.call('get_desequilibrio', self._my_string)
          #
          self.set_form_controls(article_data)
          #
          # print('Title', self.article_data['Title'])
          # print('Appearance', self.article_data['Appearance'])
          # print('Relevance', self.article_data['Relevance'])          # for item in article_data:
          #     print(item)
          # print('article_data', article_data['title'])
      except Exception as e:
          # handle the exception here, for example:
          print("An error occurred:", e)
      # row = article_data[1]
      # # Get the list of column names
      #  self.table.get_columns()






    
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







