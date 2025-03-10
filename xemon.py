import os,sys,re,time,json
import requests,bs4,string
import faker,fake_email,random
try:
    import rich, requests
except:
    os.system(" pip install rich requests ")
    import rich, requests
from faker import Faker
from fake_email import Email
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from datetime import datetime
from rich import print 
from rich.tree import Tree
from rich.panel import Panel
from rich.columns import Columns
from rich.console import Console
#---------------------------#
R="[bold red]"
G="[bold green]"
Y="[bold yellow]"
B="[bold blue]"
M="[bold magenta]"
P="[bold violet]"
C="[bold cyan]"
W="[bold white]"
r="\033[1;31m"
g="\033[1;32m"
y="\033[1;33m"
b="\033[1;34m"
m="\033[1;35m"
c="\033[1;36m"
w="\033[1;37m"
X=f"{G}[{W}+{G}]{W}"
#---------------------------#
live = 0
cp = 0
console = Console()
ua = UserAgent()
#---------------------------#
def linex():
    print(f"{W}———————————————————————————————")

def clear():
    os.system('clear')

from rich.panel import Panel
from rich import print

# Small Box-Style ASCII Logo
ascii_logo = """
[bold white]┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
[bold white]┃ [bold green]  ██████   █████  ██████  ██████  ██[bold white]   ┃
[bold white]┃ [bold green]  ██   ██ ██   ██ ██   ██ ██   ██ ██[bold white]   ┃
[bold white]┃ [bold green]  ██████  ███████ ██████  ██████  ██[bold white]   ┃
[bold white]┃ [bold green]  ██   ██ ██   ██ ██   ██ ██   ██ ██[bold white]   ┃
[bold white]┃ [bold green]  ██   ██ ██   ██ ██████  ██████  ██[bold white]   ┃
[bold white]┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""

# Compact Hacker-Style Panel
logo = Panel.fit(
    f"""{ascii_logo}

[bold green]● CREATOR   : CYBER Redwan [/bold green]  
[bold yellow]● FRAMEWORK : KILLER - BOSS[/bold yellow]  
[bold magenta]● FEATURES  : SECURE & FAST[/bold magenta]  
[bold red]● SECURITY  : AI-POWERED SHIELD[/bold red]  
[bold blue]● SPEED     : OPTIMIZED PERFORMANCE[/bold blue]  
[bold cyan]● COADER    :CYBER Redwan [/bold cyan]  
[bold green]⚠ AUTHORIZED USERS ONLY ⚠[/bold green]  
""",
    title="[bold yellow]⚡ KILLER TOOL - HACKER'S EDITION ⚡[/bold yellow]",
    subtitle="[bold magenta]★ ENGINEERED FOR DOMINANCE ★[/bold magenta]",
    border_style="red",
    padding=(1, 4)
)








def ugenX():
    ualist = [ua.random for _ in range(50)]
    return str(random.choice(ualist))

def fake_name():
    first = Faker().first_name()
    last = Faker().last_name()
    return first,last

import random

def fake_password():
    random_numbers = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    return f'Redwan{random_numbers}'

def extractor(data):
    try:
        soup = BeautifulSoup(data,"html.parser")
        data = {}
        for inputs in soup.find_all("input"):
            name = inputs.get("name")
            value = inputs.get("value")
            if name:
                data[name] = value
        return data
    except Exception as e:
        return {"error":str(e)}
def GetEmails():
    nam1 = random.choice(['eka','dwi','tri','budi','indah','dewi'])
    nam2 = random.choice(['nurhayati','handoko','setiyani','susanto','permata'])
    nam3 = random.choice(['triatmaja','siagian','manopo','jayaningrat','widodo'])
    name = f'{nam1}{nam2}{nam3}'
    domain = random.choice(['gmail.com','yahoo.com','hotmail.com','gonetor.com'])
    nu = str(random.randrange(10000, 100000))
    nope = f'{name}@{domain}'
    return nope
    
def GetBDNumber():
    prefixes = ['013', '014', '015', '016', '017', '018', '019']
    prefix = random.choice(prefixes)
    number = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    return f'{prefix}{number}'

def GetEmail():
    response = requests.post('https://api.internal.temp-mail.io/api/v3/email/new').json()
    return response['email']
    
    
def get_temp_plus():
	name = " ".join(fake_name()).replace(' ', '')
	jam = str(datetime.now().strftime("%X")).replace(':','')
	domain = random.choice(['fexbox.org','fexpost.com','fextemp.com','chitthi.in'])
	email = f'{name}.{jam}.{str(random.randrange(1000,10000))}@{domain}'
	return email
def get_code_temp_plus(email):
	mail = requests.Session()
	headers = {
			'User-Agent':'Temp%20Plus/30 CFNetwork/1220.1 Darwin/20.3.0',
			'Content-Type':'application/json',
			'Connection-type': 'wifi'
		}
	headers.update({'cookie': f'email={email}'})
	response = mail.get(f'https://tempmail.plus/api/mails', headers=headers)
	#print(response.json())
	if response.status_code == 200:
		req = response.json()
		mail_list = req.get("mail_list", [])
		if mail_list:
			subject = mail_list[0].get('subject', '')
			kode = re.search(r'(\d+)', subject)
			code = kode.group(1) if kode else 'Code not found'
			return code
		else:
			return 'not found'
	return None
	
import requests, re

def GetCode(email):
    try:
        h = {"authority":"api.internal.temp-mail.io","method":"GET","path":f"/api/v3/email/{self.email}/messages","scheme":"https","application-name":"web","sec-ch-ua-platform":"\"Android\"","application-version":"4.0.0","x-cors-header":"iaWg3pchvFx48fY","sec-ch-ua":"\"Not(A:Brand\";v=\"99\", \"Google Chrome\";v=\"133\", \"Chromium\";v=\"133\"","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Mobile Safari/537.36","dnt":"1","content-type":"application/json","accept":"*/*","origin":"https://temp-mail.io","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://temp-mail.io/","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-GB,en-US;q=0.9,en;q=0.8,bn;q=0.7","cookie":"_ga_3DVKZSPS3D=GS1.1.1741392476.1.1.1741394321.21.0.0","priority":"u=1, i"}
        r = requests.get(f"https://api.internal.temp-mail.io/api/v3/email/{email}/messages", headers=h).json()
        return r('subject')
    except:
        return None
    
def main() -> None:
    uid=None
    global live,cp,passw,num_accounts
    clear()
    console.print(logo)
    num_accounts = int(input("\033[1;93m➤ HOW MANY ACCOUNTS TO PROCESS? : \033[1;92m"))
    clear()
    console.print(logo)
    passw=fake_password()
    for make in range(int(num_accounts)):
        ses = requests.Session()
        response = ses.get(
            url='https://touch.facebook.com/reg',
            params={"_rdc":"1","_rdr":"","wtsid":"rdr_0t3qOXoIHbMS6isLw","refsrc":"deprecated"},
        )
        mts = ses.get("https://touch.facebook.com").text
        m_ts = re.search(r'name="m_ts" value="(.*?)"',str(mts)).group(1)
        formula = extractor(response.text)
        email2 = get_temp_plus()
        phone2 = GetBDNumber()
        email3 = GetEmails()
        firstname,lastname = fake_name()
        sys.stdout.write(f'\r\033[96m[REGISTERING]\033[0m\033[92m<+>\033[0m[Success:\033[92m{live}\033[0m/Faild:\033[91m{cp}\033[0m]\r')
        sys.stdout.flush()
        payload = {
            'ccp': "2",
            'reg_instance': str(formula["reg_instance"]),
            'submission_request': "true",
            'helper': "",
            'reg_impression_id': str(formula["reg_impression_id"]),
            'ns': "1",
            'zero_header_af_client': "",
            'app_id': "103",
            'logger_id': str(formula["logger_id"]),
            'field_names[0]': "firstname",
            'firstname': firstname,
            'lastname': lastname,
            'field_names[1]': "birthday_wrapper",
            'birthday_day': str(random.randint(1,28)),
            'birthday_month': str(random.randint(1,12)),
            'birthday_year': str(random.randint(1992,2009)),
            'age_step_input': str(random.randint(1, 10)),
            'field_names[2]': "gender",
            'gender': "2",
            'field_names[3]': "email",
            'email': email3,
            'field_names[4]': "mobile",
            'mobile': phone2,
            'field_names[5]': "password",
            'password': passw,
            'm_ts': m_ts,
            'email_confirm': email3,
            'email_verification': 'false',
            'referrer': 'https://www.facebook.com',
            'referrer_policy': "origin",
            'fb_dtsg': str(formula["fb_dtsg"]),
            'jazoest': str(formula["jazoest"]),
            'captcha_challenge': "",
        }

        check=ses.post("https://touch.facebook.com/reg",data=payload).text
        if 'Email is already taken' in check:
            sys.stdout.write(f'\r{X}{W} Live:{G} {email3} {R}-> Account Already Taken ')
            cp+=1
        elif 'Some required information is missing' in check:
            sys.stdout.write(f'\r{X}{W} Live:{G} {email3} {R}-> Some required information is missing ')
            live+=1
        else:
            sys.stdout.write(f'\r{X}{W} Live:{G} {email3} {R}-> Unknown ')
            live+=1
    return None
if __name__ == '__main__':
    main()
