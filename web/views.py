# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response

COMINGSOON = 'javascript:alert("Official launch coming soon!");'

CONST = {}	# TODO: this could come from a "configobj" (python-configobj) file in /usr/share/macaronic/globals.ini
CONST['title'] = 'macaronic'
CONST['website'] = 'http://macaronic.net/'
CONST['hero'] = {
	'title': 'Just deploy!',
	'text': 'With Macaronic, you can focus your efforts on your important projects, and leave the core infrastructure to us. Macaronic is ideal for educational institutions, research labs and businesses.',
	'url': COMINGSOON,
}
CONST['hero']['text']+= ' <i>Official launch coming soon!</i>'	# TODO: remove after launch
CONST['headings'] = [
	{
		'title': 'Professional Engineering',
		#'muted': 'It’ll blow your mind.',
		'text': 'Macaronic is professionally built, and peer reviewed by the community. We take the time to focus on the fine details and security implications that can take years to get right. Avoid surprises and keep your infrastructure safe. Enterprise class reliability comes as standard.',
		#'lead': 'It is amazing stuff...',
		'url': COMINGSOON,
	},
	{
		'title': 'Infrastructure Glue',
		#'muted': 'See for yourself.',
		'text': 'Macaronic combines many of the technologies that you already know, and others that you haven’t had the time to learn yet. Built on <a target="_blank" href="https://en.wikipedia.org/wiki/GNU">GNU</a>/<a target="_blank" href="https://en.wikipedia.org/wiki/Linux">Linux</a> and connected by <a target="_blank" href="http://www.python.org/">Python</a>, <a target="_blank" href="https://en.wikipedia.org/wiki/Puppet_%28software%29">Puppet</a>, and <a href="#TODO">others</a>, Macaronic federates a system of servers and tools including: DHCP, DNS, Cobbler, KVM, DRBD, GFS2, RGManager, Shorewall, Keepalived and Conntrackd to create a stable cluster infrastructure to host your network, and to manage the tools used to deploy and re-deploy a productive collection of addtional servers and workstations.',
		#'lead': 'It is amazing stuff...',
		'url': COMINGSOON,
	},
	{
		'title': 'Free and Open Source',
		#'muted': 'Checkmate.',
		'text': 'Macaronic and all of its bundled software is <a target="_blank" href="https://www.gnu.org/philosophy/free-sw.html">Free</a> and Open Source. We encourage you to use, learn about, modify, and redistribute our code. Everyone benefits from improvements, transparency ensures you know exactly what’s running your infrastructure, and you have the control to customize things exactly the way you like them.',
		#'lead': 'It is amazing stuff...',
		'url': COMINGSOON,
	},
]
CONST['sections'] = [
	{
		'title': 'Home',
		#'muted': 'It’ll blow your mind.',
		#'url': CONST['website'],	# use for absolute returns...
		'url': '/',
		'dropdown': False,
	},
	{
		'title': 'News',
		'url': True,
		'dropdown': False,
	},
	{
		'title': 'Download',
		'muted': 'Download options:',
		'url': True,
		'dropdown': False,
	},
	{
		'title': 'Documentation',
		#'muted': 'See for yourself.',
		'url': True,
		'dropdown': False,
	},
	{
		'title': 'Wisdom',
		'muted': 'A memorable quotation...',
		'html': """
			<blockquote>
			<p>An ideal language allows us to express easily what is useful for the programming task, and at the same time makes it difficult to write what leads to incomprehensible or incorrect programs.</p>
			<small><cite title="Nico Habermann">Nico Habermann</cite></small>
			</blockquote>
			""",
		'url': True,
		'dropdown': True,
	},
	{
		'title': 'About',
		#'muted': 'See for yourself.',
		'text': 'ABOUT TODO',
		'url': True,
		'dropdown': True,
	},
]
CONST['copyright'] = 'James Shubin, 2013'
CONST['blog'] = 'https://ttboj.wordpress.com/'
CONST['True'] = True	# useful for doing bool comparisons...
CONST['False'] = False

def index(request):
	"""/index.html"""
	context = {
		'active': 'home',
	}
	return render_to_response('index.html', dict(context, **CONST))

def news(request):
	"""/news.html"""
	context = {
		'active': 'news',
	}
	return render_to_response('news.html', dict(context, **CONST))

def download(request):
	"""/section.html"""
	context = {
		'active': 'download',
	}
	return render_to_response('section.html', dict(context, **CONST))

def documentation(request):
	"""/section.html"""
	context = {
		'active': 'documentation',
	}
	return render_to_response('section.html', dict(context, **CONST))

def wisdom(request):
	"""/section.html"""
	context = {
		'active': 'wisdom',
	}
	return render_to_response('section.html', dict(context, **CONST))

def about(request):
	"""/section.html"""
	context = {
		'active': 'about',
	}
	return render_to_response('section.html', dict(context, **CONST))

def page_not_found(request):	# 404 error...
	"""/notfound.html"""
	context = {
		'active': 'notfound',
	}
	return render_to_response('notfound.html', dict(context, **CONST))

