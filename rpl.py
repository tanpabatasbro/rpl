list_buku = []
while  True:
    print("masukkan data buku")
    judul = input("judul buku\t:")
    penulis = input("nama penulis\t:")

    buku_baru  = [judul,penulis]
    list_buku.append(buku_baru)

    print("\n\n","="*10,"data buku","="*10,"\n\n")
    
    print("NO.\t| judul\t\t\t\t| penulis")
    for index,buku in enumerate(list_buku):
        print(f"{index+1}\t| {buku[0]}\t\t\t\t| {buku[1]}\n")

    print("\n\n","="*20)
    lanjut = input("apakah di lanjutkan?(y/n)")

    if lanjut == "n":
        break

print("PROGRAM SELESAI")
    
