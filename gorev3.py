# - Görev 3 - Liste İşlemleri
# İstenen 11 farklı işlem aşağıdaki liste üzerinde gerçekleştirecek.

arabalar = ["BMW", "Mercedes", "Opel", "Toyota", "Renault", "Audi"]

# 1 - Listenin kendisi.
print(arabalar)

# 2 - Liste kaç elemanlıdır?
print(len(arabalar))

# 3 - Listenin ilk ve son elemanı nedir?
print(f"{arabalar[0]} - {arabalar[-1]}")

# 4 - Mazda değerini Toyota ile değiştirin.
toyotaIndex = arabalar.index("Toyota")
arabalar[toyotaIndex] = "Mazda"
print(arabalar)

# 5 - Mercedes listenin bir elemanı mıdır?
print("Mercedes" in arabalar)

# 6 - Listenin sondan 2. değeri nedir?
print(arabalar[-2])

# 7 - Listenin ilk 3 elemanını alın.
ilkUcEleman = arabalar[0:3]
print(ilkUcEleman)

# 8 - Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.
arabalar[-2:] = ["Toyota", "Renault"]
print(arabalar)

# 9 - Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
yeniArabalar = ["Audi", "Nissan"]
arabalar.extend(yeniArabalar)
print(arabalar)

# 10 - Listenin son elemanını silin.
arabalar.pop()
print(arabalar)

# 11 - Liste elemanlarını tersten yazdırınız.
arabalar.reverse()
print(arabalar)

# H. Arda Karabacak - İstinye Üniversitesi - Bilişim Güvenliği Teknolojisi