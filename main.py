import os

print("Selamat Datang di Aplikasi Sistem Pakar Diagnosis Penyakit Ginjal")

nama = input ("Nama\t: ")
pilihan = input("Halo "+nama+", Apakah anda ingin melakukan diagnosa? (y/n)")

os.system("clear")

while pilihan == "y":
  print("\nApakah anda merasa mual?")
  diag1 = input("Jawab (y/n) : ")

  if diag1 == "y" :
    print("\nApakah anda merasakan gejala berikut ini?")
    print("1. Muntah")
    print("2. Darah dalam urine")
    print("3. Demam atau menggigil")
    diag2 = input("Jawab (y/n) : ")

    if diag2 == "y" :
      print("\nApakah anda sering buang air kecil dimalam hari?")
      diag3 = input("Jawab (y/n) : ")

      if diag3 == "y" :
        print("\nApakah anda merasakan gejala berikut ini?")
        print("1. Tremor tangan")
        print("2. Mudah Lelah")
        print("3. Kulit Kemerahan")
        print("4. Volume urine berkurang")
        diag4 = input("Jawab (y/n) : ")

        if diag4 == "y" :
          print("\nHi, "+nama+" Anda menderita penyakit Gagal Ginjal Akut, silakan konsultasi dokter untuk mendapatkan penanganan lanjut")
          print("\nTerima kasih telah menggunakan sistem pakar ini.")
          print("\n===========================================================")
          pilihan = input("Halo "+nama+", Apakah anda ingin melakukan diagnosa? (y/n)")
          if pilihan == "y" :
            os.system("clear")
            print("Selamat Datang di Aplikasi Sistem Pakar")
          else :
            print("\n===========================================================")
        
        elif diag4 == "n" :
          print("\nHi "+nama+", Anda tidak mengalami penyakit ginjal, namun tetap konsultasi dokter untuk mendapatkan penanganan lanjut")
          print("\nTerima kasih telah menggunakan sistem pakar ini.")
          print("\n===========================================================")
          pilihan = input("Halo "+nama+", Apakah anda ingin melakukan diagnosa? (y/n)")
          if pilihan == "y" :
            os.system("clear")
            print("Selamat Datang di Aplikasi Sistem Pakar")
          else :
            print("\n===========================================================")

        else :
          print("\nSilahkan jawab dengan y/n.")
        
      elif diag3 == "n":
        print("\nApakah anda merasakan gejala berikut ini?")
        print("1. Mudah lelah")
        print("2. Hilang nafsu makan")
        print("3. Ada nanah di kencing")
        print("4. Rasa sakit diperut samping atau punggung bagian bawah")
        print("5. Diare")
        diag5 = input("Jawab (y/n) : ") 

        if diag5 == "y" :
          print("\nHi "+nama+", Anda menderita penyakit Infeksi Ginjal (Pielonefritis), silakan konsultasi dokter untuk mendapatkan penanganan lanjut")
          print("\nTerima kasih telah menggunakan sistem pakar ini.")
          print("\n===========================================================")
          pilihan = input("Halo "+nama+", Apakah anda ingin melakukan diagnosa? (y/n)")
          if pilihan == "y" :
            os.system("clear")
            print("Selamat Datang di Aplikasi Sistem Pakar")
          else :
            print("\n===========================================================")
        
        elif diag5 == "n" :
          print("\nHi "+nama+", Anda tidak mengalami penyakit ginjal, namun tetap konsultasi dokter untuk mendapatkan penanganan lanjut")
          print("\nTerima kasih telah menggunakan sistem pakar ini.")
          print("\n===========================================================")
          pilihan = input("Halo "+nama+", Apakah anda ingin melakukan diagnosa? (y/n)")
          if pilihan == "y" :
            os.system("clear")
            print("Selamat Datang di Aplikasi Sistem Pakar")
          else :
            print("\n===========================================================")

        else :
          print("\nSilahkan jawab dengan y/n.")
      else :
          print("\nSilahkan jawab dengan y/n.")
    
    elif diag2 == "n" :
      print("\nApakah anda merasakan gejala berikut ini?")
      print("1. Sering buang air kecil")
      print("2. Hilang nafsu makan")
      print("3. Kulit gatal")
      print("4. Perubahan badan secara signifikan")
      print("5. Nyeri dada")
      print("6. Tekanan darah tinggi")
      print("7. Insomnia")
      print("8. Keram otot")
      diag6 = input("Jawab (y/n) : ") 

      if diag6 == "y" :
        print("\nHi "+nama+", Anda menderita penyakit Gagal Ginjal Kronis, silakan konsultasi dokter untuk mendapatkan penanganan lanjut")
        print("\nTerima kasih telah menggunakan sistem pakar ini.")
        print("\n===========================================================")
        pilihan = input("Halo "+nama+", Apakah anda ingin melakukan diagnosa? (y/n)")
        if pilihan == "y" :
          os.system("clear")
          print("Selamat Datang di Aplikasi Sistem Pakar")
        else :
            print("\n===========================================================")
        
      elif diag6 == "n" :
        print("\nHi "+nama+", Anda tidak mengalami penyakit ginjal, namun tetap konsultasi dokter untuk mendapatkan penanganan lanjut")
        print("\nTerima kasih telah menggunakan sistem pakar ini.")
        print("\n===========================================================")
        pilihan = input("Halo "+nama+", Apakah anda ingin melakukan diagnosa? (y/n)")
        if pilihan == "y" :
          os.system("clear")
          print("Selamat Datang di Aplikasi Sistem Pakar")
        else :
            print("\n===========================================================")
      else :
        print("\nSilahkan jawab dengan y/n.")

    else :
      print("\nSilahkan jawab dengan y/n.")

  elif diag1 == "n" :
    print("\nApakah anda merasakan gejala berikut ini?")
    print("1. Kulit kemerahan")
    print("2. Hilang nafsu makan")
    print("3. Nyeri pada punggung bagian bawah")
    print("4. Frekuensi buang air meningkat")
    print("5. Nyeri saat buang air kecil")
    print("6. Urin berwarna merah muda, merah, atau coklat")
    diag7 = input("Jawab (y/n) : ")

    if diag7 == "y" :
      print("\nHi "+nama+", Anda menderita penyakit Batu Ginjal, silakan konsultasi dokter untuk mendapatkan penanganan lanjut")
      print("\nTerima kasih telah menggunakan sistem pakar ini.")
      print("\n===========================================================")
      pilihan = input("Halo "+nama+", Apakah anda ingin melakukan diagnosa? (y/n)")
      if pilihan == "y" :
        os.system("clear")
        print("Selamat Datang di Aplikasi Sistem Pakar")
      else :
        print("\n===========================================================")
        
    elif diag7 == "n" :
      print("\nApakah anda merasakan gejala berikut ini?")
      print("1. Darah dalam urin")
      print("2. Volume urin berkurang")
      print("3. Hilang nafsu makan")
      print("4. Tekanan darah tinggi")
      print("5. Nyeri pada punggung bagian bawah")
      print("6. Nyeri saat buang air kecil")
      print("7. Rambut dan kuku menjadi rapuh")
      diag8 = input("Jawab (y/n) : ")
      
      if diag8 == "y" :
        print("\nHi "+nama+", Anda menderita penyakit Sindrom Nefrotik, silakan konsultasi dokter untuk mendapatkan penanganan lanjut")
        print("\nTerima kasih telah menggunakan sistem pakar ini.")
        print("\n===========================================================")
        pilihan = input("Halo "+nama+", Apakah anda ingin melakukan diagnosa? (y/n)")
        if pilihan == "y" :
          os.system("clear")
          print("Selamat Datang di Aplikasi Sistem Pakar")
        else :
            print("\n===========================================================")
        
      elif diag8 == "n" :
        print("\nApakah anda merasakan gejala berikut ini?")
        print("1. Demam atau menggigil")
        print("2. Mudah lelah")
        print("3. Tekanan darah tinggi")
        print("4. Nyeri diperut bagian bawah")
        print("5. Berat badan turun")
        print("6. Pembengkakan organ tubuh tertentu")
        diag9 = input("Jawab (y/n) : ")
      
        if diag9 == "y" :
          print("\nHi "+nama+", Anda menderita penyakit Kanker Ginjal, silakan konsultasi dokter untuk mendapatkan penanganan lanjut")
          print("\nTerima kasih telah menggunakan sistem pakar ini.")
          print("\n===========================================================")
          pilihan = input("Halo "+nama+", Apakah anda ingin melakukan diagnosa? (y/n)")
          if pilihan == "y" :
            os.system("clear")
            print("Selamat Datang di Aplikasi Sistem Pakar")
          else :
            print("\n===========================================================")
        
        elif diag9 == "n" :
          print("\nHi "+nama+", Anda tidak mengalami penyakit ginjal, namun tetap konsultasi dokter untuk mendapatkan penanganan lanjut")
          print("\nTerima kasih telah menggunakan sistem pakar ini.")
          print("\n===========================================================")
          pilihan = input("Halo "+nama+", Apakah anda ingin melakukan diagnosa? (y/n)")
          if pilihan == "y" :
            os.system("clear")
            print("Selamat Datang di Aplikasi Sistem Pakar")
          else :
            print("\n===========================================================")
        else :
          print("\nSilahkan jawab dengan y/n.")
      else :
        print("\nSilahkan jawab dengan y/n.")
    else :
      print("\nSilahkan jawab dengan y/n.")
  else :
    print("\nSilahkan jawab dengan y/n.")
