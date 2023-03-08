from ._anvil_designer import leukocyteTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class leukocyte(leukocyteTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def radio_button_Cohesion_neutrofilos_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass

  def radio_button_basofilia_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass

  def radio_button_Neutrofilos_Hipersegmenados_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass

  def radio_button_Globulos_Blancos_Interrumpidos_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass

  def radio_button_neutrofilos_no_viables_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass

  def radio_button_neutrofilos_banda_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass






