# -*- Mode: python; coding: utf-8; tab-width: 8; indent-tabs-mode: t; -*-
#
# Copyright (C) 2011 Le Vu Hiep
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

import urllib
import rb
import re
import sys
import unicodedata


class ZingParser (object):
	def __init__(self, artist, title):
		self.artist = artist
		self.title = title

	def search(self, callback, *data):
		path = 'http://mp3.zing.vn/tim-kiem/bai-hat.html'
		artist = urllib.quote(self.artist)
		title = urllib.quote(self.title)
		join = urllib.quote(' - ')
		wurl = '?q=%s%s%s&filter=4&search_type=bai-hat' % (title, join, artist)
		print "search URL: " + path + wurl

		loader = rb.Loader()
		loader.get_url (path + wurl, self.got_lyrics, callback, *data)

	def got_lyrics(self, result, callback, *data):
		
		if result is None:
			callback (None, *data)
			return
		if result is not None:
			result = result.decode('iso-8859-1').encode('UTF-8')

			if re.search('<strong>0</strong>', result):
				print "======NO SONG FOUND===="
				callback (None, *data)

			elif re.search('<div class="first-search-song">', result):
                                print "=======FOUND========="
				callback(self.parse_lyrics(result), *data)
			else:
				callback (None, *data)
		else:
			callback (None, *data)

	def parse_lyrics(self, source):
		

		source = re.split('\<div\ class\=\"first-search-song\"\>',source)[1]
		source = re.split('href\=\"',source)[1]
		source = re.split('\"\>',source)[0]
		mylink = 'http://mp3.zing.vn' + source
       	        print "search URL: " + mylink
		lyrics = urllib.urlopen(mylink).read()

		lyrics = re.split('</span></span>', lyrics)[1] 
		lyrics = re.split('</p>', lyrics)[0]
		lyrics = re.sub('<[Bb][Rr] />', '', lyrics)
		lyrics = re.sub('^\\s{1,}','',lyrics)
		lyrics += "\n\nGet from Zing"
		print lyrics	
		
		return lyrics
