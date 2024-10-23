Sesli Komut Arayüzü - README
Genel Bakış
Bu Python uygulaması, kullanıcıların çeşitli sistem görevlerini kontrol etmesine, not almasına, web üzerinde arama yapmasına ve Python betiklerini çalıştırmasına olanak tanır. Arayüz, GUI için Tkinter kullanılarak oluşturulmuş olup, sesli komutları yorumlamak için SpeechRecognition ile entegre edilmiştir.

Özellikler
1. Sesli Komut İşleme
Uygulama, SpeechRecognition kütüphanesini kullanarak mikrofon aracılığıyla kullanıcı sesli komutlarını dinler.
Komutlar işlenerek uygulamaları açma, projeler/dosyalar oluşturma veya web üzerinde arama yapma (ör. Google ve Stack Overflow) gibi işlemler gerçekleştirilir.

2. Sesle Uygulama Başlatma
Uygulama, sesli komutlar aracılığıyla aşağıdaki uygulamaları açmayı destekler:
Finder (MacOS dosya yöneticisi)
TextEdit (MacOS metin düzenleyici)
Google Chrome
Spotify
Hesap Makinesi
Örnek komutlar:
"Klasör aç" → Finder'ı açar.
"Chrome çalıştır" → Google Chrome'u açar.

3. Google ve Stack Overflow Arama
Uygulama, kullanıcıların sesli giriş veya yazılı sorgulara göre Google ve Stack Overflow'da arama yapmasına olanak tanır.
Python betikleri çalıştırılırken meydana gelen hatalar otomatik olarak algılanabilir ve Stack Overflow'da çözümler aranabilir.

4. Sesli Not Alma
Kullanıcılar sesle not alabilir ve bu notlar gerçek zamanlı olarak bir metin alanına çevrilir.
"Not bitti" komutu ile not alma işlemi sonlandırılır.
Notlar bir dosyaya kaydedilebilir, temizlenebilir veya uygulama içinde düzenlenebilir.

5. Visual Studio Code Entegrasyonu
Uygulama, sesli komutlar aracılığıyla Visual Studio Code (VSCode) açmak için bir düğme sağlar.

6. Python Betik Çalıştırma
Kullanıcılar Python betiklerinin yolunu girerek betiği çalıştırabilir ve oluşan hataları otomatik olarak Stack Overflow'da arayabilir.

7. Komut Bilgisi Menüsü
"Bilgi" menüsü, kullanıcıların sistemle nasıl etkileşim kuracağını anlamalarına yardımcı olmak için mevcut sesli komutların bir özetini sağlar.
Bileşenler
GUI Düzeni:
Not Alma Bölümü:
Kullanıcıların not alma işlemini başlatmasına ve durdurmasına, notları temizlemesine ve bir dosyaya kaydetmesine olanak tanır.
Uygulama Başlatıcı:
Finder, Chrome, Spotify gibi uygulamaları açmak için düğmeler içerir.
Arama Bölümü:
Google ve Stack Overflow arama çubukları, hem sesli hem de yazılı giriş ile arama yapma imkanı sunar.
Python Betik Hata İşleme:
Python betiği çalıştırıp hatalarını Stack Overflow'da arama yapabilme özelliği sağlar.
Sesli Komutlar:
Uygulama, "aç", "çalıştır", "ara" veya "not bitti" gibi anahtar kelimeleri dinler.
Bu komutlar tespit edildiğinde, uygulama açma, proje oluşturma, not alma veya web arama gibi işlemler gerçekleştirilir.
Sesli Not Alma İçin Çoklu İşlem:
Not alma işlevi ayrı bir iş parçacığında çalışır, böylece uygulama notları alırken diğer kullanıcı girişlerine yanıt vermeye devam eder.
Hata Yönetimi:
subprocess modülü, harici komutları çalıştırmak için kullanılır ve betik çalıştırma sırasında oluşan hatalar yakalanır ve Stack Overflow'da arama yapmak için kullanılır.
Kurulum Talimatları
Gereksinimler:

Python 3.x
Gerekli Python paketleri:
SpeechRecognition
tkinter
webbrowser
subprocess
os
Kurulum:

Gerekli paketleri pip ile yükleyin:
pip install SpeechRecognition
Uygulamayı Çalıştırma:

Betiği Python ile çalıştırın:
python main.py

Uygulamanın Kullanımı:

Not alma işlemini başlatmak, notları kaydetmek veya temizlemek, uygulamaları açmak ya da arama yapmak için düğmelere tıklayın.
Mikrofonunuza doğrudan komutları söyleyin, uygulama söylediklerinizi algılar ve uygun işlemi gerçekleştirir.
Notlar
Sesli komutlar için mikrofonun doğru şekilde bağlı olduğundan emin olun, çünkü sesli komutlar ses girişine dayanmaktadır.
Uygulama şu anda MacOS için optimize edilmiştir. Diğer sistemlerde kullanmak için subprocess.run() komutlarını sisteminize uygun şekilde değiştirin.

