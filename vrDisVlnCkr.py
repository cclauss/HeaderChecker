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

dsable_wrng(InsecureRequestWarning)
adgt = list(dgtz)
hdrz = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0', 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Connection':'keep-alive',}

def check_url(url):
  url = urlparse(url)
  conn = httplib.HTTPConnection(url.netloc)
  conn.request("HEAD", url.path)
  if conn.getresponse():
    return True
  else:
    return False

try:
	if len(arg) != 2:
		inpt = raw_input('Enter the URL: ')
	else:
		inpt = arg[1]
	print 'Checking URL...'
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
	print '\nREQUEST HEADERS\n'
	for k in hdrz: print k, ':', hdrz[k]
	r = reg(url, headers=hdrz, verify=False)
	hdrz = r.headers
	kyz = hdrz.keys()
	print '\nRESPONSE HEADERS\n'
	for k in hdrz: print k, ':', hdrz[k]
	print '\nVULNERABILITIES\n'
	if 'Server' in kyz and 'X-Powered-By' in kyz and 'X-AspNet-Version' in kyz:
		s = hdrz['Server']
		for i in adgt:
			if i in s:
				print 'Server:', s
				break
			else:
				break

		xpb = hdrz['X-Powered-By']
		print 'X-Powered-By:', xpb

		xanv = hdrz['X-AspNet-Version']
		for i in adgt:
			if i in xanv:
				print 'X-AspNet-Version:', xanv
				break
			else:
				break

	elif 'Server' in kyz and 'X-Powered-By' in kyz:
		s = hdrz['Server']
		for i in adgt:
			if i in s:
				print 'Server:', s
				break
			else:
				break

		xpb = hdrz['X-Powered-By']
		print 'X-Powered-By:', xpb

	elif 'Server' in kyz and 'X-AspNet-Version' in kyz:
		s = hdrz['Server']
		for i in adgt:
			if i in s:
				print 'Server:', s
				break
			else:
				break

		xanv = hdrz['X-AspNet-Version']
		for i in adgt:
			if i in xanv:
				print 'X-AspNet-Version:', xanv
				break
			else:
				break

	elif 'X-Powered-By' in kyz and 'X-AspNet-Version' in kyz:
				xpb = hdrz['X-Powered-By']
				print 'X-Powered-By:', xpb

				xanv = hdrz['X-AspNet-Version']
				for i in adgt:
					if i in xanv:
						print 'X-AspNet-Version:', xanv
						break
					else:
						break
	elif 'X-Powered-By' in kyz:
			xpb = hdrz['X-Powered-By']
			print 'X-Powered-By:', xpb
	elif 'X-AspNet-Version' in kyz:
				xanv = hdrz['X-AspNet-Version']
				for i in adgt:
					if i in xanv:
						print 'X-AspNet-Version:', xanv
						break
					else:
						break
	else:
		print 'WednesdayThursdayFriday... See the headers below 😜\n'
		for k in hdrz:
			print k, ':', hdrz[k]
except KeyboardInterrupt: print '\b\bInterruption from Keyboard...'
except rex.ConnectionError: print 'Is it https??'
