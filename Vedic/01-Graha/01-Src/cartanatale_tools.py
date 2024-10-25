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

    szMesaGrahaSmall = ""
    szMesaGrahaLon = ""
    szVrsabhaGrahaSmall = ""
    szVrsabhaGrahaLon = ""
    szMithunaGrahaSmall = ""
    szMithunaGrahaLon = ""
    szKarkataGrahaSmall = ""
    szKarkataGrahaLon = ""
    szSimhaGrahaSmall = ""
    szSimhaGrahaLon = ""
    szKaniaGrahaSmall = ""
    szKaniaGrahaLon = ""
    szTulaGrahaSmall = ""
    szTulaGrahaLon = ""
    szVriscikaGrahaSmall = ""
    szVriscikaGrahaLon = ""
    szDhanusGrahaSmall = ""
    szDhanusGrahaLon = ""
    szMakaraGrahaSmall = ""
    szMakaraGrahaLon = ""
    szKumbaGrahaSmall = ""
    szKumbaGrahaLon = ""
    szMinaGrahaSmall = ""
    szMinaGrahaLon = ""

    for rasi in range(12):
        Log.scriviLog(5, "Num graha in " + GrahaAsc.lstRasiSansc[rasi] + ": " + str(len(lstCartaNatale[rasi])))
        for graha in lstCartaNatale[rasi]:
            #lstCartaNatale = ["Mesa","Vrsabha","Mithuna","Karkata","Simha","Kania","Tula","Vrscika","Dhanus","Makara","Kumbha","Mina"]
            Log.scriviLog(5, "   " + graha[0] + " - Lon = " + str(graha[1]) )
            match (rasi+1):
                case 1:
                    szMesaGrahaSmall = szMesaGrahaSmall + graha[0] + " "
                    szMesaGrahaLon  = szMesaGrahaLon + str(int(float(graha[1]))).zfill(2) + " "
			  #print(Style.RESET_ALL)
                    Log.scriviLog(2, "      Aggiunto in Mesa: " + szMesaGrahaSmall)
                    Log.scriviLog(2, "      Aggiunto in Mesa: " + szMesaGrahaLon)
                case 2:
                    szVrsabhaGrahaSmall = szVrsabhaGrahaSmall + graha[0] + " "
                    szVrsabhaGrahaLon  = szVrsabhaGrahaLon + str(int(float(graha[1]))).zfill(2) + " "
                    Log.scriviLog(2, "      Aggiunto in Vrsabha: " + szVrsabhaGrahaSmall)
                    Log.scriviLog(2, "      Aggiunto in Vrsabha: " + szVrsabhaGrahaLon)
                case 3:
                    szMithunaGrahaSmall = szMithunaGrahaSmall + graha[0] + " "
                    szMithunaGrahaLon  = szMithunaGrahaLon + str(int(float(graha[1]))).zfill(2) + " "
                    Log.scriviLog(2, "      Aggiunto in Mithuna: " + szMithunaGrahaSmall)
                    Log.scriviLog(2, "      Aggiunto in Mithuna: " + szMithunaGrahaLon)
                case 4:
                    szKarkataGrahaSmall = szKarkataGrahaSmall + graha[0] + " "
                    szKarkataGrahaLon  = szKarkataGrahaLon + str(int(float(graha[1]))).zfill(2) + " "
                    Log.scriviLog(2, "      Aggiunto in Karkata: " + szKarkataGrahaSmall)
                    Log.scriviLog(2, "      Aggiunto in Karkata: " + szKarkataGrahaLon)
                case 5:
                    szSimhaGrahaSmall = szSimhaGrahaSmall + graha[0] + " "
                    szSimhaGrahaLon  = szSimhaGrahaLon + str(int(float(graha[1]))).zfill(2) + " "
                    Log.scriviLog(2, "      Aggiunto in Simha: " + szSimhaGrahaSmall)
                    Log.scriviLog(2, "      Aggiunto in Simha: " + szSimhaGrahaLon)
                case 6:
                    szKaniaGrahaSmall = szKaniaGrahaSmall + graha[0] + " "
                    szKaniaGrahaLon  = szKaniaGrahaLon + str(int(float(graha[1]))).zfill(2) + " "
                    Log.scriviLog(2, "      Aggiunto in Kania: " + szKaniaGrahaSmall)
                    Log.scriviLog(2, "      Aggiunto in Kania: " + szKaniaGrahaLon)
                case 7:
                    szTulaGrahaSmall = szTulaGrahaSmall + graha[0] + " "
                    szTulaGrahaLon  = szTulaGrahaLon + str(int(float(graha[1]))).zfill(2) + " "
                    Log.scriviLog(2, "      Aggiunto in Tula: " + szTulaGrahaSmall)
                    Log.scriviLog(2, "      Aggiunto in Tula: " + szTulaGrahaLon)
                case 8:
                    szVriscikaGrahaSmall = szVriscikaGrahaSmall + graha[0] + " "
                    szVriscikaGrahaLon  = szVriscikaGrahaLon + str(int(float(graha[1]))).zfill(2) + " "
                    Log.scriviLog(2, "      Aggiunto in Vriscika: " + szVriscikaGrahaSmall)
                    Log.scriviLog(2, "      Aggiunto in Vriscika: " + szVriscikaGrahaLon)
                case 9:
                    szDhanusGrahaSmall = szDhanusGrahaSmall + graha[0] + " "
                    szDhanusGrahaLon  = szDhanusGrahaLon + str(int(float(graha[1]))).zfill(2) + " "
                    Log.scriviLog(2, "      Aggiunto in Dhanus: " + szDhanusGrahaSmall)
                    Log.scriviLog(2, "      Aggiunto in Dhanus: " + szDhanusGrahaLon)
                case 10:
                    szMakaraGrahaSmall = szMakaraGrahaSmall + graha[0] + " "
                    szMakaraGrahaLon  = szMakaraGrahaLon + str(int(float(graha[1]))).zfill(2) + " "
                    Log.scriviLog(2, "      Aggiunto in Makara: " + szMakaraGrahaSmall)
                    Log.scriviLog(2, "      Aggiunto in Makara: " + szMakaraGrahaLon)
                case 11:
                    szKumbaGrahaSmall = szKumbaGrahaSmall + graha[0] + " "
                    szKumbaGrahaLon  = szKumbaGrahaLon + str(int(float(graha[1]))).zfill(2) + " "
                    Log.scriviLog(2, "      Aggiunto in Kumba: " + szKumbaGrahaSmall)
                    Log.scriviLog(2, "      Aggiunto in Kumba: " + szKumbaGrahaLon)
                case 12:
                    szMinaGrahaSmall = szMinaGrahaSmall + graha[0] + " "
                    szMinaGrahaLon  = szMinaGrahaLon + str(int(float(graha[1]))).zfill(2) + " "
                    Log.scriviLog(2, "      Aggiunto in Mina: " + szMinaGrahaSmall)
                    Log.scriviLog(2, "      Aggiunto in Mina: " + szMinaGrahaLon)

    Log.scriviLog(9, "\n\n")
    #      0        1         2         3         4         5
    #      12345678901234567890123456789012345678901234567890123

    szBigBorder = "+------------+------------+------------+------------+"
    szSmallBorder = "+------------+"
    szEmptySpace = "                         "

    szLine01 = szBigBorder
    szLine02 = "|Pi          |Ar          |Ta          |Ge          |"
    szLine03 = "|" + szMinaGrahaSmall.rjust(12) + "|" + szMesaGrahaSmall.rjust(12) + "|" + szVrsabhaGrahaSmall.rjust(12) + "|" + szMithunaGrahaSmall.rjust(12) + "|"
    szLine04 = "|" + szMinaGrahaLon.rjust(12) + "|" + szMesaGrahaLon.rjust(12) + "|" + szVrsabhaGrahaLon.rjust(12) + "|" + szMithunaGrahaLon.rjust(12) + "|"
    szLine05 = szBigBorder
    szLine06 = "|Aq          |                         |Cn          |"
    szLine07 = "|" + szKumbaGrahaSmall.rjust(12)+ "|" + szEmptySpace + "|" + szKarkataGrahaSmall.rjust(12) + "|"
    szLine08 = "|" + szKumbaGrahaLon.rjust(12)+ "|" + szEmptySpace +  "|" + szKarkataGrahaLon.rjust(12) + "|"
    szLine09 = szSmallBorder + szEmptySpace + szSmallBorder
    szLine10 = "|Cp          |                         |Le          |"
    szLine11 = "|" + szMakaraGrahaSmall.rjust(12)+ "|" + szEmptySpace + "|" + szSimhaGrahaSmall.rjust(12) + "|"
    szLine12 = "|" + szMakaraGrahaLon.rjust(12)+ "|" + szEmptySpace +  "|" + szSimhaGrahaLon.rjust(12) + "|"
    szLine13 = szBigBorder
    szLine14 = "|Sg          |Sc          |Li          |Vi          |"
    szLine15 = "|" + szDhanusGrahaSmall.rjust(12) + "|" + szVriscikaGrahaSmall.rjust(12) + "|" + szTulaGrahaSmall.rjust(12) + "|" + szKaniaGrahaSmall.rjust(12) + "|"
    szLine16 = "|" + szDhanusGrahaLon.rjust(12) + "|" + szVriscikaGrahaLon.rjust(12) + "|" + szTulaGrahaLon.rjust(12) + "|" + szKaniaGrahaLon.rjust(12) + "|"
    szLine17 = szBigBorder


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

    Log.scriviLog(9, szLine01) #Line 01
    Log.scriviLog(9, szLine02) #Line 02
    Log.scriviLog(9, szLine03) #Line 03
    Log.scriviLog(9, szLine04) #Line 04
    Log.scriviLog(9, szLine05) #Line 05
    Log.scriviLog(9, szLine06) #Line 06
    Log.scriviLog(9, szLine07) #Line 07
    Log.scriviLog(9, szLine08) #Line 08
    Log.scriviLog(9, szLine09) #Line 09
    Log.scriviLog(9, szLine10) #Line 10
    Log.scriviLog(9, szLine11) #Line 11
    Log.scriviLog(9, szLine12) #Line 12
    Log.scriviLog(9, szLine13) #Line 13
    Log.scriviLog(9, szLine14) #Line 14
    Log.scriviLog(9, szLine15) #Line 15
    Log.scriviLog(9, szLine16) #Line 16
    Log.scriviLog(9, szLine17) #Line 17


def grahaInRasi(Log, lstCartaNatale, szGrahaSmall, iRasi, fLon):
    Log.scriviLog(5, "Passati: " + szGrahaSmall + ", " + str(iRasi) + ", " + str(fLon))
    #lstCartaNatale = ["Mesa","Vrsabha","Mithuna","Karkata","Simha","Kania","Tula","Vrscika","Dhanus","Makara","Kumbha","Mina"]
    match int(iRasi):
        case 1:
            lstMesa.append([szGrahaSmall, fLon])
            Log.scriviLog(2, "Aggiunto in Mesa")
        case 2:
            lstVrsabha.append([szGrahaSmall, fLon])
            Log.scriviLog(2, "Aggiunto in Vrsabha")
        case 3:
            lstMithuna.append([szGrahaSmall, fLon])
            Log.scriviLog(2, "Aggiunto in Mithuna")
        case 4:
            lstKarkata.append([szGrahaSmall, fLon])
            Log.scriviLog(2, "Aggiunto in: Karkata")
        case 5:
            lstSimha.append([szGrahaSmall, fLon])
            Log.scriviLog(2, "Aggiunto in Simha")
        case 6:
            lstKania.append([szGrahaSmall, fLon])
            Log.scriviLog(2, "Aggiunto in Kania")
        case 7:
            lstTula.append([szGrahaSmall, fLon])
            Log.scriviLog(2, "Aggiunto in Tula")
        case 8:
            lstVrscika.append([szGrahaSmall, fLon])
            Log.scriviLog(2, "Aggiunto in Vriscika")
        case 9:
            lstDhanus.append([szGrahaSmall, fLon])
            Log.scriviLog(2, "Aggiunto in Dhanus")
        case 10:
            lstMakara.append([szGrahaSmall, fLon])
            Log.scriviLog(2, "Aggiunto in Makara")
        case 11:
            lstKumbha.append([szGrahaSmall, fLon])
            Log.scriviLog(2, "Aggiunto in Kumba")
        case 12:
            lstMina.append([szGrahaSmall, fLon])
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

def showGrahaDetail(Log,
                    GrahaAsc,
                    GrahaSun,
                    GrahaMoon,
                    GrahaMars,
                    GrahaMercury,
                    GrahaJupiter,
                    GrahaVenus,
                    GrahaSaturn,
                    GrahaRahu,
                    GrahaKetu):

    Log.scriviLog(9, "\n\n")
    Log.scriviLog(2, "Inizio Graha detail")
    Log.scriviLog(9, "+-----------------------+")
    Log.scriviLog(9, "|      Graha Detail     |")
    Log.scriviLog(9, "+-----------------------+")
    Log.scriviLog(9, "\n")

    #Creazione delle note per ogni pianeta
    GrahaAsc.createNote()
    GrahaSun.createNote()
    GrahaMoon.createNote()
    GrahaMars.createNote()
    GrahaMercury.createNote()
    GrahaJupiter.createNote()
    GrahaVenus.createNote()
    GrahaSaturn.createNote()
    GrahaRahu.createNote()
    GrahaKetu.createNote()


    if(GrahaAsc.getRasi() != " - "):
        szLine01 = "(" + GrahaAsc.getGrahaSmall() + ")" + GrahaAsc.getGrahaSansc() + " in " + "(" + GrahaAsc.getRasi() + ")" + GrahaAsc.getRasiGrahaInSansc(GrahaAsc.getRasi()) + " Lat.: " + GrahaAsc.getLongitude() + " - " + GrahaAsc.getLongitudeAssolute() + " - " + GrahaAsc.getNote()
    else:
        szLine01 = "(" + GrahaAsc.getGrahaSmall() + ")" + GrahaAsc.getGrahaSansc() + " ** NON CALCOLABILE **"

    szLine02 = "(" + GrahaSun.getGrahaSmall() + ")" + GrahaSun.getGrahaSansc() + " in " + "(" + GrahaSun.getRasi() + ")" + GrahaSun.getRasiGrahaInSansc(GrahaSun.getRasi()) + " Lat.: " + GrahaSun.getLongitude() + " - " + GrahaSun.getLongitudeAssolute() + " - " + GrahaSun.getNote()
    szLine03 = "(" + GrahaMoon.getGrahaSmall() + ")" + GrahaMoon.getGrahaSansc() + " in " + "(" + GrahaMoon.getRasi() + ")" + GrahaMoon.getRasiGrahaInSansc(GrahaMoon.getRasi()) + " Lat.: " + GrahaMoon.getLongitude() + " - " + GrahaMoon.getLongitudeAssolute() + " - " + GrahaMoon.getNote()
    szLine04 = "(" + GrahaMars.getGrahaSmall() + ")" + GrahaMars.getGrahaSansc() + " in " + "(" + GrahaMars.getRasi() + ")" + GrahaMars.getRasiGrahaInSansc(GrahaMars.getRasi()) + " Lat.: " + GrahaMars.getLongitude() + " - " + GrahaMars.getLongitudeAssolute() + " - " + GrahaMars.getNote()
    szLine05 = "(" + GrahaMercury.getGrahaSmall() + ")" + GrahaMercury.getGrahaSansc() + " in " + "(" + GrahaMercury.getRasi() + ")" + GrahaMercury.getRasiGrahaInSansc(GrahaMercury.getRasi()) + " Lat.: "  + GrahaMercury.getLongitude() + " - " + GrahaMercury.getLongitudeAssolute() + " - " + GrahaMercury.getNote()
    szLine06 = "(" + GrahaJupiter.getGrahaSmall() + ")" + GrahaJupiter.getGrahaSansc() + " in " + "(" + GrahaJupiter.getRasi() + ")" + GrahaJupiter.getRasiGrahaInSansc(GrahaJupiter.getRasi()) + " Lat.: "  + GrahaJupiter.getLongitude() + " - " + GrahaJupiter.getLongitudeAssolute() + " - " + GrahaJupiter.getNote()
    szLine07 = "(" + GrahaVenus.getGrahaSmall() + ")" + GrahaVenus.getGrahaSansc() + " in " + "(" + GrahaVenus.getRasi() + ")" + GrahaVenus.getRasiGrahaInSansc(GrahaVenus.getRasi()) + " Lat.: "  + GrahaVenus.getLongitude() + " - " + GrahaVenus.getLongitudeAssolute() + " - " + GrahaVenus.getNote()
    szLine08 = "(" + GrahaSaturn.getGrahaSmall() + ")" + GrahaSaturn.getGrahaSansc() + " in " + "(" + GrahaSaturn.getRasi() + ")" + GrahaSaturn.getRasiGrahaInSansc(GrahaSaturn.getRasi()) + " Lat.: "  + GrahaSaturn.getLongitude() + " - " + GrahaSaturn.getLongitudeAssolute() + " - " + GrahaSaturn.getNote()
    szLine09 = "(" + GrahaRahu.getGrahaSmall() + ")" + GrahaRahu.getGrahaSansc() + " in " + "(" + GrahaRahu.getRasi() + ")" + GrahaRahu.getRasiGrahaInSansc(GrahaRahu.getRasi()) + " Lat.: "  + GrahaRahu.getLongitude() + " - " + GrahaRahu.getLongitudeAssolute() + " - " + GrahaRahu.getNote()
    szLine10 = "(" + GrahaKetu.getGrahaSmall() + ")" + GrahaKetu.getGrahaSansc() + " in " + "(" + GrahaKetu.getRasi() + ")" + GrahaKetu.getRasiGrahaInSansc(GrahaKetu.getRasi()) + " Lat.: "  + GrahaKetu.getLongitude() + " - " + GrahaKetu.getLongitudeAssolute() + " - " + GrahaKetu.getNote()



    Log.scriviLog(9, szLine01)
    Log.scriviLog(9, szLine02)
    Log.scriviLog(9, szLine03)
    Log.scriviLog(9, szLine04)
    Log.scriviLog(9, szLine05)
    Log.scriviLog(9, szLine06)
    Log.scriviLog(9, szLine07)
    Log.scriviLog(9, szLine08)
    Log.scriviLog(9, szLine09)
    Log.scriviLog(9, szLine10)


def checkIsKopa(Log, GrahaToCheck, fSunLonAss):
    Log.scriviLog(2, "Verifica se " + GrahaToCheck.getGrahaSansc() + " è in Kopa. Long. assoluta del sole: " + fSunLonAss)
    GrahaToCheck.checkIsKopa(fSunLonAss)



def checkIsPlanetWar(Log, fSunLonAbs, fMoonLonAbs, fMarsLonAbs, fMercLonAbs, fJuptLonAbs, fVenLonAbs, fSatLonAbs, fRahuLonAbs, fKetuLonAbs ):
    Log.scriviLog(2, "Verifica presenza di Guerre Planetarie")
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

    print (lstPlanetWar)
    lstPlanetWar.sort()
    print (lstPlanetWar)
    #Log.scriviLog(2, lstPlanetWar)

    i=0
    for graha in lstPlanetWar:
        if(i>7):
            break
        print(str(lstPlanetWar[i][0]) + " -> " + str(lstPlanetWar [i+1][0]))
        if(abs(float(str(lstPlanetWar[i][0]))-float(str(lstPlanetWar[i+1][0]))) < 2):
            print("Lotta planetaria tra " + str(lstPlanetWar[i][1]) + " e " + str(lstPlanetWar[i+1][1]))
            lstGrahaWar.append([str(lstPlanetWar[i][1]), str(lstPlanetWar[i+1][1])])
        i=i+1
    return lstGrahaWar


def putGrahaInBavha(Log,GrahaAsc,GrahaSun,GrahaMoon,GrahaMars,GrahaMercury,GrahaJupiter,GrahaVenus,GrahaSaturn,GrahaRahu,GrahaKetu):
    #si crea un nuovo zodiaco formato da 12 case, ogni casa ha ampiezza di 30 gradi e parte dall'ascendente taglando i segni ed
    # includendo i pianeti
    # Longitudine del pianeta nella casa è uguale al rapporto tra la logitudine assoluta dall'ascendente e 30,
    # la parte intera rappresenta la casa mentre la parte restante indica la longitudine nella casa
    # occorre quindi che il graha conosca la sua logitudine assoluta rspetto ascendente


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

