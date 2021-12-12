import helper

programs = {
    "Word" : 5,
    "Excel" : 10,
    "Firefox" : 3,
    "MySQL" : 6,
    "MongoDB" : 17,
    "Chrome" : 9
}

def create(programKey, programValue):
    programs[programKey] = programValue
    print("Program", programKey, "dengan waktu proses", programValue, "berhasil dimasukkan!")

def sort():
    return sorted(programs.items(), key=lambda item: item[1], reverse=False)
    
p = True

while p != False:
    print("\nSelamat datang di Short Job First")
    print("Menu: ")
    print("1. Masukkan program baru")
    print("2. Lihat program yang telah di urutkan")
    print("3. Lihat program yang belum di urutkan")
    print("4. Eksekusi program")
    print("0. Keluar")

    pilihan = int(input("\nMasukkan pilihan anda: "))

    if pilihan == 0:
        print("dadah......")
        p = False

    elif pilihan == 1:
        helper.header("Masukkan program baru")
        programKey = str(input("Masukkan nama program: "))
        programValue = int(input("Masukkan lama pemrosesan: "))
        create(programKey, programValue)

    elif pilihan == 2:
        helper.header("Program yang telah di urutkan")
        sjf = sort()
        for key, value in sjf:
            print('Nama Program : {}\tWaktu Pemrosesan: {}'.format(key,value))

    elif pilihan == 3:
        helper.header("Program yang belum di urutkan")
        for key, value in programs.items():
            print('Nama Program : {}\t Waktu Pemrosesan: {}'.format(key, value))

    elif pilihan == 4:
        helper.header("Eksekusi program")
        sjf = sort()
        target = sjf[0]
        print("Program", target[0], "di eksekusi...")
        del programs[target[0]]

