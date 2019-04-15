def Kalkulator():
    
    jawab = "y"
    
    while(jawab == "y"):

        print("\npilih operasi.")
        print("1. Perkalian")
        print("2. Pembagian")
        print("3. Penjumlahan")
        print("4. Pengurangan")
        jenis = input("masukan pilihan (1/2/3/4):")

        if   jenis == '1':
             print("\nPerkalian")
             angka1 = int(input("Masukan angka ke 1 : "))
             angka2 = int(input("Masukan angka ke 2 : "))
             hasil = angka1*angka2
             print(angka1,"x",angka2,"=",hasil)

        elif jenis == '2':
             print("\nPembagian")
             angka1 = int(input("Masukan angka ke 1 : "))
             angka2 = int(input("Masukan angka ke 2 : "))
             hasil = angka1/angka2
             print(angka1,":",angka2,"=",hasil)
             
        elif jenis == '3':
             print("\nPenjumlahan")
             angka1 = int(input("Masukan angka ke 1 : "))
             angka2 = int(input("Masukan angka ke 2 : "))
             hasil = angka1+angka2
             print(angka1,"+",angka2,"=",hasil)
            
        elif jenis == '4':
             print("\nPengurangan")
             angka1 = int(input("Masukan angka ke 1 : "))
             angka2 = int(input("Masukan angka ke 2 : "))
             hasil = angka1-angka2
             print(angka1,"-",angka2,"=",hasil)

        else:
            print ("Pilihan Tidak Ditemukan !!!")

            
        jawab = input("Tambah data (y/t)?")
 
