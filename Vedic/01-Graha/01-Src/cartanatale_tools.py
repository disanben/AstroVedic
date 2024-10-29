import os
import sys
from pickle import FALSE

from colorama import init, Fore, Back, Style

from load_graha import LoadGraha
from graha import Graha
from logCartaNatale import LogCartaNatale


from termcolor import colored

lstMesa = []
lstVrsabha = []
lstMithuna = []
lstKarkata = []
lstSimha = []
lstKania = []
lstTula = []
lstVrscika = []
lstDhanus = []
lstMakara = []
lstKumbha = []
lstMina = []

lstPlanetWar = []

lstLinetoPrint = []



def help_utente():
    print("\n\n")
    print("+-------------------------+")
    print("|      Manuale utente     |")
    print("+-------------------------+")

def checkFilePresence(Log, szFileName, iErr):
    if not os.path.isfile(szFileName):
        Log.scriviLog(9, "File " + szFileName + " non trovato!")
        return True
    return False


def showCartaNatale(Log, GrahaAsc, lstCartaNatale):
    init()
    Log.scriviLog(5, "Inizio caricamento Carta Natale")
    Log.scriviLog(2, str(lstCartaNatale))

    szRetrSym = "__ "
    szMesaGrahaRetr = ""
    szMesaGrahaSmall = ""
    szMesaGrahaLon = ""

    szVrsabhaGrahaRetr = ""
    szVrsabhaGrahaSmall = ""
    szVrsabhaGrahaLon = ""

    szMithunaGrahaRetr = ""
    szMithunaGrahaSmall = ""
    szMithunaGrahaLon = ""

    szKarkataGrahaRetr = ""
    szKarkataGrahaSmall = ""
    szKarkataGrahaLon = ""

    szSimhaGrahaRetr= ""
    szSimhaGrahaSmall = ""
    szSimhaGrahaLon = ""

    szKaniaGrahaRetr = ""
    szKaniaGrahaSmall = ""
    szKaniaGrahaLon = ""

    szTulaGrahaRetr = ""
    szTulaGrahaSmall = ""
    szTulaGrahaLon = ""

    szVriscikaGrahaRetr = ""
    szVriscikaGrahaSmall = ""
    szVriscikaGrahaLon = ""

    szDhanusGrahaRetr = ""
    szDhanusGrahaSmall = ""
    szDhanusGrahaLon = ""

    szMakaraGrahaRetr = ""
    szMakaraGrahaSmall = ""
    szMakaraGrahaLon = ""

    szKumbaGrahaRetr = ""
    szKumbaGrahaSmall = ""
    szKumbaGrahaLon = ""

    szMinaGrahaRetr = ""
    szMinaGrahaSmall = ""
    szMinaGrahaLon = ""

    for rasi in range(12):
        Log.scriviLog(5, "Num graha in " + GrahaAsc.Tab.lstRasiSansc[rasi] + ": " + str(len(lstCartaNatale[rasi])))
        for graha in lstCartaNatale[rasi]:
            #lstCartaNatale = ["Mesa","Vrsabha","Mithuna","Karkata","Simha","Kania","Tula","Vrscika","Dhanus","Makara","Kumbha","Mina"]
            Log.scriviLog(5, "   " + graha[0] + " - Lon = " + str(graha[1]) )
            if(graha[0] == 'AS'):
                graha[0] = graha[0]
                #graha[0] = Fore.RED + graha[0] + Style.RESET_ALL
                # Fore.RED +  + Style.RESET_ALL).rjust(12)
            match (rasi+1):
                case 1:
                    if(graha[2]):
                        szMesaGrahaRetr = szMesaGrahaRetr + szRetrSym
                    else:
                        szMesaGrahaRetr = szMesaGrahaRetr + "   "
                    szMesaGrahaSmall = str(szMesaGrahaSmall + graha[0] + " ")
                    szMesaGrahaLon  = szMesaGrahaLon + str(int(float(graha[1]))).zfill(2) + " "
			        #print(Style.RESET_ALL)
                    Log.scriviLog(2, "      Aggiunto in Mesa: " + szMesaGrahaRetr)
                    Log.scriviLog(2, "      Aggiunto in Mesa: " + szMesaGrahaSmall)
                    Log.scriviLog(2, "      Aggiunto in Mesa: " + szMesaGrahaLon)
                case 2:
                    if(graha[2]):
                        szVrsabhaGrahaRetr = szVrsabhaGrahaRetr + szRetrSym
                    else:
                        szVrsabhaGrahaRetr = szVrsabhaGrahaRetr + "   "
                    szVrsabhaGrahaSmall = str(szVrsabhaGrahaSmall + graha[0] + " ")
                    szVrsabhaGrahaLon  = szVrsabhaGrahaLon + str(int(float(graha[1]))).zfill(2) + " "
                    Log.scriviLog(2, "      Aggiunto in Vrsabha: " + szVrsabhaGrahaRetr)
                    Log.scriviLog(2, "      Aggiunto in Vrsabha: " + szVrsabhaGrahaSmall)
                    Log.scriviLog(2, "      Aggiunto in Vrsabha: " + szVrsabhaGrahaLon)
                case 3:
                    if(graha[2]):
                        szMithunaGrahaRetr = szMithunaGrahaRetr + szRetrSym
                    else:
                        szMithunaGrahaRetr = szMithunaGrahaRetr + "   "
                    szMithunaGrahaSmall = str(szMithunaGrahaSmall + graha[0] + " ")
                    szMithunaGrahaLon  = szMithunaGrahaLon + str(int(float(graha[1]))).zfill(2) + " "
                    Log.scriviLog(2, "      Aggiunto in Mithuna: " + szMithunaGrahaRetr)
                    Log.scriviLog(2, "      Aggiunto in Mithuna: " + szMithunaGrahaSmall)
                    Log.scriviLog(2, "      Aggiunto in Mithuna: " + szMithunaGrahaLon)
                case 4:
                    if(graha[2]):
                        szKarkataGrahaRetr = szKarkataGrahaRetr + szRetrSym
                    else:
                        szKarkataGrahaRetr = szKarkataGrahaRetr + "   "
                    szKarkataGrahaSmall = str(szKarkataGrahaSmall + graha[0] + " ")
                    szKarkataGrahaLon  = szKarkataGrahaLon + str(int(float(graha[1]))).zfill(2) + " "
                    Log.scriviLog(2, "      Aggiunto in Karkata: " + szKarkataGrahaRetr)
                    Log.scriviLog(2, "      Aggiunto in Karkata: " + szKarkataGrahaSmall)
                    Log.scriviLog(2, "      Aggiunto in Karkata: " + szKarkataGrahaLon)
                case 5:
                    if(graha[2]):
                        szSimhaGrahaRetr = szSimhaGrahaRetr + szRetrSym
                    else:
                        szSimhaGrahaRetr = szSimhaGrahaRetr + "   "
                    szSimhaGrahaSmall = str(szSimhaGrahaSmall + graha[0] + " ")
                    szSimhaGrahaLon  = szSimhaGrahaLon + str(int(float(graha[1]))).zfill(2) + " "
                    Log.scriviLog(2, "      Aggiunto in Simha: " + szSimhaGrahaRetr)
                    Log.scriviLog(2, "      Aggiunto in Simha: " + szSimhaGrahaSmall)
                    Log.scriviLog(2, "      Aggiunto in Simha: " + szSimhaGrahaLon)
                case 6:
                    if(graha[2]):
                        szKaniaGrahaRetr = szKaniaGrahaRetr + szRetrSym
                    else:
                        szKaniaGrahaRetr = szKaniaGrahaRetr + "   "
                    szKaniaGrahaSmall = str(szKaniaGrahaSmall + graha[0] + " ")
                    szKaniaGrahaLon  = szKaniaGrahaLon + str(int(float(graha[1]))).zfill(2) + " "
                    Log.scriviLog(2, "      Aggiunto in Kania: " + szKaniaGrahaRetr)
                    Log.scriviLog(2, "      Aggiunto in Kania: " + szKaniaGrahaSmall)
                    Log.scriviLog(2, "      Aggiunto in Kania: " + szKaniaGrahaLon)
                case 7:
                    if(graha[2]):
                        szTulaGrahaRetr = szTulaGrahaRetr + szRetrSym
                    else:
                        szTulaGrahaRetr = szTulaGrahaRetr + "   "
                    szTulaGrahaSmall = str(szTulaGrahaSmall + graha[0] + " ")
                    szTulaGrahaLon  = szTulaGrahaLon + str(int(float(graha[1]))).zfill(2) + " "
                    Log.scriviLog(2, "      Aggiunto in Tula: " + szTulaGrahaRetr)
                    Log.scriviLog(2, "      Aggiunto in Tula: " + szTulaGrahaSmall)
                    Log.scriviLog(2, "      Aggiunto in Tula: " + szTulaGrahaLon)
                case 8:
                    if(graha[2]):
                        szVriscikaGrahaRetr = szVriscikaGrahaRetr + szRetrSym
                    else:
                        szVriscikaGrahaRetr = szVriscikaGrahaRetr + "   "
                    szVriscikaGrahaSmall = str(szVriscikaGrahaSmall + graha[0] + " ")
                    szVriscikaGrahaLon  = szVriscikaGrahaLon + str(int(float(graha[1]))).zfill(2) + " "
                    Log.scriviLog(2, "      Aggiunto in Vriscika: " + szVriscikaGrahaRetr)
                    Log.scriviLog(2, "      Aggiunto in Vriscika: " + szVriscikaGrahaSmall)
                    Log.scriviLog(2, "      Aggiunto in Vriscika: " + szVriscikaGrahaLon)
                case 9:
                    if(graha[2]):
                        szDhanusGrahaRetr = szDhanusGrahaRetr + szRetrSym
                    else:
                        szDhanusGrahaRetr = szDhanusGrahaRetr + "   "
                    szDhanusGrahaSmall = str(szDhanusGrahaSmall + graha[0] + " ")
                    szDhanusGrahaLon  = szDhanusGrahaLon + str(int(float(graha[1]))).zfill(2) + " "
                    Log.scriviLog(2, "      Aggiunto in Dhanus: " + szDhanusGrahaRetr)
                    Log.scriviLog(2, "      Aggiunto in Dhanus: " + szDhanusGrahaSmall)
                    Log.scriviLog(2, "      Aggiunto in Dhanus: " + szDhanusGrahaLon)
                case 10:
                    if(graha[2]):
                        szMakaraGrahaRetr = szMakaraGrahaRetr + szRetrSym
                    else:
                        szMakaraGrahaRetr = szMakaraGrahaRetr + "   "
                    szMakaraGrahaSmall = str(szMakaraGrahaSmall + graha[0] + " ")
                    szMakaraGrahaLon  = szMakaraGrahaLon + str(int(float(graha[1]))).zfill(2) + " "
                    Log.scriviLog(2, "      Aggiunto in Makara: " + szMakaraGrahaRetr)
                    Log.scriviLog(2, "      Aggiunto in Makara: " + szMakaraGrahaSmall)
                    Log.scriviLog(2, "      Aggiunto in Makara: " + szMakaraGrahaLon)
                case 11:
                    if(graha[2]):
                        szKumbaGrahaRetr = szKumbaGrahaRetr + szRetrSym
                    else:
                        szKumbaGrahaRetr = szKumbaGrahaRetr + "   "
                    szKumbaGrahaSmall = str(szKumbaGrahaSmall + graha[0] + " ")
                    szKumbaGrahaLon  = szKumbaGrahaLon + str(int(float(graha[1]))).zfill(2) + " "
                    Log.scriviLog(2, "      Aggiunto in Kumba: " + szKumbaGrahaRetr)
                    Log.scriviLog(2, "      Aggiunto in Kumba: " + szKumbaGrahaSmall)
                    Log.scriviLog(2, "      Aggiunto in Kumba: " + szKumbaGrahaLon)
                case 12:
                    if(graha[2]):
                        szMinaGrahaRetr = szMinaGrahaRetr + szRetrSym
                    else:
                        szMinaGrahaRetr = szMinaGrahaRetr + "   "
                    szMinaGrahaSmall = str(szMinaGrahaSmall + graha[0] + " ")
                    szMinaGrahaLon  = szMinaGrahaLon + str(int(float(graha[1]))).zfill(2) + " "
                    Log.scriviLog(2, "      Aggiunto in Mina: " + szMinaGrahaRetr)
                    Log.scriviLog(2, "      Aggiunto in Mina: " + szMinaGrahaSmall)
                    Log.scriviLog(2, "      Aggiunto in Mina: " + szMinaGrahaLon)

    Log.scriviLog(9, "\n\n")
    #      0        1         2         3         4         5
    #      12345678901234567890123456789012345678901234567890123

    szBigBorder = "+----------------+----------------+----------------+----------------+"
    szSmallBorder = "+----------------+"
    szEmptySpace = "                                 "
    iJust=16

    lstLineToPrint = []
    lstLineToPrint.append(szBigBorder)
    lstLineToPrint.append("| Pi             | Ar             | Ta             | Ge             |")
    lstLineToPrint.append("|" + szMinaGrahaRetr.rjust(iJust) + "|" + szMesaGrahaRetr.rjust(iJust) + "|" + szVrsabhaGrahaRetr.rjust(iJust) + "|" + szMithunaGrahaRetr.rjust(iJust) + "|")
    lstLineToPrint.append("|" + szMinaGrahaSmall.rjust(iJust) + "|" + szMesaGrahaSmall.rjust(iJust) + "|" + szVrsabhaGrahaSmall.rjust(iJust) + "|" + szMithunaGrahaSmall.rjust(iJust) + "|")
    lstLineToPrint.append("|" + szMinaGrahaLon.rjust(iJust) + "|" + szMesaGrahaLon.rjust(iJust) + "|" + szVrsabhaGrahaLon.rjust(iJust) + "|" + szMithunaGrahaLon.rjust(iJust) + "|")
    lstLineToPrint.append(szBigBorder)
    lstLineToPrint.append("| Aq             |                                 | Cn             |")
    lstLineToPrint.append("|" + szKumbaGrahaRetr.rjust(iJust)+ "|" + szEmptySpace + "|" + szKarkataGrahaRetr.rjust(iJust) + "|")
    lstLineToPrint.append("|" + szKumbaGrahaSmall.rjust(iJust) + "|" + szEmptySpace + "|" + szKarkataGrahaSmall.rjust(iJust) + "|")
    lstLineToPrint.append("|" + szKumbaGrahaLon.rjust(iJust)+ "|" + szEmptySpace +  "|" + szKarkataGrahaLon.rjust(iJust) + "|")
    lstLineToPrint.append(szSmallBorder + szEmptySpace + szSmallBorder)
    lstLineToPrint.append("| Cp             |                                 | Le             |")
    lstLineToPrint.append("|" + szMakaraGrahaRetr.rjust(iJust)+ "|" + szEmptySpace + "|" + szSimhaGrahaRetr.rjust(iJust) + "|")
    lstLineToPrint.append("|" + szMakaraGrahaSmall.rjust(iJust)+ "|" + szEmptySpace + "|" + szSimhaGrahaSmall.rjust(iJust) + "|")
    lstLineToPrint.append("|" + szMakaraGrahaLon.rjust(iJust)+ "|" + szEmptySpace +  "|" + szSimhaGrahaLon.rjust(iJust) + "|")
    lstLineToPrint.append(szBigBorder)
    lstLineToPrint.append("| Sg             | Sc             | Li             | Vi             |")
    lstLineToPrint.append("|" + szDhanusGrahaRetr.rjust(iJust) + "|" + szVriscikaGrahaRetr.rjust(iJust) + "|" + szTulaGrahaRetr.rjust(iJust) + "|" + szKaniaGrahaRetr.rjust(iJust) + "|")
    lstLineToPrint.append("|" + szDhanusGrahaSmall.rjust(iJust) + "|" + szVriscikaGrahaSmall.rjust(iJust) + "|" + szTulaGrahaSmall.rjust(iJust) + "|" + szKaniaGrahaSmall.rjust(iJust) + "|")
    lstLineToPrint.append("|" + szDhanusGrahaLon.rjust(iJust) + "|" + szVriscikaGrahaLon.rjust(iJust) + "|" + szTulaGrahaLon.rjust(iJust) + "|" + szKaniaGrahaLon.rjust(iJust) + "|")
    lstLineToPrint.append(szBigBorder)


    '''
    Log.scriviLog(9,"+------------+------------+------------+------------+") #Line 01
    Log.scriviLog(9,"|Pi          |Ar          |Ta          |Ge          |") #Line 02
    Log.scriviLog(9,"|AARBBRCCRDDR|AARBBRCCRDDR|AARBBRCCRDDR|AARBBRCCRDDR|") #Line 03
    Log.scriviLog(9,"|01 02 03 04 |01 02 03 04 |01 02 03 04 |01 02 03 04 |") #Line 04
    Log.scriviLog(9,"+------------+------------+------------+------------+") #Line 05
    Log.scriviLog(9,"|Aq          |                         |Cn          |") #Line 06
    Log.scriviLog(9,"|AARBBRCCRDDR|                         |AARBBRCCRDDR|") #Line 07
    Log.scriviLog(9,"|01 02 03 04 |                         |01 02 03 04 |") #Line 08
    Log.scriviLog(9,"+------------+                         +------------+") #Line 09
    Log.scriviLog(9,"|Cp          |                         |Le          |") #Line 10
    Log.scriviLog(9,"|AARBBRCCRDDR|                         |AARBBRCCRDDR|") #Line 11
    Log.scriviLog(9,"|01 02 03 04 |                         |01 02 03 04 |") #Line 12
    Log.scriviLog(9,"+------------+------------+------------+------------+") #Line 13
    Log.scriviLog(9,"|Sg          |Sc          |Li          |Vi          |") #Line 14
    Log.scriviLog(9,"|AARBBRCCRDDR|AARBBRCCRDDR|AARBBRCCRDDR|AARBBRCCRDDR|") #Line 15
    Log.scriviLog(9,"|01 02 03 04 |01 02 03 04 |01 02 03 04 |01 02 03 04 |") #Line 16
    Log.scriviLog(9,"+------------+------------+------------+------------+") #Line 17
    '''
    Log.scriviLog(9, "\n\n")

    for line in lstLineToPrint:
        Log.scriviLog(9, line)


def grahaInRasi(Log, lstCartaNatale, szGrahaSmall, iRasi, fLon, bRetr):
    Log.scriviLog(5, "Passati: " + szGrahaSmall + ", " + str(iRasi) + ", " + str(fLon) + ", " + str(bRetr) )
    #lstCartaNatale = ["Mesa","Vrsabha","Mithuna","Karkata","Simha","Kania","Tula","Vrscika","Dhanus","Makara","Kumbha","Mina"]
    match int(iRasi):
        case 1:
            lstMesa.append([szGrahaSmall, fLon, bRetr])
            Log.scriviLog(2, "Aggiunto in Mesa")
        case 2:
            lstVrsabha.append([szGrahaSmall, fLon, bRetr])
            Log.scriviLog(2, "Aggiunto in Vrsabha")
        case 3:
            lstMithuna.append([szGrahaSmall, fLon, bRetr])
            Log.scriviLog(2, "Aggiunto in Mithuna")
        case 4:
            lstKarkata.append([szGrahaSmall, fLon, bRetr])
            Log.scriviLog(2, "Aggiunto in: Karkata")
        case 5:
            lstSimha.append([szGrahaSmall, fLon, bRetr])
            Log.scriviLog(2, "Aggiunto in Simha")
        case 6:
            lstKania.append([szGrahaSmall, fLon, bRetr])
            Log.scriviLog(2, "Aggiunto in Kania")
        case 7:
            lstTula.append([szGrahaSmall, fLon, bRetr])
            Log.scriviLog(2, "Aggiunto in Tula")
        case 8:
            lstVrscika.append([szGrahaSmall, fLon, bRetr])
            Log.scriviLog(2, "Aggiunto in Vriscika")
        case 9:
            lstDhanus.append([szGrahaSmall, fLon, bRetr])
            Log.scriviLog(2, "Aggiunto in Dhanus")
        case 10:
            lstMakara.append([szGrahaSmall, fLon, bRetr])
            Log.scriviLog(2, "Aggiunto in Makara")
        case 11:
            lstKumbha.append([szGrahaSmall, fLon, bRetr])
            Log.scriviLog(2, "Aggiunto in Kumba")
        case 12:
            lstMina.append([szGrahaSmall, fLon, bRetr])
            Log.scriviLog(2, "Aggiunto in Mina")

    lstCartaNatale.append(lstMesa)
    lstCartaNatale.append(lstVrsabha)
    lstCartaNatale.append(lstMithuna)
    lstCartaNatale.append(lstKarkata)
    lstCartaNatale.append(lstSimha)
    lstCartaNatale.append(lstKania)
    lstCartaNatale.append(lstTula)
    lstCartaNatale.append(lstVrscika)
    lstCartaNatale.append(lstDhanus)
    lstCartaNatale.append(lstMakara)
    lstCartaNatale.append(lstKumbha)
    lstCartaNatale.append(lstMina)

    return lstCartaNatale

def showGrahaDetail(Log, lstGrahaList):

    Log.scriviLog(9, "\n\n")
    Log.scriviLog(2, "Inizio Graha detail")
    Log.scriviLog(9, "+-----------------------+")
    Log.scriviLog(9, "|      Graha Detail     |")
    Log.scriviLog(9, "+-----------------------+")
    Log.scriviLog(9, "\n")

    #Creazione delle note per ogni pianeta



    for graha in lstGrahaList:
        graha.createNote()
        if(graha.iGrahaProgr == 0):
            if (graha.getRasi() != " - "):
                szLine = "(" + graha.Tab.lstGrahaSmall[graha.iGrahaProgr] + ") "  \
                             + graha.Tab.lstGrahaSansc[graha.iGrahaProgr].rjust(8) + " in (" + str(graha.getRasi()).rjust(2) + ") " \
                             + graha.getRasiGrahaInSansc(graha.getRasi()).rjust(8) \
                             + " Long.: " + str(graha.getLongitude()).rjust(8) + " - " + graha.getLongitudeAssolute() + " - " + graha.getNote()
                lstLinetoPrint.append(szLine)
        else:
            szLine="(" + graha.Tab.lstGrahaSmall[graha.iGrahaProgr] + ") " \
                       + graha.Tab.lstGrahaSansc[graha.iGrahaProgr].rjust(8) + " in (" + str(graha.getRasi()).rjust(2) + ") "  \
                       + graha.getRasiGrahaInSansc(graha.getRasi()).rjust(8) \
                       + " Long.: " + str(graha.getLongitude()).rjust(8)  \
                       + " - Bhava CP: " + graha.getBhava() + " [" + graha.getBhavaLon() + "]"  \
                       + " - Bhava CU: " + graha.getBhavaCusp() + " [" + graha.getBhavaLonCusp() + "] - " \
                       + graha.getNote()
            lstLinetoPrint.append(szLine)

    for line in lstLinetoPrint:
        Log.scriviLog(9, line)

def checkIsKopa(Log, GrahaToCheck, fSunLonAss):
    Log.scriviLog(2, "Verifica se " + str(GrahaToCheck.szGrahaSansc) + " è in Kopa. Long. assoluta del sole: " + fSunLonAss)
    GrahaToCheck.checkIsKopa(fSunLonAss)



def checkIsPlanetWar(Log, fSunLonAbs, fMoonLonAbs, fMarsLonAbs, fMercLonAbs, fJuptLonAbs, fVenLonAbs, fSatLonAbs, fRahuLonAbs, fKetuLonAbs ):
    Log.scriviLog(5, "Verifica presenza di Guerre Planetarie")
    lstGrahaWar=[]
    #lstGrahaProgr = [2,3,4,5,6,7,8,9,10]
    #lstGrahaLon = []

    lstPlanetWar.append([float(fSunLonAbs),2])
    lstPlanetWar.append([float(fMoonLonAbs),3])
    lstPlanetWar.append([float(fMarsLonAbs),4])
    lstPlanetWar.append([float(fMercLonAbs),5])
    lstPlanetWar.append([float(fJuptLonAbs),6])
    lstPlanetWar.append([float(fVenLonAbs),7])
    lstPlanetWar.append([float(fSatLonAbs),8])
    lstPlanetWar.append([float(fRahuLonAbs),9])
    lstPlanetWar.append([float(fKetuLonAbs),10])

    lstPlanetWar.sort()

    i=0
    for graha in lstPlanetWar:
        if(i>7):
            break
        Log.scriviLog(2, str(lstPlanetWar[i][0]) + " -> " + str(lstPlanetWar [i+1][0]))
        if(abs(float(str(lstPlanetWar[i][0]))-float(str(lstPlanetWar[i+1][0]))) < 2):
            Log.scriviLog(2, "Lotta planetaria tra " + str(lstPlanetWar[i][1]) + " e " + str(lstPlanetWar[i+1][1]))
            lstGrahaWar.append([str(lstPlanetWar[i][1]), str(lstPlanetWar[i+1][1])])
        i=i+1
    return lstGrahaWar

