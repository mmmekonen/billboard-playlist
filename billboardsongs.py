from datetime import date, timedelta
import billboard
import sys


def makeList(year):
    tracks = set()
    for date in allSaturdays(year):
        chart = billboard.ChartData('hot-100', date)
        tracks.update(
            {str(song) for song in chart.entries if str(song) not in tracks})
    print(*tracks, sep='\n')


def allSaturdays(year):
    # taken from https://stackoverflow.com/questions/2003870/how-can-i-select-all-of-the-sundays-for-a-year-using-python
    d = date(year, 1, 1)
    d += timedelta(days=(5 - d.weekday() + 7) % 7)
    while d.year == year:
        yield str(d)
        d += timedelta(days=7)


if __name__ == '__main__':
    try:
        year = int(sys.argv[1])
        makeList(year)
    except IndexError:
        print(f'Must include year: python {sys.argv[0]} <YYYY>')
    except ValueError:
        print('Year must be a number in the format YYYY.')