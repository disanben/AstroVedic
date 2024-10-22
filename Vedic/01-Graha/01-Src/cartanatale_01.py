import os
import sys

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

iPrioLog = 9
lstCartaNatale = []

print ("\n\n***********************************")
print ("    ELABORAZIONE GRAHA " + sys.argv[1] )
print ("***********************************")

print("Lista argomenti passati", sys.argv)
print("Nome del file di input per Carta Natale:" + sys.argv[1])
print("Nome del file di input per Graha:" + sys.argv[2])
print("Nome del file di input per Rasi:" + sys.argv[3])
print("Nome del file di output:" + sys.argv[4])
# Nome del file


inputCartaNatale = sys.argv[1]
confGrahaFileName = sys.argv[2]
confRasiFileName  = sys.argv[3]
outFileName   = sys.argv[4]

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


Log.scriviLog(9, "***********************************")
Log.scriviLog(9, "***  Graha di " + inputCartaNatale + " ***")
Log.scriviLog(9, "***********************************")
Log.scriviLog(9, "         -- Carta Natale --")
Log.scriviLog(9, "***********************************")

#showCartaNatale(Log)
###########################################
# 02. Inizializzazione del Graha
###########################################


#Caricamento dei GRAHA
# Il caricamento viene effettuato nella lista lstGraha
LoadGrahaMarco = LoadGraha(Log, inputCartaNatale)
LoadGrahaMarco.loadGrahaFile()


'''
print("##############################")
print("   Lista GrahaSmall", LoadGrahaMarco.getLstGrahaSmall())

print("##############################")
print("   Lista GrahaProgr", LoadGrahaMarco.getLstGrahaProgr())

print("##############################")
print("   Lista lstGrahaSansc", LoadGrahaMarco.getLstGrahaSansc())

print("##############################")
print("   Lista lstTipoAK", LoadGrahaMarco.getLstTipoAK())

print("##############################")
print("   Lista lstRasiSmall", LoadGrahaMarco.getLstRasiSmall())

print("##############################")
print("   Lista lstRasiProgr", LoadGrahaMarco.getLstRasiProgr())

print("##############################")
print("   Lista lstGrahaLng", LoadGrahaMarco.getLstGrahaLng())

print("##############################")
print("   Lista lstNakName", LoadGrahaMarco.getLstNakName())

print("##############################")
print("   Lista lstNakProgr", LoadGrahaMarco.getLstNakProgr())

print("##############################")
print("   Lista lstNakReg", LoadGrahaMarco.getLstNakReg())

print("##############################")
print("   Lista lstNakPada", LoadGrahaMarco.getLstNakPada())
'''

# Creazione del Graha:
# - Nome
# - Rasi
# - Longitudine


Log.scriviLog(5, "Inizio caricamento Graha")

LoadGrahaMarco.getAscLong()
GrahaAsc = Graha(Log, confGrahaFileName, confRasiFileName, 0, LoadGrahaMarco.getAscRasi(), LoadGrahaMarco.getAscLong())
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaAsc.getGrahaSmall(), GrahaAsc.getRasi(), GrahaAsc.getLongitude())

LoadGrahaMarco.getSunLong()
GrahaSun = Graha(Log, confGrahaFileName, confRasiFileName, 1, LoadGrahaMarco.getSunRasi(), LoadGrahaMarco.getSunLong())
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaSun.getGrahaSmall(), GrahaSun.getRasi(), GrahaSun.getLongitude())

LoadGrahaMarco.getMoonLong()
GrahaMoon = Graha(Log, confGrahaFileName, confRasiFileName, 2, LoadGrahaMarco.getMoonRasi(), LoadGrahaMarco.getMoonLong())
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaMoon.getGrahaSmall(), GrahaMoon.getRasi(), GrahaMoon.getLongitude())

LoadGrahaMarco.getMarsLong()
GrahaMars = Graha(Log, confGrahaFileName, confRasiFileName, 3, LoadGrahaMarco.getMarsRasi(), LoadGrahaMarco.getMarsLong())
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaMars.getGrahaSmall(), GrahaMars.getRasi(), GrahaMars.getLongitude())

LoadGrahaMarco.getMercuryLong()
GrahaMercury = Graha(Log, confGrahaFileName, confRasiFileName, 4, LoadGrahaMarco.getMercuryRasi(), LoadGrahaMarco.getMercuryLong())
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaMercury.getGrahaSmall(), GrahaMercury.getRasi(), GrahaMercury.getLongitude())

LoadGrahaMarco.getJupiterLong()
GrahaJupiter = Graha(Log, confGrahaFileName, confRasiFileName, 5, LoadGrahaMarco.getJupiterRasi(), LoadGrahaMarco.getJupiterLong())
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaJupiter.getGrahaSmall(), GrahaJupiter.getRasi(), GrahaJupiter.getLongitude())

LoadGrahaMarco.getVenusLong()
GrahaVenus = Graha(Log, confGrahaFileName, confRasiFileName, 6, LoadGrahaMarco.getVenusRasi(), LoadGrahaMarco.getVenusLong())
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaVenus.getGrahaSmall(), GrahaVenus.getRasi(), GrahaVenus.getLongitude())

LoadGrahaMarco.getSaturnLong()
GrahaSaturn = Graha(Log, confGrahaFileName, confRasiFileName, 7, LoadGrahaMarco.getSaturnRasi(), LoadGrahaMarco.getSaturnLong())
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaSaturn.getGrahaSmall(), GrahaSaturn.getRasi(), GrahaSaturn.getLongitude())

LoadGrahaMarco.getRahuLong()
GrahaRahu = Graha(Log, confGrahaFileName, confRasiFileName, 8, LoadGrahaMarco.getRahuRasi(), LoadGrahaMarco.getRahuLong())
lstCartaNatale = grahaInRasi(Log, lstCartaNatale, GrahaRahu.getGrahaSmall(), GrahaRahu.getRasi(), GrahaRahu.getLongitude())

LoadGrahaMarco.getKetuLong()
GrahaKetu = Graha(Log, confGrahaFileName, confRasiFileName, 9, LoadGrahaMarco.getKetuRasi(), LoadGrahaMarco.getKetuLong())
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
