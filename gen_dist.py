import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# ── Singapore-radial distances (nm) — cross-Malacca formula: da+db-180 ────────
sg = {
  'spore':0,'port_klang':160,'penang':560,'kuantan':310,'kemaman':380,
  'pasir_gudang':30,'tanjung_manis':650,'bintulu':750,'miri':850,
  'kuching':680,'labuan':1050,'kota_kinabalu':1100,'sandakan':1200,
  'lahad_datu':1260,'tawau':1360,
  'bangkok':900,'laem_chabang':830,'map_ta_phut':820,'songkhla':420,
  'sihanoukville':720,
  'ho_chi_minh':580,'vung_tau':600,'phu_my':600,
  'danang':1100,'quynhon':1050,'dung_quat':1080,
  'nghi_son':1620,'cailan':1550,'cam_pha':1750,'haiphong':1700,
  'yangon':1200,
  'belawan':650,'lhokseumawe':760,'dumai':230,'palembang':380,'panjang':350,
  'ciwandan':490,'jakarta':520,'semarang':760,'cilacap':800,
  'surabaya':820,'gresik':840,'tuban':860,'probolinggo':900,
  'banjarmasin':850,'tarjun':870,'taboneo':900,'muara_pantai':910,
  'balikpapan':1050,'samarinda':1100,'bontang':1150,
  'makassar':950,'morowali':1250,'kendari':1300,'pomalaa':1250,
  'manila':1350,'subic':1330,'batangas':1340,'limay':1320,'sual':1400,
  'cebu':1500,'iloilo':1500,'cdo':1400,'davao':1350,'gensan':1280,'zamboanga':1150,
  'guangzhou':1550,'hong_kong':1450,'shenzhen':1470,'zhanjiang':1350,
  'beihai':1280,'qinzhou':1260,'fangcheng':1250,'xiamen':1700,
  'quanzhou':1750,'fuzhou':1800,'wenzhou':1950,
  'ningbo':2200,'nantong':2320,'nanjing':2380,'shanghai':2280,
  'lianyungang':2400,'rizhao':2480,'qingdao':2550,'yantai':2680,
  'tianjin':2790,'dalian':2850,
  'kaohsiung':1600,'taichung':1750,'keelung':1870,'taipei':1870,'suao':1890,
  'busan':2640,'gwangyang':2600,'ulsan':2660,'pohang':2680,'incheon':2850,
  'hakata':2700,'kitakyushu':2720,'hiroshima':2800,'oita':2750,
  'mizushima':2820,'osaka':2880,'kobe':2880,'nagoya':2920,
  'yokohama':2950,'chiba':2960,'kawasaki':2960,'shimizu':2960,
  'kashima':2980,'niigata':3100,'muroran':3300,
  # Indian Ocean side
  'colombo':1500,'chennai':1750,'tuticorin':1750,'kakinada':1780,'vizag':1800,
  'paradip':1900,'haldia':2050,'cochin':1900,'mormugao':2350,'mangalore':2350,
  'nhava_sheva':3200,'mundra':3100,'kandla':3050,'pipavav':3350,'hazira':3300,'okha':3450,
  'chittagong':2200,'karachi':3500,'port_qasim':3500,
  'dubai':3400,'sohar':3300,'dammam':3600,'bandar_abbas':3650,'jubail':3900,
  'djibouti':3350,'salalah':2800,'jeddah':4400,'yanbu':4600,
  'sokhna':5100,'aqaba':5300,'haifa':5800,'alexandria':7000,
  'piraeus':8500,'valencia':9200,'marseille':9300,'algeciras':9700,
  'genoa':9500,'istanbul':9000,'rotterdam':9800,'antwerp':9900,'hamburg':10100,
  'constanta':9900,'novorossiysk':10100,'istanbul_marm':9200,
  'mombasa':3900,'dar_es_salaam':4100,'nacala':4700,'beira':5000,
  'maputo':5200,'durban':5800,'walvis_bay':7000,'cape_town':6800,
  'tema':8300,'abidjan':8200,'dakar':9000,'lagos':8500,
  'houston':11500,'new_orleans':11700,'baltimore':11200,'savannah':11000,'santos':10800,
  'long_beach':8700,'oakland':8700,'seattle':8500,'vancouver':8500,
  'ensenada':8600,'guaymas':9200,'la_paz':9100,
  'callao':13500,'iquique':13800,'san_antonio':14200,
  'fremantle':1800,'port_hedland':1600,'dampier':1600,
  'gladstone':3200,'newcastle_au':3500,'brisbane':3400,
}

EAST_ASIA = {
  'guangzhou','hong_kong','shenzhen','zhanjiang','beihai','qinzhou','fangcheng',
  'xiamen','quanzhou','fuzhou','wenzhou','ningbo','nantong','nanjing','shanghai',
  'lianyungang','rizhao','qingdao','yantai','tianjin','dalian',
  'kaohsiung','taichung','keelung','taipei','suao',
  'busan','gwangyang','ulsan','pohang','incheon',
  'hakata','kitakyushu','hiroshima','oita','mizushima','osaka','kobe','nagoya',
  'yokohama','chiba','kawasaki','shimizu','kashima','niigata','muroran',
  'manila','subic','batangas','limay','sual','cebu','iloilo','cdo','davao','gensan','zamboanga',
  'bangkok','laem_chabang','map_ta_phut','songkhla','sihanoukville',
  'ho_chi_minh','vung_tau','phu_my','danang','quynhon','dung_quat',
  'nghi_son','cailan','cam_pha','haiphong','yangon',
  'spore','port_klang','penang','kuantan','kemaman','pasir_gudang',
  'tanjung_manis','bintulu','miri','kuching','labuan','kota_kinabalu',
  'sandakan','lahad_datu','tawau',
  'belawan','lhokseumawe','dumai','palembang','panjang',
  'ciwandan','jakarta','semarang','cilacap','surabaya','gresik','tuban','probolinggo',
  'banjarmasin','tarjun','taboneo','muara_pantai','balikpapan','samarinda','bontang',
  'makassar','morowali','kendari','pomalaa',
}

EXACT = {}
def add(a,b,d): EXACT[(a,b)]=d; EXACT[(b,a)]=d

# ── NETPAS verified ──────────────────────────────────────────────────────────
add('tianjin','chennai',4361)
add('cailan','tanjung_manis',1175)

# ── SE Asia intra ─────────────────────────────────────────────────────────────
add('spore','port_klang',160); add('spore','penang',560); add('spore','kuantan',310)
add('spore','kemaman',380); add('spore','pasir_gudang',30); add('spore','tanjung_manis',650)
add('spore','bintulu',750); add('spore','miri',850); add('spore','kuching',680)
add('spore','labuan',1050); add('spore','kota_kinabalu',1100); add('spore','sandakan',1200)
add('spore','lahad_datu',1260); add('spore','tawau',1360)
add('spore','songkhla',420); add('spore','sihanoukville',720); add('spore','yangon',1200)
add('spore','laem_chabang',830); add('spore','map_ta_phut',820); add('spore','bangkok',900)
add('spore','ho_chi_minh',580); add('spore','vung_tau',600); add('spore','phu_my',600)
add('spore','danang',1100); add('spore','quynhon',1050); add('spore','dung_quat',1080)
add('spore','nghi_son',1620); add('spore','cailan',1550); add('spore','cam_pha',1750)
add('spore','haiphong',1700)
add('spore','belawan',650); add('spore','lhokseumawe',760); add('spore','dumai',230)
add('spore','palembang',380); add('spore','panjang',350); add('spore','ciwandan',490)
add('spore','jakarta',520); add('spore','semarang',760); add('spore','cilacap',800)
add('spore','surabaya',820); add('spore','gresik',840); add('spore','tuban',860)
add('spore','probolinggo',900)
add('spore','banjarmasin',850); add('spore','tarjun',870); add('spore','taboneo',900)
add('spore','muara_pantai',910); add('spore','balikpapan',1050); add('spore','samarinda',1100)
add('spore','bontang',1150); add('spore','makassar',950); add('spore','morowali',1250)
add('spore','kendari',1300); add('spore','pomalaa',1250)
add('spore','manila',1350); add('spore','subic',1330); add('spore','batangas',1340)
add('spore','limay',1320); add('spore','sual',1400); add('spore','cebu',1500)
add('spore','iloilo',1500); add('spore','cdo',1400); add('spore','davao',1350)
add('spore','gensan',1280); add('spore','zamboanga',1150)

# Bangkok (corrected)
add('bangkok','ho_chi_minh',830); add('bangkok','laem_chabang',80)
add('bangkok','map_ta_phut',100); add('bangkok','songkhla',480)
add('bangkok','sihanoukville',280); add('bangkok','jakarta',1700)
add('bangkok','surabaya',1820); add('bangkok','cailan',1550)
add('bangkok','haiphong',1750); add('bangkok','danang',1280)
add('bangkok','manila',1680); add('bangkok','port_klang',740); add('bangkok','penang',580)
add('bangkok','shanghai',2200)

# HCM (corrected)
add('ho_chi_minh','jakarta',1100); add('ho_chi_minh','surabaya',1450)
add('ho_chi_minh','danang',560); add('ho_chi_minh','quynhon',500)
add('ho_chi_minh','dung_quat',540); add('ho_chi_minh','vung_tau',30)
add('ho_chi_minh','phu_my',25); add('ho_chi_minh','nghi_son',1050)
add('ho_chi_minh','cailan',870); add('ho_chi_minh','haiphong',1100)
add('ho_chi_minh','cam_pha',1150); add('ho_chi_minh','manila',1050)
add('ho_chi_minh','sihanoukville',140)
add('ho_chi_minh','port_klang',430); add('ho_chi_minh','penang',750)

# Vietnam coast
add('cailan','haiphong',110); add('cailan','cam_pha',160); add('cailan','nghi_son',400)
add('cailan','danang',720); add('cailan','quynhon',860); add('cailan','dung_quat',840)
add('haiphong','cam_pha',90); add('haiphong','nghi_son',310)
add('danang','quynhon',180); add('danang','dung_quat',120)
add('nghi_son','danang',420); add('quynhon','dung_quat',60)

# Malaysia E-coast
add('kuantan','kemaman',70); add('kuantan','tanjung_manis',350)
add('kemaman','tanjung_manis',290); add('tanjung_manis','bintulu',120)
add('bintulu','miri',120); add('miri','labuan',220); add('labuan','kota_kinabalu',40)
add('kota_kinabalu','sandakan',180); add('sandakan','lahad_datu',120); add('lahad_datu','tawau',110)

# Indonesia intra
add('jakarta','ciwandan',30); add('jakarta','semarang',250); add('jakarta','surabaya',300)
add('jakarta','banjarmasin',650); add('jakarta','balikpapan',780); add('jakarta','makassar',750)
add('surabaya','semarang',200); add('surabaya','gresik',20); add('surabaya','tuban',80)
add('surabaya','probolinggo',80); add('surabaya','makassar',500); add('surabaya','bontang',800)
add('surabaya','banjarmasin',350)
add('makassar','bontang',500); add('makassar','kendari',300); add('makassar','morowali',350)
add('makassar','pomalaa',280)
add('balikpapan','samarinda',70); add('balikpapan','bontang',200); add('balikpapan','banjarmasin',400)
add('banjarmasin','tarjun',60); add('banjarmasin','taboneo',70); add('banjarmasin','muara_pantai',80)
add('belawan','lhokseumawe',200); add('belawan','penang',150)
add('panjang','ciwandan',200); add('palembang','panjang',120)
add('cilacap','jakarta',350); add('cilacap','surabaya',270)

# Philippines intra
add('manila','subic',50); add('manila','batangas',60); add('manila','limay',60)
add('manila','sual',170); add('manila','cebu',320); add('manila','iloilo',340)
add('manila','cdo',450); add('manila','davao',560); add('manila','gensan',580)
add('manila','zamboanga',480)
add('cebu','iloilo',120); add('cebu','cdo',130); add('cebu','davao',350)
add('cebu','gensan',360); add('davao','gensan',60); add('davao','zamboanga',280)
add('zamboanga','gensan',200)

# ── China coast ───────────────────────────────────────────────────────────────
add('tianjin','dalian',200); add('tianjin','qingdao',220); add('tianjin','yantai',280)
add('tianjin','incheon',350); add('tianjin','busan',680)
add('dalian','qingdao',240); add('dalian','yantai',100); add('dalian','incheon',300)
add('dalian','busan',600)
add('qingdao','rizhao',80); add('qingdao','lianyungang',200); add('qingdao','yantai',130)
add('qingdao','shanghai',350); add('qingdao','incheon',320); add('qingdao','busan',450)
add('rizhao','lianyungang',120); add('lianyungang','shanghai',160)
add('shanghai','nantong',40); add('shanghai','nanjing',200); add('shanghai','ningbo',90)
add('shanghai','wenzhou',320); add('shanghai','fuzhou',480); add('shanghai','xiamen',660)
add('shanghai','guangzhou',900); add('shanghai','busan',520); add('shanghai','incheon',500)
add('ningbo','wenzhou',140); add('wenzhou','fuzhou',200); add('fuzhou','quanzhou',80)
add('quanzhou','xiamen',80); add('xiamen','shenzhen',290); add('xiamen','hong_kong',270)
add('xiamen','guangzhou',300); add('xiamen','fuzhou',120)
add('guangzhou','shenzhen',70); add('guangzhou','hong_kong',100); add('guangzhou','zhanjiang',300)
add('guangzhou','beihai',550); add('guangzhou','qinzhou',560); add('guangzhou','fangcheng',580)
add('zhanjiang','beihai',280); add('beihai','qinzhou',30); add('qinzhou','fangcheng',30)
add('shenzhen','hong_kong',40)

# China ↔ Taiwan
add('guangzhou','kaohsiung',330); add('hong_kong','kaohsiung',280)
add('xiamen','kaohsiung',175); add('fuzhou','kaohsiung',250); add('fuzhou','keelung',300)
add('wenzhou','keelung',380); add('ningbo','keelung',420); add('ningbo','kaohsiung',480)
add('shanghai','kaohsiung',700); add('shanghai','keelung',620); add('shanghai','taichung',660)
add('qingdao','kaohsiung',900); add('qingdao','keelung',820)
add('tianjin','kaohsiung',1200); add('tianjin','keelung',1100)
add('dalian','kaohsiung',1250); add('dalian','keelung',1150)

# Taiwan intra
add('kaohsiung','taichung',160); add('kaohsiung','keelung',280); add('kaohsiung','suao',300)
add('taichung','keelung',130); add('keelung','suao',30); add('taipei','keelung',10)

# China/Taiwan ↔ Philippines
add('guangzhou','manila',600); add('hong_kong','manila',500); add('xiamen','manila',680)
add('kaohsiung','manila',550); add('keelung','manila',700)
add('shanghai','manila',1200); add('qingdao','manila',1450)

# China ↔ Korea/Japan
add('guangzhou','busan',1200); add('hong_kong','busan',1050)
add('guangzhou','incheon',1400); add('guangzhou','yokohama',2200)
add('shanghai','yokohama',1050); add('qingdao','yokohama',1200)
add('tianjin','yokohama',1350); add('dalian','yokohama',1300)
add('shanghai','osaka',980); add('qingdao','osaka',1100); add('guangzhou','osaka',1680)
add('hong_kong','yokohama',1800); add('hong_kong','osaka',1700)

# Korea intra / Korea-Japan
add('busan','gwangyang',80); add('busan','ulsan',55); add('busan','pohang',80)
add('busan','incheon',320); add('gwangyang','incheon',350)
add('ulsan','pohang',35); add('pohang','incheon',360)
add('busan','hakata',120); add('busan','kitakyushu',130); add('busan','hiroshima',230)
add('busan','osaka',380); add('busan','yokohama',680)
add('incheon','hakata',300); add('incheon','osaka',580); add('incheon','yokohama',820)

# Japan intra
add('hakata','kitakyushu',30); add('hakata','oita',80); add('hakata','hiroshima',150)
add('hakata','mizushima',190); add('hakata','osaka',310); add('hakata','kobe',310)
add('oita','hiroshima',150); add('oita','mizushima',130)
add('hiroshima','mizushima',60); add('hiroshima','osaka',260); add('hiroshima','kobe',260)
add('mizushima','osaka',200); add('osaka','kobe',25); add('osaka','nagoya',160)
add('nagoya','yokohama',180); add('yokohama','chiba',30); add('yokohama','kawasaki',20)
add('yokohama','shimizu',90); add('yokohama','kashima',100)
add('yokohama','niigata',500); add('yokohama','muroran',680)
add('niigata','muroran',300); add('muroran','hakata',800)
add('hakata','kaohsiung',600); add('osaka','kaohsiung',950)
add('yokohama','kaohsiung',1150); add('yokohama','keelung',1050)
add('hakata','manila',1550); add('osaka','manila',1550); add('yokohama','manila',1700)

# ── Indian Ocean intra (non-cross-Malacca pairs) ─────────────────────────────
# Reference anchor values from existing table:
# colombo: rotterdam=7500,hamburg=7800,houston=10200,baltimore=9900,santos=9500
#          dubai=1560,dammam=1760,sohar=1460,salalah=1200
#          mombasa=1900,dar_es_salaam=2100,lagos=6500,durban=4300
# nhava_sheva: rotterdam=6880,hamburg=7180,houston=9580,baltimore=9280,santos=8880
#              dubai=880,dammam=1080,sohar=780,salalah=1230
# chittagong: rotterdam=8300,hamburg=8600,houston=10800,baltimore=10500,santos=10100
#             dubai=2160,dammam=2360,sohar=2060,salalah=2000

# India East coast (Bay of Bengal, routes to West go around Sri Lanka tip ~+300nm vs Colombo)
_col = { # colombo distances to W destinations
  'rotterdam':7500,'antwerp':7600,'hamburg':7800,'genoa':7200,'istanbul':6700,
  'piraeus':6900,'houston':10200,'new_orleans':10400,'baltimore':9900,'savannah':9700,
  'santos':9500,'lagos':6500,'durban':4300,'mombasa':1900,'dar_es_salaam':2100,
  'dubai':1560,'dammam':1760,'sohar':1460,'salalah':1200,
  'jeddah':2700,'yanbu':2900,'djibouti':1700,'sokhna':4100,'aqaba':4300,
  'haifa':4800,'alexandria':5400,'walvis_bay':5900,'cape_town':5600,
  'tema':5600,'abidjan':5500,'dakar':6300,
}
for port,delta in [('chennai',300),('tuticorin',200),('kakinada',350),
                    ('vizag',400),('paradip',500),('haldia',650)]:
  for dest,base in _col.items():
    add(port,dest,base+delta)
# India East coast intra
add('colombo','chennai',300); add('colombo','tuticorin',200); add('colombo','cochin',500)
add('colombo','mormugao',900); add('colombo','mangalore',950)
add('chennai','tuticorin',130); add('chennai','cochin',680)
add('chennai','vizag',350); add('chennai','kakinada',380); add('chennai','paradip',450)
add('chennai','haldia',600); add('chittagong','haldia',300); add('chittagong','paradip',350)
add('vizag','kakinada',50); add('vizag','paradip',160); add('vizag','haldia',310)
add('paradip','haldia',160); add('kakinada','paradip',130)

# India West coast (closer to Suez, distances to Europe shorter than Colombo)
_nh = { # nhava_sheva distances
  'rotterdam':6880,'antwerp':6980,'hamburg':7180,'genoa':6580,'istanbul':6080,
  'piraeus':6280,'houston':9580,'new_orleans':9780,'baltimore':9280,'savannah':9080,
  'santos':8880,'lagos':6880,'durban':4680,'mombasa':2280,'dar_es_salaam':2480,
  'dubai':880,'dammam':1080,'sohar':780,'salalah':1230,
  'jeddah':2100,'yanbu':2300,'djibouti':1600,'sokhna':3600,'aqaba':3800,
  'haifa':4300,'alexandria':4900,'walvis_bay':5500,'cape_town':5200,
  'tema':6800,'abidjan':6700,'dakar':7500,'colombo':780,
}
for port,delta in [('cochin',200),('mormugao',-100),('mangalore',-100),
                    ('pipavav',-200),('hazira',-250),('okha',-300)]:
  for dest,base in _nh.items():
    add(port,dest,base+delta)
add('cochin','mormugao',280); add('cochin','mangalore',200); add('cochin','tuticorin',180)
add('mormugao','mangalore',80); add('mangalore','nhava_sheva',850)
add('pipavav','nhava_sheva',250); add('hazira','nhava_sheva',200)
add('okha','nhava_sheva',400); add('pipavav','mundra',80); add('hazira','mundra',150)

# Pakistan
for dest,base in _nh.items():
  add('karachi',dest,base+600)
  add('port_qasim',dest,base+600)
add('karachi','port_qasim',20); add('karachi','nhava_sheva',600)
add('karachi','mundra',550); add('karachi','kandla',500)
add('karachi','dubai',400); add('karachi','dammam',600)
add('karachi','sohar',300); add('karachi','salalah',800); add('karachi','bandar_abbas',350)

# Gulf extras
add('bandar_abbas','dubai',50); add('bandar_abbas','dammam',200)
add('bandar_abbas','sohar',130); add('bandar_abbas','jubail',300)
add('jubail','dammam',80); add('jubail','sohar',700); add('jubail','dubai',500)
for dest,base in _nh.items():
  add('bandar_abbas',dest,base+750)
  add('jubail',dest,base+900)

# Red Sea / Gulf of Aden
add('djibouti','jeddah',750); add('djibouti','salalah',500)
add('djibouti','sokhna',1750); add('djibouti','aqaba',1950)
add('jeddah','yanbu',200); add('jeddah','sokhna',1000); add('jeddah','aqaba',1200)
add('jeddah','haifa',1700); add('jeddah','alexandria',2300)
add('jeddah','rotterdam',4200); add('jeddah','hamburg',4500)
add('jeddah','houston',7400); add('jeddah','santos',7200)
add('yanbu','sokhna',800); add('sokhna','aqaba',200); add('aqaba','haifa',500)
add('sokhna','piraeus',1600); add('sokhna','istanbul',2000); add('sokhna','genoa',2200)
add('sokhna','rotterdam',4000); add('sokhna','hamburg',4300)
add('haifa','piraeus',950); add('haifa','istanbul',800); add('haifa','alexandria',400)
add('haifa','genoa',1600); add('haifa','rotterdam',4400); add('haifa','hamburg',4700)
add('alexandria','piraeus',500); add('alexandria','istanbul',750)
add('alexandria','genoa',1700); add('alexandria','rotterdam',3900)

# Med internal
add('piraeus','istanbul',400); add('piraeus','genoa',1100)
add('piraeus','valencia',1700); add('piraeus','marseille',1400)
add('piraeus','algeciras',2200); add('piraeus','rotterdam',3600)
add('piraeus','hamburg',3900); add('piraeus','antwerp',3650)
add('istanbul','genoa',1400); add('istanbul','rotterdam',3800)
add('istanbul','hamburg',4100); add('istanbul','antwerp',3850)
add('genoa','rotterdam',1800); add('genoa','hamburg',2000)
add('genoa','valencia',600); add('genoa','marseille',200)
add('genoa','algeciras',1400); add('genoa','antwerp',1900)
add('valencia','algeciras',600); add('marseille','algeciras',800)
add('algeciras','rotterdam',1400); add('algeciras','hamburg',1700)
add('algeciras','antwerp',1450)

# Black Sea
add('constanta','istanbul_marm',300); add('novorossiysk','istanbul_marm',500)
add('constanta','novorossiysk',250)
add('constanta','rotterdam',4100); add('constanta','hamburg',4400)
add('novorossiysk','rotterdam',4400); add('novorossiysk','hamburg',4700)
add('istanbul_marm','rotterdam',3800); add('istanbul_marm','hamburg',4100)
add('istanbul_marm','piraeus',350)

# Africa intra
add('mombasa','dar_es_salaam',200); add('mombasa','nacala',800)
add('mombasa','beira',1100); add('mombasa','maputo',1300); add('mombasa','durban',1500)
add('dar_es_salaam','nacala',600); add('dar_es_salaam','beira',900)
add('dar_es_salaam','maputo',1100); add('dar_es_salaam','durban',1300)
add('nacala','beira',350); add('nacala','maputo',550); add('nacala','durban',900)
add('beira','maputo',250); add('beira','durban',650); add('maputo','durban',450)
add('durban','cape_town',900); add('durban','walvis_bay',1500)
add('cape_town','walvis_bay',700)
for dest,base in [('rotterdam',6400),('hamburg',6700),('houston',8100),('santos',4800)]:
  add('durban',dest,base)
add('durban','lagos',5000); add('durban','tema',4800)
for dest,base in [('rotterdam',6200),('houston',8000),('santos',5500)]:
  add('cape_town',dest,base+600)
add('nacala','rotterdam',7500); add('beira','rotterdam',7300)
add('maputo','rotterdam',7000); add('nacala','durban',900)
for dest,base in [('rotterdam',4500),('antwerp',4600),('hamburg',4800)]:
  add('lagos',dest,base)
add('tema','rotterdam',4400); add('tema','hamburg',4700); add('tema','lagos',250)
add('abidjan','lagos',400); add('abidjan','tema',150)
add('abidjan','rotterdam',4500); add('dakar','rotterdam',3400)
add('walvis_bay','rotterdam',5600); add('walvis_bay','cape_town',700)

# Americas
add('savannah','houston',1100); add('savannah','new_orleans',800)
add('savannah','baltimore',800); add('savannah','santos',4200)
add('savannah','rotterdam',4000); add('savannah','hamburg',4300)
add('long_beach','seattle',1200); add('long_beach','vancouver',1300)
add('long_beach','oakland',400); add('long_beach','ensenada',150)
add('long_beach','guaymas',1000); add('long_beach','la_paz',950)
add('long_beach','callao',3800); add('long_beach','iquique',4100)
add('long_beach','san_antonio',4500); add('long_beach','houston',1900)
add('callao','iquique',350); add('callao','san_antonio',950); add('iquique','san_antonio',600)
add('ensenada','guaymas',700); add('guaymas','la_paz',400)

# Australia intra
add('fremantle','port_hedland',400); add('fremantle','dampier',420)
add('port_hedland','dampier',50); add('port_hedland','gladstone',2000)
add('dampier','gladstone',2000); add('gladstone','newcastle_au',400)
add('gladstone','brisbane',280); add('newcastle_au','brisbane',160)
add('fremantle','singapore',1800); add('port_hedland','spore',1600)
# Australia to key Western ports
add('fremantle','rotterdam',12000); add('fremantle','houston',11500)
add('fremantle','dubai',6000); add('fremantle','nhava_sheva',5100)
add('newcastle_au','rotterdam',13200); add('newcastle_au','houston',12800)
add('gladstone','rotterdam',12800)

# ── Cross-Malacca formula ─────────────────────────────────────────────────────
def is_cross(a,b): return (a in EAST_ASIA) != (b in EAST_ASIA)

def cdist(a,b):
    if a==b: return 0
    k=(a,b); rk=(b,a)
    if k in EXACT: return EXACT[k]
    if rk in EXACT: return EXACT[rk]
    da,db = sg.get(a),sg.get(b)
    if da is None or db is None: return None
    if not is_cross(a,b): return None
    return round(da+db-180)

# ── Emit rows ─────────────────────────────────────────────────────────────────
NEW_PORTS = [
  'tianjin','dalian','ningbo','lianyungang','nanjing','nantong','wenzhou',
  'xiamen','shenzhen','hong_kong','zhanjiang','fangcheng','qinzhou','beihai',
  'fuzhou','quanzhou','rizhao','yantai',
  'kaohsiung','taichung','keelung','taipei','suao',
  'incheon','ulsan','pohang','gwangyang',
  'yokohama','nagoya','osaka','kobe','hiroshima','hakata','kitakyushu',
  'chiba','kashima','kawasaki','niigata','mizushima','oita','muroran','shimizu',
  'haiphong','danang','quynhon','dung_quat','nghi_son','cam_pha','phu_my','vung_tau',
  'penang','kuantan','kemaman','bintulu','miri','kuching',
  'labuan','kota_kinabalu','sandakan','lahad_datu','tawau',
  'laem_chabang','map_ta_phut','songkhla','sihanoukville','yangon',
  'cebu','davao','batangas','gensan','cdo','iloilo','subic','limay','sual','zamboanga',
  'semarang','makassar','banjarmasin','balikpapan','samarinda','cilacap',
  'gresik','tuban','probolinggo','ciwandan','panjang',
  'belawan','lhokseumawe','dumai','morowali','kendari','pomalaa',
  'bontang','tarjun','palembang','taboneo','muara_pantai',
  'chennai','tuticorin','vizag','kakinada','paradip','haldia',
  'cochin','mormugao','mangalore','pipavav','hazira','okha',
  'karachi','port_qasim','bandar_abbas','jubail',
  'jeddah','yanbu','djibouti','sokhna','aqaba','haifa','alexandria',
  'piraeus','valencia','marseille','algeciras',
  'nacala','beira','maputo','walvis_bay','cape_town','tema','abidjan','dakar',
  'savannah','long_beach','oakland','seattle','vancouver',
  'callao','iquique','san_antonio','ensenada','guaymas','la_paz',
  'fremantle','port_hedland','dampier','gladstone','newcastle_au','brisbane',
  'constanta','novorossiysk','istanbul_marm',
]

ALL_COLS = sorted(sg.keys())

def emit_row(p):
    vals={}
    for c in ALL_COLS:
        if c==p: continue
        d=cdist(p,c)
        if d and d>0: vals[c]=d
    if not vals: return None
    return '  '+p+': { '+', '.join(f'{c}:{v}' for c,v in sorted(vals.items()))+' },'

for p in NEW_PORTS:
    r=emit_row(p)
    if r: print(r)
