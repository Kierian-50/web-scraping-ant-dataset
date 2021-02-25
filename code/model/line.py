

class Line:
    """
    This class represents a line. This is easier to use to understand and to use because you just have to do self.attr
    to have the value.
    Cette classe represente une ligne. Ca rend le code plus simple à comprendre et à utiliser car il y a juste à
    écrire self.attr pour avoir la valeur.
    Author: Kierian Tirlemont
    """
    def __init__(self, line):
        """
        The constuctor of the class that initializes the attributes with the line past in parameter.
        Le constructeur de la classe qui initialise les attributs avec la ligne passée en parametre.
        :param line: The line to analyse / La ligne à analyser.
        """
        content = line.split()
        self.gbifID = content[0]
        self.type = content[1]
        self.format = content[2]
        self.identifier = content[3]
        self.references = content[4]
        self.title = content[5]
        self.description = content[6]
        self.source = content[7]
        self.audience = content[8]
        self.created = content[9]
        self.creator = content[10]
        self.contributor = content[11]
        self.publisher = content[12]
        self.license = content[13]
        self.rightsHolder = content[14]