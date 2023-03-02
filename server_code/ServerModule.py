import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

@anvil.server.callable
def add_article(article_dict):
  app_tables.articles.add_row( created=datetime.now(), **article_dict  )

@anvil.server.callable
def get_articles():
  # Get a list of articles from the Data Table, sorted by 'created' column, in descending order
  return app_tables.articles.search(tables.order_by("created", ascending=False))
  
@anvil.server.callable
def update_article(article, article_dict):
  # Check if the article to be updated does exist in the Data Table
  # Only perform the update operation if the article exists
  if app_tables.articles.has_row(article):
    # Set the 'updated' property to datetime.now()
    article_dict['updated'] = datetime.now()
    article.update(**article_dict)
  else:
    # Raise an exception if the article doesn't exist in the Data Table
    raise Exception("Article does not exist")
       
@anvil.server.callable
def delete_article(article):
  # Check if the article to be deleted does exist in the Data Table
  # Only perform the delete operation if the article exists
  if app_tables.articles.has_row(article):
    article.delete()
  else:
    # Raise an exception if the article doesn't exist in the Data Table
    raise Exception("Article does not exist")

@anvil.server.callable
def get_desequilibrio(desequilibrio):
  # Get a list of articles from the Data Table, sorted by 'created' column, in descending order
  # Search the table for articles with the given name
  return app_tables.articles.search(tables.q['title'] == name)
  
@anvil.server.callable
def get_desequilibrio(desequilibrio):
  # Get a list of articles from the Data Table, sorted by 'created' column, in descending order
  # search for the row with the given title
  desequilibrio = app_tables.articles.search(tables.q['title'] == desequilibrio)
    # check if a row was found
  if len(desequilibrio) > 0:
      # get the first row
      return desequilibrio[0]
  else:
    return None
      