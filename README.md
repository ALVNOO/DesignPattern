# DesignPattern
---

## 📄 Laporan 
*Muhammad Alvino*

excalidraw : https://excalidraw.com/#json=w2dgND2NpXfsuCXcSDvvx,Fhg9vS5UayWRtYhJbVUEPQ

---

## Design Pattern Prototype
![prototype](https://github.com/user-attachments/assets/f4d56c3d-c613-4cab-a4f3-baca6de3cb2e)

Prototype Design Pattern yaitu pola desain yang digunakan untuk membuat objek baru dengan menyalin objek yang sudah ada (cloning), daripada membuatnya dari awal. 
Berikut adalah penjelasan setiap komponennya:

### Prototype (Interface/Abstract Class)
- Merupakan antarmuka atau kelas abstrak yang mendefinisikan metode Clone().
- Memastikan bahwa semua kelas turunan (konkrit) memiliki kemampuan untuk mengkloning dirinya sendiri.

### ConcretePrototype (Kelas Konkret yang Mengimplementasi Prototype)
- Menyimpan state (data yang akan disalin).
- Mengimplementasikan metode Clone(), yang berisi logika bagaimana objek akan diduplikasi.
- Metode Clone() akan mengembalikan salinan baru dari objek itu sendiri.


### Client (Pengguna)
- Memanggil metode Clone() untuk membuat objek baru berdasarkan objek yang sudah ada.
- Dengan cara ini, pengguna tidak perlu tahu bagaimana objek dibuat atau dari kelas konkret mana objek itu berasal.


## Class Diagram
![class prototype drawio (1)](https://github.com/user-attachments/assets/d71f8d72-542e-4acd-a064-4e310e77534d)

Etalase → Kelas yang berfungsi sebagai penyimpanan daftar publikasi (items). Juga memiliki registry (prototype_registry) untuk menyimpan prototipe publikasi yang dapat digunakan untuk cloning.
PublicationPrototype → Kelas abstrak yang mendefinisikan metode clone() untuk menduplikasi objek dan show_details() untuk menampilkan detail publikasi.
Buku, Majalah, Koran → Subclass dari PublicationPrototype dengan atribut khusus masing-masing:
  - Buku → Memiliki atribut title, author, dan price.
  - Majalah → Memiliki atribut title, edition, dan price.
  - Koran → Memiliki atribut title, publisher, dan price.


## Use Case Diagram
![usecase prototype](https://github.com/user-attachments/assets/eb1ca001-0177-45b3-86af-f701588586b8)

- Tambah Prototype : Admin dapat menambahkan prototype baru ke dalam sistem.
- Tambah Item dari Prototype : Admin dapat membuat item baru berdasarkan prototype yang sudah ada.
- Hapus Item : Admin dapat menghapus item tertentu dari sistem.
- Keluar Program : Admin dapat keluar dari sistem atau mengakhiri program.


## Sequence Diagram
![sequence prototype drawio (3)](https://github.com/user-attachments/assets/bb3be075-2066-4682-987a-89ac3f71cf59)


Tambah Prototype
- Admin memilih "Tambah Properti"
- TokoManager memanggil register_prototype() pada PrototypeRegistry
- PrototypeRegistry menyimpan prototype ke dalam dictionary untuk referensi di masa depan.

Tambah Item dari Prototype
- Admin memilih "Tambah Item dari Prototype"
- TokoManager memanggil clone_prototype() pada PrototypeRegistry
- PrototypeRegistry membuat salinan (clone) dari prototype yang tersimpan
- Sistem membuat instance baru dari hasil clone

Hapus Item 
- Admin memilih "Hapus Item"
- TokoManager memanggil delete_item()
- Item yang dipilih dihapus dari daftar

Lihat Semua Item
- Admin memilih "Lihat Semua Item"
- TokoManager memanggil display_all_items()
- Setiap item memanggil metode display_info()
- Informasi item ditampilkan ke pengguna

Keluar
- Admin memilih "Keluar"
- Sistem menutup program

## CLI
![Screenshot 2025-02-09 163122](https://github.com/user-attachments/assets/ed1af43b-a39c-4c4b-b3cf-49d4db090836)
![Screenshot 2025-02-09 163140](https://github.com/user-attachments/assets/38d73b4d-cb12-4c41-b85c-5a5da874c206)


---

## Design Pattern Composite
![composite](https://github.com/user-attachments/assets/c131dcd0-d669-4f33-abda-db3a88842135)

Composite Design Pattern, yaitu pola desain yang digunakan untuk merepresentasikan struktur hierarki (seperti pohon) dengan objek individual (Leaf) dan objek yang dapat memiliki anak (Composite).

### Component (Antarmuka/Kelas Abstrak)
- Menyediakan antarmuka umum untuk semua objek dalam struktur hierarki.
- Digunakan baik oleh objek Leaf maupun Composite, sehingga keduanya bisa diperlakukan dengan cara yang sama oleh Client.

### Leaf (Objek Tunggal)
- Implementasi metode operation() yang bersifat spesifik.
- Biasanya merupakan unit terkecil dalam hierarki.

### Composite (Objek yang Dapat Memiliki Child)
- Menyimpan daftar objek anak dalam children: List<Component>.
- Menyediakan metode add(Component) untuk menambahkan objek anak.
- Menyediakan metode remove(Component) untuk menghapus objek anak.
- Mengimplementasikan operation(), yang akan menjalankan operation() pada semua child-nya secara rekursif.

### Client
- Memanggil operation() tanpa harus tahu apakah objek yang digunakan adalah Leaf atau Composite.
- Memperlakukan struktur hierarki dengan cara yang sama, baik untuk elemen tunggal maupun grup.


## Class Diagram
![class composite drawio](https://github.com/user-attachments/assets/b808ab04-3a09-4354-8e6d-290c8d383b1e)

Composite Design Pattern, yang digunakan untuk menangani struktur hierarki dengan komponen yang dapat berupa individu (leaf) atau kumpulan objek (composite).

dengan menggunakan design pattern Composite
- Memanfaatkan Composite Design Pattern dengan baik untuk menangani struktur hierarki.
- Memudahkan manipulasi item secara seragam dengan menggunakan interface Item.
- Fleksibel dan dapat diperluas, cukup dengan menambahkan subclass baru yang mengimplementasikan Item.


## Use Case Diagram
![usecase compo dan chain](https://github.com/user-attachments/assets/2f9fe8c2-1d8d-4168-a3ea-b9bdcb7ec04a)

Use case diagram di atas menggambarkan interaksi antara aktor Admin dengan sistem yang memiliki empat fungsi utama, yaitu:

Tambah Item : Admin dapat menambahkan item baru ke dalam sistem.
Delete Item : Admin memiliki akses untuk menghapus item yang sudah ada dalam sistem.
Display Item : Admin dapat menampilkan daftar item yang tersedia di dalam sistem.
Keluar Program : Admin memiliki opsi untuk keluar dari sistem atau menutup aplikasi.


## Sequence Diagram
![sequence composite drawio (1)](https://github.com/user-attachments/assets/2cac363e-fc6f-4039-b270-330b0b38603a)

Menambahkan Properti (Item) ke dalam Toko
- Admin memilih "Tambah Properti"
- Toko memanggil add_item(), yang menambahkan item baru ke dalam daftar.
- Instance baru dari Buku/Majalah/Koran dibuat dan disimpan.

Menampilkan Semua Item
- Admin memilih "Lihat Semua Item"
- Toko memanggil display_info() pada setiap item dalam daftar
- Setiap item menjalankan display_info() untuk menampilkan informasi

Menghapus Item
- Admin memilih "Hapus Item"
- Toko memanggil remove_item(), yang menghapus item dari koleksi.

Keluar dari Program
- Admin memilih "Keluar"
- Sistem menutup program


## CLI
![ss compo](https://github.com/user-attachments/assets/3f55b11e-25f6-4387-b91a-e70d75e132d0)
![ss compo 2](https://github.com/user-attachments/assets/a76cce70-c368-40e4-8b2d-38f0daf02290)
![ss compo 3](https://github.com/user-attachments/assets/c072f5bd-a9c8-4c6e-884e-1ff89599c259)


---

## Design Pattern Chain of Responsibility
![Chain](https://github.com/user-attachments/assets/0f79717b-f32c-4e00-bdeb-1a649c0af203)

Chain of Responsibility Design Pattern, yaitu pola desain yang memungkinkan serangkaian objek (handlers) untuk menangani permintaan secara berantai sampai salah satu objek menangani permintaan tersebut.

### Handler (Interface/Kelas Abstrak)
- Menyediakan metode setNext() untuk mengatur handler berikutnya dalam rantai.
- Menyediakan metode handleRequest(), yang akan menangani permintaan atau meneruskannya ke handler berikutnya.
- Menyimpan referensi ke handler berikutnya dalam variabel next.

### ConcreteHandlerA, ConcreteHandlerB, ConcreteHandlerC (Handler Konkret)
- Setiap ConcreteHandler memiliki implementasi spesifik dari handleRequest().
- Jika handler saat ini dapat menangani permintaan, maka akan diproses.
- Jika tidak, permintaan akan diteruskan ke handler berikutnya dalam rantai.
- ConcreteHandlerA → Handler pertama dalam rantai.
- ConcreteHandlerB → Handler kedua dalam rantai.
- ConcreteHandlerC → Handler ketiga dalam rantai.

### Client
- Membuat objek ConcreteHandler dan menyusun urutan rantai dengan setNext().
- Memanggil handleRequest() pada handler pertama, yang kemudian akan diproses atau diteruskan ke handler berikutnya.


## Class Diagram
![class chain drawio](https://github.com/user-attachments/assets/fbb74316-6cfa-4d21-9097-a6cea192a1fd)

implementasi Chain of Responsibility Design Pattern, yang digunakan untuk menangani permintaan secara berantai sampai salah satu handler menanganinya.


dengan menggunakan design pattern Chain of Responsibility
- Menangani permintaan secara fleksibel.
- Memisahkan logika penanganan item dari TokoManager, sehingga mudah diperluas.
- Fleksibel—bisa menambah handler baru tanpa mengubah kode yang sudah ada.


## Use Case Diagram
![usecase compo dan chain](https://github.com/user-attachments/assets/e0b6f62a-889e-488e-975d-6bbc416d6efb)


Use case diagram di atas menggambarkan interaksi antara aktor Admin dengan sistem yang memiliki empat fungsi utama, yaitu:

Tambah Item : Admin dapat menambahkan item baru ke dalam sistem.
Delete Item : Admin memiliki akses untuk menghapus item yang sudah ada dalam sistem.
Display Item : Admin dapat menampilkan daftar item yang tersedia di dalam sistem.
Keluar Program : Admin memiliki opsi untuk keluar dari sistem atau menutup aplikasi.


## Sequence Diagram
![sequence chain drawio](https://github.com/user-attachments/assets/0a1d703e-2c9a-4348-9f5b-e856834f5310)

Menambahkan Properti (Item) ke dalam Toko
- Admin memilih "Tambah Properti"
- TokoManager memanggil handle_request() pada Handler Chain
- Handler Chain mengecek urutan handler:
   - Cek handler Buku
   - Cek handler Majalah
   - Cek handler Koran
Jika ditemukan handler yang sesuai, instance item dibuat

Menampilkan Semua Item
- Admin memilih "Lihat Semua Item"
- TokoManager memanggil display_all_items()
- Setiap item dalam daftar menjalankan display_info()
- Informasi item ditampilkan ke Admin

Menghapus Item
- Admin memilih "Hapus Item"
- TokoManager memanggil delete_item()
- Item yang sesuai dihapus dari daftar toko

Keluar dari Program
- Admin memilih "Keluar"
- Sistem menutup program

## CLI
![ss chain](https://github.com/user-attachments/assets/37b92b31-f76f-4b94-9047-f0dcfb8b380a)
