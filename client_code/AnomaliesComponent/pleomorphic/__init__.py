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
  def radio_button_protit_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Protit'
    
  def radio_button_spermits_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Spermits'

  def radio_button_Sistatogenia_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Sistatogenia'
    
  def radio_button_PTeroharpen_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'PTeroharpen'
    
  def radio_button_symprotit_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Symprotit'

  def radio_button_coloid_tectis_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Coloid Tecits'

  def radio_button_dioekothecits_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Dioekothecits'

  def radio_button_mychits_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Mychits'

  def radio_button_tecits_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Tecits'

  def radio_button_condrites_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Condrites'
    
  def radio_button_ascits_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Ascits'

  def radio_button_talus_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Talus'

  def radio_button_syinascits_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Syinascits'

  def add_component_2_tab_control(self, cmpt):
    # self.link_list_anomalies.role = 'selected'
    self.column_panel_tabcontent.clear()
    self.column_panel_tabcontent.add_component(cmpt) 


















