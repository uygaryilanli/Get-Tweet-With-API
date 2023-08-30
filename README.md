# Web-Scraping-With-API
API Kullanarak Kolay Yoldan Web Kazıma

# API DOSYALARI

- Twitter için = https://rapidapi.com/alexanderxbx/api/twitter-api45/
- Google dökümanı düzenlemek için = https://dashboard.sheety.co/

# YAPILACAKLAR
- Twitter api için yapmanız gereken tek şey, yukarıda vermiş olduğum siteden api nin ücretsiz versiyonuna abone olmak. Tabi, Rapid sitesine üye değilseniz önce siteye üye olun.
- API programına abone olduktan sonra rapid host, key ve api nin size vermiş olduğu url bilgisini kopyalayıp, dosyalarda size belirtmiş olduğum yerlere yapıştırıcaksınız.
- Sheety api için ise öncelikle sheety'nin sitesine gidip kayıt olacaksınız. Ardından, google dökümanlarına gidip kendinize excel dosyası oluşturun ve dosya başlıklarınızı parametre sözlüklerindeki "key" isimleriyle aynı olmasına önem verin.
- Anlamayanlar için, başlıklardan kastım 1. satırdaki alanlar örneğin A1 hücresine Country dediniz B1 hücresine Name gibi... (Burayı açıklama sebebim, eğer parametre sözlüğündeki key bilgileri ile excel dosyasındaki başlıklar uyuşmaz ise, api, dosyaya herhangi bir bilgi yazdırmıyor.)
- Excel dosyanızdaki başlıkları oluşturdunuz, şimdi ise o excel dosyasının url adresini kopyalayıp sheety api de istenen yere yapıştırmak, ardından oluştur demek.
- Bu işlemi yaptıktan sonra karşınıza sayfa adınızdan oluşturulmuş bir ekran çıkacak, o ekranda get ve post bölümlerinin aktif olduğundan emin olun ve eğer değilse onları aktif edin. Çünkü sadece ikisini kullanacağız. (YANİ PUT VE DELETE BÖLÜMÜ KAPALI KALABİLİR.)
- İki bölümüde aktif ettik, şimdi ise get veya post bölümünde yer alan url adresini kopyalayıp dosyalarda belirttiğim bölümlere yapıştırın. Ardından tekrar api sitesine dönüp API, Authentication ve Settings bölümlerinden Authentication bölümüne geçelim ve en alttaki Bearer (Token) kutucuğunu işaretleyelim, Token başlığındaki input alanına rastgele bir şifre oluşturun ve ardından save changes diyin.
- Kaydettikten sonra Authorization Header bölmünde kodun tamamını kopyaların "Bearer ÖrneĞİNBuşEKİLde" daha sonra o kodu alıp dosyalarda size belirttiğim bölümlere yapıştırın. Dosyadaki hedef içeriğinin
şu şekilde gözükmesi gerekiyor; "Authorization" : "Bearer ÖrneĞİNBuşEKİLde". Artık uygulama içerisine girip twitterdan dan çekmek istediğiniz tweetleri çekebilirsiniz.
