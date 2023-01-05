import csv
import sqlite3
import uuid
import Proba

connection=sqlite3.connect("Politicka_opstina1.db")
crsr=connection.cursor()

#def ispis_voda(connection, broj_parcele, naziv_KO):
#    crsr = connection.cursor()
#    crsr.execute("SELECT * FROM sqlite_schema WHERE kc_id=?", (broj_parcele, naziv_KO))
#    separator = ", "
#    rez = separator.join(crsr.fetchall())
#    return rez



with open('Ispis1.csv',mode='w') as employee_file:
    employee_writer=csv.writer(employee_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)

    parcela=int(input('Unesite broj parcele: '))
    opstina=input('Unesite naziv KO: ')
    #c=int(input('Za ispis vodovoda ukucaj 1,\nZa ispis elektroenergetskog voda ukucaj 2,\nZa ispis toplovoda ukucaj 3,\nZa ispis kanalizacionog voda ukucaj 4,\nZa ispis naftovoda ili gasovoda ukucaj 5,\nZa ispis voda telekoma ukucaj 6: '))

    #e = Proba.KO.prenos_KO_id(connection, opstina)
    d = Proba.Kc.prenos_kc_id(connection, parcela, opstina)


    ##p1 = Proba.Kc(parcela, d, opstina, e)
    ##o1 = Proba.KO(opstina,e)

    e=Proba.Kc.ispis_voda(connection,d)
    print(e)
    ##ispis_1=p1.ispis_voda(connection,d)
    employee_writer.writerow([e])





