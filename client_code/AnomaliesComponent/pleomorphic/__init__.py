from ._anvil_designer import pleomorphicTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class pleomorphic(pleomorphicTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def radio_button_rbc_paracitados_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass

  def radio_button_wbc_paracitadas_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass

  def radio_button_pteroharpen_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass

  def radio_button_rbc_Fermentados_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass

  def radio_button_ascitis_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass





