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
    cmpt.my_string = 'Acantocitos'
    cmpt.button_apariencia_click()

  def radio_button_Anisocytosis_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Anisocitosis'
    cmpt.button_apariencia_click()
    
  def radio_button_cloud_patterns_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Patron de Nubes'
    cmpt.button_apariencia_click()
    

  def radio_button_Ghost_Cells_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Celulas Fantasmas'
    cmpt.button_apariencia_click()

  def radio_button_Protein_Linkage_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Enlace de proteínas'
    cmpt.button_apariencia_click()

  def radio_button_Schistocytes_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Esquistocitos'
    cmpt.button_apariencia_click()

  def radio_button_Target_Cells_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Células Diana'
    cmpt.button_apariencia_click()

  def radio_button_Erythrocyte_Aggregation_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Agregación de eritrocitos'
    cmpt.button_apariencia_click()

  def radio_button_Single_Membrane_Protrusion_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Protrusión de membrana única'
    cmpt.button_apariencia_click()

  def radio_button_Spherocytes_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Esferocitos'
    cmpt.button_apariencia_click()

  def radio_button_Sickle_Cells_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Células Falciformes'
    cmpt.button_apariencia_click()

  def radio_button_RBC_Rings_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Anillos de glóbulos rojos'
    cmpt.button_apariencia_click()

  def radio_button_Keratocytes_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Queratocitos'
    cmpt.button_apariencia_click()

  def radio_button_Echinocytes_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Equinocitos'
    cmpt.button_apariencia_click()

  def radio_button_Anisopoikilocytosis_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Anisopoiquilocitosis'
    cmpt.button_apariencia_click()

  def radio_button_Elliptocytes_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Eliptocitos'
    cmpt.button_apariencia_click()

  def radio_button_Poikilocytes_clicked(self, **event_args):
    cmpt = InfoForm()
    self.add_component_2_tab_control(cmpt)
    cmpt.my_string = 'Poiquilocitos'
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

    
















