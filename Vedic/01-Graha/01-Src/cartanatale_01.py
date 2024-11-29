import os
import sys
from termcolor import colored
from colorama import init, Fore, Back, Style

from load_graha import LoadGraha
from graha import Graha
from Tabellario import Tabellario
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
szMsgPrefix = " MAIN - "

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
print("Nome del file di input per Bhava" + sys.argv[4])
print("Nome del file di output:" + sys.argv[5])
print("Livello Log:" + sys.argv[6])

# Nome del file


inputCartaNatale  = sys.argv[1]
confGrahaFileName = sys.argv[2]
confRasiFileName  = sys.argv[3]
confBhavaFileName = sys.argv[4]
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



Log.scriviLog(9, szMsgPrefix + "**************************************************************")
Log.scriviLog(9, szMsgPrefix + "   Graha: " + inputCartaNatale )
Log.scriviLog(9, szMsgPrefix + "--------------------------------------------------------------")
Log.scriviLog(9, szMsgPrefix + "                      Carta Natale")
Log.scriviLog(9, szMsgPrefix + "**************************************************************")

#showCartaNatale(Log)
###########################################
# 02. Inizializzazione del Graha
###########################################

Log.scriviLog(9, szMsgPrefix + "***********************************************************")
Log.scriviLog(9, szMsgPrefix + "  01.00 - Caricamento dei dati relativi alla Carta Natale  ")
Log.scriviLog(9, szMsgPrefix + "***********************************************************")
#Caricamento dei GRAHA della carta natale passata
# Il caricamento viene effettuato nella lista lstGrahaCarta
LoadGrahaCarta = LoadGraha(Log, inputCartaNatale)
LoadGrahaCarta.loadGrahaFile()

#creazione del tabellario
Tab = Tabellario(Log, confGrahaFileName, confRasiFileName, confBhavaFileName)

# Creazione del Graha:
Log.scriviLog(9, szMsgPrefix + "**************************************")
Log.scriviLog(9, szMsgPrefix + "  02.00 - Inizio caricamento Graha ")
Log.scriviLog(9, szMsgPrefix + "***************************************\n\n")

lstGrahaList = []

lstGrahaList.append(Graha(Log, Tab, 0, LoadGrahaCarta.lstRasiProgr[0], LoadGrahaCarta.lstGrahaLng[0], LoadGrahaCarta.lstRetrogade[0]))
lstGrahaList.append(Graha(Log, Tab, 1, LoadGrahaCarta.lstRasiProgr[1], LoadGrahaCarta.lstGrahaLng[1], LoadGrahaCarta.lstRetrogade[1]))
lstGrahaList.append(Graha(Log, Tab, 2, LoadGrahaCarta.lstRasiProgr[2], LoadGrahaCarta.lstGrahaLng[2], LoadGrahaCarta.lstRetrogade[2]))
lstGrahaList.append(Graha(Log, Tab, 3, LoadGrahaCarta.lstRasiProgr[3], LoadGrahaCarta.lstGrahaLng[3], LoadGrahaCarta.lstRetrogade[3]))
lstGrahaList.append(Graha(Log, Tab, 4, LoadGrahaCarta.lstRasiProgr[4], LoadGrahaCarta.lstGrahaLng[4], LoadGrahaCarta.lstRetrogade[4]))
lstGrahaList.append(Graha(Log, Tab, 5, LoadGrahaCarta.lstRasiProgr[5], LoadGrahaCarta.lstGrahaLng[5], LoadGrahaCarta.lstRetrogade[5]))
lstGrahaList.append(Graha(Log, Tab, 6, LoadGrahaCarta.lstRasiProgr[6], LoadGrahaCarta.lstGrahaLng[6], LoadGrahaCarta.lstRetrogade[6]))
lstGrahaList.append(Graha(Log, Tab, 7, LoadGrahaCarta.lstRasiProgr[7], LoadGrahaCarta.lstGrahaLng[7], LoadGrahaCarta.lstRetrogade[7]))
lstGrahaList.append(Graha(Log, Tab, 8, LoadGrahaCarta.lstRasiProgr[8], LoadGrahaCarta.lstGrahaLng[8], LoadGrahaCarta.lstRetrogade[8]))
lstGrahaList.append(Graha(Log, Tab, 9, LoadGrahaCarta.lstRasiProgr[9], LoadGrahaCarta.lstGrahaLng[9], LoadGrahaCarta.lstRetrogade[9]))


for graha in lstGrahaList:
    graha.showGraha()
    if (graha.iGrahaProgr != 0):
        graha.showGrahaPict()


i=0
for graha in lstGrahaList:
    if(LoadGrahaCarta.getAscTrue()):
        if(i > 0):
            graha.setLonAssFromAscIntere(lstGrahaList[0].getLongitudeAssoluteIntere())
            graha.setBhavaIntere()
            graha.setLonAssFromAscPiene(lstGrahaList[0].getLongitudeAssolute())
            graha.setBhavaPiene()
            graha.setLonAssFromAscCusp(lstGrahaList[0].getLongitudeAssolute())
            graha.setBhavaCusp()
    lstCartaNatale = grahaInRasi(Log, lstCartaNatale, Tab.lstGrahaSmall[i], graha.getRasi(), graha.getLongitude(), graha.bRetrogade)
    Log.scriviLog(5, szMsgPrefix + "--------------------------------")
    i=i+1



Log.scriviLog(5, szMsgPrefix + "+--------------------------------+")
Log.scriviLog(5, szMsgPrefix + "|   Verifica dei Graha in Kopa   |")
Log.scriviLog(5, szMsgPrefix + "+--------------------------------+")

for i in range(2,8):
    checkIsKopa(Log,lstGrahaList[i], lstGrahaList[1].getLongitudeAssolute())

Log.scriviLog(5, szMsgPrefix + "+--------------------------------+")
Log.scriviLog(5, szMsgPrefix + "|   Verifica Guerra Planetaria   |")
Log.scriviLog(5, szMsgPrefix + "+--------------------------------+")
#Nella guerra planetaria la distanza deve essere max 1 grado
lstGrahaWar = checkIsPlanetWar(Log,
                 lstGrahaList[1].getLongitudeAssolute(),
                 lstGrahaList[2].getLongitudeAssolute(),
                 lstGrahaList[3].getLongitudeAssolute(),
                 lstGrahaList[4].getLongitudeAssolute(),
                 lstGrahaList[5].getLongitudeAssolute(),
                 lstGrahaList[6].getLongitudeAssolute(),
                 lstGrahaList[7].getLongitudeAssolute(),
                 lstGrahaList[8].getLongitudeAssolute(),
                 lstGrahaList[9].getLongitudeAssolute())

#print(lstGrahaWar)
#scrive il primo ed il secondo in lotta, indica il promo vincente sul secondo nelle note

for graha in lstGrahaWar:
    lstGrahaList[int(graha[0])].setPlanetWar()
    lstGrahaList[int(graha[1])].setPlanetWar()

if(LoadGrahaCarta.getAscTrue()):
    Log.scriviLog(2,  "+--------------------------------------------------+")
    Log.scriviLog(2,  "|   Calcolo Bhava  (Casa Intera, Piena e Cuspide)  |")
    Log.scriviLog(2,  "+--------------------------------------------------+")

    #inizializzazione delle Bhava
    lstBhavaCP = []
    lstBhavaCU = []
    lstBhavaCI = []

    for iBhava in range(1,13):
        lstBhavaDataCP = []
        lstBhavaDataCU = []
        lstBhavaDataCI = []
        for graha in lstGrahaList:
            Log.scriviLog(2, szMsgPrefix + "iBhava= " + str(iBhava) + ", graha:" + str(graha.getGrahaSmall()) + "  bhava del graha (CP)" + str(graha.getBhavaPiene()) + ", bhava del graha (CU):" + str(graha.getBhavaCusp()) + ", bhava del graha (CI):" + str(graha.getBhavaIntere()))
            if (int(graha.getBhavaIntere()) + 1 == int(iBhava) + 1):
                lstBhavaDataCI.append(graha.getGrahaProgr())
            if(int(graha.getBhavaPiene())+1 == int(iBhava)+1):
                lstBhavaDataCP.append(graha.getGrahaProgr())
                #print(lstBhavaDataCP)
            if(int(graha.getBhavaCusp())+1 == int(iBhava)+1):
                lstBhavaDataCU.append(graha.getGrahaProgr())
        lstBhavaCP.append(lstBhavaDataCP)
        lstBhavaCU.append(lstBhavaDataCU)
        lstBhavaCI.append(lstBhavaDataCI)

    lstBhavaCP[0].append(0)
    lstBhavaCU[0].append(0)
    lstBhavaCI[0].append(0)

    #Log.scriviLog(2, szMsgPrefix + "+-------------------------------------------------------+")
    #print(lstBhavaCP)
    #print(lstBhavaCU)
    #Log.scriviLog(2, szMsgPrefix + "+-------------------------------------------------------+")

    Log.scriviLog(9, szMsgPrefix + "      +--------------------------------------------------------+")
    Log.scriviLog(9, szMsgPrefix + "      | Calcolo delle Bhava con il principio delle Case Intere |")
    Log.scriviLog(9, szMsgPrefix + "      +--------------------------------------------------------+")

    i = 1
    for lstGrahaInBhava in lstBhavaCI:
        Log.scriviLog(9, szMsgPrefix + "........................ BHAVA " + str(i).rjust(2) + " ..................................")
        for grahaInBhava in lstGrahaInBhava:
            for graha in lstGrahaList:
                if (int(graha.getGrahaProgr()) == int(grahaInBhava)):
                    #Log.scriviLog(9, szMsgPrefix + "Bhava (" + str(i) + ") " + Tab.getBhavaSanscForProgr(int(i)) + " in (" + str(graha.getRasi()) + ") " + Tab.getRasiSanscForProgr(int(graha.getRasi())) + " con graha: " + graha.szGrahaSansc)
                    Log.scriviLog(9, szMsgPrefix + "Bhava (" + str(i).rjust(2) + ") " + Tab.getBhavaSanscForProgr(
                        int(i)).rjust(8) + " in (" + str(graha.getRasi()).rjust(2) + ") " + Tab.getRasiSanscForProgr(
                        int(graha.getRasi())).rjust(2) + " con graha: " + str(graha.szGrahaSansc).rjust(
                        2) + " Long: " + str(graha.getBhavaLonIntere()))
        i = i + 1

    print()

    Log.scriviLog(9, szMsgPrefix + "      +--------------------------------------------------------+")
    Log.scriviLog(9, szMsgPrefix + "      | Calcolo delle Bhava con il principio delle Case Piene  |")
    Log.scriviLog(9, szMsgPrefix + "      +--------------------------------------------------------+")


    i = 1
    for lstGrahaInBhava in lstBhavaCP:
        Log.scriviLog(9, szMsgPrefix + "........................ BHAVA " + str(i).rjust(2) + " ..................................")
        for grahaInBhava in lstGrahaInBhava:
            for graha in lstGrahaList:
                if(int(graha.getGrahaProgr()) == int(grahaInBhava)):
                    #Log.scriviLog(9, szMsgPrefix + "Bhava (" + str(i) + ") " + Tab.getBhavaSanscForProgr(int(i)) + " in (" + str(graha.getRasi()) + ") " + Tab.getRasiSanscForProgr(int(graha.getRasi())) + " con graha: " + graha.szGrahaSansc)
                    Log.scriviLog(9, szMsgPrefix + "Bhava (" + str(i).rjust(2) + ") " + Tab.getBhavaSanscForProgr(
                        int(i)).rjust(8) + " in (" + str(graha.getRasi()).rjust(2) + ") " + Tab.getRasiSanscForProgr(
                        int(graha.getRasi())).rjust(2) + " con graha: " + str(graha.szGrahaSansc).rjust(2) + " Long: " + str(graha.getBhavaLonPiene()))
        i=i+1

print()
if(LoadGrahaCarta.getAscTrue()):
    Log.scriviLog(9, szMsgPrefix + "      +--------------------------------------------------------+")
    Log.scriviLog(9, szMsgPrefix + "      | Calcolo delle Bhava con il principio delle Cuspidi     |")
    Log.scriviLog(9, szMsgPrefix + "      +--------------------------------------------------------+")

    i = 1
    for lstGrahaInBhava in lstBhavaCU:
        Log.scriviLog(9, szMsgPrefix + "........................ BHAVA " + str(i).rjust(2) + " ..................................")
        for grahaInBhava in lstGrahaInBhava:
            for graha in lstGrahaList:
                if(int(graha.getGrahaProgr()) == int(grahaInBhava)):
                    Log.scriviLog(9, szMsgPrefix + "Bhava (" + str(i).rjust(2) + ") " + Tab.getBhavaSanscForProgr(
                        int(i)).rjust(8) + " in (" + str(graha.getRasi()).rjust(2) + ") " + Tab.getRasiSanscForProgr(
                        int(graha.getRasi())).rjust(2) + " con graha: " + str(graha.szGrahaSansc).rjust(2) + " Long:" + str(graha.getBhavaLonCusp()))
                    #Log.scriviLog(9, szMsgPrefix + "Bhava (" + str(i) + ") " + Tab.getRasiSanscForProgr(int(i)) + " graha: " + graha.szGrahaSansc)

        i=i+1




showCartaNatale(Log, lstGrahaList[0], lstCartaNatale)
showGrahaDetail(Log, lstGrahaList)

