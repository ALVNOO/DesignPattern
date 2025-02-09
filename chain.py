from datetime import datetime

# Abstract Handler
class Handler:
    def __init__(self, successor=None):
        self.successor = successor  # Handler berikutnya dalam chain
    
    def handle_request(self, item_type, *args):
        if self.successor:
            return self.successor.handle_request(item_type, *args)
        else:
            print("Jenis item tidak ditemukan!")
            return None

# Concrete Handlers
class BukuHandler(Handler):
    def handle_request(self, item_type, *args):
        if item_type == "Buku":
            return Buku(*args)
        else:
            return super().handle_request(item_type, *args)

class MajalahHandler(Handler):
    def handle_request(self, item_type, *args):
        if item_type == "Majalah":
            return Majalah(*args)
        else:
            return super().handle_request(item_type, *args)

class KoranHandler(Handler):
    def handle_request(self, item_type, *args):
        if item_type == "Koran":
            return Koran(*args)
        else:
            return super().handle_request(item_type, *args)

# Base Class
class Item:
    def __init__(self, title, publication_date, pages, rating, additional_info=None):
        self.title = title
        self.publication_date = datetime.strptime(publication_date, "%Y-%m-%d")
        self.pages = pages
        self.rating = rating
        self.additional_info = additional_info if additional_info else {}
    
    def display_info(self):
        print(f"\nJudul: {self.title}")
        print(f"Tanggal Terbit: {self.publication_date.strftime('%d-%m-%Y')}")
        print(f"Jumlah Halaman: {self.pages}")
        print(f"Rating: {self.rating}")
        print(f"Informasi Tambahan: {self.additional_info}")

# Concrete Classes
class Buku(Item):
    def __init__(self, title, publication_date, pages, rating, author):
        super().__init__(title, publication_date, pages, rating, {"Penulis": author})

class Majalah(Item):
    def __init__(self, title, publication_date, pages, rating, editionNumber):
        super().__init__(title, publication_date, pages, rating, {"Nomor Edisi": editionNumber})

class Koran(Item):
    def __init__(self, title, publication_date, pages, rating, publisher):
        super().__init__(title, publication_date, pages, rating, {"Penerbit": publisher})

# TokoManager (Client)
class TokoManager:
    def __init__(self):
        self.items = []
        
        # Membuat chain handler
        self.handler_chain = BukuHandler(MajalahHandler(KoranHandler()))
    
    def add_item(self):
        print("\nTambah Item:")
        title = input("Judul: ")
        publication_date = input("Tanggal Terbit (YYYY-MM-DD): ")
        pages = int(input("Jumlah Halaman: "))
        rating = float(input("Rating (1.0 - 5.0): "))
        
        print("Pilih Jenis Item: 1. Buku, 2. Majalah, 3. Koran")
        choice = input("Pilihan: ")
        
        if choice == "1":
            item_type = "Buku"
            author = input("Penulis: ")
            item = self.handler_chain.handle_request(item_type, title, publication_date, pages, rating, author)
        elif choice == "2":
            item_type = "Majalah"
            editionNumber = input("Nomor Edisi: ")
            item = self.handler_chain.handle_request(item_type, title, publication_date, pages, rating, editionNumber)
        elif choice == "3":
            item_type = "Koran"
            publisher = input("Penerbit: ")
            item = self.handler_chain.handle_request(item_type, title, publication_date, pages, rating, publisher)
        else:
            print("Pilihan tidak valid!")
            return
        
        if item:
            self.items.append(item)
            print("Item berhasil ditambahkan!")
    
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

# Main Function
def main():
    toko_manager = TokoManager()
    
    while True:
        print("\n=== Toko ===")
        print("1. Tambah Item")
        print("2. Hapus Item")
        print("3. Lihat Semua Item")
        print("4. Keluar")
        
        choice = input("Pilihan Anda: ")
        
        if choice == "1":
            toko_manager.add_item()
        elif choice == "2":
            toko_manager.delete_item()
        elif choice == "3":
            toko_manager.display_all_items()
        elif choice == "4":
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
