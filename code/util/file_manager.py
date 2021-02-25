from os import path
import os


class FileManager:
    """
    This class allows to manage the files part of the part with some static method.
    Cette classe permet de gérer les fichiers du projet avec quelques methodes statique.
    Author: Kierian Tirlemont
    """
    def __init__(self):
        pass

    @staticmethod
    def read_file(filename):
        """
        This method allows to reads the file which contains every data.
        Cette méthode permet de lire le fichier qui contient toutes les données.
        :param filename: The name of the file which contains data / Le nom du fichier qui contient les données
        :return: The lines in the data file / Les lignes dans le ficher de données
        """
        file = open(filename, 'r')
        lines = file.readlines()
        file.close()
        return lines

    @staticmethod
    def create_dir(filename):
        """
        This method allows to create a directory.
        Cette methode permet de créer un dossier.
        :param filename: The path to the file name / Le chemin vers le nom du fichier
        """
        os.mkdir(filename)

    @staticmethod
    def open_file(filename):
        """
        This method allows to return the open file with the path of the file.
        Cette méthode permet de retourner le fichier ouvert avec le chemin vers le fichier.
        :param filename: The path to the filename.
                         Le chemin vers le fichier.
        :return: The open file.
                 Le fichier ouvert.
        """
        return open(filename, 'wb')

    @staticmethod
    def angle_view(ant_name_image):
        """
        This method allows to find the angle of view of the image.
        Cette méthode permet de trouver l'angle de vue de l'image.
        :param ant_name_image: The name of the image
                               Le nom de l'image
        :return: The angle of view of the image.
                 L'angle de vue de l'image.
        """
        if "dorsal" in ant_name_image:
            return "dorsal"
        elif "head" in ant_name_image:
            return "head"
        elif "profile" in ant_name_image:
            return "profile"
        else:
            return "error"

    @staticmethod
    def find_next_number(filename, name_species, view_angle):
        """
        This method allows to find the number of the image in the directory.
        Cette méthode permet de trouver le numéro de l'image dans le dossier.
        :param filename:
        :param name_species: The name of the species which is the name of the directory
                             Le nom de l'espece qui est le nom du dossier.
        :param view_angle: The angle of view which is also the name of the second directory.
                           L'angle de vu qui est aussi le nom du second dossier.
        :return:
        """
        find = False
        i = 0
        while not find:
            if path.exists(filename + "/" + name_species + "/" + view_angle + "/" + str(i) + ".jpg"):
                i = +1
            else:
                return str(i)

    @staticmethod
    def dir_exist(filename):
        """
        This method allows to find if the directory for a species exists.
        Cette method permet de trouver si un dossier pour une espece existe.
        :param filename:
        :return: True : if the directory exist / False : If the directory not exists
                 Vrai : si le dossier existe / Faux : Si le dosser n'existe pas
        """
        return path.isdir(filename)
