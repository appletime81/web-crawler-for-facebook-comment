import requests
from bs4 import BeautifulSoup

cookie = 'sb=JdxVYfDT_3yIIkhcN-cKE-XU; datr=JtxVYdYxZKZXch3QBOopEbjm; c_user=100003824025972; xs=45:1C19lPi6Fkr99A:2:1633016871:-1:11327::AcWQEV2gLlYJ17zqf_OMTboS8Z4Hqd_knOogmJObHw; fr=0OGcRbuDEKBEuiLaR.AWUaswMpcuRaJ2s_oAYwkW_-Lfg.BhaSGF.b4.AAA.0.0.BhaSGF.AWUzkPqPq8o; spin=r.1004560766_b.trunk_t.1634279815_s.1_v.2_; dpr=1.100000023841858'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    'Connection': 'keep-alive',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cookie': cookie}
url = 'https://www.facebook.com/groups/999385510116409/?ref=share'
html = requests.get(url, headers=header)
html.encoding = 'UTF-8'
sp = BeautifulSoup(html.text, 'html.parser')
print(sp.select('#facebook'))

