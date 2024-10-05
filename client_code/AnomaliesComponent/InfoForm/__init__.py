from ._anvil_designer import InfoFormTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import re

class InfoForm(InfoFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self._my_string = ''
    # Any code you write here will run before the form opens.
    # Assuming `articles` is the name of the data table
    self.table = app_tables.articles  
    
    ## Propiedades de la forma 
    # self.Title = None
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
    self.Consejos = None
    #
   
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
    self.label_tittle.text = article_data['Title']

    print('Appearence before', article_data['Appearance'])
    print('Appearence after ', self.format_text(article_data['Appearance']))
    
    # self.rich_text_main_text.content = self.format_text(article_data['Appearance'])

    
    self.Anomaly_Image.source = article_data['Image']
    
    ##
    self.Created = article_data['Created']
    self.UpDated = article_data['UpDated']
    ##
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
    self.Consejos = article_data['Consejos']

  
  def button_apariencia_click(self, **event_args):
      try:
          print("Fetching data for:", self._my_string)
          article_data = anvil.server.call('get_desequilibrio', self._my_string)
          print("Data fetched successfully")
          
          print("Appearance before:", repr(article_data['Appearance']))
          
          # Unescape Unicode characters
          unescaped_text = self.unescape_unicode(article_data['Appearance'])
          print("Unescaped text:", repr(unescaped_text))
          
          formatted_content = self.format_text(unescaped_text)
          print("Formatted content:", formatted_content)
          
          self.rich_text_main_text.content = formatted_content
          self.set_form_controls(article_data)
          self.enable_buttons()
      except Exception as e:
          print("An error occurred:", str(e))
          print("Error type:", type(e))
      
  # def button_apariencia_click(self, **event_args):
  #     try:
  #         print("Fetching data for:", self._my_string)
  #         article_data = anvil.server.call('get_desequilibrio', self._my_string)
  #         print("Data fetched successfully")
  #         print("Raw 'Appearance' data:", repr(article_data['Appearance']))
  #         formatted_content = self.format_text(article_data['Appearance'])
  #         print("Formatted content:")
  #         for item in formatted_content:
  #             print(repr(item))  # This will print each formatted item
  #         self.rich_text_main_text.content = formatted_content
  #         print("Content set to Rich Text control")
  #         self.set_form_controls(article_data)
  #         self.enable_buttons()
  #     except Exception as e:
  #         print("An error occurred:", str(e))
  #         print("Error type:", type(e))

  def button_relacion_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.rich_text_main_text.content = self.Relevance
    
  def button_Implicaciones_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.rich_text_main_text.content = self.Implications
    
  def button_Sintomas_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.rich_text_main_text.content = self.Symptoms

  def button_Pleomorfica_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.rich_text_main_text.content = self.Pleomorphic

  def button_Medica_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.rich_text_main_text.content = self.MedPerspecive

  def button_Intervenciones_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.rich_text_main_text.content = self.Interventions

  def button_Trabajando_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.rich_text_main_text.content = self.WorkingWith

  def button_Investigaciones_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.rich_text_main_text.content = self.Investigations

  def button_Almica_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.rich_text_main_text.content = self.Almica

  def button_consejos_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.rich_text_main_text.content = self.Consejos
  
  import codecs
  
  def unescape_unicode(self, text):
      return codecs.decode(text, 'unicode_escape')
  
  def format_text(self, text):
      # Unescape Unicode characters
      text = self.unescape_unicode(text)
      
      # Split the text into sentences
      sentences = text.split('. ')
  
      # Create a list of bullet points for the RichText control
      formatted_content = []
      for sentence in sentences:
          if sentence.strip():  # Ignore empty sentences
              formatted_content.append({
                  'text': '• ' + sentence.strip() + '.\n',
                  'font': 'Arial, sans-serif',
                  'font_size': 14
              })
  
      return formatted_content
    
  def enable_buttons(self):
    #
    self.button_relacion.enabled = True
    self.button_Implicaciones.enabled = True
    self.button_Sintomas.enabled = True
    self.button_Pleomorfica.enabled = True
    self.button_Medica.enabled = True
    self.button_Intervenciones.enabled = True
    self.button_Trabajando.enabled = True
    self.button_Investigaciones.enabled = True
    self.button_Almica.enabled = True
    self.button_Consejos.enabled  = True

  def disable_buttons(self):
    #
    print('Disabling buttons') 
    self.button_apariencia.enabled = True
    self.button_relacion.enabled = False
    self.button_Implicaciones.enabled = False
    self.button_Sintomas.enabled = False
    self.button_Pleomorfica.enabled = False
    self.button_Medica.enabled = False
    self.button_Intervenciones.enabled = False
    self.button_Trabajando.enabled = False
    self.button_Investigaciones.enabled = False
    self.button_Almica.enabled = False
    self.button_Consejos.enabled  = False
    
  def form_show(self, **event_args):
    """This method is called when the column panel is shown on the screen"""
    self.disable_buttons()






    
















