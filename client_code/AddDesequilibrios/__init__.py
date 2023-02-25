from ._anvil_designer import AddDesequilibriosTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Add_Desequilibrio import Add_Desequilibrio

import anvil.users
import navigation
import data_access

class AddDesequilibrios(AddDesequilibriosTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    user = data_access.the_user()
    self.set_account_state(user)

    # Any code you write here will run when the form opens.
    self.refresh_articles()
    # Set an event handler on the RepeatingPanel (our 'articles_panel')
    self.articles_panel.set_event_handler('x-delete-article', self.delete_article)
  
  def refresh_articles(self):
    # Load existing articles from the Data Table, and display them in the articles_panel
    self.articles_panel.items = anvil.server.call('get_articles')
  
  def delete_article(self, article, **event_args):
    # Delete the article
    anvil.server.call('delete_article', article)
    # Refresh articles to remove the deleted article from the Homepage
    self.refresh_articles()

  def add_article_button_click(self, **event_args):
    # initialise an empty dictionary which we'll use to record user inputs
    new_article = {}
    # Open an alert displaying the 'ArticleEdit' Form
    # set the `self.item` property of the ArticleEdit Form to new_article
    # Only add the article to the Data Table if the 'Save' button is clicked
    # if the 'Cancel' button is clicked, discard new_article
    if alert(content=Add_Desequilibrio(item=new_article), title="Agregar Desequilibrio",
             large=True, buttons=[("Save", True), ("Cancel", False)]):
      # Add the article to the Data Table is the user clicks 'Save'
      anvil.server.call('add_article', new_article)
      # Refresh articles to show the new article on the Homepage
      self.refresh_articles()

  def link_login_click(self, **event_args):
    user = anvil.users.login_with_form(allow_cancel=True)
    self.set_account_state(user)

  def register_click(self, **event_args):
    user = anvil.users.signup_with_form(allow_cancel=True)
    set_account_state(user)
    # navigation.go_home()
    pass

  def set_account_state(self, user):
    self.link_register.visible = user is None
    self.link_login.visible = user is None


