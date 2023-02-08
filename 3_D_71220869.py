abc = int(input("Masukkan angka :"))
for i in range(abc):
    print('  '*i, ('* '*(abc-i))+('* '*(abc-(i+1))))
    
