import sqlite3
connection=sqlite3.connect("Politicka_opstina.db")
crsr=connection.cursor()

class KO:
    def __init__(self,id,naziv):
        self.KO_id=id
        self.naziv=naziv

def Unos_KO(connection,KO):
    sql = ''' INSERT INTO KO(KO_id,naziv)
                      VALUES(?,?) '''
    params = (KO.id, KO.naziv)
    crsr.execute(sql, params)
    connection.commit()


class Kc:
    def __init__(self, id,broj_parcele,KO_id):
        self.kc_id=id
        self.broj_parcele=broj_parcele
        self.KO_id=KO_id

def Unos_kc(connection,kc):
    sql = ''' INSERT INTO kc(kc_id,broj_parcele,KO_id)
                      VALUES(?,?) '''
    params = (kc.id, kc.broj_parcele)
    crsr.execute(sql, params)
    connection.commit()




class Vodovod:
    def __init__(self,voda_id,zona,materijal,precnik_u_mm,koordinate,kota_vrha_cijevi,kc):
        self.id=voda_id
        self.zona=zona
        self.materijal=materijal
        self.precnik_u_mm=precnik_u_mm
        self.koordinate=koordinate
        self.kota_vrha_cijevi=kota_vrha_cijevi
        self.kc=kc

def unos_voda(connection,voda):

    """
        Create a new voda into the vodovod table
        :param connection:
        :param voda:
        :return: voda id
        """
    sql=''' INSERT INTO vodovod(voda_id,zona,materijal,precnik_u_mm,koordinate,kota_vrha_cijevi,kc_id)
                  VALUES(?,?,?,?,?,?,?) '''
    params = (voda.id, voda.zona, voda.materijal, voda.precnik_u_mm, voda.koordinate, voda.kota_vrha_cijevi,voda.kc)
    crsr.execute(sql, params)
    connection.commit()

a=input('Unesite naziv katastarske opštine: ')
b=int(input('Unesite broj katastarske čestice: '))

while True:
    c = int(input('Za uplanu vodovoda ukucaj 1,\nZa uplanu elektroenergetskog voda ukucaj 2,\nZa uplanu toplovoda ukucaj 3,\nZa uplanu kanalizacionog voda ukucaj 4,\nZa uplanu naftovoda ili gasovoda ukucaj 5,\nZa uplanu voda telekoma ukucaj 6: '))
    if c==1:
        d=int(input('Unesite id voda: '))
        e=int(input('Unesite broj zone voda: '))
        f=(input('Unesite materijal voda: '))
        g=(input('Unesite prečnik voda u milimetrima: '))
        h=float(input('Unesite koordinate lomnih tačaka: '))
        i=float(input('Unesite kotu vrha cijevi: '))
        #params=(d,e,f,g,h,i)
        vd=Vodovod(d,e,f,g,h,i,b)
        unos_voda(connection,vd)

    upit = input('Da li želite da završite sa unosom? ').upper()
    while upit!='DA' and upit!='NE':
        upit=input('Unesite "da" ili "ne"!').upper()
    if upit=='NE':
        True
    elif upit=='DA':
        break
    False







