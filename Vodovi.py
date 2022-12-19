import sqlite3
import uuid

connection=sqlite3.connect("Politicka_opstina.db")
crsr=connection.cursor()

class KO:
    def __init__(self,naziv,KO_id):
        self.naziv=naziv
        self.KO_id = KO_id

    def unos_KO(connection,KO):
        """
                Create a new KO into the KO table
                :param connection:
                :param KO:
                :return: KO id
                """
        sql = ''' INSERT OR IGNORE INTO KO(naziv,KO_id)
                          VALUES(?,?) '''
        params = (KO.naziv, KO.KO_id)
        crsr.execute(sql, params)
        connection.commit()

    def prenos_KO_id(connection, naziv):
        crsr = connection.cursor()
        crsr.execute("SELECT KO_id FROM KO WHERE naziv=?", (a,))
        rez_1 = crsr.fetchone()
        connection.commit()
        return rez_1

class Kc:
    def __init__(self, broj_parcele, kc_id, KO_id):
        self.broj_parcele = broj_parcele
        self.kc_id=kc_id
        self.KO_id=KO_id


    def unos_kc(connection,kc):
        """
                Create a new kc into the kc table
                :param connection:
                :param kc:
                :return: kc id
                """
        sql = ''' INSERT OR IGNORE INTO kc(broj_parcele,kc_id,KO_id)
                          VALUES(?,?,?) '''
        params = (kc.broj_parcele, kc.kc_id,kc.KO_id)
        crsr.execute(sql, params)
        connection.commit()

    def prenos_kc_id(connection, broj_parcele):
        crsr = connection.cursor()
        crsr.execute("SELECT KO_id FROM kc WHERE broj_parcele=?", (b,))
        rez_2 = crsr.fetchone()
        connection.commit()
        return rez_2


class Vodovod:
    def __init__(self,voda_id,zona,materijal,precnik_u_mm,koordinate,kota_vrha_cijevi,kc):
        self.id=voda_id
        self.zona=zona
        self.materijal=materijal
        self.precnik_u_mm=precnik_u_mm
        self.koordinate=koordinate
        self.kota_vrha_cijevi=kota_vrha_cijevi
        self.kc=kc

    def unos_vode(connection,voda):

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

class Struja:
    def __init__(self,struja_id,napon,broj_kablova,koordinate,kota_kabla,kc):
        self.struja_id=struja_id
        self.napon=napon
        self.broja_kablova=broj_kablova
        self.koordinate=koordinate
        self.kota_kabla=kota_kabla
        self.kc=kc

    def unos_struje(connection,struja):

        """
            Create a new struja into the struja table
            :param connection:
            :param struja
            :return: struja id
            """
        sql=''' INSERT INTO struja(struja_id,napon,broj_kablova,koordinate,kota_kabla,kc_id)
                      VALUES(?,?,?,?,?,?) '''
        params = (struja.struja_id, struja.napon, struja.broja_kablova, struja.koordinate, struja.kota_kabla, struja.kc)
        crsr.execute(sql, params)
        connection.commit()

class Toplovod:
    def __init__(self, toplovod_id, materijal, precnik, broj_cijevi, koordinate, kota_cijevi,kc):
        self.toplovod_id = toplovod_id
        self.materijal = materijal
        self.precnik=precnik
        self.broj_cijevi = broj_cijevi
        self.koordinate = koordinate
        self.kota_cijevi = kota_cijevi
        self.kc = kc

    def unos_toplovoda(connection, toplovod):
        """
            Create a new toplovod into the toplovod table
            :param connection:
            :param toplovod
            :return: toplovod id
            """
        sql = ''' INSERT INTO toplovod(toplovod_id, materijal, precnik,broj_cijevi,koordinate,kota_cijevi,kc_id)
                      VALUES(?,?,?,?,?,?,?) '''
        params = (toplovod.toplovod_id, toplovod.materijal, toplovod.precnik,toplovod.broj_cijevi, toplovod.koordinate, toplovod.kota_cijevi, toplovod.kc)
        crsr.execute(sql, params)
        connection.commit()

class Kanalizacija:
    def __init__(self, kanalizacija_id, oznaka_sistema, materijal, presjek, koordinate, kota_cijevi, kc):
        self.kanalizacija_id = kanalizacija_id
        self.oznaka_sistema = oznaka_sistema
        self.materijal = materijal
        self.presjek = presjek
        self.koordinate = koordinate
        self.kota_cijevi = kota_cijevi
        self.kc = kc

    def unos_kanalizacije(connection, kanalizacija):
        """
            Create a new kanalizacija into the kanalizacija table
            :param connection:
            :param kanalizacija
            :return: kanalizacija id
            """
        sql = ''' INSERT INTO kanalizacija (kanalizacija_id,oznaka_sistema, materijal, presjek, koordinate,kota_cijevi,kc_id)
                      VALUES(?,?,?,?,?,?,?) '''
        params = (kanalizacija.kanalizacija_id, kanalizacija.oznaka_sistema, kanalizacija.materijal, kanalizacija.presjek, kanalizacija.koordinate,
                  kanalizacija.kota_cijevi, kanalizacija.kc)
        crsr.execute(sql, params)
        connection.commit()

class Naftagas:
    def __init__(self, naftagas_id, materijal, precnik, broj_cijevi, koordinate, kota_cijevi, kc):
        self.naftagas_id = naftagas_id
        self.materijal = materijal
        self.precnik = precnik
        self.broj_cijevi = broj_cijevi
        self.koordinate = koordinate
        self.kota_cijevi = kota_cijevi
        self.kc = kc

    def unos_naftagasa(connection, naftagas):
        """
        Create a new naftagas into the naftagas table
        :param connection:
        :param naftagas
        :return: naftagas id
        """
        sql = ''' INSERT INTO naftagas (naftagas_id,materijal, precnik, broj_cijevi, koordinate,kota_cijevi,kc_id)
                      VALUES(?,?,?,?,?,?,?) '''
        params = (naftagas.naftagas_id, naftagas.materijal, naftagas.precnik, naftagas.broj_cijevi, naftagas.koordinate,naftagas.kota_cijevi,naftagas.kc)
        crsr.execute(sql, params)
        connection.commit()

class Telekom:
    def __init__(self,telekom_id,vrsta_kabla,broj_cijevi,koordinate,kota_cijevi,kc):
        self.telekom_id=telekom_id
        self.vrsta_kabla=vrsta_kabla
        self.broj_cijevi=broj_cijevi
        self.koordinate=koordinate
        self.kota_cijevi=kota_cijevi
        self.kc=kc

    def unos_telekoma(connection,telekom):

        """
            Create a new telekom into the telekom table
            :param connection:
            :param telekom
            :return: telekom id
            """
        sql=''' INSERT INTO telekom(telekom_id,vrsta_kabla,broj_cijevi, koordinate,kota_cijevi,kc_id)
                      VALUES(?,?,?,?,?,?) '''
        params = (telekom.telekom_id, telekom.vrsta_kabla, telekom.broj_cijevi, telekom.koordinate, telekom.kota_cijevi, telekom.kc)
        crsr.execute(sql, params)
        connection.commit()

a=input('Unesite naziv katastarske opštine: ')
rgc_1=str(uuid.uuid4())
kat_op=KO(a,rgc_1)
KO.unos_KO(connection,kat_op)

b=input('Unesite broj katastarske čestice: ')
rgc_2=str(uuid.uuid4())
rez_1=str(KO.prenos_KO_id(connection,a))
ka_ce=Kc(b,rgc_2,rez_1)
Kc.unos_kc(connection,ka_ce)

while True:
    al = str(Kc.prenos_kc_id(connection, b))
    c = int(input('Za uplanu vodovoda ukucaj 1,\nZa uplanu elektroenergetskog voda ukucaj 2,\nZa uplanu toplovoda ukucaj 3,\nZa uplanu kanalizacionog voda ukucaj 4,\nZa uplanu naftovoda ili gasovoda ukucaj 5,\nZa uplanu voda telekoma ukucaj 6: '))
    if c==1:
        d=str(uuid.uuid4())
        e=int(input('Unesite broj zone voda: '))
        f=input('Unesite materijal voda: ')
        g=input('Unesite prečnik voda u milimetrima: ')
        h=input('Unesite koordinate lomnih tačaka: ')
        i=float(input('Unesite kotu vrha cijevi: '))

        vd=Vodovod(d,e,f,g,h,i,al)
        Vodovod.unos_vode(connection,vd)

    elif c==2:
        j=str(uuid.uuid4())
        k=int(input('Unesite napon voda: '))
        l=int(input('Unesite broj kablova istog napona: '))
        m=input('Unesite koordinate tačaka lomova voda: ')
        n=float(input('Unesite kotu kabla: '))
        st=Struja(j,k,l,m,n,al)
        Struja.unos_struje(connection,st)

    elif c==3:
        o=str(uuid.uuid4())
        p=input('Unesite materijal voda: ')
        q=int(input('Unesite precnik cijevi: '))
        r=int(input('Unesite broj cijevi: '))
        s=input('Unesite koordinate tačaka lomova voda: ')
        t=float(input('Unesite kotu cijevi: '))
        tp=Toplovod(o,p,q,r,s,t,al)
        Toplovod.unos_toplovoda(connection,tp)

    elif c==4:
        u=str(uuid.uuid4())
        v=input('Unesite oznaku sistema: ')
        w=input('Unesite materijal cijevi: ')
        x=int(input('Unesite presjek cijevi: '))
        y=input('Unesite koordinate tačaka lomova voda: ')
        z=float(input('Unesite kotu cijevi: '))
        kan=Kanalizacija(u,v,w,x,y,z,al)
        Kanalizacija.unos_kanalizacije(connection,kan)

    elif c==5:
        aa=str(uuid.uuid4())
        ab=input('Unesite materijal cijevi: ')
        ac=float(input('Unesite prečnik cijevi: '))
        ad=int(input('Unesite broj cijevi: '))
        ae=input('Unesite koordinate tačaka lomova voda: ')
        af=float(input('Unesite kotu cijevi: '))
        ng=Naftagas(aa,ab,ac,ad,ae,af,al)
        Naftagas.unos_naftagasa(connection,ng)

    elif c==6:
        ag=str(uuid.uuid4())
        ah=input('Unesite vrstu kabla: ')
        ai=int(input('Unesite broj cijevi: '))
        aj=input('Unesite koordinate tačaka lomova voda: ')
        ak=float(input('Unesite kotu cijevi: '))
        tlk=Telekom(ag,ah,ai,aj,ak,al)
        Telekom.unos_telekoma(connection,tlk)

    else:
        True

    upit_1 = input('Da li želite da završite sa unosom? ').upper()
    while upit_1 != 'DA' and upit_1 != 'NE':
        upit_1 = input('Unesite "da" ili "ne"!').upper()
    if upit_1 == 'NE':
        True
    elif upit_1 == 'DA':
        break








