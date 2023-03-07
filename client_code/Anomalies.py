import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
class Article:
    def __init__(self, title):
        # search for the row with the given title
        articles = app_tables.articles.search(q.title == title)
        # check if a row was found
        if len(articles) > 0:
            # get the first row
            article = articles[0]

            # store the data in instance variables
            self.title = article['Title']
            self.apariencia = article['Appearance']
            self.relacion = article['Relevance']
            self.implicaciones = article['Implications']
            self.sintomas = article['Symptoms']
            self.pleomorfica = article['Pleomorphic']
            self.medica = article['MedPerspective']
            self.intervenciones = article['Interventions']
            self.trabajando = article['WorkingWith']
            self.investigaciones = article['Investigations']
            self.almica = article['Almica']
        else:
            # if no row was found, set all instance variables to None
            self.title = None
            self.apariencia = None
            self.relacion = None
            self.implicaciones = None
            self.sintomas = None
            self.pleomorfica = None
            self.medica = None
            self.intervenciones = None
            self.trabajando = None
            self.investigaciones = None
            self.almica = None

    def __str__(self):
        # define how the object should be represented as a string
        return f"Article: {self.Title}"

    def fill_text_controls(self, apariencia_text_box, relacion_text_box,
                           implicaciones_text_box, sintomas_text_box,
                           pleomorfica_text_box, medica_text_box,
                           intervenciones_text_box, trabajando_text_box,
                           investigaciones_text_box, almica_text_box):
        # fill the text controls with the data from the object
        apariencia_text_box.text = self.apariencia
        relacion_text_box.text = self.relacion
        implicaciones_text_box.text = self.implicaciones
        sintomas_text_box.text = self.sintomas
        pleomorfica_text_box.text = self.pleomorfica
        medica_text_box.text = self.medica
        intervenciones_text_box.text = self.intervenciones
        trabajando_text_box.text = self.trabajando
        investigaciones_text_box.text = self.investigaciones
        almica_text_box.text = self.almica
