![alt text](https://github.com/indahdwi12/tugas_posttest1/blob/main/tugas%20POSTEST1.drawio.png?raw=true)

#penjelasan output
output dari pilihan 1 yaitu (output hasil kilogram ke pounds) dengan proses "konversi kilogram ke pounds" adalah jika :
nilai kilogram * 2.205
contoh : 15 * 2.205 = 33.075
maka nilai dari pounds adalah 33.075 jika di kalikan dengan nilai kilogram sebesar 15

output dari pilihan 2 yaitu (output hasil kilogram ke ounce/ons) dengan proses "konversi kilogram ke ons" adalah jika :
nilai kilogram * 35.274
contoh : 7 * 35.274 = 246.918
maka nilai dari ons adalah 246.918 jika di kalikan dengan nilai kilogram sebesar 7

output dari pilihan 3 yaitu (output hasil kilogram ke gram) dengan proses "konvesi kilogram ke gram" adalah jika :
nilai kilogram * 1000
contoh : 12 * 1000 = 12000
maka nilai dari gram adalah 12000 jika di kalikan dengan nilai kilogram sebesar 12

[Uploading konversi kilogram.py…]()# konversi satuan kilogram

def convert(before,after,total):
    if before=="kilogram" and after=="lb":
        result = total * 2205
    else :
        result = total * 2205
    return result

before = input("masukkan massa kilogram yang akan di konversi :")
after = input("di konversi ke :")
total = int(input("berat satuan massa :"))
final = convert(before,after,total)
print("hasil konversi ", final, "lb")
print("\n")

def convert(before,after,total):
    if before=="kilogram" and after=="ons":
        result = total * 35274
    else :
        result = total * 35274
    return result

before = input("masukkan massa kilogram yang akan di konversi :")
after = input("di konversi ke :")
total = int(input("berat satuan massa :"))
final = convert(before,after,total)
print("hasil konversi ", final, "ons")
print("\n")

def convert(before,after,total):
    if before=="kilogram" and after=="gram":
        result = total * 1000
    else :
        result = total * 1000
    return result

before = input("masukkan massa kilogram yang akan di konversi :")
after = input("di konversi ke :")
total = int(input("berat satuan massa :"))
final = convert(before,after,total)
print("hasil konversi ", final, "gram")
print("\n")


![alt text](https://github.com/indahdwi12/tugas_posttest1/blob/main/output%20konversi%20kilogram.png?raw=true)
