from ._anvil_designer import erythrocyteTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..InfoForm import InfoForm

class erythrocyte(erythrocyteTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
  
  def radio_button_Acanthocytes_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Acanthocytes'
    cmpt.button_apariencia_click()

  def radio_button_Anisocytosis_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Anisocytosis'
    cmpt.button_apariencia_click()
    
  def radio_button_cloud_patterns_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Cloud Patterns'
    cmpt.button_apariencia_click()
    

  def radio_button_Ghost_Cells_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Ghost Cells'
    cmpt.button_apariencia_click()

  def radio_button_Protein_Linkage_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Protein Linkage'
    cmpt.button_apariencia_click()

  def radio_button_Schistocytes_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Schistocytes'
    cmpt.button_apariencia_click()

  def radio_button_Target_Cells_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Target Cells'
    cmpt.button_apariencia_click()

  def radio_button_Erythrocyte_Aggregation_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Erythrocyte Aggregation'
    cmpt.button_apariencia_click()

  def radio_button_Single_Membrane_Protrusion_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Single Membrane Protrusion'
    cmpt.button_apariencia_click()

  def radio_button_Spherocytes_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Spherocytes'
    cmpt.button_apariencia_click()

  def radio_button_Sickle_Cells_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Sickle Cells'
    cmpt.button_apariencia_click()

  def radio_button_RBC_Rings_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'RBC Rings'
    cmpt.button_apariencia_click()

  def radio_button_Keratocytes_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Keratocytes'
    cmpt.button_apariencia_click()

  def radio_button_Echinocytes_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Echinocytes'
    cmpt.button_apariencia_click()

  def radio_button_Anisopoikilocytosis_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Anisopoikilocytosis'
    cmpt.button_apariencia_click()

  def radio_button_Elliptocytes_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Elliptocytes'
    cmpt.button_apariencia_click()

  def radio_button_Poikilocytes_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Poikilocytes'
    cmpt.button_apariencia_click()

  def radio_button_Rouleau_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Rouleau'
    cmpt.button_apariencia_click()

  def radio_button_Stomatocytes_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Stomatocytes'
    cmpt.button_apariencia_click()

  def add_component_2_tab_control(self, cmpt):
    # self.link_list_anomalies.role = 'selected'
    self.column_panel_tabcontent.clear()
    self.column_panel_tabcontent.add_component(cmpt) 

    
















