from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import zip
from builtins import int
from future import standard_library
standard_library.install_aliases()
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse


def get_artist_page_location(search_string):
    """Artists use some weird GUID in their URL, so we have to search first

    Arguments
    ----------
    search_string : string
        Artist to search for, will be escaped
    """
    # Escape input and create query
    escaped_search = urllib.parse.quote(search_string)
    search_url = 'http://www.setlist.fm/search?query=' + escaped_search
    # Make request
    search_html = urllib.request.urlopen(search_url).read()
    search_soup = BeautifulSoup(search_html, "html.parser")
    top_artist = search_soup.findAll('div', {'class': 'topArtistName'})
    if top_artist:
        link_suffix = top_artist[0].a['href']
        final_link = urllib.parse.urljoin('http://www.setlist.fm', link_suffix)
    else:
        raise ValueError('Couldn\'t find the artist {}'.format(search_string))

    return final_link


def get_top_from_stats(stats_url, year=None):
    """Get the top songs from the artist's stats page

    Arguments
    ----------
    stats_url : string
        Location of the artist's stats page
    """
    if year:
        stats_url += '?year={}'.format(year)

    search_html = urllib.request.urlopen(stats_url).read()
    search_soup = BeautifulSoup(search_html, "html.parser")
    top_artist = search_soup.findAll('td', {'class': 'songName'})
    song_ids = [item.span['id'] for item in top_artist]
    song_ids_ints = [int(item.replace('id', ''), 16) for item in song_ids]
    song_names = [item.span.a.get_text() for item in top_artist]
    # They should be sorted but sort just in case. I don't trust setlist.fm
    ids_and_names = zip(song_ids_ints, song_names)
    sorted_ids_and_names = sorted(ids_and_names, key=lambda v: v[0])
    sorted_names = [song[1] for song in sorted_ids_and_names]

    return sorted_names
