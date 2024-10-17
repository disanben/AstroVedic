class GRAHA:
    "La classe Graha"

    inputFileName    = ""
    szGrahaSmall     = ""
    iGrahaProgr     = 0
    sztGrahaSansc    = ""
    iRasiGrahaExalt  = 0
    iRasiGrahaDebil  = 0
    iRasiGrahaDomic1 = 0
    iRasiGrahaDomic2 = 0
    iRasiGrahaMool   = 0
    fLonMoolFrom     = 0.0
    fLonMoolTo       = 0.0


    def __init__ (self, szInputFileName):
        self.inputFileName = szInputFileName
        print("Classe Graha istanziata con file: " + self.inputFileName)

    def loadGrahaFile(self):

        file_input = open(self.inputFileName, "r", encoding='utf-8')
        i = 1
        for line in file_input.readlines():
            print("-------------------------------------------")
            print("Riga " + str(i) + ": " + line)
            line_content = line.split("|")
            print(line_content)
            #Caricamento lista GrahaSmall
            self.szGrahaSmall.append(line_content[1])
            self.iGrahaProgr.append(line_content[1])
            self.sztGrahaSansc.append(line_content[1])
            self.iRasiGrahaExalt.append(line_content[1])
            self.iRasiGrahaDebil.append(line_content[1])
            self.iRasiGrahaDomic1.append(line_content[1])
            self.iRasiGrahaDomic2.append(line_content[1])
            self.iRasiGrahaMool.append(line_content[1])
            self.fLonMoolFrom.append(line_content[1])
            self.fLonMoolTo.append(line_content[1])

            i=i+1
            print()
        file_input.close()

    def getGrahaSmall(self):
        return self.szGrahaSmall

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
