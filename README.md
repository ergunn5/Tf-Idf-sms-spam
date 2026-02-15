📩 SMS Spam Detection using TF-IDF
📌 Project Description

This project focuses on detecting spam messages using the SMS Spam dataset.
Text messages were transformed into numerical representations using the TF-IDF (Term Frequency – Inverse Document Frequency) method, and word importance was analyzed based on their statistical distribution across documents.

The goal of this study is to demonstrate how text data can be converted into weighted feature vectors suitable for machine learning and statistical analysis.

🧠 Methodology
1. Text Preprocessing

Converting text to lowercase

Removing punctuation

Stopword removal

2. Feature Extraction

TF-IDF Vectorization

TF-IDF assigns higher weights to words that are frequent in a specific message but relatively rare across the entire dataset, making it more informative than simple word frequency counts.

🛠 Libraries Used

Python

Pandas

Scikit-learn

NLTK

📊 Objective

This project aims to:

Transform raw text into numerical feature space

Analyze word importance using TF-IDF weighting

Explore the statistical structure of spam vs. non-spam messages

No deep learning models were used in this study. The focus is on understanding classical NLP feature extraction techniques.

👤 Author

Ergün Çiçek
Master’s Student in Mathematics | Data Science Studies


📩 TF-IDF ile SMS Spam Tespiti
📌 Proje Açıklaması

Bu projede SMS Spam veri seti kullanılarak istenmeyen mesajların (spam) tespiti üzerine çalışılmıştır.
Metin mesajları, TF-IDF (Term Frequency – Inverse Document Frequency) yöntemi kullanılarak sayısal temsillere dönüştürülmüş ve kelimelerin önem düzeyleri istatistiksel dağılımlarına göre analiz edilmiştir.

Bu çalışmanın amacı, metin verilerinin makine öğrenmesi ve istatistiksel analiz için uygun ağırlıklı özellik vektörlerine nasıl dönüştürüldüğünü göstermektir.

🧠 Yöntem
1. Metin Ön İşleme

Küçük harfe dönüştürme

Noktalama işaretlerinin kaldırılması

Stopword temizleme

2. Özellik Çıkarımı

TF-IDF Vektörleştirme

TF-IDF yöntemi, belirli bir mesaj içinde sık geçen ancak tüm veri setinde nadir olan kelimelere daha yüksek ağırlık verir. Bu sayede basit kelime frekansına göre daha bilgilendirici bir temsil elde edilir.

🛠 Kullanılan Kütüphaneler

Python

Pandas

Scikit-learn

NLTK

📊 Çalışmanın Amacı

Bu proje şu konulara odaklanmaktadır:

Ham metin verisinin sayısal özellik uzayına dönüştürülmesi

TF-IDF ağırlıklandırması ile kelime öneminin analiz edilmesi

Spam ve normal mesajların istatistiksel yapısının incelenmesi

Bu çalışmada derin öğrenme yöntemleri kullanılmamıştır. Amaç, klasik NLP özellik çıkarım tekniklerinin temel mantığını anlamaktır.

👤 Hazırlayan

Ergün Çiçek
Matematik Yüksek Lisans Öğrencisi | Veri Bilimi Çalışmaları
