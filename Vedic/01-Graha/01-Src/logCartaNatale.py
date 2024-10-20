import datetime


class LogCartaNatale:
    "La classe per il logo su console e file"

    szLogFile = ""
    iPri = 0

    def __init__ (self, logFile, iPriorita):
        self.szLogFile = logFile
        self.iPri = iPriorita

        fileToLog=open(self.szLogFile, "w")
        oraCorrente = datetime.datetime.now()
        fileToLog.write("Log " + self.szLogFile + " inizializzato il: " + str(oraCorrente) + " con priorita = " + str(self.iPri) + "\n\n")
        fileToLog.close()

    def scriviLog(self, iPriorita, szMess):
        if(iPriorita >= self.iPri):
            fileToLog=open(self.szLogFile, "a")
            fileToLog.write("\n" + str(datetime.datetime.now()) + " - " + szMess)
            fileToLog.close()
            print(szMess)

