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
    #
    self.disble_buttons()
   
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
    self.rich_text_main_text.content = article_data['Appearance']
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

  def disble_buttons(self):
    #
    self.button_relacion.disabled = True
    self.button_Implicaciones.disabled = True
    self.button_Sintomas.disabled = True
    self.button_Pleomorfica.disabled = True
    self.button_Medica.disabled = True
    self.button_Intervenciones.disabled = True
    self.button_Trabajando.disabled = True
    self.button_Investigaciones.disabled = True
    self.button_Almica.disabled = True

  def enable_buttons(self):
    #
    self.button_apariencia.disabled = True
    self.button_relacion.disabled = False
    self.button_Implicaciones.disabled = False
    self.button_Sintomas.disabled = False
    self.button_Pleomorfica.disabled = False
    self.button_Medica.disabled = False
    self.button_Intervenciones.disabled = False
    self.button_Trabajando.disabled = False
    self.button_Investigaciones.disabled = False
    self.button_Almica.disabled = False

    
















