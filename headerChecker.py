#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
from urllib import urlopen as uopn
from requests import get as reg
from string import digits as dgtz
from sys import argv as arg
from requests import exceptions as rex
from urlparse import urlparse
import httplib, subprocess
from requests.packages.urllib3 import disable_warnings as dsable_wrng
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from time import sleep as slp
from subprocess import call as kal
from sys import exit as x

def gch(msg = '[Y/n]'):
	try:
	from msvcrt import getch
except ImportError:
	def getch():
		import sys
		import tty
		import termios
		fd = sys.stdin.fileno()
		old = termios.tcgetattr(fd)
		try:
			tty.setraw(fd)
			return sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old)
	from sys import stdout as sto
	if msg is not None:
		print(msg, end='')
		sto.flush()
	ch = getch()
	print()
	return ch
def is_conn():
	x = gch('Are You Scanning Locally? [y/N]:')
	if x == 'n' or x == 'N' or x == '\r':
		try :
			uopn('https://www.google.com')
			return True
			main()
		except IOError:
			return False
		except Exception as e:
			print("Some Error: ", e)

	elif x == 'y' or x == 'Y':
		z = gch('Do you have gnome-screenshot? [Y/n]: ')
		if z == 'y' or z == 'Y' or z == '\r':
			return True
			main()
		elif z == 'n' or z == 'N':
			try :
				uopn('https://www.google.com')
				print('Then, INSTALLING(▼) gnome-screenshot...\n')
				slp(2)
				kal(['apt-get install gnome-screenshot -y'], shell=True)
				print('\033[H\033[J')
				return True
				main()
			except IOError:
				print('\033[91mGet Internet() Connection THEN...\033[0m')
				exit(1)
			except Exception as e:
				print("Some Error: ", e)
		else:
			print('Invalid Input...\n')
			is_conn()
	else:
		print('Invalid Input...\n')
		is_conn()
def main():
	dsable_wrng(InsecureRequestWarning)
	adgt = list(dgtz)
	hdrz = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0', 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Connection':'keep-alive',}
	if is_conn():
		if kal(['gnome-screenshot -h'], shell=True) == 127:
			print('\033[H\033[Jgnome-screenshot Not Found... #INSTALLING(▼)\n')
			print('\33]0;INSTALLING gnome-screenshot\7')
			slp(2)
			kal(['apt-get install gnome-screenshot -y'], shell=True)
		else: pass
		try:
			def check_url(url):
				url = urlparse(url)
				conn = httplib.HTTPConnection(url.netloc)
				conn.request("HEAD", url.path)
				if conn.getresponse():
					return True
				else:
					return False

			def c_s():
				s = hdrz['Server']
				for i in adgt:
					if i in s:
						print('\033[1mServer:', s, '\033[0m')
						break
					else: break

			def c_pb():
				xpb = hdrz['X-Powered-By']
				print('\033[1mX-Powered-By:', xpb, '\033[0m')

			def c_av():
				xanv = hdrz['X-AspNet-Version']
				for i in adgt:
					if i in xanv:
						print('\033[1mX-AspNet-Version:', xanv, '\033[0m')
						break
					else:
						break

			def c_rp():
				rp = hdrz['Referrer-Policy']
				if rp == 'strict-origin-when-cross-origin': pass
				else: print('Referrer-Policy:', rp)

			def c_cto():
				xcto = hdrz['X-Content-Type-Options']
				if xcto == 'nosniff': pass
				else: print('X-Content-Type-Options:', xcto)

			def c_xp():
				xxp = hdrz['X-Xss-Protection']
				if xxp == '1; mode=block': pass
				else: print('X-Xss-Protection:', xxp)

			def c_fo():
				xfo = hdrz['X-Frame-Options']
				if xfo == 'SAMEORIGIN' or xfo == 'DENY': pass
				else: print('X-Frame-Options:', xfo)

			def c_csp():
				csp = hdrz['Content-Security-Policy']
				if 'Content-Security-Policy' in csp: pass
				else: print('No Content-Security-Policy Header...')

			def c_sts():
				sts = hdrz['Strict-Transport-Security']
				if 'max-age' in sts: pass
				else: print('Strict-Transport-Security:', sts)
			print('\033[H\033[J\33]0;HeaderChecker\7')
			if len(arg) != 2:
				inpt = raw_input('Enter the URL: ')
			else:
				inpt = arg[1]
			print('\33]0;HeaderChecker: %s\7'%(inpt))
			print('\033[92mChecking URL:\033[0m\033[15m', inpt, '\033[0m\033[92m')
			if 'http://' in inpt:
				if check_url(inpt):
					url = inpt
			elif 'https://' in inpt:
				if check_url(inpt):
					url = inpt
			else:
				url_http = 'http://' + inpt
				url_https = 'https://' + inpt
				if check_url(url_http):
					url = url_http
				elif check_url(url_https):
					url = url_https
				else:
					print('Whatttttttt...')
			print('Valid URL!')
			print('\n\033[1m\033[4mREQUEST HEADERS\033[0m\n\033[15m')
			for k in hdrz: print(k, ':', hdrz[k])
			r = reg(url, headers=hdrz, verify=False)
			hdrz = r.headers
			kyz = hdrz.keys()
			print('\n\033[92m\033[1m\033[4mRESPONSE HEADERS\033[0m\n\033[15m')
			for k in hdrz: print(k, ':', hdrz[k])
			if 'Server' in kyz or 'X-Powered-By' in kyz or 'X-AspNet-Version' in kyz or 'Referrer-Policy' in kyz or 'X-Content-Type-Options' in kyz or 'X-Xss-Protection' in kyz or 'X-Frame-Options' in kyz or 'Content-Security-Policy' in kyz or 'Strict-Transport-Security' in kyz:
				print('\033[0m\033[91m\n\033[1m\033[4mVULNERABILITIES\n\033[0m\033[91m')
				if 'Server' in kyz: c_s()
				else: pass
				if 'X-Powered-By' in kyz: c_pb()
				else: pass
				if 'X-AspNet-Version' in kyz: c_av()
				else: pass
				if 'Referrer-Policy' in kyz: c_rp()
				else: print('✘ Referrer-Policy Header...')
				if 'X-Content-Type-Options' in kyz: c_cto()
				else: print('✗ X-Content-Type-Options Header...')
				if 'X-Xss-Protection' in kyz: c_xp()
				else: print('❌X-Xss-Protection Header...')
				if 'X-Frame-Options' in kyz: c_fo()
				else: print('✗ X-Frame-Options Header...')
				if 'Content-Security-Policy' in kyz: c_csp()
				else: print('✘ Content-Security-Policy Header...')
				if 'Strict-Transport-Security' in kyz: c_sts()
				else: print('✖ Strict-Transport-Security Header...')
			else: print('\033[91mWednesdayThursdayFriday... See the headers up ⤊ 😜\033[0m')
			if kal(['gnome-screenshot -w'], shell=True) == 127:
				print('\033[H\033[Jgnome-screenshot Not Found... #INSTALLING(▼)')
				slp(2)
				kal(['apt-get install gnome-screenshot -y'], shell=True)
			else: pass
			print('\033[0m')
		except KeyboardInterrupt: print('\b\b\033[91mInterruption from Keyboard...\033[0m')
	else: print('\033[91mAre You Serrous! No(✘) Internet()...\033[0m')
main()
