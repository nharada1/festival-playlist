from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
import parsers


class SetlistArtist(object):
    def __init__(self, artist_name):
        """Init an artist by getting the artist's URLs from setlist.fm

        Arguments
        ---------
        artist_name : string
            Artist name to search on setlist.fm
        """
        self.name = artist_name
        self.page_location = parsers.get_artist_page_location(artist_name)
        self.stats_location = self.page_location.replace('setlists', 'stats')

    def popular_songs(self, num_songs, year=None):
        """Return the num_songs most popular songs. Number of returned songs may be less than num_songs
        if, for example, the artist has less songs in their live repertoire

        Arguments
        ----------
        num_songs : int
            How many songs (max) to return
        """
        top_artists = parsers.get_top_from_stats(self.stats_location, year=year)
        return top_artists[0:num_songs]
