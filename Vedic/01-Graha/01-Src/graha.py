from logCartaNatale import LogCartaNatale
from Tabellario import Tabellario

class Graha:
    "La classe Graha"

    szNote = ""
    szGrahaSmall     = ""
    szRetro          = ""
    szGrahaSansc    = ""
    szRasiGrahaExalt  = ""
    szRasiGrahaDebil  = ""
    szRasiGrahaDomic1 = ""
    szRasiGrahaDomic2 = ""
    szRasiGrahaMool   = ""

    iBhavaProgrCusp  = 0
    iBhavaProgr      = 0
    iGrahaProgr      = 0
    iRasiProgr       = 0

    fBhavaLon        = 0.0
    fBhavaLonCusp    = 0.0
    fGrahaLon        = 0.0
    fGrahaLonAss     = 0.0
    fGrahaLonAssFromAsc = 0.0
    fGrahaLonAssFromAscCusp = 0.0
    fLonMoolFrom     = 0.0
    fLonMoolTo       = 0.0
    fKopaStd         = 0.0
    fKopaRetr        = 0.0
    fKobaDiff        = 0.0

    bRetrogade       = False
    bKoba            = False
    bWar             = False
    bBhavaCuspNeg    = False

    szRasiGrahaExaltSmall = ""
    szRasiGrahaExaltSansc = ""
    iRasiGrahaExalt = 0

    szRasiGrahaDebilSmall = ""
    szRasiGrahaDebilSansc = ""
    iRasiGrahaDebil = 0

    szRasiGrahaDomic1Small = ""
    szRasiGrahaDomic1Sansc = ""
    iRasiGrahaDomic1 = 0

    szRasiGrahaDomic2Small = ""
    szRasiGrahaDomic2Sansc = ""
    iRasiGrahaDomic2 = 0

    szRasiGrahaMoolSmall = ""
    szRasiGrahaMoolSansc = ""
    iRasiGrahaMool = 0

    Log = LogCartaNatale
    szMsgPrefix = "Graha - "

    Tab = Tabellario

    def __init__ (self, passLog, Tab, graha, rasi, lon, retro ):
        self.Log = passLog
        self.iGrahaProgr = int(graha)
        self.iRasiProgr  = rasi
        self.fGrahaLon   = lon
        self.szRetro     = retro
        self.Tab = Tab

        self.loadGrahaParameter()

        if(retro == "R"):
            self.bRetrogade = True
            self.Log.scriviLog(2, self.szMsgPrefix + "Pianeta Retrogrado")

        if (self.getRasi() != " - "):
            self.getLongitudeAssolute()
            self.iRasiProgr = int(rasi)
            self.fGrahaLon = float(lon)
            self.Log.scriviLog(2, self.szMsgPrefix + "Graha " + str(self.szGrahaSansc) + " inizializzato con Rasi: " + str(self.Tab.getRasiSanscForProgr(int(self.iRasiProgr))) + " (" + str(self.iRasiProgr) + ") Long: " + str(lon) + " indicazione R: " + retro + "\n")

        self.Log.scriviLog(2, self.szMsgPrefix + "Graha " + str(self.szGrahaSansc) + " inizializzato con Rasi: " + rasi + " Long: " + lon + " indicazione R: " + retro + "\n")

    def loadGrahaParameter(self):
        self.Log.scriviLog(2, self.szMsgPrefix + "Load Graha Parameter from Tab")
        self.Log.scriviLog(2, self.szMsgPrefix + "-----------------------------")
        self.setGrahaSmall()
        self.setGrahaSansc()
        if (self.iGrahaProgr != 0):
            self.setGrahaExalt()
            self.setGrahaDebil()
            self.setGrahaDomic1()
            self.setGrahaDomic2()
            self.setGrahaMoolatrikona()
            self.getKopaDef()
            self.getKopaRetr()
        else:
            self.Log.scriviLog(2, self.szMsgPrefix + "Non calcolabile: Graha e' ASC")



    def showGraha(self):

        self.Log.scriviLog(9, self.szMsgPrefix + "*********************************************")
        self.Log.scriviLog(9, self.szMsgPrefix + "****  Graha " + str(self.szGrahaSansc) + "(" + str(self.szGrahaSmall) + ")  Show")
        self.Log.scriviLog(9, self.szMsgPrefix + "********************************************")
        self.Log.scriviLog(9, self.szMsgPrefix + "Nome graha breve: " + self.szGrahaSmall)
        self.Log.scriviLog(9, self.szMsgPrefix + "Nome graha in sanscrito: " + self.szGrahaSansc)
        if(self.iGrahaProgr != 0):
            self.Log.scriviLog(9, self.szMsgPrefix + "Nel segno: (" + str(self.iRasiProgr) + "): " + self.getRasiSmall(self.iRasiProgr) + " con longitudine: " + str(self.fGrahaLon))
            self.Log.scriviLog(9, self.szMsgPrefix + "Retrogado: " + str(self.bRetrogade))
            self.Log.scriviLog(9, self.szMsgPrefix + "Rasi di esaltazione = " + self.szRasiGrahaExaltSansc + " (" + str(self.iRasiGrahaExalt) + ")")
            self.Log.scriviLog(9, self.szMsgPrefix + "Rasi di debilitazione = " + self.szRasiGrahaDebilSansc + "(" + str(self.iRasiGrahaDebil) + ")")
            self.Log.scriviLog(9, self.szMsgPrefix + "Rasi di domicilio 1 = " + self.szRasiGrahaDomic1Sansc + "(" + str(self.iRasiGrahaDomic1) + ")")
            self.Log.scriviLog(9, self.szMsgPrefix + "Rasi di domicilio 2 = " + self.szRasiGrahaDomic2Sansc + "(" + str(self.iRasiGrahaDomic2) + ")")
            self.Log.scriviLog(9, self.szMsgPrefix + "Rasi Moolatrikona = " + self.szRasiGrahaMoolSansc + "(" + str(self.iRasiGrahaMool) + ")")
            self.Log.scriviLog(9, self.szMsgPrefix + "Longitudine di partenza Moolatrikona = " + str(self.fLonMoolFrom))
            self.Log.scriviLog(9, self.szMsgPrefix + "Longitudine di fine Moolatrikona =" + str(self.fLonMoolTo))
        #self.showGrahaPict()


    def showGrahaPict(self):
        self.Log.scriviLog(9, self.szMsgPrefix + "+----------+")
        self.Log.scriviLog(9, self.szMsgPrefix + "|" + self.getRasiSmall(self.iRasiProgr) + "        |")
        if (self.bRetrogade):
            self.Log.scriviLog(9, self.szMsgPrefix + "|   __     |")
        else:
            self.Log.scriviLog(9, self.szMsgPrefix + "|          |")
        self.Log.scriviLog(9, self.szMsgPrefix + "|   " + str(self.szGrahaSmall) + "     |")
        self.Log.scriviLog(9, self.szMsgPrefix + "|   " + str(self.fGrahaLon).rjust(7) + "|")
        self.Log.scriviLog(9, self.szMsgPrefix + "+----------+")
        self.Log.scriviLog(9, self.szMsgPrefix + self.getNote())
        self.Log.scriviLog(9, self.szMsgPrefix + "\n")

    def checkIsKopa(self, fSunLonAss):
        #Calcola differenza assoluta tra long del sole e quella del graha a seconda che sia retrogado o meno
        # e se occorre, ovvero diversa da zero
        self.Log.scriviLog(2, self.szMsgPrefix + " +-- Verifica se Kopa --+")
        self.Log.scriviLog(2, self.szMsgPrefix + " Long ass. del sole: " + str(fSunLonAss))
        self.Log.scriviLog(2, self.szMsgPrefix + " Long ass. del graha: " + str(self.fGrahaLonAss))
        self.Log.scriviLog(2, self.szMsgPrefix + " Gradi max per Kopa (Std):  " + str(self.fKopaStd))
        self.Log.scriviLog(2, self.szMsgPrefix + " Gradi max per Kopa (Rtr):  " + str(self.fKopaRetr))

        if(self.fKopaStd):
            self.fKobaDiff = format(round(abs(float(fSunLonAss) - float(self.fGrahaLonAss)),2))
            self.Log.scriviLog(2, self.szMsgPrefix + " Differenza Long:  " + str(self.fKobaDiff))
            if (float(self.fKobaDiff) <= float(self.fKopaStd)):
                self.Log.scriviLog(2, self.szMsgPrefix + " Il Graha è in Kopa di gradi =  " + str(self.fKobaDiff))
                self.bKoba = True
        else:
            self.Log.scriviLog(2, self.szMsgPrefix + " Questo Graha non va mai in Kopa ")

        #self.createNote()


    def createNote(self):
        if(self.iRasiProgr == self.iRasiGrahaExalt):
            self.Log.scriviLog(2, self.szMsgPrefix + " ESALTAZIONE")
            self.szNote = self.szNote + " IN ESALTAZIONE"

        if(self.iRasiProgr == self.iRasiGrahaDebil):
            self.Log.scriviLog(2, self.szMsgPrefix + " DEBILITAZIONE")
            self.szNote = self.szNote + " IN DEBILITAZIONE"

        if(self.iRasiProgr == self.iRasiGrahaDomic1 or (self.iRasiProgr == self.iRasiGrahaDomic2)):
            self.Log.scriviLog(2, self.szMsgPrefix + " DOMICILIO")
            self.szNote = self.szNote + " IN DOMICILIO"

        if(self.iRasiProgr == self.iRasiGrahaMool):
            if(self.fGrahaLon >= self.fLonMoolFrom and self.fGrahaLon <= self.fLonMoolTo):
                self.Log.scriviLog(2, self.szMsgPrefix + " MOOLATRIKONA")
                self.szNote = self.szNote + " IN MOOLATRIKONA"

        if(self.bRetrogade):
            self.Log.scriviLog(2, self.szMsgPrefix + " RETROGADO")
            self.szNote = self.szNote + " RETROGADO"

        if(self.bKoba):
            self.Log.scriviLog(2, self.szMsgPrefix + " COMBUSTO")
            if(self.bRetrogade):
                self.szNote = self.szNote + " COMBUSTO di " + str(self.fKobaDiff) + " gradi su " + str(self.fKopaRetr)
            else:
                self.szNote = self.szNote + " COMBUSTO di " + str(self.fKobaDiff) + " gradi su " + str(self.fKopaStd)

        if(self.bWar):
            self.szNote = self.szNote + " IN GUERRA "


    def getGrahaSmall(self):
        return self.szGrahaSmall
        #self.Log.scriviLog(2, self.szMsgPrefix + self.szGrahaSmall)

    def setGrahaSmall(self):
        self.szGrahaSmall=self.Tab.lstGrahaSmall[self.iGrahaProgr]
        self.Log.scriviLog(2, self.szMsgPrefix + "GrahaSmall settato a: " + self.szGrahaSmall)

    def getGrahaProgr(self):
        return self.iGrahaProgr

    def getGrahaSansc(self):
        return self.szGrahaSansc

    def setGrahaSansc(self):
        self.szGrahaSansc=self.Tab.lstGrahaSansc[self.iGrahaProgr]
        self.Log.scriviLog(2, self.szMsgPrefix + "GrahaSansc settato a: " + self.szGrahaSansc)

    def getRasiGrahaExalt(self):
        return self.iRasiGrahaExalt

    def getRasiGrahaDebil(self):
        return self.iRasiGrahaDebil

    def getGrahaDomic1(self):
        return self.iGrahaDomic1

    def getGrahaDomic2(self):
        return self.iGrahaDomic2

    def getRasiGrahaMool(self):
        return self.iRasiGrahaMool

    def getGrahaMoolFrom(self):
        return self.lstGrahaMoolFrom

    def getGrahaMoolTo(self):
        return self.lstGrahaMoolTo

    def getRasiGrahaInSansc(self, iRasi):
        #self.Log.scriviLog(2, self.szMsgPrefix + "iRasi= " + str(iRasi))
        if (int(iRasi) > 0):
            #return self.lstRasiSansc[int(iRasi)-1]
            return self.Tab.lstRasiSansc[int(iRasi) - 1]
        else:
            return "NONE"

    def getRasiSmall(self, iRasi):
        #self.Log.scriviLog(2, self.szMsgPrefix + "iRasi= " + str(iRasi))
        if int(iRasi) > 0:
            return self.Tab.lstRasiSmall[int(iRasi)-1]
        else:
            return "NONE"


    def getRasi(self):
        return self.iRasiProgr


    def getLongitude(self):
        return self.fGrahaLon

    def getLongitudeAssolute(self):
        self.fGrahaLonAss = format(((float(self.iRasiProgr) - 1) * 30 + float(self.fGrahaLon)), ".2f").rjust(6)
        self.Log.scriviLog(2, self.szMsgPrefix + "Long Ass di " + str(self.szGrahaSansc) + ": " + str(self.fGrahaLonAss))
        return self.fGrahaLonAss

    def getKopaDef(self):
        self.fKopaStd=self.Tab.getLongKopaStd(self.iGrahaProgr)

    def getKopaRetr(self):
        self.fKopaRetr=self.Tab.getLongKopaRetro(self.iGrahaProgr)

    def isRetrogade(self):
        return self.bRetrogade

    def getNote(self):
        return self.szNote

    def setPlanetWar(self):
        self.bWar = True
        self.Log.scriviLog(2, self.szMsgPrefix + "Graha " + self.getGrahaSansc() + " impostato in guerra planetaria")
    def getIsWar(self):
        return self.bWar

    def setLonAssFromAsc(self, fAscLonAssFromAsc):
        self.Log.scriviLog(5, self.szMsgPrefix + "Graha " + str(self.szGrahaSansc) + " calcolo Longitudine (Case Piene) da " + str(fAscLonAssFromAsc) + " da ASC")
        if(float(self.getLongitudeAssolute()) > float(fAscLonAssFromAsc)):
            self.fGrahaLonAssFromAsc = format(float(self.getLongitudeAssolute()) - float(fAscLonAssFromAsc), ".2f")
        else:
            self.fGrahaLonAssFromAsc = format((float(self.getLongitudeAssolute())+360) - float(fAscLonAssFromAsc), ".2f")
        self.Log.scriviLog(5, self.szMsgPrefix + "Longitudine Assoluta da ASC: " + str(self.fGrahaLonAssFromAsc))

    def setLonAssFromAscCusp(self, fAscLonAssFromAscCusp):
        self.Log.scriviLog(5, self.szMsgPrefix + "Graha " + str(self.szGrahaSansc) + " calcolo Longitudine (Cuspide) da " + str(fAscLonAssFromAscCusp) + " da ASC")
        if(float(self.getLongitudeAssolute()) > float(fAscLonAssFromAscCusp)):
            self.fGrahaLonAssFromAscCusp = format(float(self.getLongitudeAssolute()) - float(fAscLonAssFromAscCusp) - 15, ".2f")
        else:
            self.fGrahaLonAssFromAscCusp = format((float(self.getLongitudeAssolute())+360) - float(fAscLonAssFromAscCusp) - 15, ".2f")
        self.Log.scriviLog(5, self.szMsgPrefix + "Longitudine Assoluta da ASC: " + str(self.fGrahaLonAssFromAscCusp))

        if(float(self.fGrahaLonAssFromAscCusp) < 0):
            self.fGrahaLonAssFromAscCusp = 30 + float(self.fGrahaLonAssFromAscCusp)
            self.bBhavaCuspNeg = True
            self.Log.scriviLog(2, self.szMsgPrefix + "Calcolo con ASC Cuspide risulta negativo. Settato il flag bBhavaCuspNeg a:" + str(self.bBhavaCuspNeg))

    def setBhava(self):
        self.Log.scriviLog(5, self.szMsgPrefix + "Graha " + str(self.szGrahaSansc) + " calcolo Bhava con Case Piene da " + str(self.fGrahaLonAssFromAsc) + " da ASC")
        self.iBhavaProgr = int(float(self.fGrahaLonAssFromAsc)/30)+1
        self.fBhavaLon = format(float(self.fGrahaLonAssFromAsc)-(self.iBhavaProgr-1)*30, ".2f")
        self.Log.scriviLog(5, self.szMsgPrefix + "Bhava di " + str(self.szGrahaSansc) + ": " + str(self.iBhavaProgr) + " e Long: " + str(self.fBhavaLon))

    def setBhavaCusp(self):
        self.Log.scriviLog(5, self.szMsgPrefix + "Graha " + str(self.szGrahaSansc) + " calcolo Bhava con Cuspide da " + str(self.fGrahaLonAssFromAscCusp) + " da ASC")
        self.iBhavaProgrCusp = int(float(self.fGrahaLonAssFromAscCusp)/30)+1
        self.fBhavaLonCusp = format(float(self.fGrahaLonAssFromAscCusp)-(self.iBhavaProgrCusp-1)*30, ".2f")
        self.Log.scriviLog(5, self.szMsgPrefix + "Bhava di " + str(self.szGrahaSansc) + ": " + str(self.iBhavaProgrCusp) + " e Long: " + str(self.fBhavaLonCusp))

        if(self.bBhavaCuspNeg):
            self.Log.scriviLog(2, self.szMsgPrefix + "bBhavaCuspNeg a:" + str(self.bBhavaCuspNeg) + " Retrocedo di una Bhava")
            self.iBhavaProgrCusp = self.iBhavaProgrCusp - 1
            if(self.iBhavaProgrCusp == 0):
                self.Log.scriviLog(2, self.szMsgPrefix + "il progressivo della Bhava è zero. Lo setto a 12")
                self.iBhavaProgrCusp = 12

    def getBhava(self):
        return str(self.iBhavaProgr).rjust(2)

    def getBhavaLon(self):
        return str(self.fBhavaLon).rjust(5)

    def getBhavaCusp(self):
        return str(self.iBhavaProgrCusp).rjust(2)

    def getBhavaLonCusp(self):
        return str(self.fBhavaLonCusp).rjust(5)

    def setGrahaExalt(self):
        self.iRasiGrahaExalt = int(self.Tab.getRasiGrahaExaltProgr(self.iGrahaProgr))
        self.szRasiGrahaExaltSmall = self.Tab.getRasiSmallForProgr(self.iRasiGrahaExalt)
        self.szRasiGrahaExaltSansc = self.Tab.getRasiSanscForProgr(self.iRasiGrahaExalt)
        self.Log.scriviLog(2, self.szMsgPrefix + "Rasi di esaltazione: iProgr= " + str(
            self.iRasiGrahaExalt) + " , Small: " + self.szRasiGrahaExaltSmall + " , Sansc: " + self.szRasiGrahaExaltSansc)

    def setGrahaDebil(self):
        self.iRasiGrahaDebil = int(self.Tab.getRasiGrahaDebilProgr(self.iGrahaProgr))
        self.szRasiGrahaDebilSmall = self.Tab.getRasiSmallForProgr(self.iRasiGrahaDebil)
        self.szRasiGrahaDebilSansc = self.Tab.getRasiSanscForProgr(self.iRasiGrahaDebil)
        self.Log.scriviLog(2, self.szMsgPrefix + "Rasi di debilitazione: iProgr= " + str(
            self.iRasiGrahaDebil) + " , Small: " + self.szRasiGrahaDebilSmall + " , Sansc: " + self.szRasiGrahaDebilSansc)

    def setGrahaDomic1(self):
        self.iRasiGrahaDomic1 = int(self.Tab.getRasiGrahaDomic1Progr(self.iGrahaProgr))
        self.szRasiGrahaDomic1Small = self.Tab.getRasiSmallForProgr(self.iRasiGrahaDomic1)
        self.szRasiGrahaDomic1Sansc = self.Tab.getRasiSanscForProgr(self.iRasiGrahaDomic1)
        self.Log.scriviLog(2, self.szMsgPrefix + "Rasi di Primo Domicilio: iProgr= " + str(
            self.iRasiGrahaDomic1) + " , Small: " + self.szRasiGrahaDomic1Small + " , Sansc: " + self.szRasiGrahaDomic1Sansc)

    def setGrahaDomic2(self):
        self.iRasiGrahaDomic2 = int(self.Tab.getRasiGrahaDomic2Progr(self.iGrahaProgr))
        self.szRasiGrahaDomic2Small = self.Tab.getRasiSmallForProgr(self.iRasiGrahaDomic2)
        self.szRasiGrahaDomic2Sansc = self.Tab.getRasiSanscForProgr(self.iRasiGrahaDomic2)
        self.Log.scriviLog(2, self.szMsgPrefix + "Rasi di Secondo Domicilio: iProgr= " + str(
            self.iRasiGrahaDomic2) + " , Small: " + self.szRasiGrahaDomic2Small + " , Sansc: " + self.szRasiGrahaDomic2Sansc)

    def setGrahaMoolatrikona(self):
        self.iRasiGrahaMool = int(self.Tab.getRasiGrahaMoolProgr(self.iGrahaProgr))
        self.szRasiGrahaMoolSmall = self.Tab.getRasiSmallForProgr(self.iRasiGrahaMool)
        self.szRasiGrahaMoolSansc = self.Tab.getRasiSanscForProgr(self.iRasiGrahaMool)
        self.fLonMoolFrom = float(self.Tab.getRasiGrahaMoolLongFromProgr(self.iGrahaProgr))
        self.fLonMoolTo = float(self.Tab.getRasiGrahaMoolLongToProgr(self.iGrahaProgr))
        self.Log.scriviLog(2, self.szMsgPrefix + "Rasi di Moolatrikona: iProgr= " + str(
            self.iRasiGrahaMool) + " , Small: " + self.szRasiGrahaMoolSmall + " , Sansc: " + self.szRasiGrahaMoolSansc)
        self.Log.scriviLog(2, self.szMsgPrefix + "Long. di Moolatrikona da: " + str(self.fLonMoolFrom) + "  a: " + str(
            self.fLonMoolTo))


