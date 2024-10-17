from load_graha import LoadGraha

# Formato file di input:
#  Campo 0: Nome Graha abbreviato
#  Campo 1: progressivo Graha
#  Campo 2: Nome Graha Sanscrito
#  Campo 3: Tipo di AK
#  Campo 4: Nome Rasi del Graha in forma abbreviata
#  Campo 5: Progressivo del Rasi
#  Campo 6: Longitudine del Graha
#  Campo 7: Nome Nakshatra
#  Campo 8: Progressivo Nakshatra
#  Campo 9: Reggente Nakshatra
#  Campo 10: Pada della Nakshatra

print ("\n\n***********************************\n")
print ("    ELABORAZIONE GRAHA MARCO \n")
print ("***********************************\n")

# Nome del file
file_name = "Graha_Marco.txt"
inputFileName = "Marco.txt"
#lstGrahaProgr = []
#lstGrahaSansc = []
#lstTipoAK = []
#lstRasiSmall = []
#lstRasiProgr = []
#lstGrahaLng = []
#lstNakName = []
#lstNakProgr = []
#lstNakReg = []
#lstNakPada = []


file_uno = open(file_name, "w")
file_uno.write("***********************************\n")
file_uno.write("***        Graha di Marco       ***\n")
file_uno.write("***********************************\n")
file_uno.close()    # ricordate sempre di chiudere i file!

#file_input = open(inputFileName, "r", encoding='utf-8')

#print(file_input)

#Caricamento dei GRAHA
# Il caricamento viene effettuato nella lista lstGraha

#i = 1
#for line in file_input.readlines():
#    print("-------------------------------------------")
#    print("Riga " + str(i) + ": " + line)
#    line_content = line.split("|")
#    print(line_content)
#    #Caricamento lista GrahaSmall
#    lstGrahaSmall.append(line_content[0])
#    lstGrahaProgr.append(line_content[1])
#    lstGrahaSansc.append(line_content[2])
#    lstTipoAK.append(line_content[3])
#    lstRasiSmall.append(line_content[4])
#    lstRasiProgr.append(line_content[5])
#    lstGrahaLng.append(line_content[6])
#    lstNakName.append(line_content[7])
#    lstNakProgr.append(line_content[8])
#    lstNakReg.append(line_content[9])
#    lstNakPada.append(line_content[10])
#
#
#    i=i+1
#    print()
#file_input.close()

#LoadGraha = load_Graha()
LoadGrahaMarco = LoadGraha(inputFileName)
LoadGrahaMarco.loadGrahaFile()

#getLstGrahaSmall

print("##############################")
print("   Lista GrahaSmall")
#lsGS = LoadGrahaMarco.getLstGrahaSmall
#print(lsGS)
print(LoadGrahaMarco.getLstGrahaSmall())

print("##############################")
print("   Lista GrahaProgr")
print(LoadGrahaMarco.getLstGrahaProgr())

print("##############################")
print("   Lista lstGrahaSansc")
print(LoadGrahaMarco.getLstGrahaSansc())

print("##############################")
print("   Lista lstTipoAK")
print(LoadGrahaMarco.getLstTipoAK())

print("##############################")
print("   Lista lstRasiSmall")
print(LoadGrahaMarco.getLstRasiSmall())

print("##############################")
print("   Lista lstRasiProgr")
print(LoadGrahaMarco.getLstRasiProgr())

print("##############################")
print("   Lista lstGrahaLng")
print(LoadGrahaMarco.getLstGrahaLng())

print("##############################")
print("   Lista lstNakName")
print(LoadGrahaMarco.getLstNakName())

print("##############################")
print("   Lista lstNakProgr")
print(LoadGrahaMarco.getLstNakProgr())

print("##############################")
print("   Lista lstNakReg")
print(LoadGrahaMarco.getLstNakReg())

print("##############################")
print("   Lista lstNakPada")
print(LoadGrahaMarco.getLstNakPada())
