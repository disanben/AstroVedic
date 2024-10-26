from logCartaNatale import LogCartaNatale

class Graha:
    "La classe Graha"

    szNote = ""
    szConfGrahaFileName   = ""
    szConfRasiFileName    = ""
    szConfKopaFileName      = ""
    szGrahaSmall     = ""
    szRetro          = ""
    iBhava           = 0
    iBhavaLon        = 0.0
    iGrahaProgr      = 0
    iRasiProgr       = 0
    fGrahaLon        = 0.0
    fGrahaLonAss    = 0.0
    fGrahaLonAssFromAsc = 0.0
    szGrahaSansc    = ""
    iRasiGrahaExalt  = 0
    iRasiGrahaDebil  = 0
    iRasiGrahaDomic1 = 0
    iRasiGrahaDomic2 = 0
    iRasiGrahaMool   = 0
    fLonMoolFrom     = 0.0
    fLonMoolTo       = 0.0
    fKopaStd         = 0.0
    fKopaRetr        = 0.0
    fKobaDiff        = 0.0
    bRetrogade       = False
    bKoba            = False
    bWar             = False

    lstGrahaSmall      = []
    lstGrahaProgr      = []
    lstGrahaSansc      = []
    lstRasiGrahaExalt  = []
    lstRasiGrahaDebil  = []
    lstRasiGrahaDomic1 = []
    lstRasiGrahaDomic2 = []
    lstRasiGrahaMool   = []
    lstLonMoolFrom     = []
    lstLonMoolTo       = []
    lstRasiSmall       = []
    lstRasiProgr       = []
    lstRasiSansc       = []

    lstKopaGrahaStd         = []
    lstKopaGrahaRetro       = []

    Log = LogCartaNatale
    szMsgPrefix = "Graha - "

    def __init__ (self, passLog, confGrahaFileName, confRasiFileName, graha, rasi, lon, retro ):
        self.Log = passLog
        self.szConfGrahaFileName = confGrahaFileName
        self.szConfRasiFileName = confRasiFileName
        self.iGrahaProgr = graha
        self.iRasiProgr = rasi
        self.fGrahaLon  = lon
        self.szRetro    = retro
        self.Log.scriviLog(2, "\n\n" )

        self.Log.scriviLog(2, self.szMsgPrefix + "istanziata con file di input: " + self.szConfGrahaFileName + " e " + self.szConfRasiFileName )
        self.Log.scriviLog(2, self.szMsgPrefix + "Parametri iniziali: graha=" + str(self.iGrahaProgr) + ", rasi=" + str(self.iRasiProgr) + ", longitudine=" + str(self.fGrahaLon) + " e indicazione: " + self.szRetro )

        if(retro == "R"):
            self.bRetrogade = True
            self.Log.scriviLog(2, self.szMsgPrefix + "Pianeta Retrogrado")

        #Carica file di configurazione per auto-configurarsi
        self.loadGrahaFile()
        self.loadRasiFile()

        if (self.getRasi() != " - "):
            self.getLongitudeAssolute()


    def loadGrahaFile(self):
        #"Carica sia le liste dei graha che i parametri di default del graha"
        file_input = open(self.szConfGrahaFileName, "r", encoding='utf-8')
        i = 1
        for line in file_input.readlines():
            self.Log.scriviLog(2, self.szMsgPrefix + "------- Graha File -----------")
            self.Log.scriviLog(2, self.szMsgPrefix + "Riga " + str(i) + ": " + line)
            line_content = line.split("|")

            self.lstGrahaSmall.append(line_content[0])
            self.lstGrahaProgr.append(line_content[1])
            self.lstGrahaSansc.append(line_content[2])
            self.lstRasiGrahaExalt.append(line_content[3])
            self.lstRasiGrahaDebil.append(line_content[4])
            self.lstRasiGrahaDomic1.append(line_content[5])
            self.lstRasiGrahaDomic2.append(line_content[6])
            self.lstRasiGrahaMool.append(line_content[7])
            self.lstLonMoolFrom.append(line_content[8])
            self.lstLonMoolTo.append(line_content[9])
            self.lstKopaGrahaStd.append(line_content[10])
            self.lstKopaGrahaRetro.append(line_content[11])

            if line_content[1] == str(self.iGrahaProgr):
                #print("Trovato graha corretto. Caricamento dei parametri di default")
                #Su|1|Surya  | 1| 7| 5| 5|0|0|
                self.szGrahaSmall     = line_content[0]
                self.szGrahaSansc    = line_content[2]
                self.iRasiGrahaExalt  = line_content[3]
                self.iRasiGrahaDebil  = line_content[4]
                self.iRasiGrahaDomic1 = line_content[5]
                self.iRasiGrahaDomic2 = line_content[6]
                self.iRasiGrahaMool   = line_content[7]
                self.fLonMoolFrom     = line_content[8]
                self.fLonMoolTo       = line_content[9]
                self.fKopaStd         = line_content[10]
                self.fKopaRetr        = line_content[11]
            i=i+1
        file_input.close()


    def loadRasiFile(self):
    #"Carica sia le liste dei graha che i parametri di default del graha"
        file_input = open(self.szConfRasiFileName, "r", encoding='utf-8')
        i = 1
        for line in file_input.readlines():
            self.Log.scriviLog(2, self.szMsgPrefix + "-------- Rasi File ------------")
            self.Log.scriviLog(2, self.szMsgPrefix + "Riga " + str(i) + ": " + line)
            line_content = line.split("|")
            #print(line_content)
            #Caricamento lista GrahaSmall
            #Caricamento del graha corretto
            #print(line_content[1] + " - " + str(self.iGrahaProgr))
            self.lstRasiSmall.append(line_content[0])
            self.lstRasiProgr.append(line_content[1])
            self.lstRasiSansc.append(line_content[2])
            i=i+1
        file_input.close()


    def showGraha(self):
        szGrahaNameInSans = self.getRasiGrahaInSansc(self.iRasiProgr)
        self.Log.scriviLog(9, self.szMsgPrefix + "*********************************************")
        self.Log.scriviLog(9, self.szMsgPrefix + "****  Graha " + self.szGrahaSansc + "(" + self.szGrahaSmall + ")  Show")
        self.Log.scriviLog(9, self.szMsgPrefix + "********************************************")
        self.Log.scriviLog(9, self.szMsgPrefix + "Nome graha breve: " + self.szGrahaSmall)
        self.Log.scriviLog(9, self.szMsgPrefix + "Nome graha in sanscrito: " + self.szGrahaSansc)
        self.Log.scriviLog(9, self.szMsgPrefix + "Nel segno: (" + str(self.iRasiProgr) + "): " + self.getRasiSmall(self.iRasiProgr) + " con longitudine: " + str(self.fGrahaLon))
        self.Log.scriviLog(9, self.szMsgPrefix + "Retrogado: " + self.bRetrogade)
        self.Log.scriviLog(9, self.szMsgPrefix + "Rasi di esaltazione = " + self.getRasiGrahaInSansc(self.iRasiGrahaExalt) + "(" + self.iRasiGrahaExalt + ")")
        self.Log.scriviLog(9, self.szMsgPrefix + "Rasi di debilitazione = " + self.getRasiGrahaInSansc(self.iRasiGrahaDebil) + "(" + self.iRasiGrahaDebil + ")")
        self.Log.scriviLog(9, self.szMsgPrefix + "Rasi di domicilio 1 = " + self.getRasiGrahaInSansc(self.iRasiGrahaDomic1) + "(" + self.iRasiGrahaDomic1 + ")")
        self.Log.scriviLog(9, self.szMsgPrefix + "Rasi di domicilio 2 = " + self.getRasiGrahaInSansc(self.iRasiGrahaDomic2) + "(" + self.iRasiGrahaDomic2 + ")")
        self.Log.scriviLog(9, self.szMsgPrefix + "Rasi Moolatrikona = " + self.getRasiGrahaInSansc(self.iRasiGrahaMool) + "(" + self.iRasiGrahaMool + ")")
        self.Log.scriviLog(9, self.szMsgPrefix + "Longitudine di partenza Moolatrikona = " + self.fLonMoolFrom)
        self.Log.scriviLog(9, self.szMsgPrefix + "Longitudine di fine Moolatrikona =" + self.fLonMoolTo)
        self.showGrahaPict()

    def showGrahaPict(self):
        self.Log.scriviLog(9, self.szMsgPrefix + "+----------+")
        self.Log.scriviLog(9, self.szMsgPrefix + "|" + self.getRasiSmall(self.iRasiProgr) + "        |")
        self.Log.scriviLog(9, self.szMsgPrefix + "|   " + self.szGrahaSmall + "     |")
        self.Log.scriviLog(9, self.szMsgPrefix + "|   " + self.fGrahaLon + "|")
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
                self.Log.scriviLog(2, self.szMsgPrefix + " Il Graha è in Koba di gradi =  " + str(self.fKobaDiff))
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

        if(self.iRasiProgr == self.iRasiGrahaDomic1 or self.iRasiProgr == self.iRasiGrahaDomic2):
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

    def getGrahaProgr(self):
        return self.iGrahaProgr

    def getGrahaSansc(self):
        return self.szGrahaSansc

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
            return self.lstRasiSansc[int(iRasi)-1]
        else:
            return "NONE"

    def getRasiSmall(self, iRasi):
        #self.Log.scriviLog(2, self.szMsgPrefix + "iRasi= " + str(iRasi))
        if int(iRasi) > 0:
            return self.lstRasiSmall[int(iRasi)-1]
        else:
            return "NONE"

    def getRasi(self):
        return self.iRasiProgr


    def getLongitude(self):
        return self.fGrahaLon

    def getLongitudeAssolute(self):
        self.fGrahaLonAss = format(((float(self.iRasiProgr) - 1) * 30 + float(self.fGrahaLon)), ".2f").rjust(6)
        self.Log.scriviLog(2, self.szMsgPrefix + " Long Ass di " + self.getGrahaSansc() + ": " + str(self.fGrahaLonAss))
        return self.fGrahaLonAss

    def getKopaDef(self):
        return self.lstGrahaMoolTo

    def getKopaRetr(self):
        return self.lstGrahaMoolTo

    def isRetrogade(self):
        return self.bRetrogade

    def getNote(self):
        return self.szNote

    def setPlanetWar(self):
        self.bWar = True
        self.Log.scriviLog(2, self.szMsgPrefix + "Graha " + self.getGrahaSansc() + " impostato in guerra planetaria")
    def getIsWar(self):
        return self.bWar

    def setLon(self, fAscLonAssFromAsc):
        self.Log.scriviLog(2, self.szMsgPrefix + "Graha " + self.getGrahaSansc() + " calcolo Bhava da " + str(fAscLonAssFromAsc) + " da ASC")
        self.fGrahaLonAssFromAsc = 0.0