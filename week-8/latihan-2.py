import helper

helper.header("Latihan 2 Petabit")

totalRam = int(input("Kapasitas RAM: "))
totalBlok = int(input("Blok/unit: "))
petabit = helper.hitungPetaBit(helper.ubahRamKeMbps(totalRam), totalBlok)

print("Kapasitas peta bit adalah ", petabit , "KB per blok" )
print("\nProgram tereksekusi")

ramUntukProgram = int(input("Kapasitas Program : "))
blokTerpakai = helper.hitungPetaBit(helper.ubahRamKeMbps(ramUntukProgram), petabit)

print("\nInformasi Kondisi peta bit")
print("-"*50)

print("total blok = ", totalBlok)
print("Blok terpakai = ", blokTerpakai)

print("\njumlah blok bernilai 1 = ", blokTerpakai)
print("jumlah blok bernilai 0 = ", totalBlok - blokTerpakai)
