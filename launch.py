from saving_file_structure import FileManager
from web_scraping import WebScraping
from time import sleep

if __name__ == "__main__":
    """
    The entry point of the program.
    Le point d'entrée du programme 
    Author: Kierian Tirlemont
    """
    # Init object
    file_manager = FileManager('C:/Users/kieri/PycharmProjects/download-image-from-page/ant_images')
    web_scraping = WebScraping(
        'https://www.gbif.org/occurrence/gallery?dataset_key=13b70480-bd69-11dd-b15f-b8a03c50a862')
    # The boolean for the infinite loop / Le boolean pour la boucle infinie
    finish = False
    # The index of the set of image / L'index du jeu d'image
    i = 6

    # Open the web site / Ouvre le site web.
    web_scraping.open_site()
    sleep(10)
    # Accepts cookies / Accepte les cookies
    web_scraping.click('/html/body/div[4]/aside[6]/div/div[2]/a[2]')
    while not finish:

        FileManager.write_file("C:/Users/kieri/PycharmProjects/download-image-from-page/i.txt", str(i))

        # Try to click on the set of image / Essaye de cliquer sur le jeu d'image
        try:
            web_scraping.click('/html/body/div[4]/main/div/div/div[1]/div/div/div/section[3]/div/div/a[' + str(i) + ']')
        except Exception:
            try:
                # If the program don't find the element then try to click on the more button. The page displays only
                # 100 set of images and each time you must click on more.
                # Si le programme ne trouve pas l'élément alors essaye de cliquer sur le boutton "more". La page affiche
                # seulement 100 jeu de données donc a chaque fois il faut appuyer sur "more".
                for z in range(1, i, 100):
                    print("More")
                    web_scraping.click('/html/body/div[4]/main/div/div/div[1]/div/div/div/section[3]/div/div/div')
                    sleep(5)
                # Try to reclick on the current set of images / Essaye de recliquer sur le jeu d'image courant.
                web_scraping.click(
                    '/html/body/div[4]/main/div/div/div[1]/div/div/div/section[3]/div/div/a[' + str(i) + ']')
            except Exception:
                # If it doesn't work, it's probably the end of the page
                # Si ca ne fonctionne pas, c'est probablement la fin de la page.
                print("Exception : Can't find an image and the more button")
                exit(-1)
        sleep(15)

        # Find the name of the species / Trouve le nom de l'espece
        species_name = web_scraping.recover_text_content(
            '/html/body/div[4]/main/div/div/div[1]/div/article/ng-include/section[1]/div/div[1]/header/h1/span')
        species_name = species_name.replace(" ", "_")
        species_name = species_name.lower()
        print("species name : " + species_name)

        # If the species hasn't directories then create it
        # Si l'espèce n'a pas de dossier alors on les créées
        if not file_manager.species_already_exist(species_name):
            file_manager.create_directory(species_name)
            file_manager.create_directory(species_name+"/"+"dorsal")
            file_manager.create_directory(species_name+"/"+"head")
            file_manager.create_directory(species_name+"/"+"profile")

        # For each image of the set of images/
        # Pour chaque image contenu dans le jeu d'image
        for j in range(1, int(web_scraping.recover_text_content(
                "/html/body/div[4]/main/div/div/div[1]/div/article/ng-include/div[2]/section[1]/div/div/div["
                "1]/div/a/div")) + 1):
            # Find the name of the image to find the angle of view of the image because it's written in the title.
            # Trouve le nom de l'image pour trouver l'angle de vue de l'image car c'est écrit dans le titre.
            image_name = web_scraping.recover_text_content(
                '/html/body/div[4]/main/div/div/div[1]/div/article/ng-include/div[2]/section[3]/div/div/div[' +
                    str(j) + ']/div/figure/figcaption/dl/div[1]/dd/span')
            image_name = image_name.replace(" ", "_")
            image_name = image_name.lower()
            angle_view = FileManager.angle_view(image_name)

            # If the angle of view is profile or head or dorsal else the picture will be taken for our dataset
            # Si l'angle de vue est le profile ou la tete ou le dos sinon l'image ne fera pas parti du dataset.
            if angle_view != "error":
                print("image : " + image_name)
                # Click on the picture to save it.
                # Clique sur l'image pour enregistrer l'image.
                web_scraping.click('/html/body/div[4]/main/div/div/div[1]/div/article/ng-include/div[2]/section[3]' +
                                   '/div/div/div['+str(j)+']/div/figure/a/img')
                file = file_manager.open_file(species_name + "/" +angle_view + "/" +
                                              file_manager.find_the_number_of_image(species_name, angle_view)+".jpg")
                web_scraping.download_image(file)
                sleep(5)
                # Back on the set of images to choose another picture
                # Retour sur la page de jeu de données pour enregistrer une autre image.
                web_scraping.back()
            sleep(5)
        # Back on the main page
        # Retour sur la page principale
        web_scraping.back()
        sleep(15)
        i = i + 1
