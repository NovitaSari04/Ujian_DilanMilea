# Jarak Dilan Milea
'''
Dilan:
Lokasi : Green Office Park 9
Kelurahan : Sampora
Kecamatan : Cisauk
Kabupaten : Tangerang
Provinsi : Banten

Milea:
Lokasi : NextSPACE by UnionSPACE
Kelurahan : CITARUM
Kecamatan : Bandung Wetan
Kota : Bandung
Provinsi : Jawa Barat
'''
import requests
import json

provDilan = 'Banten'
provMilea = 'Jawa Barat'

url1 = 'http://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/provinsi.json'
data1 = requests.get(url1)
hasil1 = data1.json()

noDilan = hasil1 [provDilan]
noMilea = hasil1 [provMilea]

url2 = 'https://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/kodepos.json'
data2 = requests.get(url2)
hasil2 = data2.json()

dilan = {'kelurahan':'SAMPORA',
'kecamatan':'CISAUK',
'kabupaten': 'TANGERANG',
'provinsi' : 'BANTEN'}

milea = {'kelurahan' : 'CITARUM',
'kecamatan' : 'BANDUNG WETAN',
'kabupaten':'BANDUNG',
'provinsi' : 'JAWA BARAT'}

for i in range (hasil2):
    if dilan['kelurahan'] == hasil2 ['Urban']:
        kodeDilan = hasil2 ['postal_code']
    if milea['kelurahan'] == hasil2 ['Urban']:
        kodeMilea = hasil2 ['postal_code'] 

apikey = '4so5q9zrJyhfJHCqYpmlZWVZBn5ocQTcQ9wMmtGPZk7nTiFTum5zyKb3JiLcEZPH'
url3 = 'https://www.zipcodeapi.com/rest/{apikey}/distance.json/{kodeDilan}/{kodeMilea}/km'
data3 = requests.get(url3)

jarak = data3.json()

print(f'Kode pos lokasi Dilan adalah {kodeDilan}')
print(f'Kode pos lokasi Milea adalah {kodeMilea}')
print(f'Jarak Dilan & Milea adalah {jarak} km')