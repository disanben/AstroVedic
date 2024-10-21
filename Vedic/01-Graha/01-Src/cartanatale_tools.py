import os
import sys
from load_graha import LoadGraha
from graha import Graha
from logCartaNatale import LogCartaNatale

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



def help_utente():
    print("\n\n")
    print("+-------------------------+")
    print("|      Manuale utente     |")
    print("+-------------------------+")


def showCartaNatale(Log, GrahaAsc, lstCartaNatale):

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

    szLine01 = "(" + GrahaAsc.getGrahaSmall() + ")" + GrahaAsc.getGrahaSansc() + " in " + "(" + GrahaAsc.getRasi() + ")" + GrahaAsc.getRasiGrahaInSansc(GrahaAsc.getRasi()) + " Lat.: " + GrahaAsc.getLongitude() + " - " + GrahaAsc.getNote()
    szLine02 = "(" + GrahaSun.getGrahaSmall() + ")" + GrahaSun.getGrahaSansc() + " in " + "(" + GrahaSun.getRasi() + ")" + GrahaSun.getRasiGrahaInSansc(GrahaSun.getRasi()) + " Lat.: " + GrahaSun.getLongitude() + " - " + GrahaSun.getNote()
    szLine03 = "(" + GrahaMoon.getGrahaSmall() + ")" + GrahaMoon.getGrahaSansc() + " in " + "(" + GrahaMoon.getRasi() + ")" + GrahaMoon.getRasiGrahaInSansc(GrahaMoon.getRasi()) + " Lat.: " + GrahaMoon.getLongitude() + " - " + GrahaMoon.getNote()
    szLine04 = "(" + GrahaMars.getGrahaSmall() + ")" + GrahaMars.getGrahaSansc() + " in " + "(" + GrahaMars.getRasi() + ")" + GrahaMars.getRasiGrahaInSansc(GrahaMars.getRasi()) + " Lat.: " + GrahaMars.getLongitude() + " - " + GrahaMars.getNote()
    szLine05 = "(" + GrahaMercury.getGrahaSmall() + ")" + GrahaMercury.getGrahaSansc() + " in " + "(" + GrahaMercury.getRasi() + ")" + GrahaMercury.getRasiGrahaInSansc(GrahaMercury.getRasi()) + " Lat.: " + GrahaMercury.getLongitude() + " - " + GrahaMercury.getNote()
    szLine06 = "(" + GrahaJupiter.getGrahaSmall() + ")" + GrahaJupiter.getGrahaSansc() + " in " + "(" + GrahaJupiter.getRasi() + ")" + GrahaJupiter.getRasiGrahaInSansc(GrahaJupiter.getRasi()) + " Lat.: " + GrahaJupiter.getLongitude() + " - " + GrahaJupiter.getNote()
    szLine07 = "(" + GrahaVenus.getGrahaSmall() + ")" + GrahaVenus.getGrahaSansc() + " in " + "(" + GrahaVenus.getRasi() + ")" + GrahaVenus.getRasiGrahaInSansc(GrahaVenus.getRasi()) + " Lat.: " + GrahaVenus.getLongitude() + " - " + GrahaVenus.getNote()
    szLine08 = "(" + GrahaSaturn.getGrahaSmall() + ")" + GrahaSaturn.getGrahaSansc() + " in " + "(" + GrahaSaturn.getRasi() + ")" + GrahaSaturn.getRasiGrahaInSansc(GrahaSaturn.getRasi()) + " Lat.: " + GrahaSaturn.getLongitude() + " - " + GrahaSaturn.getNote()
    szLine09 = "(" + GrahaRahu.getGrahaSmall() + ")" + GrahaRahu.getGrahaSansc() + " in " + "(" + GrahaRahu.getRasi() + ")" + GrahaRahu.getRasiGrahaInSansc(GrahaRahu.getRasi()) + " Lat.: " + GrahaRahu.getLongitude() + " - " + GrahaRahu.getNote()
    szLine10 = "(" + GrahaKetu.getGrahaSmall() + ")" + GrahaKetu.getGrahaSansc() + " in " + "(" + GrahaKetu.getRasi() + ")" + GrahaKetu.getRasiGrahaInSansc(GrahaKetu.getRasi()) + " Lat.: " + GrahaKetu.getLongitude() + " - " + GrahaKetu.getNote()



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
