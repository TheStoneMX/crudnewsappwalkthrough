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
    anvil.server.call('get_desequilibrio', self._my_string)



# class Article:
#     def __init__(self, title):
#         # search for the row with the given title
#         articles = app_tables.articles.search(q.title == title)
#         # check if a row was found
#         if len(articles) > 0:
#             # get the first row
#             article = articles[0]

#             # store the data in instance variables
#             self.title = article['title']
#             self.apariencia = article['Apariencia']
#             self.relacion = article['Relacion']
#             self.implicaciones = article['Implicaciones']
#             self.sintomas = article['Sintomas']
#             self.pleomorfica = article['pleomorfica']
#             self.medica = article['medica']
#             self.intervenciones = article['intervenciones']
#             self.trabajando = article['trabajando']
#             self.investigaciones = article['investigaciones']
#             self.almica = article['almica']
#         else:
#             # if no row was found, set all instance variables to None
#             self.title = None
#             self.apariencia = None
#             self.relacion = None
#             self.implicaciones = None
#             self.sintomas = None
#             self.pleomorfica = None
#             self.medica = None
#             self.intervenciones = None
#             self.trabajando = None
#             self.investigaciones = None
#             self.almica = None

#     def __str__(self):
#         # define how the object should be represented as a string
#         return f"Article: {self.title}"

#     def fill_text_controls(self, apariencia_text_box, relacion_text_box,
#                            implicaciones_text_box, sintomas_text_box,
#                            pleomorfica_text_box, medica_text_box,
#                            intervenciones_text_box, trabajando_text_box,
#                            investigaciones_text_box, almica_text_box):
#         # fill the text controls with the data from the object
#         apariencia_text_box.text = self.apariencia
#         relacion_text_box.text = self.relacion
#         implicaciones_text_box.text = self.implicaciones
#         sintomas_text_box.text = self.sintomas
#         pleomorfica_text_box.text = self.pleomorfica
#         medica_text_box.text = self.medica
#         intervenciones_text_box.text = self.intervenciones
#         trabajando_text_box.text = self.trabajando
#         investigaciones_text_box.text = self.investigaciones
#         almica_text_box.text = self.almica
