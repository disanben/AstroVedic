import os
import sys
from termcolor import colored
from colorama import init, Fore, Back, Style

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
init()
print(colored("hello", "red"), colored("world", "green"))
print(Fore.RED + 'some red text')
print(Fore.RED + Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
'''

#print(Fore.RED + Back.GREEN + 'and with a green background')
#print(Style.RESET_ALL)

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
print("Nome del file di input per Kopa:" + sys.argv[4])
print("Nome del file di output:" + sys.argv[5])
print("Livello Log:" + sys.argv[6])

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
confKopaFileName  = sys.argv[4]
outFileName       = sys.argv[5]
iPrioLog          = sys.argv[6]


###########################################
# 011. Creazione file di Output
###########################################

Log = LogCartaNatale(outFileName, iPrioLog)


###########################################
# 01. Verifica presenza del file di input
###########################################
if checkFilePresence(Log, inputCartaNatale, 1001):
   exit(1001)
if checkFilePresence(Log, confGrahaFileName, 1002):
   exit(1002)
if checkFilePresence(Log, confRasiFileName, 1003):
   exit(1003)
if checkFilePresence(Log, confKopaFileName, 1004):
   exit(1004)

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
#Fore.RED + Back.GREEN + Style.RESET_ALL
LoadGrahaCarta.getAscLong()
GrahaAsc = Graha(Log, confGrahaFileName, confRasiFileName, confKopaFileName,0, LoadGrahaCarta.getAscRasi(), LoadGrahaCarta.getAscLong(), "")

if(LoadGrahaCarta.getAscTrue()):
    lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaAsc.getGrahaSmall(), GrahaAsc.getRasi(), GrahaAsc.getLongitude() )
    #lstCartaNatale = grahaInRasi(Log, lstCartaNatale, Fore.RED + Back.GREEN + GrahaAsc.getGrahaSmall() + Fore.WHITE + Back.BLACK, GrahaAsc.getRasi(), GrahaAsc.getLongitude())

#LoadGrahaCarta.getSunLong()
GrahaSun = Graha(Log, confGrahaFileName, confRasiFileName, confKopaFileName,1, LoadGrahaCarta.getSunRasi(), LoadGrahaCarta.getSunLong(), LoadGrahaCarta.getSunRetro())
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaSun.getGrahaSmall(), GrahaSun.getRasi(), GrahaSun.getLongitude())

#LoadGrahaCarta.getMoonLong()
GrahaMoon = Graha(Log, confGrahaFileName, confRasiFileName, confKopaFileName,2, LoadGrahaCarta.getMoonRasi(), LoadGrahaCarta.getMoonLong(), LoadGrahaCarta.getMoonRetro())
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaMoon.getGrahaSmall(), GrahaMoon.getRasi(), GrahaMoon.getLongitude())

#LoadGrahaCarta.getMarsLong()
GrahaMars = Graha(Log, confGrahaFileName, confRasiFileName, confKopaFileName,3, LoadGrahaCarta.getMarsRasi(), LoadGrahaCarta.getMarsLong(), LoadGrahaCarta.getMarsRetro())
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaMars.getGrahaSmall(), GrahaMars.getRasi(), GrahaMars.getLongitude())

#LoadGrahaCarta.getMercuryLong()
GrahaMercury = Graha(Log, confGrahaFileName, confRasiFileName, confKopaFileName,4, LoadGrahaCarta.getMercuryRasi(), LoadGrahaCarta.getMercuryLong(), LoadGrahaCarta.getMercuryRetro())
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaMercury.getGrahaSmall(), GrahaMercury.getRasi(), GrahaMercury.getLongitude())

#LoadGrahaCarta.getJupiterLong()
GrahaJupiter = Graha(Log, confGrahaFileName, confRasiFileName, confKopaFileName,5, LoadGrahaCarta.getJupiterRasi(), LoadGrahaCarta.getJupiterLong(), LoadGrahaCarta.getJupiterRetro())
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaJupiter.getGrahaSmall(), GrahaJupiter.getRasi(), GrahaJupiter.getLongitude())

#LoadGrahaCarta.getVenusLong()
GrahaVenus = Graha(Log, confGrahaFileName, confRasiFileName, confKopaFileName,6, LoadGrahaCarta.getVenusRasi(), LoadGrahaCarta.getVenusLong(), LoadGrahaCarta.getVenusRetro())
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaVenus.getGrahaSmall(), GrahaVenus.getRasi(), GrahaVenus.getLongitude())

#LoadGrahaCarta.getSaturnLong()
GrahaSaturn = Graha(Log, confGrahaFileName, confRasiFileName, confKopaFileName,7, LoadGrahaCarta.getSaturnRasi(), LoadGrahaCarta.getSaturnLong(), LoadGrahaCarta.getSaturnRetro())
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaSaturn.getGrahaSmall(), GrahaSaturn.getRasi(), GrahaSaturn.getLongitude())

#LoadGrahaCarta.getRahuLong()
GrahaRahu = Graha(Log, confGrahaFileName, confRasiFileName, confKopaFileName,8, LoadGrahaCarta.getRahuRasi(), LoadGrahaCarta.getRahuLong(), LoadGrahaCarta.getRahuRetro())
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaRahu.getGrahaSmall(), GrahaRahu.getRasi(), GrahaRahu.getLongitude())

#LoadGrahaCarta.getKetuLong()
GrahaKetu = Graha(Log, confGrahaFileName, confRasiFileName, confKopaFileName,9, LoadGrahaCarta.getKetuRasi(), LoadGrahaCarta.getKetuLong(), LoadGrahaCarta.getKetuRetro())
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
