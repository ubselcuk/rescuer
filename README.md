![logo](logo.png) 


- pip install fpdf
- pip install Pillow


## Kullanım

```bash
cd rescuer
rescuer.py -i "folder" or --input "folder"
# Dönüştürmek istediğiniz dosyaların bulunduğu klasörü girmeniz gerekiyor.
# Eğer belirtilmezse varsayılan olarak input klasörünü seçecektir.
rescuer.py -o "something" or --output "something"
# Pdf dosyasının adı. Dosya varsayılan olarak output klasöründe oluşur.
rescuer.py -r "file" or --rotate "file"
# Döndürmek istediğiniz dosyayı bu komutla çevirebilirsiniz.
rescuer.py -h or --horizontal
# Pdf'i yatay olarak oluşturur. Dikey dosyaları otomatik döndürür. 
rescuer.py -v or --vertical
# Pdf'i dikey olarak oluşturur. Yatay dosyaları otomatik döndürür. 
rescuer.py -d or --default
# Dosyaları döndürmez, oldukları halleri ile kalırlar. 
```

## Links
[fpdf](https://pypi.org/project/fpdf/)
[pillow](https://pypi.org/project/Pillow/)
[python](https://www.python.org/downloads/windows/)


## License
[MIT](https://choosealicense.com/licenses/mit/)




