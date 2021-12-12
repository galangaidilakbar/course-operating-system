def header(title):
    print("-" * 50)
    print("\t\t", title)
    print("-" * 50)

def ubahRamKeMbps(ramInGbps):
    return ramInGbps * 1024

def hitungPetaBit(ram, blok):
    return ram / blok