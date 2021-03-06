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
        # Optional arguments and checks
        if parsed_args.w:
            try:
                f = open(parsed_args.w, 'w')
            except Exception as e:
                print("Couldn't create file {}".format(parsed_args.w))
                print("Underlying code says: {}".format(e))
                return
        if parsed_args.y:
            if not parsed_args.y.isdigit():
                print("Please enter a valid year (no abbreviations)")
                return
            year = int(parsed_args.y)

        # Start CSV header, purposely lowercase
        artists_not_found = []
        print('artist, title', file=f)
        for line in lines:
            try:
                artist = SetlistArtist(line)

                # Get popular songs for each artist, will only return however many exist
                songs = artist.popular_songs(parsed_args.n, year=year)
                for song in songs:
                        print(artist.name + ', ' + song, file=f)
            except ValueError as v:
                artists_not_found.append(line)
                pass
    finally:
        if f:
            f.close()
        if artists_not_found:
            print("Failed to find the following artists: {}".format(artists_not_found))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a CSV of the most popular live songs by a set of artists')
    parser.add_argument('artist_list', help='Text file with a list of artists one per line OR comma separated string of artists')
    parser.add_argument('-n', required=False, type=int, default=15, help='Save n top songs for each artist (default: 15)')
    parser.add_argument('-w', required=False, help='Save to output file instead of writing to stdout')
    parser.add_argument('-y', required=False, help='Filter songs played only during given year (default no filtering)')
    args = parser.parse_args()

    main(args)
