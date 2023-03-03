from ._anvil_designer import InfoFormTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..erythrocyte import erythrocyte

class InfoForm(InfoFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.string = 'erythrocyte'
    # Any code you write here will run before the form opens.

  def button_apariencia_click(self, **event_args):
    # we query DB and fill the Info Form
    cmpt = erythrocyte()
    
    anvil.server.call('get_desequilibrio', desiquilibrio_name)




