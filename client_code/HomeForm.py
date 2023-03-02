from ._anvil_designer import HomeFormTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

import anvil.users
import navigation
# import data_access

class HomeForm(HomeFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.base_title = "Home"
    # user = data_access.the_user()
    # self.set_account_state(user)
    navigation.home_form = self
    navigation.go_home()

  def link_home_click(self, **event_args):
    navigation.go_home()
    
  def link_create_report_click(self, **event_args):
    navigation.go_create_report()

  def link_add_anomaly_click(self, **event_args):
    navigation.go_register_anomaly()

  def link_biblioteca_anomalies_click(self, **event_args):
    navigation.go_biblioteca_anomalies()
    
  def set_active_nav(self, state):
    self.link_home.role = 'selected' if state == 'home' else None
    self.link_create_report.role = 'selected' if state == 'report' else None
    self.link_list_anomalies.role = 'selected' if state == 'list' else None
    self.link_register_anomaly.role = 'selected' if state == 'register' else None
 
  def load_component(self, cmpt):
    self.column_panel_content.clear()
    self.column_panel_content.add_component(cmpt)
    
    # if data_access.the_user():
    #   self.set_account_state(data_access.the_user())
  # def set_account_state(self, user):
  #   self.link_account.visible = user is not None
  #   self.link_logout.visible = user is not None
  #   self.link_login.visible = user is None
  #   self.link_register.visible = user is None


