echo "Lancio dell'applicazione per calcolo della carta natale"

SET NOME=%1
SET LOG=%2
SET CFG_PATH="..\\02-Cfg\\"
SET INPUT_PATH="..\\11-DataInput\\"
SET OUTPUT_PATH="..\\12-CarteNataliOutput\\"

python cartanatale_01.py %INPUT_PATH%%NOME%.txt %CFG_PATH%Graha.cfg %CFG_PATH%Rasi.cfg %CFG_PATH%Bhava.cfg %OUTPUT_PATH%Carta_Natale_%NOME%.txt %LOG%
