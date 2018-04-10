#!/usr/bin/env python
# -*- coding: utf-8 -*-
from requests import get as reg
from string import digits as dgtz
from sys import argv as arg
from requests import exceptions as rex
from urlparse import urlparse
import httplib, sys
from requests.packages.urllib3 import disable_warnings as dsable_wrng
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from os import system as stm
from sys import exit as x

dsable_wrng(InsecureRequestWarning)
adgt = list(dgtz)
hdrz = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0', 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Connection':'keep-alive',}

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
				print 'Server:', s
				break
			else:
				print '\nWednesdayThursdayFriday... See the headers up ⤊ 😜'
				break

	def c_pb():
		xpb = hdrz['X-Powered-By']
		print 'X-Powered-By:', xpb

	def c_av():
		xanv = hdrz['X-AspNet-Version']
		for i in adgt:
			if i in xanv:
				print 'X-AspNet-Version:', xanv
				break
			else:
				break

	def c_rp():
		rp = hdrz['Referrer-Policy']
		if rp == 'strict-origin-when-cross-origin': pass
		else: print 'Referrer-Policy:', rp

	def c_cto():
		xcto = hdrz['X-Content-Type-Options']
		if xcto == 'nosniff': pass
		else: print 'X-Content-Type-Options:', xcto

	def c_xp():
		xxp = hdrz['X-Xss-Protection']
		if xxp == '1; mode=block': pass
		else: print 'X-Xss-Protection:', xxp

	def c_fo():
		xfo = hdrz['X-Frame-Options']
		if xfo == 'SAMEORIGIN' or xfo == 'DENY': pass
		else: print 'X-Frame-Options:', xfo

	def c_csp():
		csp = hdrz['Content-Security-Policy']
		print 'Content-Security-Policy:', csp

	def c_sts():
		sts = hdrz['Strict-Transport-Security']
		if 'max-age' in sts: pass
		else: print 'Strict-Transport-Security:', sts

	if len(arg) != 2:
		inpt = raw_input('Enter the URL: ')
	else:
		inpt = arg[1]
	print '\033[H\033[J'
	print 'Checking URL: %s'%(inpt)
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
			print 'Whatttttttt...'
	print 'Valid URL!'
	print '\nREQUEST HEADERS\n'
	for k in hdrz: print k, ':', hdrz[k]
	r = reg(url, headers=hdrz, verify=False)
	hdrz = r.headers
	kyz = hdrz.keys()
	print '\nRESPONSE HEADERS\n'
	for k in hdrz: print k, ':', hdrz[k]
	if 'Server' in kyz or 'X-Powered-By' in kyz or 'X-AspNet-Version' in kyz or 'Referrer-Policy' in kyz or 'X-Content-Type-Options' in kyz or 'X-Xss-Protection' in kyz or 'X-Frame-Options' in kyz or 'Content-Security-Policy' in kyz or 'Strict-Transport-Security' in kyz:
		print '\nVULNERABILITIES\n'
		if 'Server' in kyz: c_s()
		else: pass
		if 'X-Powered-By' in kyz: c_pb()
		else: pass
		if 'X-AspNet-Version' in kyz: c_av()
		else: pass
		if 'Referrer-Policy' in kyz: c_rp()
		else: print 'No Referrer-Policy Header...'
		if 'X-Content-Type-Options' in kyz: c_cto()
		else: print 'No X-Content-Type-Options Header...'
		if 'X-Xss-Protection' in kyz: c_xp()
		else: print 'No X-Xss-Protection Header...'
		if 'X-Frame-Options' in kyz: c_fo()
		else: print 'No X-Frame-Options Header...'
		# if 'Content-Security-Policy' in kyz: c_csp()
		# else: print 'No Content-Security-Policy Header...'
		if 'Strict-Transport-Security' in kyz: c_sts()
		else: print 'NO Strict-Transport-Security Header...'
	else: print 'WednesdayThursdayFriday... See the headers up ⤊ 😜'
	stm('gnome-screenshot -w')
except KeyboardInterrupt: print '\b\bInterruption from Keyboard...'
