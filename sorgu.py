import pymysql.cursors
host = input("host: ")
user = input("user: ")
password = input("password: ")
db = input("database: ")
charset = input("charset: ")


con = pymysql.connect(host=host,
                    user=user,
                    password=password,
                    db=db,
                    charset=charset,
                    cursorclass= pymysql.cursors.DictCursor)


db = con.cursor()


sorgulamaYontemi = input("sorgulama yöntemi: ")


if sorgulamaYontemi == "id":
    enBuyukid = input("en büyük id: ")
    enKucukid = input("en küçük id: ")
    idKolonismi = input("id kolon ismi: ")
    VTisim = input("tablonun ismi: ")
    db.execute('SELECT * FROM '+VTisim+' WHERE '+idKolonismi+' BETWEEN '+enKucukid+' AND '+enBuyukid)
    con.commit()
    sonucidSorgu = db.fetchall()
    for i in sonucidSorgu:
        print(i[''+idKolonismi+''])
    
elif sorgulamaYontemi == "isim":
    isimArguman = input("ismin içinde geçen harf veya harfler, sayı ya da sayılar: ")
    isimKolonismi = input("isim kolon ismi: ")
    VTisim2 = input("tablonun ismi: ")
    db.execute('SELECT * FROM '+VTisim2+' WHERE '+isimKolonismi+' LIKE "%'+isimArguman+'%"')
    con.commit()
    sonucisimSorgu = db.fetchall()
    for i in sonucisimSorgu:
        print(i[''+isimKolonismi+''])

elif sorgulamaYontemi == "sırala":
    kolonismi = input("kolon ismi: ")
    VTisim6 = input("tablo ismi: ")
    db.execute('SELECT * FROM '+VTisim6+' ORDER BY '+kolonismi)
    con.commit()
    orderSonuc = db.fetchall()
    for i in orderSonuc:
        print(i[''+kolonismi+''])

elif sorgulamaYontemi == "incele":
    kolonismi2 = input("kolon ismi: ")
    VTisim7 = input("tablo ismi: ")
    db.execute('SELECT DISTINCT '+kolonismi2+' FROM '+VTisim7)
    con.commit()
    inspectSonuc = db.fetchall()
    for i in inspectSonuc:
        print(i[''+kolonismi2+''])

elif sorgulamaYontemi == "min":
    kolonismi3 = input("kolon ismi: ")
    VTisim8 = input("tablo ismi: ")
    db.execute('SELECT MIN('+kolonismi3+') FROM '+VTisim8)
    con.commit()
    minSonuc = db.fetchall()
    for i in minSonuc:
        print(i)

elif sorgulamaYontemi == "max":
    kolonismi4 = input("kolon ismi: ")
    VTisim9 = input("tablo ismi: ")
    db.execute('SELECT MAX('+kolonismi4+') FROM '+VTisim9)
    con.commit()
    maxSonuc = db.fetchall()
    for i in maxSonuc:
        print(i)

elif sorgulamaYontemi == "toplam":
    kolonismi5 = input("kolon ismi: ")
    VTisim10 = input("tablo ismi: ")
    db.execute('SELECT SUM('+kolonismi5+') FROM '+VTisim10)
    con.commit()
    sumSonuc = db.fetchall()
    for i in sumSonuc:
        print(i)

elif sorgulamaYontemi == "ortalama":
    kolonismi6 = input("kolon ismi: ")
    VTisim11 = input("tablo ismi: ")
    db.execute('SELECT AVG('+kolonismi6+') FROM '+VTisim11)
    con.commit()
    avgSonuc = db.fetchall()
    for i in avgSonuc:
        print(i)

elif sorgulamaYontemi == "toplam_kayit":
    idKolonismi3 = input("id kolonunun ismi: ")
    VTisim12 = input("tablo ismi: ")
    db.execute('SELECT COUNT('+idKolonismi3+') FROM '+VTisim12)
    con.commit()
    sonucCount = db.fetchall()
    for i in sonucCount:
        print(i)

elif sorgulamaYontemi == "ikili_birleştir":
    ilkKolonismi = input("ilk kolon ismi: ")
    ikinciKolonismi = input("ikinci kolon ismi: ")
    VTisim13 = input("tablo ismi: ")
    db.execute('SELECT CONCAT('+ilkKolonismi+', " ", '+ikinciKolonismi+') FROM '+VTisim13)
    con.commit()
    sonucikiliBirlestir = db.fetchall()
    for i in sonucikiliBirlestir:
        print(i)

elif sorgulamaYontemi == "üçlü_birleştir":
    ilkKolonismi2 = input("ilk kolon ismi: ")
    ikinciKolonismi2 = input("ikinci kolon ismi: ")
    üçüncüKolonismi = input("üçüncü kolon ismi: ")
    VTisim14 = input("tablo ismi: ")
    db.execute('SELECT CONCAT('+ilkKolonismi2+', " ", '+ikinciKolonismi2+', " ", '+üçüncüKolonismi+') FROM '+VTisim14)
    con.commit()
    sonucüçlüBirleştir = db.fetchall()
    for i in sonucüçlüBirleştir:
        print(i)




elif sorgulamaYontemi == "şifre":
    sifreSelectMethod = input("şifre bulma metodu: ")
    if sifreSelectMethod == "isim":
        isimArguman2 = input("ismin içinde geçen harf ya da harfler, sayı ya da sayılar: ")
        isimKolonismi2 = input("isim kolon ismi: ")
        VTisim3 = input("tablonun ismi: ")
        db.execute('SELECT * FROM '+VTisim3+' WHERE '+isimKolonismi2+' LIKE "%'+isimArguman2+'%"')
        con.commit()
        sonucsifreSorgu = db.fetchall()
        for i in sonucsifreSorgu:
            print(i[''+isimKolonismi2+''])
    elif sifreSelectMethod == "şifre içeriği":
        sifreArguman = input("şifrenin içinde geçen harf ya da harfler, sayı ya da sayılar:")
        sifreKolonismi = input("şifre kolon ismi: ")
        VTisim4 = input("tablonun ismi: ")
        db.execute('SELECT * FROM '+VTisim4+' WHERE '+sifreKolonismi+' LIKE "%'+sifreArguman+'%"')
        con.commit()
        sonucsifreSorgu2 = db.fetchall()
        for i in sonucsifreSorgu2:
            print(i[''+sifreKolonismi+''])

    elif sifreSelectMethod == "id":
        idArguman = input("id: ")
        idKolonismi2 = input("id kolon ismi: ")
        VTisim5 = input("tablonun ismi: ")
        db.execute('SELECT * FROM '+VTisim5+' WHERE '+idKolonismi2+' LIKE "%'+idArguman+'%"')
        con.commit()
        sonucsifreSorgu3 = db.fetchall()
        for i in sonucsifreSorgu3:
            print(i[''+idKolonismi2+''])


       
        



    








