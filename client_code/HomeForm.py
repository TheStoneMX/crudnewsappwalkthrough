from ._anvil_designer import HomeFormTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from CreateReportComponent import CreateReportComponent
from ListAnomaliesComponent import ListAnomaliesComponent
from RegisterAnomaly import RegisterAnomaly

class HomeForm(HomeFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def link_create_report_click(self, **event_args):
    cmpt = CreateReportComponent()
    self.column_panel_content.clear()
    self.column_panel_content.add_component(cmpt)
    

  def link_list_anomalies_click(self, **event_args):
    cmpt = ListAnomaliesComponent()
    self.column_panel_content.clear()
    self.column_panel_content.add_component(cmpt)

  def link_add_anomaly_click(self, **event_args):
    cmpt = RegisterAnomaly()
    self.column_panel_content.clear()
    self.column_panel_content.add_component(cmpt)



