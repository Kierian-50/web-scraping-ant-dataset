import requests
import shutil
from bs4 import BeautifulSoup


class WebScraping:
    """
    The class that allows to do the web scrapping with BeautifulSoup
    Cette class permet de faire du web scrapping avec BeautifulSoup.
    Author: Kierian Tirlemont
    """
    def __init__(self):
        pass

    @staticmethod
    def download_image(file, url):
        """
        This method allows to download an image if the url is just the image like in the example bellow.
        Cette méthode permet de télécharger une image si l'url est l'image comme sur l'exemple ci-dessous.
        https://api.gbif.org/v1/image/unsafe/https%3A%2F%2Fwww.antweb.org%2Fimages%2Fcasent0648601%2Fcasent0648601_l_1_high.jpg
        :param url: The url where we can find the image / L'url qui permet de trouver l'image
        :param file: The file where we'll save the image on the computer.
                     Le fichier où nous allons enregistrer l'image sur notre pc.
        """
        response = requests.get(url, stream=True)
        shutil.copyfileobj(response.raw, file)

    @staticmethod
    def get_characteristic(url):
        """
        This method allows to get the characteristics of the set of data.
        Cette méthode permet de recupérrer les caractéristiques du jeu de données.
        :param url: The url where we can find the url / L'url où on peut trouver l'url.
        :return: The characteristic found in the url / Les caractéristiques trouvé dans l'url.
        """
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        res = []
        for s in soup.findAll('div', id="classification"):
            for element in s.findChildren('a'):
                res.append(element.text)
        return res