import helper

helper.header("Latihan 1 Petabit")

ram = int(input("Kapasitas RAM: "))
blok = int(input("Blok/unit: "))
petabit = helper.hitungPetaBit(helper.ubahRamKeMbps(ram), blok)

print("-" * 50)
print("Kapasitas peta bit adalah ", petabit , "KB per blok" )
