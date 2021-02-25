from os import path
import os


class FileManager:
    """
    This class allows to manage the tree structure of the file to create a correct dataset.
    Cette classe permet de gérer l'arborescence du fichier pour creer un dataset correct.
    Author: Kierian Tirlemont
    """

    def __init__(self, absolute_path):
        """
        The constructor of the class, here we just need the ant_image absolute path.
        Le constructeur de classe, ici on a juste besoin du chemin absolu du fichier ant_image.
        :param absolute_path: The absolute path for the ant_images directory
                              Le chemin absolu pour accéder au dossier ant_image.
        """
        self.absolute_path = absolute_path

    def species_already_exist(self, species_name):
        """
        This method allows to find if the directory for a species exists.
        Cette method permet de trouver si un dossier pour une espece existe.
        :param species_name: The name of the species with underscore
                             Le nom de l'espèce avec des underscore.
        :return: True : if the directory exist / False : If the directory not exists
                 Vrai : si le dossier existe / Faux : Si le dosser n'existe pas
        """
        return path.isdir(self.absolute_path + "/" + species_name)

    def create_directory(self, species_name):
        """
        This method allows to create a directory.
        Cette méthode permet de creer un dosssier.
        :param species_name: The name of the species which will be the name of the directory.
                             Le nom de l'espèce qui sera le nom du dossier.
        """
        os.mkdir(self.absolute_path + "/" + species_name)

    def find_the_number_of_image(self, name_species, view_angle):
        """
        This method allows to find the number of the image in the directory.
        Cette méthode permet de trouver le numéro de l'image dans le dossier.
        :param name_species: The name of the species which is the name of the directory
                             Le nom de l'espece qui est le nom du dossier.
        :param view_angle: The angle of view which is also the name of the second directory.
                           L'angle de vu qui est aussi le nom du second dossier.
        :return:
        """
        find = False
        i = 0
        while not find:
            if path.exists(self.absolute_path + "/" + name_species + "/" + view_angle + "/" + str(i)+".jpg"):
                i = +1
            else:
                return str(i)

    def open_file(self, filename):
        """
        This method allows to return the open file with the path of the file.
        Cette méthode permet de retourner le fichier ouvert avec le chemin vers le fichier.
        :param filename: The path to the filename.
                         Le chemin vers le fichier.
        :return: The open file.
                 Le fichier ouvert.
        """
        return open(self.absolute_path+"/"+filename, 'wb')  # Le fichier ou l'image sera stocké

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
    def write_file(filename, content):
        f = open(filename, "a")
        f.write(content)
        f.write("\n")
        f.flush()
        f.close()
