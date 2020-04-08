# Soal 3 - Jarak Dilan Milea
import requests

# Data Dilan
dilan = {
    'kelurahan':'SAMPORA',
    'kecamatan':'CISAUK',
    'kabupaten':'TANGERANG',
    'provinsi':'BANTEN'
}

# Data Milea
milea = {
    'kelurahan':'CITARUM',
    'kecamatan':'BANDUNG WETAN',
    'kabupaten':'BANDUNG',
    'provinsi':'JAWA BARAT'
}

# Mencari kode provinsi BANTEN dan JAWA BARAT
url_kodeprov = 'https://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/provinsi.json'
data_kodeprov = requests.get(url_kodeprov)

kodeprov = data_kodeprov.json()
kodeprov_keys = kodeprov.keys()
kodeprov_values = kodeprov.values()
kodeprov_dict = dict(zip(kodeprov_values, kodeprov_keys))

kodeprov_dilan = kodeprov_dict[dilan['provinsi']]
kodeprov_milea = kodeprov_dict[milea['provinsi']]

# Mencari kode pos Dilan dan Milea
url_kodepos = 'http://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/kodepos.json'
data_kodepos = requests.get(url_kodepos)

kodepos = data_kodepos.json()
# kodepos_dilan = kodepos[kodeprov_dilan]
# kodepos_milea = kodepos[kodeprov_milea]

for i in kodepos[kodeprov_dilan] :
    if i['urban'] == dilan['kelurahan'] and i["sub_district"] == dilan['kecamatan'] and i["city"] == dilan['kabupaten'] :
        kodepos_dilan = i["postal_code"]

for i in kodepos[kodeprov_milea] :
    if i['urban'] == milea['kelurahan'] and i["sub_district"] == milea['kecamatan'] and i["city"] == milea['kabupaten'] :
        kodepos_milea = i["postal_code"]

# Menentukan jarak Dilan dan Milea
apikey ='9mkHDVaN6FSy48k6Govz8DU619IdmJloCCUpISJ6ZbZZMiHbAG7uH9LhAad9ROqC'
url_jarak = f'http://www.zipcodeapi.com/rest/{apikey}/distance.json/{kodepos_dilan}/{kodepos_milea}/km'
data_jarak =  requests.get(url_jarak)
jarak = data_jarak.json()

print(f"Kode Pos lokasi Dilan adalah {kodepos_dilan}")
print(f"Kode Pos lokasi Milea adalah {kodepos_milea}")
print(f"Jarak Dilan & Milea adalah {jarak['distance']} km")