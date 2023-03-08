from ._anvil_designer import AnomaliesComponentTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .erythrocyte import erythrocyte
from .leukocyte import leukocyte
from .plasma import plasma
from .thrombocyte import thrombocyte
from .pleomorphic import pleomorphic

class AnomaliesComponent(AnomaliesComponentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def button_Info_click(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)

  def button_erythrocyte_click(self, **event_args):
    cmpt = erythrocyte()
    self.add_component_2_tab_control(cmpt)

  def button_leukocyte_click(self, **event_args):
    cmpt = leukocyte()
    self.add_component_2_tab_control(cmpt)

  def button_plasma_click(self, **event_args):
    cmpt = plasma()
    self.add_component_2_tab_control(cmpt)

  def button_thrombocyte_click(self, **event_args):
    cmpt = thrombocyte()
    self.add_component_2_tab_control(cmpt)

  def button_pleomorphic_click(self, **event_args):
    cmpt = pleomorphic()
    self.add_component_2_tab_control(cmpt)
    
  def add_component_2_tab_control(self, cmpt):
    # self.link_list_anomalies.role = 'selected'
    self.column_panel_tabcontent.clear()
    self.column_panel_tabcontent.add_component(cmpt) 



