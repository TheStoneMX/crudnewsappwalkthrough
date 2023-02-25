from ._anvil_designer import SangreVivaComponentTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from .dryBlood import dryBlood
from .erythrocyte import erythrocyte
from .leukocyte import leukocyte
from .Microbes import Microbes
from .Plasma import Plasma
from .Pleomorphic import Pleomorphic
from .Trombocyte import Trombocyte

class SangreVivaComponent(SangreVivaComponentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def tab_click(self, **event_args):
    sender = event_args.get("sender", None)
    if not sender:
      print("Can't get sender from : ", event_args)
      return
    
    for comp in self.flow_anomalies_panel.get_components():
      if type(comp) is Button():
        if comp == sender:
          self.column_panel_tabcontent.clear()
          self.column_panel_tabcontent.add_component(comp.tag)
        else:
          comp.background = "#eee"
          
  def form_show(self, **event_args):
    # Show the frst tab.
    self.link_tab1.tag = Microbes()
    self.link_tab2.tag = Plasma()
    self.link_tab3.tag = Pleomorphic()
    self.link_tab3.tag = Trombocyte()
    self.link_tab3.tag = dryBlood()
    self.link_tab3.tag = erythrocyte()
    self.link_tab3.tag = leukocyte()
       
    self.tab_click(sender = self.link_tab1)

  def button_erythrocyte_click(self, **event_args):
    cmpt = erythrocyte()
    # self.link_list_anomalies.role = 'selected'
    self.column_panel_tabcontent.clear()
    self.column_panel_tabcontent.add_component(cmpt)

  def button_leukocyte_click(self, **event_args):
    cmpt = leukocyte()
    # self.link_list_anomalies.role = 'selected'
    self.column_panel_tabcontent.clear()
    self.column_panel_tabcontent.add_component(cmpt)

  def button_sangre_seca_click(self, **event_args):
    cmpt = dryBlood()
    # self.link_list_anomalies.role = 'selected'
    self.column_panel_tabcontent.clear()
    self.column_panel_tabcontent.add_component(cmpt)

  def button_trombocyte_click(self, **event_args):
    cmpt = Trombocyte()
    # self.link_list_anomalies.role = 'selected'
    self.column_panel_tabcontent.clear()
    self.column_panel_tabcontent.add_component(cmpt)

  def button_pleomorphic_click(self, **event_args):
    cmpt = Pleomorphic()
    # self.link_list_anomalies.role = 'selected'
    self.column_panel_tabcontent.clear()
    self.column_panel_tabcontent.add_component(cmpt)

  def button_plasma_click(self, **event_args):
    cmpt = Plasma()
    # self.link_list_anomalies.role = 'selected'
    self.column_panel_tabcontent.clear()
    self.column_panel_tabcontent.add_component(cmpt)

  def button_microbes_click(self, **event_args):
    cmpt = Microbes()
    # self.link_list_anomalies.role = 'selected'
    self.column_panel_tabcontent.clear()
    self.column_panel_tabcontent.add_component(cmpt)







