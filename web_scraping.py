from selenium import webdriver
import shutil
import requests


class WebScraping:
    """
    This class brings the tools to make web scraping using selenium with the goal to save a lot of images.
    Cette classe apporte les outils idéaux pour effectuer du web scraping avec le but d'enregistrer un grand nombre
    d'images.
    Author: Kierian Tirlemont
    """

    def __init__(self, url):
        """
        The constructor of the class that allows to create the webdriver and init the url.
        Le contructeur de la classe qui permet de creer le webdriver et d'initialiser l'url.
        :param url: The current URL where we'll work to find the images.
                    L'url où nous allons récupérer les images.
        """
        self.driver = webdriver.Chrome()
        self.url = url

    def open_site(self):
        """
        This method allows to open the website of the class thought his url.
        Cette méthode permet d'ouvrir le web site de la classe à travers l'url.
        """
        self.driver.get(self.url)

    def click(self, xPaths):
        """
        This method allows to click on an element past in parameter.
        Cette methode permet de cliquer sur un élément passé en paramètre.
        :param xPaths: The element where we want to click.
                       L'élément où on veut cliquer
        """
        self.driver.find_element_by_xpath(xPaths).click()

    def recover_text_content(self, xPaths):
        """
        This method allows to recover the text of a an element past in parameter.
        Cette méthode permet de recupérer le texte d'un élément passé en paramètre.
        :param xPaths: The element that you want to know the content.
                       L'élément où nous voulons récupérer le contenu.
        :return: The text of the element / Le texte de l'élément.
        """
        return self.driver.find_element_by_xpath(xPaths).text

    def download_image(self, file):
        """
        This method allows to download an image if the current page is just the image like in the example bellow.
        Cette méthode permet de télécharger une image si la page actuelle est l'image comme sur l'exemple ci-dessous.
        https://api.gbif.org/v1/image/unsafe/https%3A%2F%2Fwww.antweb.org%2Fimages%2Fcasent0648601%2Fcasent0648601_l_1_high.jpg
        :param file: The file where we'll save the image on the computer.
                     Le fichier où nous allons enregistrer l'image sur notre pc.
        """
        response = requests.get(self.driver.current_url, stream=True)  # Recup l'image
        shutil.copyfileobj(response.raw, file)

    def back(self):
        """
        This method allows to go to the previous page.
        Cette méthode permet d'aller à la page précedente.
        """
        self.driver.execute_script("window.history.go(-1)")
