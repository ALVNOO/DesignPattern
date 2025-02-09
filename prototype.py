from datetime import datetime
import copy

# Class Parent (Prototype)
class Toko:
    def __init__(self, title, publication_date, pages, rating, additional_info=None):
        self.title = title  # String
        self.publication_date = datetime.strptime(publication_date, "%Y-%m-%d")  # Date
        self.pages = pages  # Integer
        self.rating = rating  # Float
        self.additional_info = additional_info if additional_info else {}  # Dictionary
    
    def display_info(self):
        print(f"\nJudul: {self.title}")
        print(f"Tanggal Terbit: {self.publication_date.strftime('%d-%m-%Y')}")
        print(f"Jumlah Halaman: {self.pages}")
        print(f"Rating: {self.rating}")
        print(f"Informasi Tambahan: {self.additional_info}")
    
    def clone(self):
        return copy.deepcopy(self)

# Class Child 1 (Buku)
class Buku(Toko):
    def __init__(self, title, publication_date, pages, rating, author):
        additional_info = {"Penulis": author}
        super().__init__(title, publication_date, pages, rating, additional_info)

# Class Child 2 (Majalah)
class Majalah(Toko):
    def __init__(self, title, publication_date, pages, rating, editionNumber):
        additional_info = {"Nomor Edisi": editionNumber}
        super().__init__(title, publication_date, pages, rating, additional_info)

# Class Child 3 (Koran)
class Koran(Toko):
    def __init__(self, title, publication_date, pages, rating, publisher):
        additional_info = {"Penerbit": publisher}
        super().__init__(title, publication_date, pages, rating, additional_info)

# Prototype Registry
class PrototypeRegistry:
    def __init__(self):
        self.prototypes = {}
    
    def register_prototype(self, key, prototype):
        self.prototypes[key] = prototype
    
    def clone_prototype(self, key, **kwargs):
        if key in self.prototypes:
            cloned_obj = self.prototypes[key].clone()
            cloned_obj.__dict__.update(kwargs)
            return cloned_obj
        else:
            print("Prototipe tidak ditemukan!")
            return None

# Class TokoManager
class TokoManager:
    def __init__(self):
        self.items = []  # Menyimpan daftar objek Buku, Majalah, Koran
        self.prototype_registry = PrototypeRegistry()

    def add_prototype(self):
        print("\nTambah Prototipe:")
        title = input("Judul: ")
        publication_date = input("Tanggal Terbit (YYYY-MM-DD): ")
        pages = int(input("Jumlah Halaman: "))
        rating = float(input("Rating (1.0 - 5.0): "))
        
        print("Pilih Jenis Item: 1. Buku, 2. Majalah, 3. Koran")
        choice = input("Pilihan: ")

        if choice == "1":
            author = input("Penulis: ")
            prototype = Buku(title, publication_date, pages, rating, author)
            self.prototype_registry.register_prototype("buku", prototype)
        elif choice == "2":
            editionNumber = input("Nomor Edisi: ")
            prototype = Majalah(title, publication_date, pages, rating, editionNumber)
            self.prototype_registry.register_prototype("majalah", prototype)
        elif choice == "3":
            publisher = input("Penerbit: ")
            prototype = Koran(title, publication_date, pages, rating, publisher)
            self.prototype_registry.register_prototype("koran", prototype)
        else:
            print("Pilihan tidak valid!")
    
    def add_item_from_prototype(self):
        print("\nTambahkan Item dari Prototipe:")
        key = input("Masukkan jenis item (buku, majalah, koran): ")
        new_title = input("Judul Baru: ")
        new_item = self.prototype_registry.clone_prototype(key, title=new_title)
        
        if new_item:
            self.items.append(new_item)
            print("Item berhasil ditambahkan dari prototipe!")
    
    def delete_item(self):
        title = input("\nMasukkan judul item yang ingin dihapus: ")
        for i, item in enumerate(self.items):
            if item.title == title:
                self.items.pop(i)
                print("Item berhasil dihapus!\n")
                return
        print("Item tidak ditemukan!\n")

    def display_all_items(self):
        print("\n=== DAFTAR ITEM ===")
        for item in self.items:
            item.display_info()

# main
def main():
    toko_manager = TokoManager()

    while True:
        print("\n=== Toko ===")
        print("1. Tambah Prototipe")
        print("2. Tambah Item dari Prototipe")
        print("3. Hapus Item")
        print("4. Lihat Semua Item")
        print("5. Keluar")
        
        choice = input("Pilihan Anda: ")

        if choice == "1":
            toko_manager.add_prototype()
        elif choice == "2":
            toko_manager.add_item_from_prototype()
        elif choice == "3":
            toko_manager.delete_item()
        elif choice == "4":
            toko_manager.display_all_items()
        elif choice == "5":
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
