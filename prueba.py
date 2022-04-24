import pandas as pd

while True:
    try:
        carpetaMes=str.upper(input("Nombre de la carpeta del mes: "))
        
        ruta = "C:/LABORATORIOS/ALTAS/"+ carpetaMes + "/altas.xlsx"
        print("la ruta es: {}".format(ruta))

        myfile = pd.read_excel(ruta,"ndftw")

        EUROFARMA = myfile[(myfile.Alta=="ALTA") & (myfile.CT=='C09C0')|(myfile.CT=='C09D1')|(myfile.CT=='A10N1')|(myfile.CT=='A10N3')|(myfile.CT=='M04A0')|(myfile.CT=='C05C0')|(myfile.CT=='C05B0')|(myfile.CT=='J01D1')|(myfile.CT=='A11A1')]
        EUROFARMA.to_excel("C:/LABORATORIOS/ALTAS/"+ carpetaMes+"/Eurofarma.xlsx","eurofarma") 

        print("Archivo Eurofarma Creado")


        BIOCODEX = myfile[(myfile.Alta=="ALTA") & (myfile.CT=='V06C0')|(myfile.CT=='1')|(myfile.CT=='A07F0')]
        BIOCODEX.to_excel("C:/LABORATORIOS/ALTAS/"+ carpetaMes+"/BIOCODEX.xlsx","biocodex") #GENERA UN EXCEL

        print("Archivo Biocodex Creado")


        BL = myfile[(myfile.Alta=="ALTA") & (myfile.CT.str.startswith("S01"))]
        BL.to_excel("C:/LABORATORIOS/ALTAS/"+ carpetaMes+"/BL.xlsx","bausch") #GENERA UN EXCEL

        print("Archivo B&L Creado")


        Bayer = myfile[(myfile.Alta=="ALTA") & ((myfile.CT.str.startswith("A02A"))|(myfile.CT.str.startswith("R01"))|(myfile.CT=='88A10')|(myfile.CT=='88A50')|(myfile.CT=='88B2A')|(myfile.CT=='88B30')|(myfile.CT=='A03A0')|(myfile.CT=='A03C0')|(myfile.CT=='A03D0')|(myfile.CT=='A03E0')|(myfile.CT=='A07F0')|(myfile.CT=='A07H0')|(myfile.CT=='A07X0')|(myfile.CT=='R06A0')| (myfile.CT=='H02B0')|(myfile.CT=='A11A1')|(myfile.CT=='A11A4')|(myfile.CT=='A11B1')|(myfile.CT=='A11B2')|(myfile.CT=='A11B4')|(myfile.CT=='A11C3')|(myfile.CT=='A11G1')|(myfile.CT=='A11G2')|(myfile.CT=='B03A1')|(myfile.CT=='B03A2')|(myfile.CT=='D02A0')|(myfile.CT=='D03A1')|(myfile.CT=='D03A9')|(myfile.CT=='D05X0')|(myfile.CT=='D07A0')|(myfile.CT=='D08A0')|(myfile.CT=='D11A0')|(myfile.CT=='G01B0')|(myfile.CT=='G02X9'))]
        Bayer.to_excel("C:/LABORATORIOS/ALTAS/"+ carpetaMes+"/Bayer.xlsx","bayer") #GENERA UN EXCEL

        print("Archivo BAYER Creado")

        BOEHRINGER = myfile[(myfile.Alta=="ALTA") & ((myfile.CT=="R03K2")|(myfile.CT=="R03L1")|(myfile.CT=='R03A3')|(myfile.CT=='R03D1')|(myfile.CT=='R03F1')|(myfile.CT=='R03L2')|(myfile.CT=='R03L3')|(myfile.CT=='R03A4')|(myfile.CT=='R03C1')|(myfile.CT=='R01A1')|(myfile.CT=='R03E1')|(myfile.CT=='R03K1')|(myfile.CT=='C09D1')|(myfile.CT=='C09D3')| (myfile.CT=='R03X2')|(myfile.CT=='A10P1')|(myfile.CT=='A10P3')|(myfile.CT=='A10P5')|(myfile.CT=='A10N1')|(myfile.CT=='A10N3')|(myfile.CT=='A10S0')|(myfile.CT=='A10P9')|(myfile.CT=='B01E0')|(myfile.CT=='B01F0')|(myfile.CT=='B01A0')|(myfile.CT=='C09C0')|(myfile.CT=='C09D9')|(myfile.CT=='G04A9')|(myfile.CT=='G04A2')|(myfile.CT=='G04X0'))]
        BOEHRINGER.to_excel("C:/LABORATORIOS/ALTAS/"+ carpetaMes+"/Boehriger.xlsx","B.I") #GENERA UN EXCEL

        print("Archivo BOEHRINGER Creado")

        break
    except FileNotFoundError:
        print("no existe la carpeta, vuelve a colocar el nombre correctamente")