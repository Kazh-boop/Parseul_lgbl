from lib2to3.pgen2.token import OP
from toTXT import ToTXT
from toXML import ToXML
import sys, time, os

# Affichage de l'assistance
def helpPDFtoFiles():
    print("\npython3 launch.py <Folder path> [Option]")
    print("\tFolder path:")
    print("\t\tExact or relative path")
    print("\tOption:")
    print("\t\tIf this parameter is leave blank, the option by default is -x")
    print("\t\t-x Parser from .pdf to .xml files")
    print("\t\t-t Parser from .pdf to .txt files")

# Verification de l'existence du dossier rentre en parametre
def checkFolderExist():
    return os.path.exists(FOLDER)

# Verification de l'option passée en parametre
def checkOption(option):
    if option is not None and option != '-t' and option !='-x':
        return False
    else:
        return True

def finishMessage():
    # Calcul de la duree du programme
    interval = time.time() - start_time
    interval = round(interval, 2)

    # Affichage de fin de programme
    print('\n' + "pdfParser execution completed")
    print('\t' + str(numberTotalFiles) + " files processed")
    print('\t' + "Completed in " + str(interval) + " seconds" + '\n')

# Heure et index initial
start_time = time.time()

# Verification du nombre de variables et initialisation des variables en parametre
if len(sys.argv) < 2:
    helpPDFtoFiles()

elif len(sys.argv) == 2:
    FOLDER = sys.argv[1]
    OPTION = '-x'

elif len(sys.argv) == 3:
    FOLDER = sys.argv[1]
    OPTION = sys.argv[2]

else:
    helpPDFtoFiles()

# assistance
if FOLDER == '-h' or FOLDER == "help":
    helpPDFtoFiles()

# cas de dossier invalide
elif checkFolderExist() == False:
    print("The \"" + FOLDER + "\" folder does not exist")
    print("For more information : python3 launch.py -h")

# cas d'option invalide
elif checkOption(OPTION) == False:
    print("Invalid option \"" + OPTION + "\"")
    print("For more information : python3 launch.py -h")

# cas valide
else:
    # Initialise la class ToFormat
    if OPTION == '-t':
        ToTXT.__init__(ToTXT, FOLDER)
        numberTotalFiles = len(ToTXT.files)
        ToTXT.allPDF(ToTXT, numberTotalFiles)
    else:
        ToXML.__init__(ToXML, FOLDER)
        numberTotalFiles = len(ToXML.files)
        ToXML.allPDF(ToXML, numberTotalFiles)

    finishMessage()
