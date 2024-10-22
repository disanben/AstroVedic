import os
import sys
from termcolor import colored
from colorama import Fore, Back, Style

from load_graha import LoadGraha
from graha import Graha
from logCartaNatale import LogCartaNatale

from cartanatale_tools import *



# Formato file di input:
#  Campo 0: Nome Graha abbreviato
#  Campo 1: progressivo Graha
#  Campo 2: Nome Graha Sanscrito
#  Campo 3: Tipo di AK
#  Campo 4: Nome Rasi del Graha in forma abbreviata
#  Campo 5: Progressivo del Rasi
#  Campo 6: Longitudine del Graha
#  Campo 7: Nome Nakshatra
#  Campo 8: Progressivo Nakshatra
#  Campo 9: Reggente Nakshatra
#  Campo 10: Pada

#help_utente()

'''
print(colored("hello", "red"), colored("world", "green"))
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
'''

iPrioLog = 0
lstCartaNatale = []

'''
szCfgPath="..\\02-Cfg\\"
szInputFilePath="..\\11-DataInput\\"
szOutputFilePath="..\\12-CarteNataliOutput\\"
'''


print ("\n\n***********************************")
print ("    ELABORAZIONE GRAHA " + sys.argv[1] )
print ("***********************************")

print("Lista argomenti passati", sys.argv)
print("Nome del file di input per Carta Natale:" + sys.argv[1])
print("Nome del file di input per Graha:" + sys.argv[2])
print("Nome del file di input per Rasi:" + sys.argv[3])
print("Nome del file di output:" + sys.argv[4])
print("Livello Log:" + sys.argv[5])

# Nome del file

'''
inputCartaNatale = szInputFilePath + sys.argv[1]
confGrahaFileName = szCfgPath + sys.argv[2]
confRasiFileName  = szCfgPath + sys.argv[3]
outFileName   = szOutputFilePath + sys.argv[4]

print("Lista file")
print("Nome del file di input per Carta Natale:" + inputCartaNatale)
print("Nome del file di input per Graha:" + confGrahaFileName)
print("Nome del file di input per Rasi:" + confRasiFileName)
print("Nome del file di output:" + outFileName)
'''

inputCartaNatale  = sys.argv[1]
confGrahaFileName = sys.argv[2]
confRasiFileName  = sys.argv[3]
outFileName       =  sys.argv[4]
iPrioLog          = sys.argv[5]

###########################################
# 01. Verifica presenza del file di input
###########################################
if not os.path.isfile(inputCartaNatale):
   print("File " + inputCartaNatale + " non trovato!")
   exit(101)
if not os.path.isfile(confGrahaFileName):
   print("File " + confGrahaFileName + " non trovato!")
   exit(102)
if not os.path.isfile(confRasiFileName):
   print("File " + confRasiFileName + " non trovato!")
   exit(103)

#lstGrahaProgr = []
#lstGrahaSansc = []
#lstTipoAK = []
#lstRasiSmall = []
#lstRasiProgr = []
#lstGrahaLng = []
#lstNakName = []
#lstNakProgr = []
#lstNakReg = []
#lstNakPada = []

###########################################
# 011. Creazione file di Output
###########################################

Log = LogCartaNatale(outFileName, iPrioLog)


Log.scriviLog(9, "**************************************************************")
Log.scriviLog(9, "   Graha: " + inputCartaNatale )
Log.scriviLog(9, "--------------------------------------------------------------")
Log.scriviLog(9, "                      Carta Natale")
Log.scriviLog(9, "**************************************************************")

#showCartaNatale(Log)
###########################################
# 02. Inizializzazione del Graha
###########################################


#Caricamento dei GRAHA
# Il caricamento viene effettuato nella lista lstGraha
LoadGrahaCarta = LoadGraha(Log, inputCartaNatale)
LoadGrahaCarta.loadGrahaFile()


'''
print("##############################")
print("   Lista GrahaSmall", LoadGrahaCarta.getLstGrahaSmall())

print("##############################")
print("   Lista GrahaProgr", LoadGrahaCarta.getLstGrahaProgr())

print("##############################")
print("   Lista lstGrahaSansc", LoadGrahaCarta.getLstGrahaSansc())

print("##############################")
print("   Lista lstTipoAK", LoadGrahaCarta.getLstTipoAK())

print("##############################")
print("   Lista lstRasiSmall", LoadGrahaCarta.getLstRasiSmall())

print("##############################")
print("   Lista lstRasiProgr", LoadGrahaCarta.getLstRasiProgr())

print("##############################")
print("   Lista lstGrahaLng", LoadGrahaCarta.getLstGrahaLng())

print("##############################")
print("   Lista lstNakName", LoadGrahaCarta.getLstNakName())

print("##############################")
print("   Lista lstNakProgr", LoadGrahaCarta.getLstNakProgr())

print("##############################")
print("   Lista lstNakReg", LoadGrahaCarta.getLstNakReg())

print("##############################")
print("   Lista lstNakPada", LoadGrahaCarta.getLstNakPada())
'''

# Creazione del Graha:
# - Nome
# - Rasi
# - Longitudine


Log.scriviLog(5, "Inizio caricamento Graha")

#if(LoadGrahaCarta.getAscTrue()):
LoadGrahaCarta.getAscLong()
GrahaAsc = Graha(Log, confGrahaFileName, confRasiFileName, 0, LoadGrahaCarta.getAscRasi(), LoadGrahaCarta.getAscLong())

if(LoadGrahaCarta.getAscTrue()):
    lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaAsc.getGrahaSmall(), GrahaAsc.getRasi(), GrahaAsc.getLongitude())

LoadGrahaCarta.getSunLong()
GrahaSun = Graha(Log, confGrahaFileName, confRasiFileName, 1, LoadGrahaCarta.getSunRasi(), LoadGrahaCarta.getSunLong())
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaSun.getGrahaSmall(), GrahaSun.getRasi(), GrahaSun.getLongitude())

LoadGrahaCarta.getMoonLong()
GrahaMoon = Graha(Log, confGrahaFileName, confRasiFileName, 2, LoadGrahaCarta.getMoonRasi(), LoadGrahaCarta.getMoonLong())
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaMoon.getGrahaSmall(), GrahaMoon.getRasi(), GrahaMoon.getLongitude())

LoadGrahaCarta.getMarsLong()
GrahaMars = Graha(Log, confGrahaFileName, confRasiFileName, 3, LoadGrahaCarta.getMarsRasi(), LoadGrahaCarta.getMarsLong())
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaMars.getGrahaSmall(), GrahaMars.getRasi(), GrahaMars.getLongitude())

LoadGrahaCarta.getMercuryLong()
GrahaMercury = Graha(Log, confGrahaFileName, confRasiFileName, 4, LoadGrahaCarta.getMercuryRasi(), LoadGrahaCarta.getMercuryLong())
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaMercury.getGrahaSmall(), GrahaMercury.getRasi(), GrahaMercury.getLongitude())

LoadGrahaCarta.getJupiterLong()
GrahaJupiter = Graha(Log, confGrahaFileName, confRasiFileName, 5, LoadGrahaCarta.getJupiterRasi(), LoadGrahaCarta.getJupiterLong())
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaJupiter.getGrahaSmall(), GrahaJupiter.getRasi(), GrahaJupiter.getLongitude())

LoadGrahaCarta.getVenusLong()
GrahaVenus = Graha(Log, confGrahaFileName, confRasiFileName, 6, LoadGrahaCarta.getVenusRasi(), LoadGrahaCarta.getVenusLong())
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaVenus.getGrahaSmall(), GrahaVenus.getRasi(), GrahaVenus.getLongitude())

LoadGrahaCarta.getSaturnLong()
GrahaSaturn = Graha(Log, confGrahaFileName, confRasiFileName, 7, LoadGrahaCarta.getSaturnRasi(), LoadGrahaCarta.getSaturnLong())
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaSaturn.getGrahaSmall(), GrahaSaturn.getRasi(), GrahaSaturn.getLongitude())

LoadGrahaCarta.getRahuLong()
GrahaRahu = Graha(Log, confGrahaFileName, confRasiFileName, 8, LoadGrahaCarta.getRahuRasi(), LoadGrahaCarta.getRahuLong())
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaRahu.getGrahaSmall(), GrahaRahu.getRasi(), GrahaRahu.getLongitude())

LoadGrahaCarta.getKetuLong()
GrahaKetu = Graha(Log, confGrahaFileName, confRasiFileName, 9, LoadGrahaCarta.getKetuRasi(), LoadGrahaCarta.getKetuLong())
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaKetu.getGrahaSmall(), GrahaKetu.getRasi(), GrahaKetu.getLongitude())

'''
GrahaAsc.showGrahaPict()
GrahaSun.showGrahaPict()
GrahaMoon.showGrahaPict()
GrahaMars.showGrahaPict()
GrahaMercury.showGrahaPict()
GrahaJupiter.showGrahaPict()
GrahaVenus.showGrahaPict()
GrahaRahu.showGrahaPict()
GrahaKetu.showGrahaPict()
'''

showCartaNatale(Log, GrahaAsc, lstCartaNatale)

showGrahaDetail(Log,GrahaAsc,GrahaSun,GrahaMoon,GrahaMars,GrahaMercury,GrahaJupiter,GrahaVenus,GrahaSaturn,GrahaRahu,GrahaKetu)
