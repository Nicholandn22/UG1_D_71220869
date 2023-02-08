while True:
    print('--------Nilai ke 1--------')
    a1 = int(input('Nilai Harian : '))
    a2 = int(input('Nilai UTS: '))
    a3 = int(input('Nilai UAS: '))


    print('--------Nilai ke 2--------')
    b1 = int(input('Nilai Harian : '))
    b2 = int(input('Nilai UTS: '))
    b3 = int(input('Nilai UAS: '))

    print('--------Total Nilai--------')

    ha1 = int((a1) *30/100)
    hts1 = int((a2) *30/100)
    has1 = int((a3) *40/100)

    ha2 = int((b1) *30/100)
    hts2 = int((b2) *30/100)
    has2= int((b3) *40/100)

    hasil = ((ha1 + hts1 + has1) + (ha2 + hts2 + has2)) /2
    cd = 79
    dc = 49

    if hasil <= cd:
        print('Total nilai yang didapat : ',hasil)
        print('Total nilai dalam huruf : B')
    elif hasil <= dc:
        print('Total nilai yang didapat : ',hasil)
        print('Total nilai dalam huruf : C')
    else :
        print('error')
