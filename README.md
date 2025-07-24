# YourBookingHub.org - Complete Multi-Tenant Hotel Email Automation SaaS

## 🎯 Tam Özellikli Hotel Email Otomasyonu

Bu paket, oteller için geliştirilmiş yapay zeka destekli email otomasyon sistemidir.

### ✨ Yeni Özellikler

- **📁 Dosya Yükleme Sistemi**: Yeni otel oluştururken app_complete.py dahil tüm dosyalar yüklenebilir
- **🎮 Başlat/Durdur Kontrolleri**: Hotel dashboard'da sistem kontrolü için butonlar
- **🎨 Profesyonel Tasarım**: Modern, responsive ve kullanıcı dostu arayüz
- **🤖 Otomatik Script Çalıştırma**: Başlat butonu ile app_complete.py otomatik çalışır
- **📂 Akıllı Dosya Organizasyonu**: Python, resim ve diğer dosyalar otomatik sınıflandırılır

### 🚀 Kurulum

1. **Gereksinimleri yükleyin:**
```bash
pip install -r requirements.txt
```

2. **Sistemi başlatın:**
```bash
python multi_tenant_app.py
```

3. **Tarayıcıda açın:**
```
http://localhost:5000
```

### 🔐 Giriş Bilgileri

**Admin Paneli:** `/admin`
- Kullanıcı: `admin`
- Şifre: `admin123`

**Demo Oteller:**
- Cornelia: `/hotel/cornelia` (admin/admin123)
- Rixos: `/hotel/rixos` (admin/admin123)

### 📁 Klasör Yapısı

```
yourbookinghub_complete_final/
├── multi_tenant_app.py          # Ana uygulama
├── app_complete.py              # Email otomasyonu script'i
├── requirements.txt             # Python gereksinimleri
├── README.md                   # Bu dosya
├── templates/                  # HTML template'leri
│   ├── yourbookinghub_homepage.html
│   ├── admin_login.html
│   ├── admin_dashboard.html
│   ├── create_hotel.html
│   ├── hotel_login.html
│   └── hotel_dashboard.html
├── hotel_files/               # Otel dosyaları (otomatik oluşur)
│   └── [domain_name]/
│       ├── scripts/          # Python dosyaları
│       ├── images/           # Resim dosyaları
│       ├── templates/        # HTML template'leri
│       └── documents/        # Diğer dökümanlar
└── docs/                     # Dokümantasyon
```

### 🎯 Özellikler

#### 1. Multi-Tenant Sistem
- Her otel için ayrı domain (cornelia.yourbookinghub.org)
- Kişiselleştirilmiş dashboard'lar
- Bağımsız dosya depolama

#### 2. AI Email Otomasyonu
- OpenAI GPT-4o entegrasyonu
- 5 dil desteği (TR, EN, DE, FR, RU)
- Otomatik email analizi ve yanıt

#### 3. Gmail Entegrasyonu
- OAuth 2.0 güvenli bağlantı
- Otomatik email okuma
- Akıllı yanıt gönderme

#### 4. Dosya Yönetimi
- Drag & drop yükleme
- Otomatik dosya tipi tanıma
- Güvenli dosya saklama

### 🔧 Kullanım

#### Yeni Otel Oluşturma:
1. Admin panel'e giriş yapın
2. "Yeni Otel Oluştur" butonuna tıklayın
3. Otel bilgilerini doldurun
4. app_complete.py ve diğer dosyaları yükleyin
5. Otel hesabı otomatik oluşturulur

#### Email Otomasyonunu Başlatma:
1. Otel dashboard'a giriş yapın
2. "Başlat" butonuna tıklayın
3. app_complete.py script'i console'da çalışır
4. Sistem otomatik email işlemeye başlar

### 📊 Dashboard Özellikleri

- **Real-time Sistem Durumu**: Çalışıyor/Durduruldu göstergesi
- **Email İstatistikleri**: Günlük/aylık işlenen email sayıları
- **Gmail Bağlantı Durumu**: OAuth durumu ve yönetimi
- **Son Aktiviteler**: Email işleme geçmişi

### 🌐 Production Deployment

Bu sistem production'da kullanım için hazırlanmıştır:
- Güvenli dosya yönetimi
- SQLite veritabanı
- Session yönetimi
- Error handling

### 📞 Destek

- Email: poyraz100000@gmail.com
- 24/7 Teknik Destek

### 📝 Notlar

- Sistem 5000 portunda çalışır
- Hotel dosyaları `hotel_files/` klasöründe saklanır
- Her otel için ayrı klasör yapısı oluşturulur
- Başlat butonu ile script'ler otomatik çalışır

Bu paket ile otelleriniz için tam otomatik email yönetimi kurabilirsiniz!