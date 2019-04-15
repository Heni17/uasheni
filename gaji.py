def Gaji():

    from texttable import Texttable
    table = Texttable (max_width=900)
    
    nama = []
    jabatan = []
    gaji = []
    no = 0
    jawab = "y"

    while(jawab == 'y'):
        nama.append(input("\nMasukan nama : "))
        jab = input("jabatan : ")
        jabatan.append(jab)
        if (jab == 'programmer'):
            gaji.append(3000000)
            jawab=input("\n Tambah lagi? ")
            no+=1
        elif (jab == 'qc'):
           gaji.append(2500000)
           jawab=input("\n Tambah lagi? ")
           no+=1
        elif (jab == 'marketing'):
            gaji.append(4000000)
            jawab=input("\n Tambah lagi? ")
            no+=1
        else:
             print("\njabatan tidak ditemukan")
             print menu import login

    for i in range (no):
        table.set_cols_dtype(['i','t','t','i'])
        table.add_rows([['NO','NAMA','JABATAN','GAJI'],
                        [i+1,nama[i],jabatan[i],gaji[i]]])
    print(table.draw())
