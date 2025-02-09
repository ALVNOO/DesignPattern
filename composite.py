from datetime import datetime

# Component - Interface Base Class
class Item:
    def display_info(self):
        pass

# Leaf Classes (Buku, Majalah, Koran)
class Buku(Item):
    def __init__(self, title, publication_date, pages, rating, author):
        self.title = title
        self.publication_date = datetime.strptime(publication_date, "%Y-%m-%d")
        self.pages = pages
        self.rating = rating
        self.author = author

    def display_info(self):
        print(f"\n[Buku] Judul: {self.title}")
        print(f"Tanggal Terbit: {self.publication_date.strftime('%d-%m-%Y')}")
        print(f"Jumlah Halaman: {self.pages}")
        print(f"Rating: {self.rating}")
        print(f"Penulis: {self.author}")

class Majalah(Item):
    def __init__(self, title, publication_date, pages, rating, editionNumber):
        self.title = title
        self.publication_date = datetime.strptime(publication_date, "%Y-%m-%d")
        self.pages = pages
        self.rating = rating
        self.editionNumber = editionNumber

    def display_info(self):
        print(f"\n[Majalah] Judul: {self.title}")
        print(f"Tanggal Terbit: {self.publication_date.strftime('%d-%m-%Y')}")
        print(f"Jumlah Halaman: {self.pages}")
        print(f"Rating: {self.rating}")
        print(f"Nomor Edisi: {self.editionNumber}")

class Koran(Item):
    def __init__(self, title, publication_date, pages, rating, publisher):
        self.title = title
        self.publication_date = datetime.strptime(publication_date, "%Y-%m-%d")
        self.pages = pages
        self.rating = rating
        self.publisher = publisher

    def display_info(self):
        print(f"\n[Koran] Judul: {self.title}")
        print(f"Tanggal Terbit: {self.publication_date.strftime('%d-%m-%Y')}")
        print(f"Jumlah Halaman: {self.pages}")
        print(f"Rating: {self.rating}")
        print(f"Penerbit: {self.publisher}")

# Composite Class - Mengelola koleksi item
class Toko(Item):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, title):
        for item in self.items:
            if item.title == title:
                self.items.remove(item)
                print(f"Item '{title}' berhasil dihapus!\n")
                return
        print(f"Item '{title}' tidak ditemukan!\n")

    def display_info(self):
        print(f"\n=== {self.name} ===")
        if not self.items:
            print("Toko masih kosong!")
        for item in self.items:
            item.display_info()

# CLI Menu
def main():
    toko = Toko("Toko Buku & Majalah")
    
    while True:
        print("\n=== MENU TOKO ===")
        print("1. Tambah Item")
        print("2. Hapus Item")
        print("3. Lihat Semua Item")
        print("4. Keluar")
        choice = input("Pilih menu: ")

        if choice == "1":
            title = input("Judul: ")
            publication_date = input("Tanggal Terbit (YYYY-MM-DD): ")
            pages = int(input("Jumlah Halaman: "))
            rating = float(input("Rating (1.0 - 5.0): "))
            
            print("Pilih Jenis Item: 1. Buku, 2. Majalah, 3. Koran")
            item_type = input("Pilihan: ")

            if item_type == "1":
                author = input("Penulis: ")
                item = Buku(title, publication_date, pages, rating, author)
            elif item_type == "2":
                editionNumber = input("Nomor Edisi: ")
                item = Majalah(title, publication_date, pages, rating, editionNumber)
            elif item_type == "3":
                publisher = input("Penerbit: ")
                item = Koran(title, publication_date, pages, rating, publisher)
            else:
                print("Pilihan tidak valid!")
                continue

            toko.add_item(item)
            print("Item berhasil ditambahkan!\n")
        
        elif choice == "2":
            title = input("Masukkan judul item yang ingin dihapus: ")
            toko.remove_item(title)
        
        elif choice == "3":
            toko.display_info()
        
        elif choice == "4":
            print("Terima kasih telah menggunakan program ini!")
            break
        
        else:
            print("Pilihan tidak valid!\n")

if __name__ == "__main__":
    main()
