class LoadGraha:
    "La classe LoadGraha"

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


    def __init__ (self, szInputFileName):
        print("Classe LoadGraha istanziata")

        self.inputFileName = szInputFileName
        print("Nome del file di input: " + self.inputFileName)

    def loadGrahaFile(self):

        file_input = open(self.inputFileName, "r", encoding='utf-8')
        i = 1
        for line in file_input.readlines():
            print("-------------------------------------------")
            print("Riga " + str(i) + ": " + line)
            line_content = line.split("|")
            print(line_content)
            #Caricamento lista GrahaSmall
            self.lstGrahaSmall.append(line_content[0])
            self.lstGrahaProgr.append(line_content[1])
            self.lstGrahaSansc.append(line_content[2])
            self.lstTipoAK.append(line_content[3])
            self.lstRasiSmall.append(line_content[4])
            self.lstRasiProgr.append(line_content[5])
            self.lstGrahaLng.append(line_content[6])
            self.lstNakName.append(line_content[7])
            self.lstNakProgr.append(line_content[8])
            self.lstNakReg.append(line_content[9])
            self.lstNakPada.append(line_content[10])


            i=i+1
            print()
        file_input.close()

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
