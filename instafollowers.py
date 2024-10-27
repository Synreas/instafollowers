# instafollowers.py
#
# %% github.com/Synreas 
# 
# @@ instagram.com/@berkay8455
#
#
# !! BeautifulSoup4 kütüphanesinin kurulu olduğundan emin olun
#
# ~~ çevrim dışı çalışan bir uygulamadır (verileriniz güvendedir)
#
#
# ?? Nasıl kullanılır:
# -- 1-) instagram - ayarlar - hareketlerin - bilgilerini indir
#        - takipçiler ve takip edilenler - indirin
# -- 2-) dosya hazır olduğunda indirip dosyaları ayıklayın
# -- 3-) ayıklanan dosyalar arasında 
#        * following.html
#        * recent_follow_requests.html
#        * following_1.html
#        dosyalarını bu klasöre taşıyın
#        ! klasörde mevcut following_1.html dosyası varsa
#          eski dosyanın adını following_2.html yapıp sonra
#          sonra taşıyın
#        | eski following_2.html dosyasını silmekte sorun yoktur
# -- 4-) klasörde mevcut dosyalar şu şekilde gözükmeli:
#        * instafollowers.py
#        * recent_follow_requests.html
#        * following.html
#        * followers_1.html
#        * followers_2.html (opsiyonel)
# -- 5-) instafollowers.py yi çalıştırın
# -- 6-) isimler listelendikten sonra terminale girdiğiniz her harf
#        ya da isim için gönderdiğiniz takip isteklerinizden takipçileriniz 
#        arasında olmayanlar gösterilir (hepsini görmek için * yazın)
# -- 7-) çıkmak için sadece ENTER a basın
#

try:
	from bs4 import BeautifulSoup

except:
	print("\n!!BeautifulSoup4 kütüphanesinin kurulu olduğundan emin olun.")
	input()
	exit()

following = []      # takip edilenler
followers = []      # takipçiler
old_followers = []  # eski takipçiler
fames = []          # geri takip etmeyenler
reqs = []           # istekler
denied = []         # kabul edilmeyen istekler
quitted = []        # takipten çıkanlar


# html dosyalarındaki verilerin beautifulsoup4 ile
# parçalanıp listeleri girilmesi
def upload_data(ls, data):
	with open(data, "r") as f:
		soup = BeautifulSoup(f, "html.parser")
		users = soup.find_all("a", target="_blank")
		for user in users:
			ls.append(user.string)


# list1'de olup liste2'de olmayanların tespit edilip 
# list3'e aktarılması
def find(list1, list2, list3):
	for i in list1:
		if i not in list2:
			list3.append(i)

# verilerin gösterilmesi
def show():
	print("")
	print(f"{len(following)} tane takip edilen")
	print(f"{len(followers)} tane takipçi")
	if(len(fames) > 0):
		print("\nseni geri takip etmeyenler:\n")
		for i in range(len(fames)):
			print(str(i + 1) + (" " if i + 1 < 10 else "") + "-) " + fames[i]) 
		print("")
	if(len(quitted) > 0):
		print('yakın zamanda takibi bırakanlar:')
		for i in range(len(quitted)):
			print(str(i+1) + '-) ' + quitted[i])
		print('')

# takip isteklerinin aranması
def search_denied():
	if(len(denied) > 0):
		while True:
			u = input()
			if(u==""): break
			elif(u=="*"):
				for i in range(len(denied)):
					print(str(i+1) + "-) " + denied[i])
			else:
				for i in denied:
					if(u in i):
						print("-" + i)
			print("")
		
try:
	upload_data(following, "following.html")

except:
	print("")
	print("&&& Takip edilen listesi yüklenemedi!")

try:	
	upload_data(followers, "followers_1.html")

except:
	print("")
	print("&&& Takipçi listesi yüklenemedi!")

try:	
	upload_data(reqs, "recent_follow_requests.html")

except:
	print("")
	print("&&& Takip istekleri listesi yüklenemedi!")

try:
	upload_data(old_followers, "followers_2.html")

except:
	print("")
	print("&&& Eski takipçi listesi yüklenemedi!")

else:
	find(old_followers, followers, quitted)	

if(len(following) > 0 and len(followers) > 0):
	find(following, followers, fames)

if(len(reqs) > 0 and len(following) > 0):
	find(reqs, following, denied)

show()
search_denied()