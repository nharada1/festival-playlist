Upcoming music festival? Create a playlist of the lineup's most popular live songs. Based on data from [setlist.fm](http://www.setlist.fm). Output CSV file will work with [Ivy](http://www.ivyishere.org/) to create Spotify playlists.

# Requirements:

* Python 2.7 or 3.4+
* beautifulsoup 4
* futures

# Installation:
No installation required, just ensure dependencies are correctly installed. If using pip, run `pip install -r requirements.txt`.

# Usage:
Run festival-playlist with either a textfile of artists or pass artist list directly into the command line. 

```
$ python generate_playlist.py "wilco, chvrches, panda bear" -n 5

artist, title
wilco, A Shot in the Arm
wilco, I'm the Man Who Loves You
wilco, Jesus, Etc.
wilco, I Am Trying to Break Your Heart
wilco, Handshake Drugs
chvrches, The Mother We Share
chvrches, Recover
chvrches, Lies
chvrches, We Sink
chvrches, Gun
panda bear, Surfers Hymn
panda bear, You Can Count On Me
panda bear, Last Night at the Jetty
panda bear, Boys Latin
panda bear, Crosswords
```

# Help text:

```
usage: generate_playlist.py [-h] [-n N] [-w W] [-y Y] artist_list

Create a CSV of the most popular live songs by a set of artists

positional arguments:
  artist_list  Text file with a list of artists one per line OR comma
               separated string of artists

optional arguments:
  -h, --help   show this help message and exit
  -n N         Save n top songs for each artist (default: 15)
  -w W         Save to output file instead of writing to stdout
  -y Y         Filter songs played only during given year (default no
               filtering)
```

### Disclaimer
Neither I nor festival-playlist are affiliated with Spotify, setlist.fm, or Ivy. This product is in no way endorsed or approved by any of these services.
