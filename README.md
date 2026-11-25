
# KampüsBul - Üniversite Kayıp Eşya Takip Sistemi

## Proje Tanımı

KampüsBul, üniversite öğrencilerinin kampüs içerisinde kaybettikleri veya buldukları eşyaları paylaşabilecekleri web tabanlı bir uygulamadır.

## Çözülen Problem

Üniversite kampüslerinde kaybolan eşyaların sahiplerine ulaştırılması zor olabilmektedir. KampüsBul, kayıp ve bulunan eşya ilanlarını tek bir platformda toplayarak bu süreci kolaylaştırmayı amaçlamaktadır.

## Hedef Kullanıcılar

- Üniversite öğrencileri
- Akademik personel
- İdari personel

## Kullanılan Teknolojiler

- Python
- Flask
- HTML
- CSS
- SQLite
- Git ve GitHub
- GitHub Projects

## Proje Özellikleri

- [x] Kayıp ve bulunan eşya ilanı oluşturma
- [x] İlanları listeleme
- [ ] İlanları türüne göre filtreleme
- [ ] Eşya adına göre arama yapma
- [ ] Teslim edilen eşya ilanını kapatma

## Proje Yönetimi

Projenin geliştirme süreci GitHub Projects üzerinden takip edilmektedir.

Görevler üç farklı sütunda yönetilmektedir:

- Todo (Yapılacak)
- In Progress (Devam Ediyor)
- Done (Tamamlandı)

Her görev için açıklama ve kabul kriterleri belirlenmiştir.

[Proje Yönetim Panosu](https://github.com/users/omerakyol0/projects/2/views/1)

## Kurulum ve Çalıştırma

Uygulamanın çalıştırılması için Python ve Git kurulu olmalıdır.

### 1. GitHub deposunu bilgisayarınıza indirin.

```bash
git clone https://github.com/omerakyol0/KampusBul.git
```

### 2. Proje klasörüne girin.

```bash
cd KampusBul
```

### 3. Gerekli kütüphaneleri yükleyin.

```bash
python -m pip install -r requirements.txt
```

### 4. Uygulamayı başlatın.

```bash
python app.py
```

### 5. Tarayıcıdan uygulamayı açın.

http://127.0.0.1:5000

SQLite veritabanı uygulama ilk çalıştırıldığında otomatik olarak oluşturulmaktadır.

## Geliştirilen Özelliklerin Test Edilmesi

### Özellik 1: İlan Oluşturma

Kullanıcıların kayıp veya bulunan eşya ilanı oluşturmasını sağlar.

Test adımları:

1. Uygulamayı başlatın.
2. Yeni İlan Oluştur butonuna tıklayın.
3. Eşya adı, ilan türü, konum ve açıklama alanlarını doldurun.
4. İlanı Yayınla butonuna tıklayın.
5. İlanın başarıyla oluşturulduğuna ilişkin mesajı kontrol edin.

Beklenen sonuç:

İlan SQLite veritabanına kaydedilmeli ve başarı mesajı görüntülenmelidir. Zorunlu alanlar boş bırakıldığında kayıt yapılmamalıdır.

### Özellik 2: İlan Listeleme

Veritabanında kayıtlı ilanların ana sayfada görüntülenmesini sağlar.

Test adımları:

1. Uygulamada bir veya birden fazla ilan oluşturun.
2. Ana Sayfa butonuna tıklayın.
3. Oluşturulan ilanların görüntülendiğini kontrol edin.
4. Toplam ilan sayısını kontrol edin.
5. En son oluşturulan ilanın ilk sırada görüntülendiğini kontrol edin.

Beklenen sonuç:

Veritabanında kayıtlı ilanlar yeniden eskiye doğru sıralanmalı ve ilanların eşya adı, türü, konumu, açıklaması, durumu ve tarihi görüntülenmelidir.

## Gelecekte Geliştirilmesi Planlanan Özellikler

- İlan filtreleme
- Eşya arama
- İlan kapatma

## Projenin Mevcut Durumu

Proje geliştirme aşamasındadır. İlk sürümde ilan oluşturma ve ilan listeleme özellikleri geliştirilmiştir. Diğer özellikler proje yönetim panosunda planlanmıştır.

## Geliştirici

Ömer Akyol

Harran Üniversitesi - Bilgisayar Mühendisliği
