**İlk çalıştırma:**

- python3 kütüphanesinin kendi venv modülü ile bir sanal ortam oluşturun
```python -m venv venv```
- bu ortamı aktif edin (GNU/Linux / MacOS)
```source venv/bin/activate```
- bu ortamı aktif edin (Windows CMD)
```source .\\venv\Scripts\activate.bat```
- bu ortamı aktif edin (Windows Powershell)
```source . venv\Scripts\activate```
- gerekli kütüphaneleri yükleyin
```pip install -r requirements.txt```

*daha sonra main.py çalıştırın:*
```
python main.py
```

**Problemin İyi Tanımlanması:**

**Problemin Tanımı:** İş Makinesi Atama Problemi, belirli bir iş listesi ile bir dizi iş makinesi arasında optimal atama yapmayı amaçlayan bir optimizasyon problemini ifade eder. Her iş, farklı iş süreleri ile her bir makine üzerinde tamamlanabilir.

**Giriş Parametreleri:** Problemin giriş parametreleri şunlardır:

-  `cost_matrix` : İşlerin her biri için her bir makine üzerindeki iş sürelerini içeren bir maliyet matrisi.
-  `num_jobs` : Toplam iş sayısı.
-  `num_machines` : Kullanılabilir iş makinelerinin sayısı.

**Çıkış Beklentileri:** Problemin çıkış beklentileri şunlardır:

-  `optimal_assignments` : Her bir işin atanacağı makine endekslerini içeren bir dizi.
-  `total_cost` : Atama sonucu elde edilen toplam maliyet.

**Genel Yapı ve Sınırlamalar:** Problemin genel yapısı şu şekildedir: Her bir iş sadece bir makineye atanabilir ve her bir makine aynı anda sadece bir işi işleyebilir. Ayrıca, atama sonucu maliyeti minimize etmek amaçlanır.

**Temel Modelin İyi Tanımlanması:**

**Temel Model:** Problemin temel modeli şu şekildedir: İş makinesi atama problemini çözmek için, her bir işin atanacağı makine endekslerini içeren bir çözüm uzayını minimize eden bir matematiksel model kullanılır.

**Veri Yapıları ve Algoritmalar:** Problemin çözümünde kullanılacak veri yapıları şunlardır:

-   İş makinesi atama matrisi (`cost_matrix`).
-   Atama çözümü için kullanılacak algoritmalar şunlardır: `Hungarian Method`, `Simulated Annealing`.

**Katkı Sağlama:** Temel model, iş makinesi atama problemini matematiksel bir çerçevede ifade ederek, çözüm uzayındaki en iyi atamayı bulmada önemli bir rol oynar. Bu model, maliyeti minimize etme amacı doğrultusunda çeşitli algoritmaların uygulanmasına olanak tanır.

**Proje İstenilen Programlama Dili İle Gerçekleştirilebilir: **

**Kullanılan Programlama Dili:** Proje, Python programlama dili kullanılarak gerçekleştirilmiştir.

**Dilin Seçimi ve Kullanımı:** Python, proje için seçilen dil olmasının temel nedenleri şunlardır: Python'un geniş kütüphane desteği, okunabilir syntax yapısı ve hızlı prototip geliştirme yetenekleri. Python, hem matematiksel modellendirme hem de çeşitli optimizasyon algoritmalarının implementasyonu için uygun bir dil olarak tercih edilmiştir.

**En Az İki Algoritmanın Gerçekleştirimi:**

**İlk Algoritma: Hungarian Method**

**Temel Yaklaşım:** Hungarian Method, iş makinesi atama problemini çözmek için kullanılan bir çözüm algoritmasıdır. Problemi çözmek için bir maliyet matrisi kullanır ve optimum atamayı bulmaya çalışır.

**Avantajlar ve Dezavantajlar:** Hungarian Method'un avantajları şunlardır: hızlı çalışma zamanı, doğru sonuçlar. Dezavantajları ise: büyük boyutlu matrislerle performans sorunları yaşayabilir.

**İkinci Algoritma: Simulated Annealing**

**Farklı Yaklaşım:** Simulated Annealing, iş makinesi atama problemini çözmek için kullanılan bir metaheuristik algoritmadır. Rastgele atamalardan başlayarak, enerji fonksiyonunu minimize etmeye çalışır.

**Kullanım Gerekçeleri ve Performans Değerlendirmesi:** Simulated Annealing'in kullanım gerekçeleri şunlardır: global optimizasyon problemleriyle başa çıkabilme yeteneği, başlangıç çözümünden kaçış yeteneği.

**Algoritmaların Etkinliklerinin Değerlendirilmesi:**

**Her İki Algoritmanın Teorik Analizi:**

**Zaman ve Hafıza Karmaşıklıkları:** Hungarian Method'un teorik zaman ve hafıza karmaşıklığı düşüktür: O(n^3) ve O(n^2) sırasıyla. Simulated Annealing'in teorik zaman ve hafıza karmaşıklığı ise problem özelinde değişebilir.

**Avantajlar ve Dezavantajlar:** Her iki algoritmanın teorik avantajları ve dezavantajları şunlardır: Hungarian Method hızlı çalışma zamanına sahiptir ancak büyük matrislerle performans sorunları yaşanabilir. Simulated Annealing ise genel optimizasyon problemlerine uygundur ancak başlangıç durumuna bağlı olarak sonuçlar değişebilir.

**Her İki Algoritmanın Pratik Uygulaması:**

**Farklı Girdi Setleri:** Algoritmalar, farklı iş sayıları ve maliyet matrisleri içeren girdi setleri üzerinde test edildi.

**Performans Karşılaştırması:** Zaman ve hafıza kullanımı gibi pratik ölçütlerle her iki algoritmanın performansı şu şekildedir: [Performans karşılaştırması sonuçları]. Hungarian Method genellikle küçük ve orta ölçekli problemlerde daha etkilidir, Simulated Annealing ise büyük ve karmaşık problemlerde daha avantajlı olabilir.