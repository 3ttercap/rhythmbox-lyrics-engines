# -*- Mode: python; coding: utf-8; tab-width: 8; indent-tabs-mode: t; -*-
#
# Copyright (C) 2012 Le Vu Hiep
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# The Rhythmbox authors hereby grant permission for non-GPL compatible
# GStreamer plugins to be used and distributed together with GStreamer
# and Rhythmbox. This permission is above and beyond the permissions granted
# by the GPL license by which Rhythmbox is covered. If you modify this code
# you may extend this exception to your version of the code, but you are not
# obligated to do so. If you do not wish to do so, delete this exception
# statement from your version.
#
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301  USA.

import urllib2
import rb
import re
import sys
import urllib
import HTMLParser

class MaxiParser (object):
	def __init__(self, artist, title):
		self.artist = artist
		self.title = title

	def search(self, callback, *data):
		artist = urllib.quote(self.artist)
		title = urllib.quote(self.title)
		title =	re.sub('(\-|\.wav|\.mp3|\.mid\.wma)','',title)

		if re.search('[uU]nknown',artist):
			join = urllib.quote('-')
			content = '%s' % (title)

		else:
			join = urllib.quote('-')
			content = '%s%s%s' % (title, join, artist)
	
		path ='https://www.google.com/search?sclient=psy-ab&hl=vi&safe=off&source=hp&q='+content+'+site:maxilyrics.com&pbx=1&oq='+content+'+site:maxilyrics.com&aq=f&aqi=&aql=&gs_sm=e&gs_upl=3203972l3209682l9l3209897l17l17l0l0l0l0l190l1691l14.3l17l0&fp=1&biw=1280&bih=640&cad=b&btnI=1&bav=on.2,or.r_gc.r_pw.r_cp.,cf.osb&tch=1&ech=1&psi=9e8vT5_5OcOaiAfk47i7Dg.1328541646416.3'
	    	req_headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0','Cookie': 'Hello Google','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Language': 'en-us,en;q=0.5','Accept-Encoding': 'gzip,deflate','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7','Connection': 'keep-alive','Referer': 'http://www.google.com/search?sourceid=chrome&ie=UTF-8&q='+content}
    		req  = urllib2.Request(path, headers=req_headers)
		response = urllib2.urlopen(req)
		lyrURL = response.info().getheader('Location')
		self.got_lyrics(lyrURL, callback, *data)
#		self.parse_lyrics(lyrURL)

	def got_lyrics(self, url, callback, *data):
		if url is None:
			callback(None, *data)
                        return
                if url is not None:
			callback(self.parse_lyrics(url), *data)
		else:
			callback(None, *data)

	def parse_lyrics(self, uRL):
#	   	print "Final URL: ===> " + uRL
		lyrics = urllib.urlopen(uRL).read()
		lyrics = re.split('<div class=\"contentdiv_leftbox_data\">', lyrics)[1] 
		lyrics = re.split('</div>', lyrics)[0]
		lyrics = re.sub('<[Bb][Rr] />', '\n', lyrics)
		lyrics = re.sub('^\\s{1,}','',lyrics)

		unen = HTMLParser.HTMLParser()
		lyrics = unen.unescape(lyrics)
		lyrics += "\n\nGet from MaxiLyrics"
#		print lyrics
		return lyrics
