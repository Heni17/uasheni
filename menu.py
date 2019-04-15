from koding.nilai import Nilai
from koding.gaji  import Gaji
from koding.pembayaran import Pembayaran
from koding.kalkulator import Kalkulator
import getpass

def Login():
        
        print ("\nLogin")
        user = input("Username : ")
        password = getpass.getpass("Password : ")
        if user == 'heni' and password == '123':
            Menu()
        else :
            print ("\nUsername atau Password yang anda masukan salah !!!")
            Login()
            
def Menu():

         print("\nMenu :")
         print("1.Nilai")
         print("2.Gaji") 
         print("3.Pembayaran")
         print("4.Kalkulator")
         pilihan = (input("Masukan pilihan (1/2/3/4) ? "))
         if   pilihan == '1' :
              Nilai()
              Tambah()
         elif pilihan == '2' :
              Gaji()
              Tambah()
         elif pilihan == '3' :
              Pembayaran()
              Tambah()
         elif pilihan == '4' :
              Kalkulator()
              Tambah()
         else :
              print ("Pilihan Tidak Ditemukan !!!")
              Tambah()

def Tambah() :
    
        tambah =input("\t\nKembali ke Menu (y/t) : ")
        if tambah == 'y' :
            Menu()
        else :
            print("\nTerimakasih")
            input('')
            
Login()
