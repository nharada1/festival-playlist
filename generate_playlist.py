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

    f = None
    try:
        if parsed_args.w:
            f = open(parsed_args.w, 'w')

        print('artist, title', file=f)
        for line in lines:
            artist = SetlistArtist(line)
            songs = artist.popular_songs(parsed_args.n)
            for song in songs:
                    print(artist.name + ', ' + song, file=f)
    finally:
        if f:
            f.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a CSV of the most popular live songs by a set of artists')
    parser.add_argument('artist_list', help='Text file with a list of artists one per line OR comma separated string of artists')
    parser.add_argument('-n', required=True, type=int, default=15, help='Save n top songs for each artist')
    parser.add_argument('-w', required=False, help='(optional) Save to output file instead of writing to stdout')
    args = parser.parse_args()

    main(args)
