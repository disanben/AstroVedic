from logCartaNatale import LogCartaNatale

class LoadGraha:
    "La classe LoadGraha, legge il file di input [Nome].txt ed istanzia le classi dei pianeti"

    inputFileName = ""
    lstGrahaSmall = []
    lstGrahaProgr = []
    lstGrahaSansc = []
    lstTipoAK = []
    lstRasiSmall = []
    lstRasiProgr = []
    lstGrahaLng = []
    lstNakName = []
    lstNakProgr = []
    lstNakReg = []
    lstNakPada = []
    lstRetrogade  = []

    szName = ""
    szCitta = ""
    szData = ""
    szCittaLat=""
    szCittaLon=""
    szOra = ""

    bAsc = True

    Log = LogCartaNatale
    szMsgPrefix = "Load Graha"


    def __init__ (self, passLog, szInputFileName):
        self.inputFileName = szInputFileName
        self.Log = passLog
        print("Nome del file di input: " + self.inputFileName)
        self.Log.scriviLog(2, self.szMsgPrefix + " - istanziata con file di input: " + self.inputFileName)

    def loadGrahaFile(self):

        file_input = open(self.inputFileName, "r", encoding='utf-8')

        #Benedetto|10.06.1966|01:35|Catania|37.4716N|14.8473E|
        header=file_input.readline()
        header_content=header.split("|")

        self.szName     = header_content[0]
        self.szData     = header_content[1]
        self.szOra      = header_content[2]
        self.szCitta    = header_content[3]
        self.szCittaLat = header_content[4]
        self.szCittaLon = header_content[5]

        self.Log.scriviLog(9, self.szMsgPrefix + "\n\n")
        self.Log.scriviLog(9, self.szMsgPrefix + "-----------------------------------------------------------------------------------------")
        self.Log.scriviLog(9, self.szMsgPrefix + " -                    Lettura dati di nascita di: " + self.szName)
        self.Log.scriviLog(9, self.szMsgPrefix + " -     Nato il: " + self.szData + " alle ore: " + self.szOra + " a " + self.szCitta + " (" + self.szCittaLat + " - " + self.szCittaLon + ")")
        self.Log.scriviLog(9, self.szMsgPrefix + "-----------------------------------------------------------------------------------------")


        i = 1
        for line in file_input.readlines():
            self.Log.scriviLog(2, self.szMsgPrefix + "--------- Input File ------------")
            self.Log.scriviLog(2, self.szMsgPrefix + "Riga " + str(i) + ": " + line)
            line_content = line.split("|")
            #print(line_content)
            #Caricamento lista GrahaSmall
            self.lstGrahaSmall.append(line_content[0])
            self.lstGrahaProgr.append(line_content[1])
            self.lstGrahaSansc.append(line_content[2])
            self.lstTipoAK.append(line_content[3])
            self.lstRasiSmall.append(line_content[4])
            self.lstRasiProgr.append(line_content[5])
            self.lstGrahaLng.append(line_content[6])
            #self.lstNakName.append(line_content[7])
            self.lstNakProgr.append(line_content[7])
            #self.lstNakReg.append(line_content[9])
            self.lstNakPada.append(line_content[8])
            self.lstRetrogade.append(line_content[9])


            i=i+1
        file_input.close()
        self.Log.scriviLog(2, self.szMsgPrefix + " - Caricamento Graha presenti in " + self.inputFileName + " --> PASSED")

        if(self.szOra == "XX:XX"):
            self.Log.scriviLog(9, self.szMsgPrefix + " - Ora di nascita ignota - Ascendente e Case non calcolate")
            self.lstRasiSmall[0]=" - "
            self.lstRasiProgr[0]=" - "
            self.lstGrahaLng[0]=" - "
            #self.lstNakName.append(line_content[7])
            self.lstNakProgr[0]=" - "
            #self.lstNakReg.append(line_content[9])
            self.lstNakPada[0]=" - "
            self.bAsc=False



    def getLstGrahaSmall(self):
        return self.lstGrahaSmall

    def getLstGrahaProgr(self):
        return self.lstGrahaProgr

    def getLstGrahaSansc(self):
        return self.lstGrahaSansc

    def getLstTipoAK(self):
        return self.lstTipoAK

    def getLstRasiSmall(self):
        return self.lstRasiSmall

    def getLstRasiProgr(self):
        return self.lstRasiProgr

    def getLstGrahaLng(self):
        return self.lstGrahaLng

    def getLstNakName(self):
        return self.lstNakName

    def getLstNakProgr(self):
        return self.lstNakProgr

    def getLstNakReg(self):
        return self.lstNakReg

    def getLstNakPada(self):
        return self.lstNakPada

#Sun
    def getSunRasi(self):
        return self.lstRasiProgr[1]
    def getSunLong(self):
        return self.lstGrahaLng[1]
    def getSunRetro(self):
        return self.lstRetrogade[1]
#Moon
    def getMoonRasi(self):
        return self.lstRasiProgr[2]
    def getMoonLong(self):
        return self.lstGrahaLng[2]
    def getMoonRetro(self):
        return self.lstRetrogade[2]

#Mars
    def getMarsRasi(self):
        return self.lstRasiProgr[3]
    def getMarsLong(self):
        return self.lstGrahaLng[3]
    def getMarsRetro(self):
        return self.lstRetrogade[3]

#Mercury
    def getMercuryRasi(self):
        return self.lstRasiProgr[4]
    def getMercuryLong(self):
        return self.lstGrahaLng[4]
    def getMercuryRetro(self):
        return self.lstRetrogade[4]

#Jupiter
    def getJupiterRasi(self):
        return self.lstRasiProgr[5]
    def getJupiterLong(self):
        return self.lstGrahaLng[5]
    def getJupiterRetro(self):
        return self.lstRetrogade[5]

#Venus
    def getVenusRasi(self):
        return self.lstRasiProgr[6]
    def getVenusLong(self):
        return self.lstGrahaLng[6]
    def getVenusRetro(self):
        return self.lstRetrogade[6]

#Saturn
    def getSaturnRasi(self):
        return self.lstRasiProgr[7]
    def getSaturnLong(self):
        return self.lstGrahaLng[7]
    def getSaturnRetro(self):
        return self.lstRetrogade[7]

#Rahu
    def getRahuRasi(self):
        return self.lstRasiProgr[8]
    def getRahuLong(self):
        return self.lstGrahaLng[8]
    def getRahuRetro(self):
        return self.lstRetrogade[8]

#Ketu
    def getKetuRasi(self):
        return self.lstRasiProgr[9]
    def getKetuLong(self):
        return self.lstGrahaLng[9]
    def getKetuRetro(self):
        return self.lstRetrogade[9]

#Asc
    def getAscRasi(self):
        return self.lstRasiProgr[0]
    def getAscLong(self):
        return self.lstGrahaLng[0]
    def getAscTrue(self):
        return self.bAsc
