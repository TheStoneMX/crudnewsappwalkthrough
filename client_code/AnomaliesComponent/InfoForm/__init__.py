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
    self.rich_text_main_text.content = self.format_text( article_data['Appearance'] )
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
          # we query DB and fill the Info Form
          article_data = anvil.server.call('get_desequilibrio', self._my_string)
          #
          self.set_form_controls(article_data)
          self.enable_buttons()
      except Exception as e:
          # handle the exception here, for example:
          print("An error occurred:", e)
  

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
  
  def format_text(self, text):
      # Ensure the text is always treated as a string
      text = str(text)  # Convert to string if it's not already
  
      # Replace escaped sequences with their actual characters
      try:
          # Encode the text to bytes, then decode it back to handle escaped characters
          text = text.encode('latin1').decode('unicode_escape').encode('latin1').decode('utf-8')
      except Exception as e:
          print("Encoding Error: ", e)
  
      # Split the text into sentences based on periods
      bullet_points = text.split(". ")
  
      # Create a list of bullet points for the RichText control
      formatted_content = [
          {"tag": "ul", "content": [{"tag": "li", "content": point} for point in bullet_points if point]}
      ]
  
      # Return the formatted content to be used in the RichText control
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
    print('enable_buttons', self.enable_buttons)
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






    
















