import os
import sys
from termcolor import colored
from colorama import init, Fore, Back, Style

from load_graha import LoadGraha
from graha import Graha
from logCartaNatale import LogCartaNatale

from cartanatale_tools import *



# Formato file di input:
#  Campo  0: Nome Graha abbreviato
#  Campo  1: progressivo Graha
#  Campo  2: Nome Graha Sanscrito
#  Campo  3: Tipo di AK
#  Campo  4: Nome Rasi del Graha in forma abbreviata
#  Campo  5: Progressivo del Rasi
#  Campo  6: Longitudine del Graha
#  Campo  7: Nome Nakshatra
#  Campo  8: Progressivo Nakshatra
#  Campo  9: Reggente Nakshatra
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

lstCartaNatale = []

'''
szCfgPath="..\\02-Cfg\\"
szInputFilePath="..\\11-DataInput\\"
szOutputFilePath="..\\12-CarteNataliOutput\\"
'''

print ("\n\n")
print ("***********************************************")
print ("    ELABORAZIONE GRAHA " + sys.argv[1] )
print ("***********************************************")

print("Lista argomenti passati", sys.argv)
print("Nome del file di input per Carta Natale:" + sys.argv[1])
print("Nome del file di input per Graha:" + sys.argv[2])
print("Nome del file di input per Rasi:" + sys.argv[3])
#print("Nome del file di input per Kopa:" + sys.argv[4])
print("Nome del file di output:" + sys.argv[4])
print("Livello Log:" + sys.argv[5])

# Nome del file


inputCartaNatale  = sys.argv[1]
confGrahaFileName = sys.argv[2]
confRasiFileName  = sys.argv[3]
outFileName       = sys.argv[4]
iPrioLog          = sys.argv[5]


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



Log.scriviLog(9, "**************************************************************")
Log.scriviLog(9, "   Graha: " + inputCartaNatale )
Log.scriviLog(9, "--------------------------------------------------------------")
Log.scriviLog(9, "                      Carta Natale")
Log.scriviLog(9, "**************************************************************")

#showCartaNatale(Log)
###########################################
# 02. Inizializzazione del Graha
###########################################


#Caricamento dei GRAHA della carta natale passata
# Il caricamento viene effettuato nella lista lstGrahaCarta
LoadGrahaCarta = LoadGraha(Log, inputCartaNatale)
LoadGrahaCarta.loadGrahaFile()

# Creazione del Graha:
Log.scriviLog(5, "Inizio caricamento Graha")
LoadGrahaCarta.getAscLong()
GrahaAsc = Graha(Log, confGrahaFileName, confRasiFileName,0, LoadGrahaCarta.getAscRasi(), LoadGrahaCarta.getAscLong(), "")

if(LoadGrahaCarta.getAscTrue()):
    lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaAsc.getGrahaSmall(), GrahaAsc.getRasi(), GrahaAsc.getLongitude() )
    #lstCartaNatale = grahaInRasi(Log, lstCartaNatale, Fore.RED + Back.GREEN + GrahaAsc.getGrahaSmall() + Fore.WHITE + Back.BLACK, GrahaAsc.getRasi(), GrahaAsc.getLongitude())

Log.scriviLog(5, "\n")
GrahaSun = Graha(Log, confGrahaFileName, confRasiFileName,1, LoadGrahaCarta.getSunRasi(), LoadGrahaCarta.getSunLong(), LoadGrahaCarta.getSunRetro())
GrahaSun.setLonAssFromAsc(GrahaAsc.getLongitudeAssolute())
GrahaSun.setBhava()
GrahaSun.setLonAssFromAscCusp(GrahaAsc.getLongitudeAssolute())
GrahaSun.setBhavaCusp()
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaSun.getGrahaSmall(), GrahaSun.getRasi(), GrahaSun.getLongitude())

Log.scriviLog(5, "\n")
GrahaMoon = Graha(Log, confGrahaFileName, confRasiFileName, 2, LoadGrahaCarta.getMoonRasi(), LoadGrahaCarta.getMoonLong(), LoadGrahaCarta.getMoonRetro())
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaMoon.getGrahaSmall(), GrahaMoon.getRasi(), GrahaMoon.getLongitude())
GrahaMoon.setLonAssFromAsc(GrahaAsc.getLongitudeAssolute())
GrahaMoon.setBhava()
GrahaMoon.setLonAssFromAscCusp(GrahaAsc.getLongitudeAssolute())
GrahaMoon.setBhavaCusp()

Log.scriviLog(5, "\n")
GrahaMars = Graha(Log, confGrahaFileName, confRasiFileName, 3, LoadGrahaCarta.getMarsRasi(), LoadGrahaCarta.getMarsLong(), LoadGrahaCarta.getMarsRetro())
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaMars.getGrahaSmall(), GrahaMars.getRasi(), GrahaMars.getLongitude())
GrahaMars.setLonAssFromAsc(GrahaAsc.getLongitudeAssolute())
GrahaMars.setBhava()
GrahaMars.setLonAssFromAscCusp(GrahaAsc.getLongitudeAssolute())
GrahaMars.setBhavaCusp()

Log.scriviLog(5, "\n")
GrahaMercury = Graha(Log, confGrahaFileName, confRasiFileName,4, LoadGrahaCarta.getMercuryRasi(), LoadGrahaCarta.getMercuryLong(), LoadGrahaCarta.getMercuryRetro())
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaMercury.getGrahaSmall(), GrahaMercury.getRasi(), GrahaMercury.getLongitude())
GrahaMercury.setLonAssFromAsc(GrahaAsc.getLongitudeAssolute())
GrahaMercury.setBhava()
GrahaMercury.setLonAssFromAscCusp(GrahaAsc.getLongitudeAssolute())
GrahaMercury.setBhavaCusp()

Log.scriviLog(5, "\n")
GrahaJupiter = Graha(Log, confGrahaFileName, confRasiFileName, 5, LoadGrahaCarta.getJupiterRasi(), LoadGrahaCarta.getJupiterLong(), LoadGrahaCarta.getJupiterRetro())
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaJupiter.getGrahaSmall(), GrahaJupiter.getRasi(), GrahaJupiter.getLongitude())
GrahaJupiter.setLonAssFromAsc(GrahaAsc.getLongitudeAssolute())
GrahaJupiter.setBhava()
GrahaJupiter.setLonAssFromAscCusp(GrahaAsc.getLongitudeAssolute())
GrahaJupiter.setBhavaCusp()

Log.scriviLog(5, "\n")
GrahaVenus = Graha(Log, confGrahaFileName, confRasiFileName, 6, LoadGrahaCarta.getVenusRasi(), LoadGrahaCarta.getVenusLong(), LoadGrahaCarta.getVenusRetro())
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaVenus.getGrahaSmall(), GrahaVenus.getRasi(), GrahaVenus.getLongitude())
GrahaVenus.setLonAssFromAsc(GrahaAsc.getLongitudeAssolute())
GrahaVenus.setBhava()
GrahaVenus.setLonAssFromAscCusp(GrahaAsc.getLongitudeAssolute())
GrahaVenus.setBhavaCusp()

Log.scriviLog(5, "\n")
GrahaSaturn = Graha(Log, confGrahaFileName, confRasiFileName, 7, LoadGrahaCarta.getSaturnRasi(), LoadGrahaCarta.getSaturnLong(), LoadGrahaCarta.getSaturnRetro())
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaSaturn.getGrahaSmall(), GrahaSaturn.getRasi(), GrahaSaturn.getLongitude())
GrahaSaturn.setLonAssFromAsc(GrahaAsc.getLongitudeAssolute())
GrahaSaturn.setBhava()
GrahaSaturn.setLonAssFromAscCusp(GrahaAsc.getLongitudeAssolute())
GrahaSaturn.setBhavaCusp()

Log.scriviLog(5, "\n")
GrahaRahu = Graha(Log, confGrahaFileName, confRasiFileName, 8, LoadGrahaCarta.getRahuRasi(), LoadGrahaCarta.getRahuLong(), LoadGrahaCarta.getRahuRetro())
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaRahu.getGrahaSmall(), GrahaRahu.getRasi(), GrahaRahu.getLongitude())
GrahaRahu.setLonAssFromAsc(GrahaAsc.getLongitudeAssolute())
GrahaRahu.setBhava()
GrahaRahu.setLonAssFromAscCusp(GrahaAsc.getLongitudeAssolute())
GrahaRahu.setBhavaCusp()

Log.scriviLog(5, "\n")
GrahaKetu = Graha(Log, confGrahaFileName, confRasiFileName, 9, LoadGrahaCarta.getKetuRasi(), LoadGrahaCarta.getKetuLong(), LoadGrahaCarta.getKetuRetro())
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaKetu.getGrahaSmall(), GrahaKetu.getRasi(), GrahaKetu.getLongitude())
GrahaKetu.setLonAssFromAsc(GrahaAsc.getLongitudeAssolute())
GrahaKetu.setBhava()
GrahaKetu.setLonAssFromAscCusp(GrahaAsc.getLongitudeAssolute())
GrahaKetu.setBhavaCusp()

Log.scriviLog(5, "+--------------------------------+")
Log.scriviLog(5, "|   Verifica dei Graha in Kopa   |")
Log.scriviLog(5, "+--------------------------------+")

checkIsKopa(Log,GrahaMoon, GrahaSun.getLongitudeAssolute())
checkIsKopa(Log,GrahaMars, GrahaSun.getLongitudeAssolute())
checkIsKopa(Log,GrahaMercury, GrahaSun.getLongitudeAssolute())
checkIsKopa(Log,GrahaVenus, GrahaSun.getLongitudeAssolute())
checkIsKopa(Log,GrahaJupiter, GrahaSun.getLongitudeAssolute())
checkIsKopa(Log,GrahaSaturn, GrahaSun.getLongitudeAssolute())

Log.scriviLog(5, "+--------------------------------+")
Log.scriviLog(5, "|   Verifica Guerra Planetaria   |")
Log.scriviLog(5, "+--------------------------------+")
#Nella guerra planetaria la distanza deve essere max 1 grado
lstGrahaWar = checkIsPlanetWar(Log,
                 GrahaSun.getLongitudeAssolute(),
                 GrahaMoon.getLongitudeAssolute(),
                 GrahaMars.getLongitudeAssolute(),
                 GrahaMercury.getLongitudeAssolute(),
                 GrahaJupiter.getLongitudeAssolute(),
                 GrahaVenus.getLongitudeAssolute(),
                 GrahaSaturn.getLongitudeAssolute(),
                 GrahaRahu.getLongitudeAssolute(),
                 GrahaKetu.getLongitudeAssolute())

print(lstGrahaWar)
#scrive il primo ed il secondo in lotta, indica il promo vincente sul secondo nelle note
for graha in lstGrahaWar:
    print(graha[0] + " - " + graha[1])
    match int(graha[0]):
        case 2:
            GrahaSun.setPlanetWar()
        case 3:
            GrahaMoon.setPlanetWar()
        case 4:
            GrahaMars.setPlanetWar()
        case 5:
            GrahaMercury.setPlanetWar()
        case 6:
            GrahaJupiter.setPlanetWar()
        case 7:
            GrahaVenus.setPlanetWar()
        case 8:
            GrahaSaturn.setPlanetWar()
        case 9:
            GrahaRahu.setPlanetWar()
        case 9:
            GrahaKetu.setPlanetWar()

    match int(graha[1]):
        case 2:
            GrahaSun.setPlanetWar()
        case 3:
            GrahaMoon.setPlanetWar()
        case 4:
            GrahaMars.setPlanetWar()
        case 5:
            GrahaMercury.setPlanetWar()
        case 6:
            GrahaJupiter.setPlanetWar()
        case 7:
            GrahaVenus.setPlanetWar()
        case 8:
            GrahaSaturn.setPlanetWar()
        case 9:
            GrahaRahu.setPlanetWar()
        case 9:
            GrahaKetu.setPlanetWar()


putGrahaInBavha(Log,GrahaAsc,GrahaSun,GrahaMoon,GrahaMars,GrahaMercury,GrahaJupiter,GrahaVenus,GrahaSaturn,GrahaRahu,GrahaKetu)


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
