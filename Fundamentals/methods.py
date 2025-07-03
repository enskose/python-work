# methods: nesnelere ait olan fonksiyonlardır 

fam = ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]

fam.index('mom') # fam listesi için index() methodunu çağırıp 'mom' değerinin index numarasını öğreniyoruz. çıktı: 4
fam.count(1.73) # 1.73 değerinden sadece 1 tane olduğu için çıktı: 1

sister = 'liz'
sister.capitalize() # ilk harfini büyük yazar
sister.replace('z', 'sa') # 'z' harfini 'sa' ile değiştirerek 'Liz' = 'Lisa' oldu

# bazı methodlar çağrıldıkları nesneleri değiştirirler

fam = ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]
fam.append('me')
fam.append(1.48)
fam.reverse()

print(fam)

