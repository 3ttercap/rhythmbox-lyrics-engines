# Rhythmbox Lyrics Engines #

Engines for Rhythmbox lyrics plugin (lyric parser)
These engines helps Rhythmbox lyrics plugin (https://github.com/dmo60/lLyrics) retrieve:
  1. Vietnamese lyrics from the music website named mp3.zing.vn.
  1. English lyrics from MaxiLyrics.com.

**INSTALL**

---

How to installing this parser (tested on Ubuntu 10.04):
  1. Download the tar ball file and **extract** it.
  1. Copy the new **LyricsSites.py** and files: **ZingParser.py**, and **MaxiParser.py** to "~/.local/share/rhythmbox/plugins/lyrics/" OR "$libdir/rhythmbox/plugins/lyrics" (usually "**/usr/lib/rhythmbox/plugins/lyrics/**").
  1. Launch Rhythmbox and enable the parser under "Edit > Plugins" > "Song Lyrics" > "Configure".

**Note**: you **should modify** LyricsSites.py on your own in cases:
  1. You only want either the English or Vietnamese parser, don't use my LyricsSites.py
  1. You don't want to use the my modified LyricsSites.py.

```

from LyrcParser import LyrcParser
from AstrawebParser import AstrawebParser
from LeoslyricsParser import LeoslyricsParser
from WinampcnParser import WinampcnParser
from TerraParser import TerraParser
from ZingParser import ZingParser
from MaxiParser import MaxiParser

lyrics_sites = [
	{ 'id': 'lyrc.com.ar', 		'class': LyrcParser, 		'name': _("Lyrc (lyrc.com.ar)") 		},
	{ 'id': 'astraweb.com', 	'class': AstrawebParser, 	'name': _("Astraweb (www.astraweb.com)") 	},
	{ 'id': 'leoslyrics.com', 	'class': LeoslyricsParser, 	'name': _("Leo's Lyrics (www.leoslyrics.com)") 	},
	{ 'id': 'winampcn.com', 	'class': WinampcnParser, 	'name': _("WinampCN (www.winampcn.com)") 	},
	{ 'id': 'terra.com.br',		'class': TerraParser,		'name': _("TerraBrasil (terra.com.br)")		},
	{ 'id': 'mp3.zing.vn',		'class': ZingParser,		'name': _("ZingVietNam (mp3.zing.vn)")		},
        { 'id': 'maxilyrics.com',       'class': MaxiParser,            'name': _("MaxiLyrics (MaxiLyrics)")            }
	

]

```

Lyrics are property and copyright of their owner.


---

for TB
