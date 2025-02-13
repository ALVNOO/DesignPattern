import copy

class PublicationPrototype:
    def clone(self):
        return copy.deepcopy(self)

    def show_details(self):
        raise NotImplementedError("Subclasses must implement show_details method")

class Buku(PublicationPrototype):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show_details(self):
        return f"Buku: {self.title} | Penulis: {self.author} | Harga: Rp{self.price}"

class Majalah(PublicationPrototype):
    def __init__(self, title, edition, price):
        self.title = title
        self.edition = edition
        self.price = price

    def show_details(self):
        return f"Majalah: {self.title} | Edisi: {self.edition} | Harga: Rp{self.price}"

class Koran(PublicationPrototype):
    def __init__(self, title, publisher, price):
        self.title = title
        self.publisher = publisher
        self.price = price

    def show_details(self):
        return f"Koran: {self.name} | Penerbit: {self.publisher} | Harga: Rp{self.price}"

class Etalase:
    def __init__(self):
        self.items = {"book": [], "magazine": [], "newspaper": []}
        self.prototype_registry = {
            "book": Buku("", "John Doe", 0),
            "magazine": Majalah("Tech Monthly", "", 0),
            "newspaper": Koran("", "Daily News Publisher", 0)
        }

    def add_item(self, category, item):
        if category in self.items:
            self.items[category].append(item)

    def remove_item(self, category, index):
        if category in self.items and 0 <= index < len(self.items[category]):
            removed_item = self.items[category].pop(index)
            print(f"Item '{removed_item.title if hasattr(removed_item, 'title') else removed_item.name}' berhasil dihapus.")
        else:
            print("Indeks tidak valid.")

    def show_catalog(self):
        for category, items in self.items.items():
            if items:
                print(f"\nKategori: {category.capitalize()}")
                for idx, item in enumerate(items):
                    print(f"{idx}. {item.show_details()}")

    def get_prototype(self, category):
        return self.prototype_registry.get(category).clone() if category in self.prototype_registry else None

# Membuat etalase
etalase = Etalase()

# CLI Menu
def main():
    while True:
        print("\nMenu:")
        print("1. Tambah produk")
        print("2. Hapus produk")
        print("3. Lihat semua produk")
        print("4. Keluar")
        choice = input("Masukkan pilihan: ")

        if choice == "1":
            print("\nPilih jenis produk yang ingin ditambahkan:")
            print("1. Buku")
            print("2. Majalah")
            print("3. Koran")
            item_choice = input("Masukkan pilihan: ")
            category_map = {"1": "book", "2": "magazine", "3": "newspaper"}

            prototype = etalase.get_prototype(category_map.get(item_choice))
            if prototype:
                if item_choice == "1":
                    prototype.title = input("Masukkan judul buku: ")
                    print(f"Penulis: {prototype.author} (tetap)")
                elif item_choice == "2":
                    print(f"Nama Majalah: {prototype.title} (tetap)")
                    prototype.edition = input("Masukkan edisi: ")
                elif item_choice == "3":
                    prototype.name = input("Masukkan nama koran: ")
                    print(f"Penerbit: {prototype.publisher} (tetap)")
                prototype.price = int(input("Masukkan harga: "))  
                etalase.add_item(category_map.get(item_choice), prototype)
            else:
                print("Pilihan tidak valid.")

        elif choice == "2":
            etalase.show_catalog()
            category = input("Masukkan kategori produk (book/magazine/newspaper): ")
            index = int(input("Masukkan indeks produk yang ingin dihapus: "))
            etalase.remove_item(category, index)
        
        elif choice == "3":
            etalase.show_catalog()

        elif choice == "4":
            print("Terima kasih!")
            break

        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()