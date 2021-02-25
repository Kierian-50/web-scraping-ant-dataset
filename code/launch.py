from model.line import Line
from util.file_manager import FileManager
from util.web_scraping import WebScraping

if __name__ == "__main__":
    """
    The entry point of the program.
    Le point d'entrée du programme 
    Author: Kierian Tirlemont
    """
    # The path in the file / Les chemins des fichiers
    path_to_txt = "C:/Users/kieri/PycharmProjects/download-from-text/resources/multimedia.txt"
    path_to_img = "C:/Users/kieri/PycharmProjects/download-from-text/ant-images/"

    # Find the lines which are in the file / Trouver les lignes qui sont dans le fichier texte
    lines = FileManager.read_file(path_to_txt)

    # Init var
    old_line_object = Line(lines[0])
    i = 0

    # For each lines in the line / Pour chaque ligne du fichiers
    for line in lines:
        # Create an line object / Crée un objet ligne
        line_object = Line(line)

        try:
            # Find the characteristic of the dataset / Trouve les caractéristiques du jeu de données.
            characteristic = WebScraping.get_characteristic(line_object.references)
            species_name = characteristic[3].replace(' ', '_')

            print("characteristic : ")
            print(characteristic)

            # Group by dataset
            # Groupe par jeu de données
            if line_object.gbifID != old_line_object.gbifID:
                old_line_object = line_object
                # If the species has already a directory
                # Si l'espèce a déjà un dossier
                if not FileManager.dir_exist(path_to_img + species_name):
                    FileManager.create_dir(path_to_img + species_name)
                    FileManager.create_dir(path_to_img + species_name + "/dorsal")
                    FileManager.create_dir(path_to_img + species_name + "/head")
                    FileManager.create_dir(path_to_img + species_name + "/profile")

            print("link : "+line_object.identifier)

            # The angle of view of the picture / L'angle de vue de l'image
            angle_view = FileManager.angle_view(line_object.description)

            # If the angle of view is interesting for us else we don't take the images
            # Si l'angle de vue est interessant pour nous sinon on ne prend pas l'image
            if angle_view != "error":
                # Find the extension of the image / Trouve l'extension de l'image
                ext = line_object.format.split('/')[1]
                # Download the images / Enregistre l'image
                file = FileManager.open_file(path_to_img + species_name + "/" + angle_view + "/" + str(i) + "." + ext)
                WebScraping.download_image(file, line_object.identifier)
        except Exception as E:
            print(E)
        i = i + 1