import helper

programs = ["MySQL", "PostgreSQL", "MongoDB"]

p = True
while p != False:
    print("\nSelamat datang di First in first out")
    print("Menu: ")
    print("1. Masukkan nama program")
    print("2. Lihat urutan program")
    print("3. Eksekusi program pertama")
    print("0. Keluar")

    pilihan = int(input("\nMasukkan pilihan anda: "))

    if pilihan == 0:
        print("dadahhh.....")
        p = False

    elif pilihan == 1:
        helper.header("Memasukkan Program baru")
        namaProgram = str(input("Masukkan nama program: "))
        programs.append(namaProgram)
        print("program ", namaProgram, "berhasil di masukkan")

    elif pilihan == 2:
        helper.header("List program yang akan di eksekusi")
        for program in programs:
            print(program)

    elif pilihan == 3:
        helper.header("Eksekusi program")
        print("Program ", programs[0], "di eksekusi...")
        programs.pop(0)

    else :
        print("Oups.. terjadi kesalahan, coba pilih 1 untuk memasukkan nama program!")
