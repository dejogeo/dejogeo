import sqlite3
connection=sqlite3.connect("Politicka_opstina.db")
crsr=connection.cursor()
sql_command="""CREATE TABLE IF NOT EXISTS KO (                       
KO_id INTEGER PRIMARY KEY,
naziv VARCHAR(30));"""
crsr.execute(sql_command)
connection.commit()                                                        #Tabela katastarske opštine
crsr.execute("""CREATE TABLE IF NOT EXISTS kc (
kc_id INTEGER PRIMARY KEY,
broj_parcele VARCHAR(8),
KO_id INTEGER,
CONSTRAINT fk_KO
    FOREIGN KEY (KO_id)
    REFERENCES KO(KO_id));""")
connection.commit()                                                         #Tabela parcele
sql_command="""CREATE TABLE IF NOT EXISTS vodovod (
voda_id INTEGER PRIMARY KEY,
zona INTEGER,
materijal VARCHAR(10),
precnik_u_mm FLOAT,
koordinate FLOAT,
kota_vrha_cijevi FLOAT,
kc_id INTEGER,
CONSTRAINT fk_kc
    FOREIGN KEY (kc_id)
    REFERENCES kc(kc_id));"""
crsr.execute(sql_command)
connection.commit()                                                          #Tabela vodovoda
sql_command="""CREATE TABLE IF NOT EXISTS struja (
struja_id INTEGER PRIMARY KEY,
napon INTEGER,
broj_kablova INTEGER,
koordinate FLOAT,
kota_kabla FLOAT,
kc_id INTEGER,
CONSTRAINT fk_kc
    FOREIGN KEY (kc_id)
    REFERENCES kc(kc_id));"""
crsr.execute(sql_command)
connection.commit()                                                          #Tabela elektroenergetskog voda

sql_command="""CREATE TABLE IF NOT EXISTS toplovod (
toplovod_id INTEGER PRIMARY KEY,
materijal VARCHAR(20),
precnik FLOAT,
broj_cijevi INTEGER,
koordinate FLOAT,
kota_cijevi FLOAT,
kc_id INTEGER,
CONSTRAINT fk_kc
    FOREIGN KEY (kc_id)
    REFERENCES kc(kc_id));"""
crsr.execute(sql_command)                                                           #Tabela toplovoda
sql_command="""CREATE TABLE IF NOT EXISTS kanalizacija (
kanalizacija_id INTEGER PRIMARY KEY,
oznaka_sistema VARCHAR(10),
materijal VARCHAR(20),
presjek FLOAT,
koordinate FLOAT,
kota_cijevi FLOAT,
kc_id INTEGER,
CONSTRAINT fk_kc
    FOREIGN KEY (kc_id)
    REFERENCES kc(kc_id));"""
crsr.execute(sql_command)                                                   #Tabela kanalizacije
sql_command="""CREATE TABLE IF NOT EXISTS naftagas (
naftagas_id INTEGER PRIMARY KEY,
materijal VARCHAR(20),
precnik FLOAT,
broj_cijevi INTEGER,
koordinate FLOAT,
kota_cijevi FLOAT,
kc_id INTEGER,
CONSTRAINT fk_kc
    FOREIGN KEY (kc_id)
    REFERENCES kc(kc_id));"""
crsr.execute(sql_command)                                                   #Tabela voda nafte i plina
sql_command="""CREATE TABLE IF NOT EXISTS telekom (
telekom INTEGER PRIMARY KEY,
vrsta_kabla VARCHAR(20),
broj_cijevi INTEGER,
koordinate FLOAT,
kota_cijevi FLOAT,
kc_id INTEGER,
CONSTRAINT fk_kc
    FOREIGN KEY (kc_id)
    REFERENCES kc(kc_id));"""
crsr.execute(sql_command)
connection.commit()
connection.close()
