echo "   Studio della Carta Natale"


NOME=$1
CFG_PATH="../02-Cfg/"
INPUT_PATH="../11-DataInput/"
OUTPUT_PATH="../12-CarteNataliOutput/"

python cartanatale_01.py ${INPUT_PATH}$NOME.txt ${CFG_PATH}Graha.cfg ${CFG_PATH}Rasi.cfg ${CFG_PATH}Bhava.cfg ${OUTPUT_PATH}Carta_Natale_${NOME}.txt 2

