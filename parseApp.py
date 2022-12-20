from PyQt6.QtWidgets import (
    QApplication, QVBoxLayout, QWidget, QLabel, QPushButton, QLineEdit, QTextEdit, QGridLayout, QScrollArea, QGroupBox
)
from PyQt6.QtCore import Qt

import sys
import fungsiCFG as cfg

# set of rules Bahasa Indonesia yang sudah dalam bentuk Chomsky Normal Form
rules = {
    "K": ["K2 K3", "K2 Pel" "K2 K4", "K2 K5", "K2 K6", "K2 O", "K2 Ket", "K SP"],
    "K2":["S P"],
    "K3":["Pel O"],
    "K4":["Pel Ket"],
    "K5":["O Ket"],
    "K6":["O Pel"],
    "S": ['ibunya', 'adik', 'nasi', 'dapur', 'tugas', 'perempuan', 'taman', 'kota', 'pesan', 'siswa', 'kini', 'tadi', 'akhir', 'semester', 'paman', 'sepeda', 'motornya', 'anak', 'pemograman', 'komputer', 'orang', 'pasangan', 'tangan', 'gelas', 'mobil', 'peluru', 'gubernur', 'surat', 'tamu', 'materi', 'perkuliahan', 'seni', 'kakak', 'kandung', 'kelas', 'polisi', 'daerah', 'kado', 'sebentar', 'acara', 'sela', 'mantannya', 'masalah', 'dewa', 'laki', 'bapak', 'penipuan', 'balet', 'pengajaran', 'pemerintah', 'rakyat', 'bola', 'rombongan', 'haji', 'tubuhnya', 'ayah', 'kemarin', 'pagi', 'sekolah', 'kakek', 'rumah', 'pasar', 'pengikat', 'kakinya', 'pisau', 'isu', 'makar', 'rekreasi', 'susu', 'milik', 'gitar', 'kangkung', 'tumis', 'besok', 'pak', 'lurah', 'ikan', 'rambut', 'ujian', 'edaran', 'oleh-oleh', 'adikku', 'anaknya', 'ibu', 'Lukman', 'dodit', 'oki', 'johan', 'cianjir', 'yusuf', 'daffa', 'anwar', 'nadya', 'rahmi', 'tina', 'Joko', 'Theo', 'sintia', 'Nina', 'andi', 'reno', 'ratna ', 'dodi', 'zulkifli', 'rudi', 'kami', 'itu', 'aku ', 'dia', 'ia', 'mereka', 'nya', 'NP Noun', 'NP PropNoun', 'NP Pronoun', 'NP Verb', 'Adv NP', 'Prep NP', 'Prep Verb', 'Prep Adj', 'Adj NP', 'NP Adj'],
    "P": ['memasak', 'mengerjakan', 'bertemu', 'mengirim', 'melaksanakan', 'memperbaiki', 'bermain', 'main', 'belajar', 'berkebun', 'bergandengan', 'pecah', 'tahan', 'mengeluarkan', 'bersalaman', 'mempresentasikan', 'mempelajari', 'menunjuk', 'melakukan', 'penangkapan', 'membawa', 'mengobrol', 'goreng', 'lukis', 'tersebut', 'berhenti', 'menangisi', 'merasa', 'berbicara', 'memperjelas', 'mengajar', 'menyimak', 'menari', 'menyimpulkan', 'memberikan', 'bantuan', 'mengajarkan', 'mulai', 'berenang', 'tidur', 'kedapatan', 'merokok', 'berada', 'mengucilkan', 'berangkat', 'mengambang', 'pergi', 'bersepeda', 'pulang', 'bekerja', 'datang', 'berkunjung', 'berbelanja', 'bersedia', 'membantu', 'bertamasya', 'kebutuhan', 'memutuskan', 'memotong', 'menggunakan', 'menanggapi', 'ikut', 'asalkan', 'turut', 'memerah', 'peternakan', 'memainkan', 'terlihat', 'memancing', 'mencukur', 'Adv VP', 'Verb NP', 'Prep NP', 'Prep Verb', 'Prep Adj', 'baru', 'singkat', 'keras', 'tua', 'hangat', 'baik', 'lama', 'miskin', 'santai', 'dekat', 'rapi', 'rapat', 'Adv Adj', 'VP Prep', 'Adj Verb', 'Verb Adj'],
    "Pel": ['ibunya', 'adik', 'nasi', 'dapur', 'tugas', 'perempuan', 'taman', 'kota', 'pesan', 'siswa', 'kini', 'tadi', 'akhir', 'semester', 'paman', 'sepeda', 'motornya', 'anak', 'pemograman', 'komputer', 'orang', 'pasangan', 'tangan', 'gelas', 'mobil', 'peluru', 'gubernur', 'surat', 'tamu', 'materi', 'perkuliahan', 'seni', 'kakak', 'kandung', 'kelas', 'polisi', 'daerah', 'kado', 'sebentar', 'acara', 'sela', 'mantannya', 'masalah', 'dewa', 'laki', 'bapak', 'penipuan', 'balet', 'pengajaran', 'pemerintah', 'rakyat', 'bola', 'rombongan', 'haji', 'tubuhnya', 'ayah', 'kemarin', 'pagi', 'sekolah', 'kakek', 'rumah', 'pasar', 'pengikat', 'kakinya', 'pisau', 'isu', 'makar', 'rekreasi', 'susu', 'milik', 'gitar', 'kangkung', 'tumis', 'besok', 'pak', 'lurah', 'ikan', 'rambut', 'ujian', 'edaran', 'oleh-oleh', 'adikku', 'anaknya', 'ibu', 'Lukman', 'dodit', 'oki', 'johan', 'cianjir', 'yusuf', 'daffa', 'anwar', 'nadya', 'rahmi', 'tina', 'Joko', 'Theo', 'sintia', 'Nina', 'andi', 'reno', 'ratna ', 'dodi', 'zulkifli', 'rudi', 'kami', 'itu', 'aku ', 'dia', 'ia', 'mereka', 'nya', ' NP Noun', 'NP PropNoun', 'NP Pronoun', 'NP Verb', 'Adv NP', 'Prep NP', 'Prep Verb', 'Prep Adj', 'Adj NP', 'NP Adj', 'memasak', 'mengerjakan', 'bertemu', 'mengirim', 'melaksanakan', 'memperbaiki', 'bermain', 'main', 'belajar', 'berkebun', 'bergandengan', 'pecah', 'tahan', 'mengeluarkan', 'bersalaman', 'mempresentasikan', 'mempelajari', 'menunjuk', 'melakukan', 'penangkapan', 'membawa', 'mengobrol', 'goreng', 'lukis', 'tersebut', 'berhenti', 'menangisi', 'merasa', 'berbicara', 'memperjelas', 'mengajar', 'menyimak', 'menari', 'menyimpulkan', 'memberikan', 'bantuan', 'mengajarkan', 'mulai', 'berenang', 'tidur', 'kedapatan', 'merokok', 'berada', 'mengucilkan', 'berangkat', 'mengambang', 'pergi', 'bersepeda', 'pulang', 'bekerja', 'datang', 'berkunjung', 'berbelanja', 'bersedia', 'membantu', 'bertamasya', 'kebutuhan', 'memutuskan', 'memotong', 'menggunakan', 'menanggapi', 'ikut', 'asalkan', 'turut', 'memerah', 'peternakan', 'memainkan', 'terlihat', 'memancing', 'mencukur', 'Adv VP', 'Verb NP', 'Prep NP', 'Prep Verb', 'Prep Adj', 'baru', 'singkat', 'keras', 'tua', 'hangat', 'baik', 'lama', 'miskin', 'santai', 'dekat', 'rapi', 'rapat', 'Adv Adj', 'VP Prep', 'Adj Verb', 'Verb Adj', 'Prep Verb'],
    "O" : ['ibunya', 'adik', 'nasi', 'dapur', 'tugas', 'perempuan', 'taman', 'kota', 'pesan', 'siswa', 'kini', 'tadi', 'akhir', 'semester', 'paman', 'sepeda', 'motornya', 'anak', 'pemograman', 'komputer', 'orang', 'pasangan', 'tangan', 'gelas', 'mobil', 'peluru', 'gubernur', 'surat', 'tamu', 'materi', 'perkuliahan', 'seni', 'kakak', 'kandung', 'kelas', 'polisi', 'daerah', 'kado', 'sebentar', 'acara', 'sela', 'mantannya', 'masalah', 'dewa', 'laki', 'bapak', 'penipuan', 'balet', 'pengajaran', 'pemerintah', 'rakyat', 'bola', 'rombongan', 'haji', 'tubuhnya', 'ayah', 'kemarin', 'pagi', 'sekolah', 'kakek', 'rumah', 'pasar', 'pengikat', 'kakinya', 'pisau', 'isu', 'makar', 'rekreasi', 'susu', 'milik', 'gitar', 'kangkung', 'tumis', 'besok', 'pak', 'lurah', 'ikan', 'rambut', 'ujian', 'edaran', 'oleh-oleh', 'adikku', 'anaknya', 'ibu', 'Lukman', 'dodit', 'oki', 'johan', 'cianjir', 'yusuf', 'daffa', 'anwar', 'nadya', 'rahmi', 'tina', 'Joko', 'Theo', 'sintia', 'Nina', 'andi', 'reno', 'ratna ', 'dodi', 'zulkifli', 'rudi', 'kami', 'itu', 'aku ', 'dia', 'ia', 'mereka', 'nya', ' NP Noun', 'NP PropNoun', 'NP Pronoun', 'NP Verb', 'Adv NP', 'Prep NP', 'Prep Verb', 'Prep Adj', 'Adj NP', 'NP Adj'],
    "Ket": ['ibunya', 'adik', 'nasi', 'dapur', 'tugas', 'perempuan', 'taman', 'kota', 'pesan', 'siswa', 'kini', 'tadi', 'akhir', 'semester', 'paman', 'sepeda', 'motornya', 'anak', 'pemograman', 'komputer', 'orang', 'pasangan', 'tangan', 'gelas', 'mobil', 'peluru', 'gubernur', 'surat', 'tamu', 'materi', 'perkuliahan', 'seni', 'kakak', 'kandung', 'kelas', 'polisi', 'daerah', 'kado', 'sebentar', 'acara', 'sela', 'mantannya', 'masalah', 'dewa', 'laki', 'bapak', 'penipuan', 'balet', 'pengajaran', 'pemerintah', 'rakyat', 'bola', 'rombongan', 'haji', 'tubuhnya', 'ayah', 'kemarin', 'pagi', 'sekolah', 'kakek', 'rumah', 'pasar', 'pengikat', 'kakinya', 'pisau', 'isu', 'makar', 'rekreasi', 'susu', 'milik', 'gitar', 'kangkung', 'tumis', 'besok', 'pak', 'lurah', 'ikan', 'rambut', 'ujian', 'edaran', 'oleh-oleh', 'adikku', 'anaknya', 'ibu', 'Lukman', 'dodit', 'oki', 'johan', 'cianjir', 'yusuf', 'daffa', 'anwar', 'nadya', 'rahmi', 'tina', 'Joko', 'Theo', 'sintia', 'Nina', 'andi', 'reno', 'ratna ', 'dodi', 'zulkifli', 'rudi', 'kami', 'itu', 'aku ', 'dia', 'ia', 'mereka', 'nya', ' NP Noun', 'NP PropNoun', 'NP Pronoun', 'NP Verb', 'Adv NP', 'Prep NP', 'Prep Verb', 'Prep Adj', 'Adj NP', 'NP Adj', 'memasak', 'mengerjakan', 'bertemu', 'mengirim', 'melaksanakan', 'memperbaiki', 'bermain', 'main', 'belajar', 'berkebun', 'bergandengan', 'pecah', 'tahan', 'mengeluarkan', 'bersalaman', 'mempresentasikan', 'mempelajari', 'menunjuk', 'melakukan', 'penangkapan', 'membawa', 'mengobrol', 'goreng', 'lukis', 'tersebut', 'berhenti', 'menangisi', 'merasa', 'berbicara', 'memperjelas', 'mengajar', 'menyimak', 'menari', 'menyimpulkan', 'memberikan', 'bantuan', 'mengajarkan', 'mulai', 'berenang', 'tidur', 'kedapatan', 'merokok', 'berada', 'mengucilkan', 'berangkat', 'mengambang', 'pergi', 'bersepeda', 'pulang', 'bekerja', 'datang', 'berkunjung', 'berbelanja', 'bersedia', 'membantu', 'bertamasya', 'kebutuhan', 'memutuskan', 'memotong', 'menggunakan', 'menanggapi', 'ikut', 'asalkan', 'turut', 'memerah', 'peternakan', 'memainkan', 'terlihat', 'memancing', 'mencukur', 'Adv VP', 'Verb NP', 'Prep NP', 'Prep Verb', 'Prep Adj', 'baru', 'singkat', 'keras', 'tua', 'hangat', 'baik', 'lama', 'miskin', 'santai', 'dekat', 'rapi', 'rapat', 'Adv Adj', 'VP Prep', 'Adj Verb', 'Verb Adj', 'Prep Verb', 'Prep NumP2'],
    "NP": ['ibunya', 'adik', 'nasi', 'dapur', 'tugas', 'perempuan', 'taman', 'kota', 'pesan', 'siswa', 'kini', 'tadi', 'akhir', 'semester', 'paman', 'sepeda', 'motornya', 'anak', 'pemograman', 'komputer', 'orang', 'pasangan', 'tangan', 'gelas', 'mobil', 'peluru', 'gubernur', 'surat', 'tamu', 'materi', 'perkuliahan', 'seni', 'kakak', 'kandung', 'kelas', 'polisi', 'daerah', 'kado', 'sebentar', 'acara', 'sela', 'mantannya', 'masalah', 'dewa', 'laki', 'bapak', 'penipuan', 'balet', 'pengajaran', 'pemerintah', 'rakyat', 'bola', 'rombongan', 'haji', 'tubuhnya', 'ayah', 'kemarin', 'pagi', 'sekolah', 'kakek', 'rumah', 'pasar', 'pengikat', 'kakinya', 'pisau', 'isu', 'makar', 'rekreasi', 'susu', 'milik', 'gitar', 'kangkung', 'tumis', 'besok', 'pak', 'lurah', 'ikan', 'rambut', 'ujian', 'edaran', 'oleh-oleh', 'adikku', 'anaknya', 'ibu', 'Lukman', 'dodit', 'oki', 'johan', 'cianjir', 'yusuf', 'daffa', 'anwar', 'nadya', 'rahmi', 'tina', 'Joko', 'Theo', 'sintia', 'Nina', 'andi', 'reno', 'ratna ', 'dodi', 'zulkifli', 'rudi', 'kami', 'itu', 'aku ', 'dia', 'ia', 'mereka', 'nya', ' NP Noun', 'NP PropNoun', 'NP Pronoun', 'NP Verb', 'Adv NP', 'Prep NP', 'Prep Verb', 'Prep Adj', 'Adj NP', 'NP Adj'],
    "VP": ['memasak', 'mengerjakan', 'bertemu', 'mengirim', 'melaksanakan', 'memperbaiki', 'bermain', 'main', 'belajar', 'berkebun', 'bergandengan', 'pecah', 'tahan', 'mengeluarkan', 'bersalaman', 'mempresentasikan', 'mempelajari', 'menunjuk', 'melakukan', 'penangkapan', 'membawa', 'mengobrol', 'goreng', 'lukis', 'tersebut', 'berhenti', 'menangisi', 'merasa', 'berbicara', 'memperjelas', 'mengajar', 'menyimak', 'menari', 'menyimpulkan', 'memberikan', 'bantuan', 'mengajarkan', 'mulai', 'berenang', 'tidur', 'kedapatan', 'merokok', 'berada', 'mengucilkan', 'berangkat', 'mengambang', 'pergi', 'bersepeda', 'pulang', 'bekerja', 'datang', 'berkunjung', 'berbelanja', 'bersedia', 'membantu', 'bertamasya', 'kebutuhan', 'memutuskan', 'memotong', 'menggunakan', 'menanggapi', 'ikut', 'asalkan', 'turut', 'memerah', 'peternakan', 'memainkan', 'terlihat', 'memancing', 'mencukur', 'Adv VP', 'Verb NP', 'Prep NP', 'Prep Verb', 'Prep Adj', 'baru', 'singkat', 'keras', 'tua', 'hangat', 'baik', 'lama', 'miskin', 'santai', 'dekat', 'rapi', 'rapat', 'Adv Adj', 'VP Prep', 'Adj Verb', 'Verb Adj', 'Prep Verb'],
    "NumP": ["Prep Num NP", "suatu"],
    "AdjP": ["Adj', 'Adv Adj"],
    "PP": ['Prep NP', 'Prep Adj'],
    "Pronoun": ['kami', 'itu', 'aku ', 'dia', 'ia', 'mereka', 'nya'],
    "PropNoun": ['Lukman', 'dodit', 'oki', 'johan', 'cianjir', 'yusuf', 'daffa', 'anwar', 'nadya', 'rahmi', 'tina', 'Joko', 'Theo', 'sintia', 'Nina', 'andi', 'reno', 'ratna ', 'dodi', 'zulkifli', 'rudi'],
    "Noun": ['ibunya', 'adik', 'nasi', 'dapur', 'tugas', 'perempuan', 'taman', 'kota', 'pesan', 'siswa', 'kini', 'tadi', 'akhir', 'semester', 'paman', 'sepeda', 'motornya', 'anak', 'pemograman', 'komputer', 'orang', 'pasangan', 'tangan', 'gelas', 'mobil', 'peluru', 'gubernur', 'surat', 'tamu', 'materi', 'perkuliahan', 'seni', 'kakak', 'kandung', 'kelas', 'polisi', 'daerah', 'kado', 'sebentar', 'acara', 'sela', 'mantannya', 'masalah', 'dewa', 'laki', 'bapak', 'penipuan', 'balet', 'pengajaran', 'pemerintah', 'rakyat', 'bola', 'rombongan', 'haji', 'tubuhnya', 'ayah', 'kemarin', 'pagi', 'sekolah', 'kakek', 'rumah', 'pasar', 'pengikat', 'kakinya', 'pisau', 'isu', 'makar', 'rekreasi', 'susu', 'milik', 'gitar', 'kangkung', 'tumis', 'besok', 'pak', 'lurah', 'ikan', 'rambut', 'ujian', 'edaran', 'oleh-oleh', 'adikku', 'anaknya', 'ibu'],
    "Adj": ['baru', 'singkat', 'keras', 'tua', 'hangat', 'baik', 'lama', 'miskin', 'santai', 'dekat', 'rapi', 'rapat'],
    "Adv": ['sedang', 'sudah', 'saja', 'saling', 'telah', 'akan', 'sangat', 'tidak', 'langsung', 'cara', 'dengan', 'sangat', 'bersama', 'agar', 'lebih', 'tunai'],
    "Num": ['suatu'],
    "Prep": ['di', 'dengan', 'kepada', 'para', 'dari', 'yang', 'sebagai', 'untuk'],
    "Verb": ['memasak', 'mengerjakan', 'bertemu', 'mengirim', 'melaksanakan', 'memperbaiki', 'bermain', 'main', 'belajar', 'berkebun', 'bergandengan', 'pecah', 'tahan', 'mengeluarkan', 'bersalaman', 'mempresentasikan', 'mempelajari', 'menunjuk', 'melakukan', 'penangkapan', 'membawa', 'mengobrol', 'goreng', 'lukis', 'tersebut', 'berhenti', 'menangisi', 'merasa', 'berbicara', 'memperjelas', 'mengajar', 'menyimak', 'menari', 'menyimpulkan', 'memberikan', 'bantuan', 'mengajarkan', 'mulai', 'berenang', 'tidur', 'kedapatan', 'merokok', 'berada', 'mengucilkan', 'berangkat', 'mengambang', 'pergi', 'bersepeda', 'pulang', 'bekerja', 'datang', 'berkunjung', 'berbelanja', 'bersedia', 'membantu', 'bertamasya', 'kebutuhan', 'memutuskan', 'memotong', 'menggunakan', 'menanggapi', 'ikut', 'asalkan', 'turut', 'memerah', 'peternakan', 'memainkan', 'terlihat', 'memancing', 'mencukur']
}
 
class ListLexicon(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Database")
        self.resize(400, 600)
        
        self.scroll = QScrollArea()
        groupBox = QGroupBox()
        kamusLayout = QGridLayout()
        groupBox.setLayout(kamusLayout)
        
        self.scroll.setWidget(groupBox)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        outerLayout = QVBoxLayout()
        outerLayout.addWidget(self.scroll)
        self.setLayout(outerLayout)
        
        pronLabel = QLabel("Kata Ganti:")
        nounLabel = QLabel("Kata Benda:")
        propLabel = QLabel("Kata Benda Khusus:")
        verbLabel = QLabel("Kata Kerja:")
        adjLabel = QLabel("Kata Sifat:")
        advLabel = QLabel("Kata Keterangan:")
        prepLabel = QLabel("Preposisi:")
        numLabel = QLabel("Numeralia:")
        
        pron = "kami | itu | aku | dia | ia | mereka | nya"
        noun = "ibunya | adik | nasi | dapur | tugas | perempuan | taman | kota | pesan | siswa | kini | tadi | akhir | semester | paman | sepeda | motornya | anak | pemograman | komputer | orang | pasangan | tangan | gelas | mobil | peluru | gubernur | surat | tamu | materi | perkuliahan | seni | kakak | kandung | kelas | polisi | daerah | kado | sebentar | acara | sela | mantannya | masalah | dewa | laki | bapak | penipuan | balet | pengajaran | pemerintah | rakyat | bola | rombongan | haji | tubuhnya | ayah | kemarin | pagi | sekolah | kakek | rumah | pasar | pengikat | kakinya | pisau | isu | makar | rekreasi | susu | milik | gitar | kangkung | tumis | besok | pak | lurah | ikan | rambut | ujian | edaran | oleh-oleh | adikku | anaknya | ibu"
        prop = "Lukman | dodit | oki | johan | cianjir | yusuf | daffa | anwar | nadya | rahmi | tina | Joko | Theo | sintia | Nina | andi | reno | ratna  | dodi | zulkifli | rudi"
        verb = "memasak | mengerjakan | bertemu | mengirim | melaksanakan | memperbaiki | bermain | main | belajar | berkebun | bergandengan | pecah | tahan | mengeluarkan | bersalaman | mempresentasikan | mempelajari | menunjuk | melakukan | penangkapan | membawa | mengobrol | goreng | lukis | tersebut | berhenti | menangisi | merasa | berbicara | memperjelas | mengajar | menyimak | menari | menyimpulkan | memberikan | bantuan | mengajarkan | mulai | berenang | tidur | kedapatan | merokok | berada | mengucilkan | berangkat | mengambang | pergi | bersepeda | pulang | bekerja | datang | berkunjung | berbelanja | bersedia | membantu | bertamasya | kebutuhan | memutuskan | memotong | menggunakan | menanggapi | ikut | asalkan | turut | memerah | peternakan | memainkan | terlihat | memancing | mencukur"
        adj = "baru | singkat | keras | tua | hangat | baik | lama | miskin | santai | dekat | rapi | rapat"
        adv = "sedang | sudah | saja | saling | telah | akan | sangat | tidak | langsung | cara | dengan | sangat | bersama | agar | lebih | tunai"
        prep = "di | dengan | kepada | para | dari | yang | sebagai | untuk"
        num = "suatu"
        
        pronText = QTextEdit()
        pronText.setText(pron.replace(' ', '').replace('|', '\n')) 
        nounText = QTextEdit()
        nounText.setText(noun.replace(' ', '').replace('|', '\n'))
        propText = QTextEdit()
        propText.setText(prop.replace(' ', '').replace('|', '\n'))
        verbText = QTextEdit()
        verbText.setText(verb.replace(' ', '').replace('|', '\n'))
        adjText = QTextEdit()
        adjText.setText(adj.replace(' ', '').replace('|', '\n'))
        advText = QTextEdit()
        advText.setText(adv.replace(' ', '').replace('|', '\n'))
        prepText = QTextEdit()
        prepText.setText(prep.replace(' ', '').replace('|', '\n'))
        numText = QTextEdit()
        numText.setText(num.replace(' ', '').replace('|', '\n'))

        kamusLayout.addWidget(pronLabel, 0, 0)
        kamusLayout.addWidget(pronText, 1, 0, 1, 5)
        kamusLayout.addWidget(nounLabel, 2, 0)
        kamusLayout.addWidget(nounText, 3, 0, 1, 5)
        kamusLayout.addWidget(propLabel, 4, 0)
        kamusLayout.addWidget(propText, 5, 0, 1, 5)
        kamusLayout.addWidget(verbLabel, 6, 0)
        kamusLayout.addWidget(verbText, 7, 0, 1, 5)
        kamusLayout.addWidget(adjLabel, 8, 0)
        kamusLayout.addWidget(adjText, 9, 0, 1, 5)
        kamusLayout.addWidget(advLabel, 10, 0)
        kamusLayout.addWidget(advText, 11, 0, 1, 5)
        kamusLayout.addWidget(prepLabel, 12, 0)
        kamusLayout.addWidget(prepText, 13, 0, 1, 5)
        kamusLayout.addWidget(numLabel, 14, 0)
        kamusLayout.addWidget(numText, 15, 0, 1, 5)


class CFG(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplikasi Parsing Bahasa Baku Bahasa Indonesia")
        self.resize(300,200)
        self.window1 = ListLexicon()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.inputLabel = QLabel("Masukkan kalimat yang akan dicek :")
        self.checkButton = QPushButton("Check Validasi")
        self.checkButton.clicked.connect(self.klik)
        self.kalimatEntry = QLineEdit()
        self.statusLabel = QLabel("Status:")
        layout.addWidget(self.inputLabel)
        layout.addWidget(self.kalimatEntry)
        layout.addWidget(self.statusLabel)
        layout.addWidget(self.checkButton)

        kamusButton = QPushButton("Lihat Database")
        kamusButton.clicked.connect(self.toggle_window1)
        layout.addWidget(kamusButton)


    def klik(self):
        kalimat = self.kalimatEntry.text()
        
        if len(kalimat) == 0:
            self.statusLabel.setText("Masukkan kalimat terlebih dahulu.")
        elif cfg.hitungCYK(rules, kalimat.lower().split(' '), 'K'):
            self.statusLabel.setText("Status: Valid")
        else:
            self.statusLabel.setText("Status: Tidak Valid")
            
 
    def toggle_window1(self):
        if not self.window1.isVisible():
            self.window1.show()
   
app = QApplication(sys.argv)
window = CFG()
window.show()
sys.exit(app.exec())