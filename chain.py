from datetime import datetime

# ==========================
# Abstract Handler (Chain of Responsibility)
# ==========================
class Handler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler  # Menunjuk ke handler berikutnya dalam rantai

    def handle_request(self, item_type, *args):
        if self.next_handler:
            return self.next_handler.handle_request(item_type, *args)
        else:
            print("Jenis item tidak valid!")
            return None

    def delete_request(self, items, title):
        if self.next_handler:
            return self.next_handler.delete_request(items, title)
        else:
            return False  # Tidak ditemukan

# ==========================
# Class Parent (Superclass)
# ==========================
class KaryaTulis:
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

# ==========================
# Class Child (Concrete Components)
# ==========================
class Buku(KaryaTulis):
    def __init__(self, title, publication_date, pages, rating, author):
        additional_info = {"Penulis": author}  
        super().__init__(title, publication_date, pages, rating, additional_info)

class Majalah(KaryaTulis):
    def __init__(self, title, publication_date, pages, rating, editionNumber):
        additional_info = {"Nomor Edisi": editionNumber}  
        super().__init__(title, publication_date, pages, rating, additional_info)

class Koran(KaryaTulis):
    def __init__(self, title, publication_date, pages, rating, publisher):
        additional_info = {"Penerbit": publisher}  
        super().__init__(title, publication_date, pages, rating, additional_info)

# ==========================
# Concrete Handlers (Handlers untuk Chain of Responsibility)
# ==========================
class BukuHandler(Handler):
    def handle_request(self, item_type, *args):
        if item_type == "1":
            return Buku(*args)  # Membuat objek Buku
        else:
            return super().handle_request(item_type, *args)

    def delete_request(self, items, title):
        for i, item in enumerate(items):
            if isinstance(item, Buku) and item.title == title:
                del items[i]
                print("Buku berhasil dihapus!")
                return True
        return super().delete_request(items, title)

class MajalahHandler(Handler):
    def handle_request(self, item_type, *args):
        if item_type == "2":
            return Majalah(*args)  # Membuat objek Majalah
        else:
            return super().handle_request(item_type, *args)

    def delete_request(self, items, title):
        for i, item in enumerate(items):
            if isinstance(item, Majalah) and item.title == title:
                del items[i]
                print("Majalah berhasil dihapus!")
                return True
        return super().delete_request(items, title)

class KoranHandler(Handler):
    def handle_request(self, item_type, *args):
        if item_type == "3":
            return Koran(*args)  # Membuat objek Koran
        else:
            return super().handle_request(item_type, *args)

    def delete_request(self, items, title):
        for i, item in enumerate(items):
            if isinstance(item, Koran) and item.title == title:
                del items[i]
                print("Koran berhasil dihapus!")
                return True
        return super().delete_request(items, title)

# ==========================
# Etalase (Mengelola Buku, Majalah, dan Koran)
# ==========================
class Etalase:
    def __init__(self):
        self.items = []  # Menyimpan daftar item
        
        # Membentuk rantai handler
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
            extra_info = input("Penulis: ")
        elif choice == "2":
            extra_info = input("Nomor Edisi: ")
        elif choice == "3":
            extra_info = input("Penerbit: ")
        else:
            print("Pilihan tidak valid!")
            return
        
        # Memproses dengan Chain of Responsibility
        item = self.handler_chain.handle_request(choice, title, publication_date, pages, rating, extra_info)

        if item:
            self.items.append(item)
            print("Item berhasil ditambahkan!")

    def delete_item(self):
        title = input("\nMasukkan judul item yang ingin dihapus: ")
        if not self.handler_chain.delete_request(self.items, title):
            print("Item tidak ditemukan!")

    def display_all_items(self):
        print("\n=== DAFTAR SEMUA ITEM ===")
        for item in self.items:
            item.display_info()

# ==========================
# Main Program
# ==========================
def main():
    etalase = Etalase()

    while True:
        print("\n=== Toko ===")
        print("1. Tambah Item")
        print("2. Hapus Item")
        print("3. Lihat Semua Item")
        print("4. Keluar")
        
        choice = input("Pilihan Anda: ")

        if choice == "1":
            etalase.add_item()
        elif choice == "2":
            etalase.delete_item()
        elif choice == "3":
            etalase.display_all_items()
        elif choice == "4":
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()