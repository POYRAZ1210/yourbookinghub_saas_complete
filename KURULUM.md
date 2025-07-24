# YourBookingHub.org - Kurulum Rehberi

## 🚀 Hızlı Başlangıç

### 1. Dosyaları İndirin
```bash
# Klasörü bilgisayarınıza kopyalayın
cd yourbookinghub_complete_final
```

### 2. Python Gereksinimlerini Yükleyin
```bash
pip install -r requirements.txt
```

### 3. Sistemi Başlatın
```bash
python multi_tenant_app.py
```

### 4. Tarayıcıda Açın
```
http://localhost:5000
```

## 🔐 İlk Giriş

### Admin Paneli
- URL: `http://localhost:5000/admin`
- Kullanıcı: `admin`
- Şifre: `admin123`

### Demo Oteller (Hazır)
- **Cornelia**: `http://localhost:5000/hotel/cornelia` (admin/admin123)
- **Rixos**: `http://localhost:5000/hotel/rixos` (admin/admin123)

## 📝 Yeni Otel Oluşturma

1. **Admin panel'e giriş yapın**
2. **"Yeni Otel Oluştur" butonuna tıklayın**
3. **Otel bilgilerini doldurun:**
   - Otel Adı (örn: "Delphin Imperial")
   - Domain Adı (örn: "delphin") 
   - Admin Email ve Şifre
   - Gmail Hesabı (opsiyonel)

4. **Dosyaları yükleyin:**
   - app_complete.py (email otomasyonu için)
   - Logo dosyaları (.jpg, .png)
   - HTML template'leri
   - Diğer dökümanlar

5. **"Otel Hesabı Oluştur" butonuna tıklayın**

## 🤖 Email Otomasyonunu Başlatma

### Adım 1: Otel Dashboard'a Giriş
```
http://localhost:5000/hotel/[domain_name]
```

### Adım 2: Gmail Bağlantısı (Opsiyonel)
- Gmail hesabınızı bağlayın
- OAuth onayı verin

### Adım 3: Sistemi Başlatın
- **"Başlat" butonuna tıklayın**
- app_complete.py script'i otomatik çalışır
- Email işleme başlar

## 📁 Dosya Organizasyonu

Sistem otomatik olarak şu klasör yapısını oluşturur:

```
hotel_files/
└── [domain_name]/
    ├── scripts/          # Python dosyaları (app_complete.py)
    ├── images/           # Logo ve resimler
    ├── templates/        # HTML template'leri
    └── documents/        # PDF, Word vb. dökümanlar
```

## ⚙️ Gelişmiş Ayarlar

### Environment Variables (.env dosyası)
```env
FLASK_SECRET_KEY=your-secret-key
GMAIL_CLIENT_ID=your-gmail-client-id
GMAIL_CLIENT_SECRET=your-gmail-client-secret
OPENAI_API_KEY=your-openai-api-key
```

### Port Değiştirme
```python
# multi_tenant_app.py dosyasının sonunda
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)  # Port 8000'e değiştirildi
```

## 🔧 Sorun Giderme

### Port Zaten Kullanımda Hatası
```bash
# Farklı port ile başlatın
python multi_tenant_app.py --port 8000
```

### Dosya Yükleme Problemi
- Dosya boyutunu kontrol edin (max 10MB)
- Dosya formatını kontrol edin
- Yetkileri kontrol edin

### Email Otomasyonu Çalışmıyor
- app_complete.py dosyasının yüklendiğinden emin olun
- OpenAI API key'inin doğru olduğunu kontrol edin
- Gmail OAuth ayarlarını kontrol edin

## 📞 Destek

Sorun yaşarsanız:
- Email: poyraz100000@gmail.com
- 24/7 teknik destek

## 🎯 Önemli Notlar

- **Güvenlik**: Production'da strong secret key kullanın
- **Dosyalar**: hotel_files/ klasörünü yedekleyin
- **Veritabanı**: SQLite dosyası otomatik oluşturulur
- **Log'lar**: Console'da sistem durumunu takip edin

Başarılı kurulum sonrası tam otomatik email yönetimi aktif olacak!