![syslog_simulator_logo](/img/logo.png)

<br />

![Twitterda takip et](https://img.shields.io/twitter/follow/enesilhaydin?style=social)
![GitHub En Son commit](https://img.shields.io/github/last-commit/enesilhaydin/syslogsimulator)
![GitHub](https://img.shields.io/github/license/enesilhaydin/syslogsimulator)

<br />

`syslogsimulator` hazır ürün loglarını SIEM veya log toplayıcısına istediğiniz portta belirli sürelerde göndermeyi sağlayan küçük bir araçtır. 
<br />

<br />



## 🚀Nedir

Çeşitli donanım ve yazılım loglarının yanı sıra isteğinize göre düzenlenediğiniz okunabilir formattaki logları hedef makinaya göndermeyi sağlayan açık kaynak araçtır.

<br />

## 🔨Kullanımı
Python3 ile aşağıdaki belirtilen konfigürasyonlar girilerek çalıştırılmaktadır.
```bash
python3 syslogsimulator.py -s 1.1.1.1 -s 2.2.2.2 -s 3.3.3.3 -p 514 -P tcp -r 1 -d 0.1
```
 + `-s veya --server` 
    + `Gereklilik : Zorunlu`
    +  `Çoklu Kullanım : Evet`
 + `-p veya --port`
    + `Gereklilik : İsteğe Bağlı`
    + `Default : 514`
 + `-d veya --delay`
    + `Gereklilik : İsteğe Bağlı`
    + `Default : 0.5 saniye`
 + `-P veya --protocol`
    + `Gereklilik : İsteğe Bağlı`
    + `Default : udp`
 + `-r veya --rotate`
    + `Gereklilik : İsteğe Bağlı`
    + `Default : 1`
    + 🔔 `Eğer 10 değeri girilirse sınırsız rotate oluşacaktır.`
    
<br />


## 📰Örnek Log Paketleri

Syslog Simulator için kullanılan örnek loglar https://github.com/elastic/beats/tree/master/x-pack/filebeat/module reposundan temin edilmiştir.

<br />

## ⏳Geliştirme ve Kaynak Ekleme

	### Yeni Kaynak Ekleme
<br />

## ✔️Todo

+ çoklu kaynak gönderimi eklenmesi.
+ linux veya windows üzerinde çalıştırılma tespit fonksiyonu.
+ ~~udp/tcp port seçimi özelliğinin eklenmesi.~~
+ ~~default kaynak loglarının eklenmesi.~~
+ json/csv kaynaklarının parsing edilmesi.
