from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from builtins import open
from future import standard_library
standard_library.install_aliases()
from SetlistArtist import SetlistArtist
import argparse
import os


def main(parsed_args):
    if os.path.isfile(parsed_args.artist_list):
        with open(parsed_args.artist_list) as f:
            lines = f.read().splitlines()
    else:
        lines = parsed_args.artist_list.split(',')
        lines = [l.strip() for l in lines]

    # Both optional
    f = None
    year = None
    # Choose to read from command line or file for input
    try:
        # Optional arguments
        if parsed_args.w:
            f = open(parsed_args.w, 'w')
        if parsed_args.y:
            year = parsed_args.y

        # Start CSV header, purposely lowercase
        print('artist, title', file=f)
        for line in lines:
            artist = SetlistArtist(line)
            # Get popular songs for each artist, will only return however many exist
            songs = artist.popular_songs(parsed_args.n, year=year)
            for song in songs:
                    print(artist.name + ', ' + song, file=f)
    finally:
        if f:
            f.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a CSV of the most popular live songs by a set of artists')
    parser.add_argument('artist_list', help='Text file with a list of artists one per line OR comma separated string of artists')
    parser.add_argument('-n', required=False, type=int, default=15, help='Save n top songs for each artist (default: 15)')
    parser.add_argument('-w', required=False, help='Save to output file instead of writing to stdout')
    parser.add_argument('-y', required=False, help='Filter songs played only during given year (default no filtering)')
    args = parser.parse_args()

    main(args)
