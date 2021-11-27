print("Pratikum 4")
print()
data=[]
while True:
    nama=input("Nama Lengkap\t: ")
    nim=input("NIM Mahasiswa\t: ")
    tugas=int(input("Nilai Tugas\t: "))
    uts=int(input("Nilai UTS\t: "))
    uas=int(input("Nilai UAS\t: "))
    hitung=(int(tugas)*30/100)+(int(uts)*35/100)+(int(uas)*35/100)
    data.append([nama, nim, tugas, uts, uas, hitung])
    lanjut=input("Tambah Data Lagi?(y/t)")
    if lanjut=="t" or lanjut=="T":
        print("Data Mahasiswa")
        print(65*"=")
        print("| {0:^10} | {1:^10} | {2:^6} | {3:^4} | {4:^4} | {5:^12} |".format("NAMA", "NIM", "TUGAS", "UTS", "UAS", "NILAI AKHIR"))
        print(65*"=")
        for x in data:
            print("| {0:>10} | {1:>10} | {2:>6} | {3:>4} | {4:>4} | {5:>12} |".format(x[0],x[1],x[2],x[3],x[4],x[5]))
            print(65*"=")
        else:
            break

