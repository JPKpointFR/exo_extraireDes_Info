

def extraire_extension(nomFichier):
    nomFichier_split = nomFichier.split(".")
    if len(nomFichier) > 1:
        return nomFichier_split[-1]
    return None


def obtenir_definition_extension(extension, definition):
    for d in definition:
        if d[0].lower() == extension.lower():
            return d[1]
    return None


fichiers = ("notepad.exe", "nom.fichier.perso.doc", "notes.TXT",
            "vacances.jpeg", "planning", "data.dat")

definition_extension = (("exe", "Executable"),
                        ("doc", "Document Word"),
                        ("txt", "Document Texte"),
                        ("jpeg", "Image JPEG"))

# definition_extension_dict = {"exe": "Executable",
#                              "doc": "Document Word",
#                              "txt": "Document Texte",
#                              "jpeg": "Image JPEG"}


for fichier in fichiers:
    ext = extraire_extension(fichier)
    if ext:
        definition = obtenir_definition_extension(ext, definition_extension)
        #definition = definition_extension_dict.get(ext.lower())
        if definition == None:
            definition = "Extension non connue"
    else:
        definition = "Aucune extension"
    print(f"({fichier} {definition})")


'''
notepad.exe (Executable)
nom.fichier.perso.doc (Document Word)
notes.TXT (Document Word)
vacances.jpeg (Document JPEG)
planning (Aucune extension)
data.dat (Extension non connue)
'''


"""extraire = input("Extraire les extension: ")

if extraire == "notepad":
    print("notepad.exe (Executable)")
elif extraire == "nom.fichier.perso":
    print("nom.fichier.perso.doc (Document Word)")
elif extraire == "notes.TXT":
    print("notes.TXT (Document Word)")
elif extraire == "vacances.jpeg":
    print("vacances.jpeg (Document JPEG)")
elif extraire == "planning":
    print("planning (Aucune extension)")
elif extraire == "data.dat":
    print("data.dat (Extension non connue)")"""
