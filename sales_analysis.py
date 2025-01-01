import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
aylar = ['Ocak','Şubat','Mart','Nisan','Mayıs','Haziran',
         'Temmuz','Ağustos','Eylül','Ekim','Kasım','Aralık']
urun_a = np.random.randint(1000,5000,12)
urun_b = np.random.randint(2000,6000,12)
urun_c = np.random.randint(3000,7000,12)

veri = pd.DataFrame({
    'Ay': aylar,
    'Ürün A': urun_a,
    'Ürün B': urun_b,
    'Ürün C': urun_c
})
##########################
print("Satış İstatistikleri:")
print("\nOrtalama Satışlar:")
print(veri[['Ürün A','Ürün B','Ürün C']].mean())
print("\nMaksimum Satışlar:")
print(veri[['Ürün A','Ürün B','Ürün C']].max())
##########################
plt.figure(figsize=(12, 6))
plt.plot(veri['Ay'], veri['Ürün A'], marker='o', label='Ürün A')
plt.plot(veri['Ay'], veri['Ürün B'], marker='s', label='Ürün B')
plt.plot(veri['Ay'], veri['Ürün C'], marker='^', label='Ürün C')

plt.title('Tablo 1:Aylık Ürün Satışları')
plt.xlabel('Aylar')
plt.ylabel('Satış Miktarı')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.figure(figsize=(8, 8))
toplam_satislar = veri[['Ürün A','Ürün B','Ürün C']].sum()
plt.pie(toplam_satislar, labels=toplam_satislar.index, autopct='%1.1f%%')
plt.title('Tablo 2:Toplam Satışların Ürünlere Göre Dağılımı')
plt.tight_layout()
plt.show()
##########################
print("\nÜrünler Arası Korelasyon:")
print(veri[['Ürün A','Ürün B','Ürün C']].corr())
veri['Toplam Satış'] = veri[['Ürün A','Ürün B','Ürün C']].sum(axis=1)
print("\nEn Yüksek Satış Yapılan 3 Ay:")
print(veri[['Ay','Toplam Satış']].nlargest(3,'Toplam Satış'))
