from logCartaNatale import LogCartaNatale

class Tabellario:
    "La classe Tabellario"


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
    szMsgPrefix = "Tabellario - "

    def __init__ (self, passLog, confGrahaFileName, confRasiFileName):
        self.Log = passLog
        self.szConfGrahaFileName = confGrahaFileName
        self.szConfRasiFileName = confRasiFileName

        self.Log.scriviLog(2, "\n\n" )

        self.Log.scriviLog(2, self.szMsgPrefix + "*******************************")
        self.Log.scriviLog(2, self.szMsgPrefix + "     Crazione del Tabellario ")
        self.Log.scriviLog(2, self.szMsgPrefix + "*******************************\n\n")
        self.Log.scriviLog(2, self.szMsgPrefix + "istanziata con file di input: " + self.szConfGrahaFileName + " e " + self.szConfRasiFileName )


        #Carica file di configurazione per auto-configurarsi
        self.loadGrahaFile()
        self.loadRasiFile()


    def loadGrahaFile(self):
        #"Carica sia le liste dei graha che i parametri di default del graha"
        self.Log.scriviLog(2, self.szMsgPrefix + "+------------------------------+")
        self.Log.scriviLog(2, self.szMsgPrefix + "+ Caricamento info per i Graha +")
        self.Log.scriviLog(2, self.szMsgPrefix + "+------------------------------+\n")
        file_input = open(self.szConfGrahaFileName, "r", encoding='utf-8')
        i = 1
        for line in file_input.readlines():
            #self.Log.scriviLog(2, self.szMsgPrefix + "------- Graha File -----------")
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

            i=i+1
        file_input.close()
        self.Log.scriviLog(2, self.szMsgPrefix + " - Dati presenti nel file di input caricati nelle liste: lstGrahaSmall, lstGrahaProgr, lstGrahaSansc, lstRasiGrahaExalt, lstRasiGrahaDebil, lstRasiGrahaDomic1, lstRasiGrahaDomic2, lstRasiGrahaMool, lstLonMoolFrom, lstLonMoolTo, lstKopaGrahaStd, lstKopaGrahaRetro")
        self.Log.scriviLog(2, self.szMsgPrefix + " - Caricamento Graha presenti in " + self.szConfGrahaFileName + " --> PASSED\n")



    def loadRasiFile(self):
        #"Carica sia le liste dei graha che i parametri di default del graha"
        self.Log.scriviLog(2, self.szMsgPrefix + "+------------------------------+")
        self.Log.scriviLog(2, self.szMsgPrefix + "+ Caricamento info per i Rasi  +")
        self.Log.scriviLog(2, self.szMsgPrefix + "+------------------------------+\n")
        file_input = open(self.szConfRasiFileName, "r", encoding='utf-8')
        i = 1
        for line in file_input.readlines():
            #self.Log.scriviLog(2, self.szMsgPrefix + "-------- Rasi File ------------")
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
        self.Log.scriviLog(2, self.szMsgPrefix + " - Dati presenti nel file di input caricati nelle liste: lstRasiSmall, lstRasiProgr, lstRasiSansc")
        self.Log.scriviLog(2, self.szMsgPrefix + " - Caricamento Graha presenti in " + self.szConfGrahaFileName + " --> PASSED\n")

    def getRasiGrahaExaltProgr(self, iGrahaProgr):
        return self.lstRasiGrahaExalt[iGrahaProgr]

    def getRasiGrahaDebilProgr(self, iGrahaProgr):
        return self.lstRasiGrahaDebil[iGrahaProgr]

    def getRasiGrahaDomic1Progr(self, iGrahaProgr):
        return self.lstRasiGrahaDomic1[iGrahaProgr]

    def getRasiGrahaDomic2Progr(self, iGrahaProgr):
        return self.lstRasiGrahaDomic2[iGrahaProgr]

    def getRasiGrahaMoolProgr(self, iGrahaProgr):
        return self.lstRasiGrahaMool[iGrahaProgr]

    def getRasiGrahaMoolLongFromProgr(self, iGrahaProgr):
        return self.lstLonMoolFrom[iGrahaProgr]

    def getRasiGrahaMoolLongToProgr(self, iGrahaProgr):
        return self.lstLonMoolTo[iGrahaProgr]

    def getRasiSmallForProgr(self, iRasiProgr):
        if(iRasiProgr > 1):
            return self.lstRasiSmall[iRasiProgr-1]
        else:
            return "NONE"

    def getRasiSanscForProgr(self, iRasiProgr):
        if (iRasiProgr > 1):
            return self.lstRasiSansc[iRasiProgr - 1]
        else:
            return "NONE"

    def getLongKopaStd(self, iGrahaProgr):
        return self.lstKopaGrahaStd[iGrahaProgr]

    def getLongKopaRetro(self, iGrahaProgr):
        return self.lstKopaGrahaRetro[iGrahaProgr]