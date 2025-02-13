from abc import ABC, abstractmethod

# Komponen Abstrak
class Item(ABC):
    @abstractmethod
    def show_details(self, indent=0):
        pass

# Leaf: Representasi Produk
class Product(Item):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_details(self, indent=0):
        print(" " * indent + f"- {self.name} (Rp{self.price})")

# Leaf: Buku
class Buku(Product):
    def __init__(self, title, author, price):
        super().__init__(title, price)
        self.author = author

    def show_details(self, indent=0):
        print(" " * indent + f"- {self.name} oleh {self.author} (Rp{self.price})")

# Leaf: Majalah
class Majalah(Product):
    def __init__(self, name, edition, price):
        super().__init__(name, price)
        self.edition = edition

    def show_details(self, indent=0):
        print(" " * indent + f"- {self.name} Edisi {self.edition} (Rp{self.price})")

# Leaf: Koran
class Koran(Product):
    def __init__(self, title, publisher, price):
        super().__init__(title, price)
        self.publisher = publisher

    def show_details(self, indent=0):
        print(" " * indent + f"- {self.name} oleh {self.publisher} (Rp{self.price})")

# Composite: Kategori yang Bisa Memuat Produk atau Subkategori
class Category(Item):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, name):
        self.items = [item for item in self.items if not (isinstance(item, Product) and item.name == name)]

    def show_details(self, indent=0):
        print(" " * indent + f"[{self.name}]")
        for item in self.items:
            item.show_details(indent + 2)

# CLI Etalase Karya Tulis
class Etalase:
    def __init__(self):
        self.store = Category("Etalase Karya Tulis")

    def add_product(self):
        category_name = input("Masukkan kategori (Buku/Majalah/Koran): ")
        if category_name.lower() == "buku":
            title = input("Masukkan judul buku: ")
            author = input("Masukkan penulis buku: ")
            price = int(input("Masukkan harga buku: "))
            product = Buku(title, author, price)
        elif category_name.lower() == "majalah":
            name = input("Masukkan nama majalah: ")
            edition = input("Masukkan nomor edisi: ")
            price = int(input("Masukkan harga majalah: "))
            product = Majalah(name, edition, price)
        elif category_name.lower() == "koran":
            title = input("Masukkan judul koran: ")
            publisher = input("Masukkan nama publisher: ")
            price = int(input("Masukkan harga koran: "))
            product = Koran(title, publisher, price)
        else:
            print("Kategori tidak ditemukan!")
            return
        
        for category in self.store.items:
            if category.name.lower() == category_name.lower():
                category.add_item(product)
                print("Produk berhasil ditambahkan!")
                return
        
        new_category = Category(category_name)
        new_category.add_item(product)
        self.store.add_item(new_category)
        print("Produk berhasil ditambahkan!")

    def remove_product(self):
        product_name = input("Masukkan nama produk yang ingin dihapus: ")
        for category in self.store.items:
            category.remove_item(product_name)
        print("Produk berhasil!")

    def run(self):
        while True:
            print("\n===== Etalase Karya Tulis =====")
            print("\n1. Tambah Produk")
            print("2. Hapus Produk")
            print("3. Lihat Semua Produk")
            print("4. Keluar")
            choice = input("Pilih opsi: ")
            if choice == "1":
                self.add_product()
            elif choice == "2":
                self.remove_product()
            elif choice == "3":
                self.store.show_details()
            elif choice == "4":
                print("Terima kasih!")
                break

if __name__ == "__main__":
    cli = Etalase()
    cli.run()
