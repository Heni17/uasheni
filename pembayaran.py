def Pembayaran():
    
    jawab = "y"

    while(jawab == "y"):
        from texttable import Texttable
        table = Texttable (max_width=800)
   
        nama  = (input("\nMasukan nama  : "))
        nim   = (input("Masukan NIM   : "))
        kelas = (input("Masukan kelas : "))
        
        UTS= (input("\nBayar UTS (y/t) ? "))
        if    UTS == 'y':
              uang_UTS = 50000
        else:
              uang_UTS = 0

        UAS = (input("\nBayar UAS (y/t) ? "))
        if    UAS == 'y':
              uang_UAS = 50000
        else:
              uang_UAS = 0
              
        Bulanan = (input("\nBayar bulanan (y/t) ? "))
        if    Bulanan == 'y':
              uang_Bulanan = int(input("\nDi bayar berapa bulan ? "))
              total_Bulanan = 500000*uang_Bulanan
        else:
              total_Bulanan = 0
              
        Seminar = (input("\nBayar seminar (y/t) ? "))
        if     Seminar == 'y':
               uang_Seminar = 100000
        else:
               uang_Seminar = 0
            
        Kas = (input("\nBayar kas (y/t) ? "))
        if     Kas == 'y':
               uang_Kas = int(input("\nDi bayar berapa bulan ? "))
               total_Kas = 20000*uang_Kas
        else:
               total_Kas = 0

        print ("\n\nBeban admin 5000")
        input('')
        uang_Admin = 5000

        total = uang_UTS+uang_UAS+total_Bulanan+uang_Seminar+total_Kas+uang_Admin

   
        table.set_cols_dtype(['t','t','t','i','i','i','i','i','i','i'])
        table.add_rows([['NAMA','NIM','KELAS','UTS','UAS','BULANAN','SEMINAR','KAS','ADMIN','TOTAL'],
                         [nama,nim,kelas,uang_UTS,uang_UAS,total_Bulanan,uang_Seminar,total_Kas,uang_Admin,total]])
        print (table.draw())
        
        jawab = input("Tambah data (y/t)?")
