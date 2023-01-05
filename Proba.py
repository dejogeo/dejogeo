import sqlite3
import uuid

connection=sqlite3.connect("Politicka_opstina1.db")
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

    def prenos_KO_id(connection, naziv_KO):
        crsr = connection.cursor()
        crsr.execute("SELECT KO_id FROM KO WHERE naziv=?", (naziv_KO,))
        separator = ", "
        rez_1 = separator.join(crsr.fetchone())
        #print(rez_1)
        #connection.commit()
        return rez_1
        #print(rez_1)

class Kc:
    def __init__(self, broj_parcele, kc_id, KO_naziv, KO_id):
        self.broj_parcele = broj_parcele
        self.kc_id=kc_id
        self.KO_naziv=KO_naziv
        self.KO_id = KO_id


    def unos_kc(connection,kc):
        """
                Create a new kc into the kc table
                :param connection:
                :param kc:
                :return: kc id
                """
        sql = ''' INSERT OR IGNORE INTO kc(broj_parcele,kc_id,KO_naziv, KO_id)
                          VALUES(?,?,?,?) '''
        params = (kc.broj_parcele, kc.kc_id,kc.KO_naziv,kc.KO_id)
        crsr.execute(sql, params)
        connection.commit()

    def prenos_kc_id(connection, broj_parcele,naziv_KO):
        crsr = connection.cursor()
        crsr.execute("SELECT kc_id FROM kc WHERE broj_parcele=? AND KO_naziv=?", (broj_parcele,naziv_KO))
        separator = ", "
        rez_2 = separator.join(crsr.fetchone())
        return rez_2

    def kontrola_parcele(connection, broj_kc, naziv_parcele):
        crsr = connection.cursor()
        crsr.execute("SELECT kc_id FROM kc WHERE broj_parcele=? AND KO_naziv=?", (broj_kc,naziv_parcele))
        rez_3 = crsr.fetchall()
        return rez_3

    def ispis_voda(connection, idkc):
        crsr = connection.cursor()
        crsr.execute("SELECT * FROM struja WHERE kc_id=?", (idkc,))
        #separator = ", "
        rez = str(','.join(str(item) for item in crsr.fetchall()))[1:-1]
        #print(type(rez))
        #rez = ','.join(str(item) for item in crsr.fetchone())
        return rez


class Vodovod:
    def __init__(self,voda_id,zona,materijal,precnik_u_mm,koordinate,kota_vrha_cijevi,KO_naziv, kc):
        self.id=voda_id
        self.zona=zona
        self.materijal=materijal
        self.precnik_u_mm=precnik_u_mm
        self.koordinate=koordinate
        self.kota_vrha_cijevi=kota_vrha_cijevi
        self.KO_naziv=KO_naziv
        self.kc=kc


    def unos_vode(connection,voda):

        """
            Create a new voda into the vodovod table
            :param connection:
            :param voda:
            :return: voda id
            """
        sql=''' INSERT INTO vodovod(voda_id,zona,materijal,precnik_u_mm,koordinate,kota_vrha_cijevi,KO_naziv, kc_id)
                      VALUES(?,?,?,?,?,?,?,?) '''
        params = (voda.id, voda.zona, voda.materijal, voda.precnik_u_mm, voda.koordinate, voda.kota_vrha_cijevi, voda.KO_naziv, voda.kc)
        crsr.execute(sql, params)
        connection.commit()

class Struja:
    def __init__(self,struja_id,napon,broj_kablova,koordinate,kota_kabla,KO_naziv, kc):
        self.struja_id=struja_id
        self.napon=napon
        self.broja_kablova=broj_kablova
        self.koordinate=koordinate
        self.kota_kabla=kota_kabla
        self.KO_naziv=KO_naziv
        self.kc=kc

    def unos_struje(connection,struja):

        """
            Create a new struja into the struja table
            :param connection:
            :param struja
            :return: struja id
            """
        sql=''' INSERT INTO struja(struja_id,napon,broj_kablova,koordinate,kota_kabla,KO_naziv,kc_id)
                      VALUES(?,?,?,?,?,?,?) '''
        params = (struja.struja_id, struja.napon, struja.broja_kablova, struja.koordinate, struja.kota_kabla, struja.KO_naziv, struja.kc)
        crsr.execute(sql, params)
        connection.commit()

class Toplovod:
    def __init__(self, toplovod_id, materijal, precnik, broj_cijevi, koordinate, kota_cijevi, KO_naziv, kc):
        self.toplovod_id = toplovod_id
        self.materijal = materijal
        self.precnik=precnik
        self.broj_cijevi = broj_cijevi
        self.koordinate = koordinate
        self.kota_cijevi = kota_cijevi
        self.KO_naziv=KO_naziv
        self.kc = kc

    def unos_toplovoda(connection, toplovod):
        """
            Create a new toplovod into the toplovod table
            :param connection:
            :param toplovod
            :return: toplovod id
            """
        sql = ''' INSERT INTO toplovod(toplovod_id, materijal, precnik,broj_cijevi,koordinate,kota_cijevi,KO_naziv,kc_id)
                      VALUES(?,?,?,?,?,?,?,?) '''
        params = (toplovod.toplovod_id, toplovod.materijal, toplovod.precnik,toplovod.broj_cijevi, toplovod.koordinate, toplovod.kota_cijevi, toplovod.KO_naziv, toplovod.kc)
        crsr.execute(sql, params)
        connection.commit()

class Kanalizacija:
    def __init__(self, kanalizacija_id, oznaka_sistema, materijal, presjek, koordinate, kota_cijevi, KO_naziv, kc):
        self.kanalizacija_id = kanalizacija_id
        self.oznaka_sistema = oznaka_sistema
        self.materijal = materijal
        self.presjek = presjek
        self.koordinate = koordinate
        self.kota_cijevi = kota_cijevi
        self.KO_naziv=KO_naziv
        self.kc = kc

    def unos_kanalizacije(connection, kanalizacija):
        """
            Create a new kanalizacija into the kanalizacija table
            :param connection:
            :param kanalizacija
            :return: kanalizacija id
            """
        sql = ''' INSERT INTO kanalizacija (kanalizacija_id,oznaka_sistema, materijal, presjek, koordinate,kota_cijevi,KO_naziv,kc_id)
                      VALUES(?,?,?,?,?,?,?,?) '''
        params = (kanalizacija.kanalizacija_id, kanalizacija.oznaka_sistema, kanalizacija.materijal, kanalizacija.presjek, kanalizacija.koordinate,
                  kanalizacija.kota_cijevi, kanalizacija.KO_naziv, kanalizacija.kc)
        crsr.execute(sql, params)
        connection.commit()

class Naftagas:
    def __init__(self, naftagas_id, materijal, precnik, broj_cijevi, koordinate, kota_cijevi, KO_naziv, kc):
        self.naftagas_id = naftagas_id
        self.materijal = materijal
        self.precnik = precnik
        self.broj_cijevi = broj_cijevi
        self.koordinate = koordinate
        self.kota_cijevi = kota_cijevi
        self.KO_naziv=KO_naziv
        self.kc = kc

    def unos_naftagasa(connection, naftagas):
        """
        Create a new naftagas into the naftagas table
        :param connection:
        :param naftagas
        :return: naftagas id
        """
        sql = ''' INSERT INTO naftagas (naftagas_id,materijal, precnik, broj_cijevi, koordinate,kota_cijevi,KO_naziv,kc_id)
                      VALUES(?,?,?,?,?,?,?,?) '''
        params = (naftagas.naftagas_id, naftagas.materijal, naftagas.precnik, naftagas.broj_cijevi, naftagas.koordinate,naftagas.kota_cijevi,naftagas.KO_naziv,naftagas.kc)
        crsr.execute(sql, params)
        connection.commit()

class Telekom:
    def __init__(self,telekom_id,vrsta_kabla,broj_cijevi,koordinate,kota_cijevi,KO_naziv,kc):
        self.telekom_id=telekom_id
        self.vrsta_kabla=vrsta_kabla
        self.broj_cijevi=broj_cijevi
        self.koordinate=koordinate
        self.kota_cijevi=kota_cijevi
        self.KO_naziv=KO_naziv
        self.kc=kc

    def unos_telekoma(connection,telekom):

        """
            Create a new telekom into the telekom table
            :param connection:
            :param telekom
            :return: telekom id
            """
        sql=''' INSERT INTO telekom(telekom_id,vrsta_kabla,broj_cijevi, koordinate,kota_cijevi,KO_naziv,kc_id)
                      VALUES(?,?,?,?,?,?,?) '''
        params = (telekom.telekom_id, telekom.vrsta_kabla, telekom.broj_cijevi, telekom.koordinate, telekom.kota_cijevi, telekom.KO_naziv, telekom.kc)
        crsr.execute(sql, params)
        connection.commit()



#a=input('Unesite naziv katastarske opštine: ')
#rgc_1=str(uuid.uuid4())
#kat_op=KO(a,rgc_1)
#KO.unos_KO(connection,kat_op)
#
#b=input('Unesite broj katastarske čestice: ')
#rgc_2=str(uuid.uuid4())
#rez_1=str(KO.prenos_KO_id(connection,a))
#ka_ce=Kc(b,rgc_2,a,rez_1)
#
#rez_3=Kc.kontrola_parcele(connection,b,a)
#if rez_3==[]:
#    Kc.unos_kc(connection, ka_ce)
#
#while True:
#    rez_2 = Kc.prenos_kc_id(connection, b, a)
#    print('-------------------------------------')
#    am = int(input('Za uplanu novog voda, unesite 1,\nza ažuriranje postojećeg voda, unesite 2,\nza isplanu postojećeg voda, unesite 3: '))
#    if am==1:
#        while True:
#            print('-------------------------------------')
#            al = str(Kc.prenos_kc_id(connection, b,a))
#            c = int(input('Za uplanu vodovoda ukucaj 1,\nZa uplanu elektroenergetskog voda ukucaj 2,\nZa uplanu toplovoda ukucaj 3,\nZa uplanu kanalizacionog voda ukucaj 4,\nZa uplanu naftovoda ili gasovoda ukucaj 5,\nZa uplanu voda telekoma ukucaj 6: '))
#            if c==1:
#                d=str(uuid.uuid4())
#                e=int(input('Unesite broj zone voda: '))
#                f=input('Unesite materijal voda: ')
#                g=input('Unesite prečnik voda u milimetrima: ')
#                h=input('Unesite koordinate lomnih tačaka: ')
#                i=float(input('Unesite kotu vrha cijevi: '))
#
#                vd=Vodovod(d,e,f,g,h,i,a,al)
#                Vodovod.unos_vode(connection,vd)
#
#            elif c==2:
#                j=str(uuid.uuid4())
#                k=int(input('Unesite napon voda: '))
#                l=int(input('Unesite broj kablova istog napona: '))
#                m=input('Unesite koordinate tačaka lomova voda: ')
#                n=float(input('Unesite kotu kabla: '))
#                st=Struja(j,k,l,m,n,a,al)
#                Struja.unos_struje(connection,st)
#
#            elif c==3:
#                o=str(uuid.uuid4())
#                p=input('Unesite materijal voda: ')
#                q=int(input('Unesite precnik cijevi: '))
#                r=int(input('Unesite broj cijevi: '))
#                s=input('Unesite koordinate tačaka lomova voda: ')
#                t=float(input('Unesite kotu cijevi: '))
#                tp=Toplovod(o,p,q,r,s,t,a,al)
#                Toplovod.unos_toplovoda(connection,tp)
#
#            elif c==4:
#                u=str(uuid.uuid4())
#                v=input('Unesite oznaku sistema: ')
#                w=input('Unesite materijal cijevi: ')
#                x=int(input('Unesite presjek cijevi: '))
#                y=input('Unesite koordinate tačaka lomova voda: ')
#                z=float(input('Unesite kotu cijevi: '))
#                kan=Kanalizacija(u,v,w,x,y,z,a,al)
#                Kanalizacija.unos_kanalizacije(connection,kan)
#
#            elif c==5:
#                aa=str(uuid.uuid4())
#                ab=input('Unesite materijal cijevi: ')
#                ac=float(input('Unesite prečnik cijevi: '))
#                ad=int(input('Unesite broj cijevi: '))
#                ae=input('Unesite koordinate tačaka lomova voda: ')
#                af=float(input('Unesite kotu cijevi: '))
#                ng=Naftagas(aa,ab,ac,ad,ae,af,a,al)
#                Naftagas.unos_naftagasa(connection,ng)
#
#            elif c==6:
#                ag=str(uuid.uuid4())
#                ah=input('Unesite vrstu kabla: ')
#                ai=int(input('Unesite broj cijevi: '))
#                aj=input('Unesite koordinate tačaka lomova voda: ')
#                ak=float(input('Unesite kotu cijevi: '))
#                tlk=Telekom(ag,ah,ai,aj,ak,a,al)
#                Telekom.unos_telekoma(connection,tlk)
#
#            else:
#                True
#
#            upit_1 = input('Da li želite da završite sa unosom? ').upper()
#            while upit_1 != 'DA' and upit_1 != 'NE':
#                upit_1 = input('Unesite "da" ili "ne"!').upper()
#            if upit_1 == 'NE':
#                True
#            elif upit_1 == 'DA':
#                break
#        break
#    if am==2:
#        while True:
#            print('-------------------------------------')
#            an=int(input('Za ažuriranje vodovoda, unesite 1,\nza ažuriranje elektroenergetskog voda, unesite 2,\nza ažuriranje toplovoda ukucaj 3,\nza ažuriranje kanalizacionog voda ukucaj 4,\nza ažuriranje naftovoda ili gasovoda ukucaj 5,\nza ažuriranje voda telekoma ukucaj 6: '))
#            if an==1:
#                ao=int(input('Za ažuriranje zone vodovoda, unesite 1,\nza ažuriranje materijala voda, unesite 2,\nza ažuriranje prečnika cijevi (mm), unesite 3,\nza ažuriranje koordinata lomova voda, unesite 4,\nza ažuriranje kote vrha cijevi, unesite 5: '))
#                if ao==1:
#                    ap=int(input('Unesite novu zonu vodovoda: '))
#                    crsr.execute('''UPDATE vodovod SET zona = ? WHERE kc_id=? AND KO_naziv=?''',(ap,rez_2,a))
#                    connection.commit()
#                elif ao==2:
#                    ar=input('Unesite novi materijal vodovoda: ')
#                    crsr.execute('''UPDATE vodovod SET materijal = ? WHERE kc_id=? ''AND KO_naziv=?''',(ar,rez_2,a))
#                    connection.commit()
#                elif ao==3:
#                    at=int(input('Unesite novi prečnik cijevi vodovoda (u mm): '))
#                    crsr.execute('''UPDATE vodovod SET precnik_u_mm = ? WHERE kc_id=? AND KO_naziv=?''',(at,rez_2,a))
#                    connection.commit()
#                elif ao==4:
#                    au=input('Unesite nove koordinate lomova cijevi vodovoda: ')
#                    crsr.execute('''UPDATE vodovod SET koordinate = ? WHERE kc_id=? AND KO_naziv=?''',(au,rez_2,a))
#                    connection.commit()
#                elif ao==5:
#                    av=int(input('Unesite novu kotu vrha cijevi vodovoda: '))
#                    crsr.execute('''UPDATE vodovod SET kota_vrha_cijevi = ? WHERE kc_id=? AND KO_naziv=?''',(av,rez_2,a))
#                    connection.commit()
#            if an == 2:
#                print('-------------------------------------')
#                aw = int(input('Za ažuriranje napona voda, unesite 1,\nza ažuriranje broja kablova voda, unesite 2,\nza ažuriranje koordinata lomova voda, unesite 3,\nza ažuriranje kote kabla, unesite 4: '))
#                if aw== 1:
#                    ax = int(input('Unesite novi napon voda: '))
#                    crsr.execute('''UPDATE struja SET napon = ? WHERE kc_id=? AND KO_naziv=?''',(ax,rez_2,a))
#                    connection.commit()
#                elif aw == 2:
#                    ay = int(input('Unesite novi broj kablova voda: '))
#                    crsr.execute('''UPDATE struja SET broj_kablova = ? WHERE kc_id=? AND KO_naziv=?''',(ay,rez_2,a))
#                    connection.commit()
#                elif aw == 3:
#                    az = input('Unesite nove koordinate lomova voda: ')
#                    crsr.execute('''UPDATE struja SET koordinate = ? WHERE kc_id=? AND KO_naziv=?''',(az,rez_2,a))
#                    connection.commit()
#                elif aw == 4:
#                    ba = int(input('Unesite novu kotu kabla: '))
#                    crsr.execute('''UPDATE struja SET kota_kabla = ? WHERE kc_id=? AND KO_naziv=?''',(ba,rez_2,a))
#                    connection.commit()
#            if an==3:
#                print('-------------------------------------')
#                bb=int(input('Za ažuriranje materijala toplovoda, unesite 1,\nza ažuriranje prečnika cijevi toplovoda, unesite 2,\nza ažuriranje broja cijevi, unesite 3,\nza ažuriranje koordinata lomova voda, unesite 4,\nza ažuriranje kote vrha cijevi, unesite 5: '))
#                if bb==1:
#                    bc=input('Unesite novi materijal toplovoda: ')
#                    crsr.execute('''UPDATE toplovod SET materijal = ? WHERE kc_id=? AND KO_naziv=?''',(bc,rez_2,a))
#                    connection.commit()
#                elif bb==2:
#                    bd=int(input('Unesite novi prečnik cijevi toplovoda (u mm): '))
#                    crsr.execute('''UPDATE toplovod SET precnik = ? WHERE kc_id=? AND KO_naziv=?''',(bd,rez_2,a))
#                    connection.commit()
#                elif bb==3:
#                    be=int(input('Unesite novi broj cijevi toplovoda: '))
#                    crsr.execute('''UPDATE toplovod SET broj_cijevi = ? WHERE kc_id=? AND KO_naziv=?''',(be,rez_2,a))
#                    connection.commit()
#                elif bb==4:
#                    bf=input('Unesite nove koordinate lomova cijevi toplovoda: ')
#                    crsr.execute('''UPDATE toplovod SET koordinate = ? WHERE kc_id=? AND KO_naziv=?''',(bf,rez_2,a))
#                    connection.commit()
#                elif bb==5:
#                    bg=int(input('Unesite novu kotu vrha cijevi toplovoda: '))
#                    crsr.execute('''UPDATE toplovod SET kota_cijevi = ? WHERE kc_id=? AND KO_naziv=?''',(bg,rez_2,a))
#                    connection.commit()
#            if an==4:
#                print('-------------------------------------')
#                bh=int(input('Za ažuriranje oznake sistema kanalizacije, unesite 1,\nza ažuriranje materijala cijevi kanalizacije, unesite 2,\nza ažuriranje presjeka cijevi, unesite 3,\nza ažuriranje koordinata lomova voda, unesite 4,\nza ažuriranje kote vrha cijevi, unesite 5: '))
#                if bh==1:
#                    bi=input('Unesite novu oznaku sistema kanalizacije: ')
#                    crsr.execute('''UPDATE kanalizacija SET oznaka_sistema = ? WHERE kc_id=? AND KO_naziv=?''',(bi,rez_2,a))
#                    connection.commit()
#                elif bh==2:
#                    bj=input('Unesite novi materijal cijevi kanalizacije: ')
#                    crsr.execute('''UPDATE kanalizacija SET materijal = ? WHERE kc_id=? AND KO_naziv=?''',(bj,rez_2,a))
#                    connection.commit()
#                elif bh==3:
#                    bk=input('Unesite novi presjek cijevi kanalizacije (u mm): ')
#                    crsr.execute('''UPDATE kanalizacija SET presjek = ? WHERE kc_id=? AND KO_naziv=?''',(bk,rez_2,a))
#                    connection.commit()
#                elif bh==4:
#                    bl=input('Unesite nove koordinate lomova cijevi kanalizacije: ')
#                    crsr.execute('''UPDATE kanalizacija SET koordinate = ? WHERE kc_id=? AND KO_naziv=?''',(bl,rez_2,a))
#                    connection.commit()
#                elif bh==5:
#                    bm=int(input('Unesite novu kotu vrha cijevi kanalizacije: '))
#                    crsr.execute('''UPDATE kanalizacija SET kota_cijevi = ? WHERE kc_id=? AND KO_naziv=?''',(bm,rez_2,a))
#                    connection.commit()
#            if an==5:
#                print('-------------------------------------')
#                bn=int(input('Za ažuriranje materijala naftovoda ili gasovoda, unesite 1,\nza ažuriranje prečnika cijevi naftovoda ili gasovoda, unesite 2,\nza ažuriranje broja cijevi, unesite 3,\nza ažuriranje koordinata lomova voda, unesite 4,\nza ažuriranje kote vrha cijevi, unesite 5: '))
#                if bn==1:
#                    bo=input('Unesite novi materijal naftovoda ili gasovoda: ')
#                    crsr.execute('''UPDATE naftagas SET materijal = ? WHERE kc_id=? AND KO_naziv=?''',(bo,rez_2,a))
#                    connection.commit()
#                elif bn==2:
#                    bp=int(input('Unesite novi prečnik cijevi naftovoda ili gasovoda (u mm): '))
#                    crsr.execute('''UPDATE naftagas SET precnik = ? WHERE kc_id=? AND KO_naziv=?''',(bp,rez_2,a))
#                    connection.commit()
#                elif bn==3:
#                    br=int(input('Unesite novi broj cijevi toplovoda: '))
#                    crsr.execute('''UPDATE naftagas SET broj_cijevi = ? WHERE kc_id=? AND KO_naziv=?''',(br,rez_2,a))
#                    connection.commit()
#                elif bn==4:
#                    bs=input('Unesite nove koordinate lomova cijevi naftovoda ili gasovoda: ')
#                    crsr.execute('''UPDATE naftagas SET koordinate = ? WHERE kc_id=? AND KO_naziv=?''',(bs,rez_2,a))
#                    connection.commit()
#                elif bn==5:
#                    bt=int(input('Unesite novu kotu vrha cijevi naftovoda ili gasovoda: '))
#                    crsr.execute('''UPDATE naftagas SET kota_cijevi = ? WHERE kc_id=? AND KO_naziv=?''',(bt,rez_2,a))
#                    connection.commit()
#            if an == 6:
#                print('-------------------------------------')
#                bu = int(input('Za ažuriranje vrste kabla telekomunikacija, unesite 1,\nza ažuriranje broja cijevi voda, unesite 2,\nza ažuriranje koordinata lomova voda, unesite 3,\nza ažuriranje kote cijevi, unesite 4: '))
#                if bu == 1:
#                    bv = input('Unesite novu vrstu kabla: ')
#                    crsr.execute('''UPDATE telekom SET vrsta_kabla = ? WHERE kc_id=? AND KO_naziv=?''',(bv,rez_2,a))
#                    connection.commit()
#                elif bu == 2:
#                    bw = int(input('Unesite novi broj cijevi voda: '))
#                    crsr.execute('''UPDATE telekom SET broj_cijevi = ? WHERE kc_id=? AND KO_naziv=?''',(bw,rez_2,a))
#                    connection.commit()
#                elif bu == 3:
#                    bx = input('Unesite nove koordinate lomova voda: ')
#                    crsr.execute('''UPDATE telekom SET koordinate = ? WHERE kc_id=? AND KO_naziv=?''',(bx,rez_2,a))
#                    connection.commit()
#                elif bu == 4:
#                    by = int(input('Unesite novu kotu cijevi voda: '))
#                    crsr.execute('''UPDATE telekom SET kota_kabla = ? WHERE kc_id=? AND KO_naziv=?''',(by,rez_2,a))
#                    connection.commit()
#                else:
#                    True
#
#            else:
#                True
#            upit_2 = input('Da li želite da završite sa ažuriranjem? ').upper()
#            while upit_2 != 'DA' and upit_2 != 'NE':
#                upit_2 = input('Unesite "da" ili "ne"!').upper()
#            if upit_2 == 'NE':
#                True
#            elif upit_2 == 'DA':
#                break
#        break
#    if am==3:
#        while True:
#            print('-------------------------------------')
#            bz=int(input('Za brisanje vodovoda, unesite 1,\nza brisanje elektroenergetskog voda, unesite 2,\nza brisanje toplovoda ukucaj 3,\nza brisanje kanalizacionog voda ukucaj 4,\nza brisanje naftovoda ili gasovoda ukucaj 5,\nza brisanje voda telekoma ukucaj 6: '))
#            if bz==1:
#                crsr.execute('''DELETE FROM vodovod WHERE kc_id=? AND KO_naziv=?''',(rez_2,a))
#                connection.commit()
#            elif bz==2:
#                crsr.execute('''DELETE FROM struja WHERE kc_id=? AND KO_naziv=?''',(rez_2,a))
#                connection.commit()
#            elif bz==3:
#                crsr.execute('''DELETE FROM toplovod WHERE kc_id=? AND KO_naziv=?''',(rez_2,a))
#                connection.commit()
#            elif bz==4:
#                crsr.execute('''DELETE FROM kanalizacija WHERE kc_id=? AND KO_naziv=?''',(rez_2,a))
#                connection.commit()
#            elif bz==5:
#                crsr.execute('''DELETE FROM naftagas WHERE kc_id=? AND KO_naziv=?''',(rez_2,a))
#                connection.commit()
#            elif bz==6:
#                crsr.execute('''DELETE FROM telekom WHERE kc_id=? AND KO_naziv=?''',(rez_2,a))
#                connection.commit()
#            else:
#                True
#
#            upit_3 = input('Da li želite da završite sa isplanom? ').upper()
#            while upit_3 != 'DA' and upit_3 != 'NE':
#                upit_3 = input('Unesite "da" ili "ne"!').upper()
#            if upit_3 == 'NE':
#                True
#            elif upit_3 == 'DA':
#                break
#        break
#    else:
#        print('------------------')
#        print('UNESITE BROJ 1-3!')
#        True




