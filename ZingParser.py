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
		##wurl = '?q=%s%s%s' % (artist, join, title)
		##http://mp3.zing.vn/tim-kiem/bai-hat.html?q=hong+nhung-mot+coi+di+ve&filter=4&search_type=bai-hat
		wurl = '?q=%s%s%s&filter=4&search_type=bai-hat' % (title, join, artist)
		print "search URL: " + path + wurl

		loader = rb.Loader()
		loader.get_url (path + wurl, self.got_lyrics, callback, *data)

	def got_lyrics(self, result, callback, *data): ## kiem tra coi lyrics co cho bai nay ko?
		
		if result is None:
			callback (None, *data)
			return
		if result is not None:
			result = result.decode('iso-8859-1').encode('UTF-8')

			if re.search('<strong>0</strong>', result): ## ko tim thay bai nao
				print "======NOT FOUND ANY SONG===="
				callback (None, *data)

			elif re.search('<div class="first-search-song">', result): ## tim thay co' tag cua lyrics
                                print "=======FOUND SONG========="
				callback(self.parse_lyrics(result), *data)
			else:
				callback (None, *data)
		else:
			callback (None, *data)

#	def get_lyrics_link(self, source):
#		source = re.split('\<div\ class\=\"first-search-song\"\>',source)[1]
#		source = re.split('href\=\"',source)[1]
#		source = re.split('\"\>',source)[0]
#		mylink = 'http://mp3.zing.vn' + source
#               print "@@@@@@@@@@@@@ search URL: " + mylink
#		loader = rb.Loader()
#               loader.get_url (mylink, self.parse_lyrics)
                
	
	def parse_lyrics(self, source):
		
		print "@@@@@@@@@ Dang tim bai hat"
		source = re.split('\<div\ class\=\"first-search-song\"\>',source)[1]
		source = re.split('href\=\"',source)[1]
		source = re.split('\"\>',source)[0]
		mylink = 'http://mp3.zing.vn' + source
       	        print "@@@@@@@@@@@@@ search URL: " + mylink
		lyrics = urllib.urlopen(mylink).read()

		lyrics = re.split('</span></span>', lyrics)[1] 
		lyrics = re.split('</p>', lyrics)[0]
		lyrics = re.sub('<[Bb][Rr] />', '', lyrics)
		lyrics = re.sub('^\\s','',lyrics)
#		lyrics = lyrics.encode('utf-8', 'ignore')
		lyrics += "\n\nGet from Zing"
		print lyrics	
		
		return lyrics
