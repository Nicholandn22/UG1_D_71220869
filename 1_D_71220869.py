print('========== KASIR ==========')

a = int(input('Harga Barang : '))
b = input('Apakah anda membeli barang lagi ? [yes/no] : ')
if b == 'yes':
    while True:
        a1 = int(input('Harga Barang : '))
        
        b1 = input('Apakah anda membeli barang lagi ? [yes/no] : ')

        if b1 == 'yes':
            continue
        elif b1 == 'no':
            break
        else :
            break
        
elif b == 'no':
    a1 = 0
    total2 = a  + a1
    print(total2)

else: 
    print('INVALID')
total = a  + a1
print(total)