import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from SangreVivaComponent import SangreVivaComponent
from HomeAnonComponent import HomeAnonComponent
from Add_DesequilibrioComponent import Add_DesequilibrioComponent 
from .AnomaliesComponent import AnomaliesComponent

home_form = None

def get_form():
  if not home_form:
    raise Exception("You must set the home form first.")   
  return home_form

def go_create_report():
  set_active_nav('report')
  set_title("Crear Reporte de Sangre Viva/Seca")
  form = get_form()
  form.load_component(SangreVivaComponent())

def go_biblioteca_anomalies():
  set_active_nav('list')
  set_title("Lista De Desequilibrios")
  form = get_form()
  form.load_component(AnomaliesComponent())

def go_add_anomaly():
  set_active_nav('anomalies')
  set_title("Agregar Desequilibrio")
  form = get_form()
  form.load_component(RegisterAnomalyComponent()) 

def go_register_anomaly():
  set_active_nav('register')
  set_title("Agregar Desequilibrio")
  form = get_form()
  form.load_component(Add_DesequilibrioComponent())    

def go_home():
  set_active_nav('home')
  set_title("")
  form = get_form()
  user = anvil.users.get_user()
  # if user:
  form.load_component(HomeAnonComponent())
  # else:
  #   form.load_component(HomeAnonComponent())

def set_title(text):
  form = get_form()
  base_title = form.base_title
  return
  
  if text:
    form.label_title.text = base_title + " - " + text
  else:
    form.label_title.text = base_title

def set_active_nav(state):
  form = get_form()
  # form.set_active_nav(state)

