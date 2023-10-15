# konversi satuan kilogram

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