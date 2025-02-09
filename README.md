# DesignPattern
---

## 📄 Laporan 
*Muhammad Alvino*

https://excalidraw.com/#json=w2dgND2NpXfsuCXcSDvvx,Fhg9vS5UayWRtYhJbVUEPQ

---

## Design Pattern Prototype
![prototype](https://github.com/user-attachments/assets/393578d6-e2c9-4ea9-8b04-576b0c36dfef)

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
![class prototype](https://github.com/user-attachments/assets/0cbee59b-3e88-4840-824d-612b17f67e8a)
Class diagram ini menggambarkan implementasi Prototype Design Pattern yang digunakan untuk mengelola berbagai jenis publikasi seperti Buku, Majalah, dan Koran.


## Use Case Diagram
![usecase prototype](https://github.com/user-attachments/assets/2faf80fa-a569-49a0-88b6-5cbb88143b01)
- Tambah Prototype : Admin dapat menambahkan prototype baru ke dalam sistem.
- Tambah Item dari Prototype : Admin dapat membuat item baru berdasarkan prototype yang sudah ada.
- Hapus Item : Admin dapat menghapus item tertentu dari sistem.
- Keluar Program : Admin dapat keluar dari sistem atau mengakhiri program.



---

## Design Pattern Composite
![composite](https://github.com/user-attachments/assets/3c51beac-adce-4cbd-983a-0e3fd227ea78)
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
![class composite](https://github.com/user-attachments/assets/45de93d4-e807-4a77-8897-b6130f00e505)
Composite Design Pattern, yang digunakan untuk menangani struktur hierarki dengan komponen yang dapat berupa individu (leaf) atau kumpulan objek (composite).

dengan menggunakan design pattern Composite
- Memanfaatkan Composite Design Pattern dengan baik untuk menangani struktur hierarki.
- Memudahkan manipulasi item secara seragam dengan menggunakan interface Item.
- Fleksibel dan dapat diperluas, cukup dengan menambahkan subclass baru yang mengimplementasikan Item.


## Use Case Diagram
![usecase compo dan chain](https://github.com/user-attachments/assets/45d7c7c6-1250-4dd0-b27f-ee26d6d13cd1)



---

## Design Pattern Chain of Responsibility
![Chain](https://github.com/user-attachments/assets/586f93fe-8b57-418e-be37-18db684f5e87)
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
![class chain](https://github.com/user-attachments/assets/0732db54-3eba-4e6b-a826-a1c8f97674e2)
implementasi Chain of Responsibility Design Pattern, yang digunakan untuk menangani permintaan secara berantai sampai salah satu handler menanganinya.


dengan menggunakan design pattern Chain of Responsibility
- Menangani permintaan secara fleksibel.
- Memisahkan logika penanganan item dari TokoManager, sehingga mudah diperluas.
- Fleksibel—bisa menambah handler baru tanpa mengubah kode yang sudah ada.


## Use Case Diagram
![usecase compo dan chain](https://github.com/user-attachments/assets/bb530b11-dcb7-45e2-bdcc-6dfea4011024)

