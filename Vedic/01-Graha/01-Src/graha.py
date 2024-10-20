from logCartaNatale import LogCartaNatale

class Graha:
    "La classe Graha"

    szConfGrahaFileName   = ""
    szConfRasiFileName    = ""
    szGrahaSmall     = ""
    iGrahaProgr      = 0
    iRasiProgr       = 0
    fGrahaLon        = 0.0
    szGrahaSansc    = ""
    iRasiGrahaExalt  = 0
    iRasiGrahaDebil  = 0
    iRasiGrahaDomic1 = 0
    iRasiGrahaDomic2 = 0
    iRasiGrahaMool   = 0
    fLonMoolFrom     = 0.0
    fLonMoolTo       = 0.0

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

    Log = LogCartaNatale
    szMsgPrefix = "Graha - "

    def __init__ (self, passLog, confGrahaFileName, confRasiFileName, graha, rasi, lon ):
        self.Log = passLog
        self.szConfGrahaFileName = confGrahaFileName
        self.szConfRasiFileName = confRasiFileName
        self.iGrahaProgr = graha
        self.iRasiProgr = rasi
        self.fGrahaLon  = lon
        self.Log.scriviLog(2, "\n\n" )

        self.Log.scriviLog(2, self.szMsgPrefix + "istanziata con file di input: " + self.szConfGrahaFileName + " e " + self.szConfRasiFileName )
        self.Log.scriviLog(2, self.szMsgPrefix + "Parametri iniziali: graha=" + str(self.iGrahaProgr) + ", rasi=" + str(self.iRasiProgr) + ", longitudine=" + str(self.fGrahaLon))


        #Carica file di configurazione per auto-configurarsi
        self.loadGrahaFile()
        self.loadRasiFile()
        #self.showGraha()


    def loadGrahaFile(self):
        #"Carica sia le liste dei graha che i parametri di default del graha"
        file_input = open(self.szConfGrahaFileName, "r", encoding='utf-8')
        i = 1
        for line in file_input.readlines():
            #print("-------------------------------------------")
            #print("Riga " + str(i) + ": " + line)
            line_content = line.split("|")
            #print(line_content)
            #Caricamento lista GrahaSmall
            #Caricamento del graha corretto
            #print(line_content[1] + " - " + str(self.iGrahaProgr))
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
            i=i+1
        file_input.close()

    def loadRasiFile(self):
    #"Carica sia le liste dei graha che i parametri di default del graha"
        file_input = open(self.szConfRasiFileName, "r", encoding='utf-8')
        i = 1
        for line in file_input.readlines():
            #print("-------------------------------------------")
            #print("Riga " + str(i) + ": " + line)
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
        self.Log.scriviLog(2, self.szMsgPrefix + "*********************************************")
        self.Log.scriviLog(2, self.szMsgPrefix + "****  Graha " + self.szGrahaSansc + "(" + self.szGrahaSmall + ")  Show")
        self.Log.scriviLog(2, self.szMsgPrefix + "********************************************")
        self.Log.scriviLog(2, self.szMsgPrefix + "Nome graha breve: " + self.szGrahaSmall)
        self.Log.scriviLog(2, self.szMsgPrefix + "Nome graha in sanscrito: " + self.szGrahaSansc)
        self.Log.scriviLog(2, self.szMsgPrefix + "Nel segno: (" + str(self.iRasiProgr) + "): " + self.getRasiSmall(self.iRasiProgr) + " con longitudine: " + str(self.fGrahaLon))
        self.Log.scriviLog(2, self.szMsgPrefix + "Rasi di esaltazione = " + self.getRasiGrahaInSansc(self.iRasiGrahaExalt) + "(" + self.iRasiGrahaExalt + ")")
        self.Log.scriviLog(2, self.szMsgPrefix + "Rasi di debilitazione = " + self.getRasiGrahaInSansc(self.iRasiGrahaDebil) + "(" + self.iRasiGrahaDebil + ")")
        self.Log.scriviLog(2, self.szMsgPrefix + "Rasi di domicilio 1 = " + self.getRasiGrahaInSansc(self.iRasiGrahaDomic1) + "(" + self.iRasiGrahaDomic1 + ")")
        self.Log.scriviLog(2, self.szMsgPrefix + "Rasi di domicilio 2 = " + self.getRasiGrahaInSansc(self.iRasiGrahaDomic2) + "(" + self.iRasiGrahaDomic2 + ")")
        self.Log.scriviLog(2, self.szMsgPrefix + "Rasi Moolatrikona = " + self.getRasiGrahaInSansc(self.iRasiGrahaMool) + "(" + self.iRasiGrahaMool + ")")
        self.Log.scriviLog(2, self.szMsgPrefix + "Longitudine di partenza Moolatrikona = " + self.fLonMoolFrom)
        self.Log.scriviLog(2, self.szMsgPrefix + "Longitudine di fine Moolatrikona =" + self.fLonMoolTo)
        self.showGrahaPict()

    def showGrahaPict(self):
        self.Log.scriviLog(2, self.szMsgPrefix + "+----------+")
        self.Log.scriviLog(2, self.szMsgPrefix + "|" + self.getRasiSmall(self.iRasiProgr) + "        |")
        self.Log.scriviLog(2, self.szMsgPrefix + "|   " + self.szGrahaSmall + "     |")
        self.Log.scriviLog(2, self.szMsgPrefix + "|   " + self.fGrahaLon + "|")
        self.Log.scriviLog(2, self.szMsgPrefix + "+----------+")
        if(self.iRasiProgr == self.iRasiGrahaExalt):
            self.Log.scriviLog(2, self.szMsgPrefix + " ESALTAZIONE")

        if(self.iRasiProgr == self.iRasiGrahaDebil):
            self.Log.scriviLog(2, self.szMsgPrefix + " DEBILITAZIONE")

        if(self.iRasiProgr == self.iRasiGrahaDomic1 or self.iRasiProgr == self.iRasiGrahaDomic2):
            self.Log.scriviLog(2, self.szMsgPrefix + " DOMICILIO")

        self.Log.scriviLog(2, self.szMsgPrefix + "\n")

    def getGrahaSmall(self):
        return self.szGrahaSmall
        self.Log.scriviLog(2, self.szMsgPrefix + self.szGrahaSmall)

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
