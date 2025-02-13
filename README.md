![class diagram chain drawio](https://github.com/user-attachments/assets/27a30d51-6e78-4179-9a52-40859ae35fae)# DesignPattern
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

- Tambah Produk : Admin dapat menambahkan prototype baru ke dalam sistem.
- Hapus Produk : Admin dapat membuat item baru berdasarkan prototype yang sudah ada.
- Lihat semua produk : Admin dapat menghapus item tertentu dari sistem.


## Sequence Diagram
![sequence prototype drawio (3)](https://github.com/user-attachments/assets/bb3be075-2066-4682-987a-89ac3f71cf59)


Menambahkan Produk
Alur:

- User memilih tambah produk → Pengguna memulai proses untuk menambahkan produk baru.
- Pilih jenis produk (Buku/Majalah/Koran) → Pengguna memilih jenis produk yang ingin ditambahkan.
- User memilih kategori produk → Pengguna memilih kategori tempat produk akan disimpan.
- Meminta prototype dari registry → Sistem meminta prototipe produk dari Prototype Registry.
- Clone objek → PublicationPrototype membuat salinan (cloning) objek berdasarkan prototipe.
- Mengembalikan hasil cloning → Hasil cloning dikembalikan ke Prototype Registry.
- Mengembalikan objek hasil cloning → Prototype Registry mengembalikan objek hasil cloning ke Etalase.
- Menambahkan objek ke daftar produk → Objek hasil cloning ditambahkan ke daftar produk dalam etalase.
- Menampilkan pesan berhasil ditambahkan → Sistem mengonfirmasi bahwa produk telah berhasil ditambahkan.

Menghapus Produk
Alur:

- User memilih hapus produk → Pengguna memulai proses penghapusan produk.
- Meminta kategori dan indeks produk → Sistem meminta pengguna untuk memasukkan kategori dan indeks produk yang ingin dihapus.
- Masukkan kategori dan indeks produk → Pengguna menginput kategori dan indeks produk.
- Cek apakah indeks dan kategori valid → Sistem memeriksa apakah data yang dimasukkan benar dan produk tersedia.
- Hapus produk → Jika valid, produk dihapus dari daftar etalase.
- Konfirmasi produk berhasil dihapus → Sistem memberikan notifikasi bahwa produk telah berhasil dihapus.

Menampilkan Semua Produk
Alur:

- User memilih lihat semua produk → Pengguna meminta daftar produk yang tersedia.
- Ambil daftar produk berdasarkan kategori → Sistem mengambil daftar produk berdasarkan kategori yang tersedia.
- Meminta menampilkan detailnya → Sistem meminta detail produk untuk ditampilkan.
- Mengembalikan detail → Sistem mengembalikan informasi detail dari produk.
- Menampilkan daftar produk ke User → Produk yang tersedia ditampilkan kepada pengguna.

## CLI
![SS PROTOTYPE 1](https://github.com/user-attachments/assets/f07632c3-b641-4319-a10b-66e7045aab1a)
![SS PROTOTYPE 2](https://github.com/user-attachments/assets/b0e23172-afd3-4281-aec6-dd3ce1d941ba)
![SS PROTOTYPE 3](https://github.com/user-attachments/assets/38c5f32b-362a-4634-a626-ecf396a80791)
![SS PROTOTYPE 4](https://github.com/user-attachments/assets/42252708-15db-464f-a06f-96bd6134033c)


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
![class diagram composite drawio](https://github.com/user-attachments/assets/ca815b72-651b-4bea-8b51-1e7d0d575fb8)

Composite Design Pattern, yang digunakan untuk menangani struktur hierarki dengan komponen yang dapat berupa individu (leaf) atau kumpulan objek (composite).

- Etalase → Kelas utama yang merepresentasikan etalase toko yang berisi kategori produk 
- Category = Composite → Kelas yang merepresentasikan kategori dalam etalase dan dapat menyimpan daftar item
- Item = Component → Interface yang mendefinisikan metode show_details() untuk menampilkan detail produk atau kategori
- Product = Leaf → Kelas dasar untuk produk yang mengimplementasikan Item
- Buku, Majalah, Koran → Subclass dari Product dengan atribut spesifik masing-masing


## Use Case Diagram
![usecase compo dan chain](https://github.com/user-attachments/assets/2f9fe8c2-1d8d-4168-a3ea-b9bdcb7ec04a)

Use case diagram di atas menggambarkan interaksi antara aktor Admin dengan sistem yang memiliki empat fungsi utama, yaitu:

Tambah Item : Admin dapat menambahkan item baru ke dalam sistem
Hapus Item : Admin memiliki akses untuk menghapus item yang sudah ada dalam sistem
Lihat semua Item : Admin dapat menampilkan daftar item yang tersedia di dalam sistem


## Sequence Diagram
![sequence composite drawio (1)](https://github.com/user-attachments/assets/2cac363e-fc6f-4039-b270-330b0b38603a)

Tambah Item
- User memilih opsi "Tambah Produk"
- Sistem meminta input kategori, nama, penulis/penerbit, dan harga produk
- User memasukkan data yang diminta
- Etalase memeriksa apakah kategori sudah ada
- Jika kategori belum ada, maka sistem membuat kategori baru
- Produk ditambahkan ke dalam kategori yang sesuai
- Sistem menampilkan detail produk yang baru ditambahkan
- Sistem mengembalikan detail produk ke Etalase
- Sistem mengembalikan status sukses
- Sistem menampilkan konfirmasi bahwa produk berhasil ditambahkan kepada User

Lihat Semua Produk
- User memilih opsi "Lihat Semua Produk"
- Etalase meminta daftar produk berdasarkan kategori
- Etalase meminta detail dari setiap produk
- Produk mengembalikan detailnya ke Category
- Category mengembalikan daftar produk ke Etalase
- Sistem menampilkan daftar produk kepada User

Hapus Produk
- User memilih opsi "Hapus Produk"
- Sistem meminta User memasukkan nama produk yang ingin dihapus
- User menginput nama produk yang akan dihapus
- Etalase meminta Category untuk menghapus produk
- Category memeriksa apakah produk ada
- Jika produk ada, produk dihapus dari kategori
- Sistem mengembalikan status penghapusan
- Sistem menampilkan konfirmasi bahwa produk telah berhasil dihapus


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
![class diagram chain drawio](https://github.com/user-attachments/assets/4acedd97-710b-4d90-bfff-17bdbbeb7915)


implementasi Chain of Responsibility Design Pattern, yang digunakan untuk menangani permintaan secara berantai sampai salah satu handler menanganinya.

- Handler → Interface yang menjadi dasar bagi semua handler dalam rantai
- BukuHandler = ConcreteHandler → Handler yang menangani permintaan terkait buku
- MajalahHandler = ConcreteHandler → Handler yang menangani permintaan terkait majalah
- KoranHandler = ConcreteHandler → Handler yang menangani permintaan terkait koran
- Etalase → Kelas utama yang menyimpan daftar karya tulis dan menangani permintaan
- KaryaTulis → Kelas yang merepresentasikan objek karya tulis



## Use Case Diagram
![usecase compo dan chain](https://github.com/user-attachments/assets/e0b6f62a-889e-488e-975d-6bbc416d6efb)


Use case diagram di atas menggambarkan interaksi antara aktor Admin dengan sistem yang memiliki empat fungsi utama, yaitu:

Tambah Item : Admin dapat menambahkan item baru ke dalam sistem.
Hapus Item : Admin memiliki akses untuk menghapus item yang sudah ada dalam sistem.
Lihat semua Item : Admin dapat menampilkan daftar item yang tersedia di dalam sistem.


## Sequence Diagram
![sequence chain drawio](https://github.com/user-attachments/assets/0a1d703e-2c9a-4348-9f5b-e856834f5310)

Tambah Produk
- User memilih opsi "Tambah Produk"
- Etalase meminta User untuk menginput atribut produk
- User memasukkan atribut produk (misalnya, nama, kategori, harga, dll.)
- Etalase meneruskan request ke Handler
- Handler membuat objek item berdasarkan input yang diterima
- Handler mengembalikan objek item yang telah dibuat ke Etalase
- Etalase memberikan konfirmasi bahwa item berhasil ditambahkan

Hapus Item
- User memilih opsi "Hapus Item"
- Etalase meminta input judul item yang ingin dihapus
- User memasukkan judul item
- Etalase meminta Handler untuk mencari item berdasarkan judul
- Handler mencari item yang sesuai dan menghapusnya
- Handler mengembalikan hasil pencarian ke Etalase
- Item dihapus dari daftar
- Etalase memberikan konfirmasi bahwa item berhasil dihapus

Lihat Semua Item
- User memilih opsi "Lihat Semua Item"
- Etalase mengambil semua item dalam daftar
- Etalase meminta informasi dari Handler untuk setiap item
- Handler mengembalikan informasi item yang diminta
- Etalase menampilkan daftar semua item kepada User

## CLI
![ss chain](https://github.com/user-attachments/assets/37b92b31-f76f-4b94-9047-f0dcfb8b380a)
