import requests

url = 'https://mooc.lenovo.com'

user_agent=r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'

headers = {'User-Agent': user_agent, 'Connection': 'keep-alive'}

cookies = dict(
        s_fid='3694BD7F2F9EE338-2C1D7F78853DC140', s_vi='[CS]v1|2E450D34050329BD-6000118480049350[CE]',
        ldapinfo='true', _ga='GA1.2.1515804974.1555487355', _gid='GA1.2.2079571833.1557026251', 
        wordpress_test_cookie='WP+Cookie+check', 
        wordpress_logged_in_54f986524cf2aaa424224f0fed313d77='wuzy15%7C1588735052%7CTngpTtn0ADouxnxvWoZIaF93V3Vwzj0vxFuJWFSgGps%7C2c5bb7efe5419d5159e3c85c6b68fecde7a05ed0a1e635c08b909f740898fbae', 
        PHPSESSID='em7dhmdk1hbm4gni4v79rfqo93'
        )

rsp=requests.get(url, cookies=cookies, headers=headers)

print(rsp.content)