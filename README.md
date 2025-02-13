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
Prototype (Abstract Class)
- Ini adalah kelas abstrak yang mendefinisikan metode Clone().
- Metode Clone() berfungsi untuk menyalin objek tanpa bergantung pada kelas konkret.

### ConcretePrototype (Kelas Konkret yang Mengimplementasi Prototype)
- Implementasi dari kelas Prototype.
- Menyimpan state atau data yang akan disalin saat objek diduplikasi.
- Mengimplementasikan metode Clone() yang benar-benar menyalin objek.


### PrototypeRegistry
- Merupakan registry (daftar) yang menyimpan berbagai prototipe dalam sebuah map (key-value pair).
- Memungkinkan pengambilan objek prototipe berdasarkan kunci (key) dengan metode getPrototype(key: String).
- Tujuannya adalah mempermudah akses ke prototipe yang telah dibuat sebelumnya tanpa perlu menginstansiasi ulang.


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
- Menjadi dasar bagi semua elemen dalam hierarki.
- Memiliki metode abstrak doThis(), yang harus diimplementasikan oleh semua subclass.
- Memungkinkan penggunaan polimorfisme untuk menangani Leaf dan Composite secara seragam.

### Leaf (Objek Tunggal)
- Objek konkret yang tidak memiliki child.
- Mengimplementasikan metode doThis() secara spesifik.

### Composite (Objek yang Dapat Memiliki Child)
- Dapat menyimpan beberapa Component (baik Leaf maupun Composite lainnya).
- Memiliki daftar elemen (elements: List<Component>), yang dapat berupa Leaf atau Composite lainnya.
- Memungkinkan penambahan elemen dengan addElement(Component).
- Mengimplementasikan doThis() dengan cara yang dapat mempengaruhi semua elemen yang dikandungnya.


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
![SS COMPOSITE 1](https://github.com/user-attachments/assets/d45042fa-393a-4bfb-b31e-8661df703d5b)
![SS COMPOSITE 2](https://github.com/user-attachments/assets/c9bb95cd-2c24-4753-98ed-51d182b9f543)
![SS COMPOSITE 3](https://github.com/user-attachments/assets/d5592a81-c1ac-44f8-9caa-d4800f27e9f5)
![SS COMPOSITE 4](https://github.com/user-attachments/assets/7cef0f3f-c96c-402d-b7a9-5172b24fe1ed)


---

## Design Pattern Chain of Responsibility
![Chain](https://github.com/user-attachments/assets/0f79717b-f32c-4e00-bdeb-1a649c0af203)

Chain of Responsibility Design Pattern, yaitu pola desain yang memungkinkan serangkaian objek (handlers) untuk menangani permintaan secara berantai sampai salah satu objek menangani permintaan tersebut.

### Handler (Interface/Kelas Abstrak)
- Merupakan kelas antarmuka yang mendefinisikan struktur dasar handler dalam rantai.
- Memiliki atribut next: Handler, yang merupakan referensi ke handler berikutnya dalam rantai.
- Memiliki metode setNext() untuk mengatur handler berikutnya.
- Memiliki metode handleRequest(), yang akan diimplementasikan oleh subclass.

### ConcreteHandlerA, ConcreteHandlerB, ConcreteHandlerC (Handler Konkret)
- ConcreteHandlerA dan ConcreteHandlerB adalah implementasi spesifik dari Handler.
- Masing-masing memiliki metode handleRequest(), yang dapat menangani permintaan atau meneruskan ke handler berikutnya dalam rantai.
- Jika HandlerA tidak menangani permintaan, maka akan diteruskan ke HandlerB, dan seterusnya hingga permintaan diproses atau tidak ada lagi handler yang dapat menangani.


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
![SS CHAIN 1](https://github.com/user-attachments/assets/18947b81-0411-4e58-bfe8-3ce9eb09317f)
![SS CHAIN 2](https://github.com/user-attachments/assets/713fd6cf-af70-427f-8814-8a09a98e9fc8)
![SS CHAIN 3](https://github.com/user-attachments/assets/0cadae77-958a-44a7-afbf-f87414b7110f)
![SS CHAIN 4](https://github.com/user-attachments/assets/d985b6db-3831-4c6d-9b16-c88bec66a972)

