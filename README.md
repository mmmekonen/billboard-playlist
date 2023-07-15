# billboard-playlist  

Autogenerates a Spotify playlist of all the songs that were on the [Billboard Hot-100](https://www.billboard.com/charts/hot-100/) weekly charts for a specified year.

## How to use
Run the following command with YYYY as a four digit code for the year to make a playlist for the specified year

```
python billboardsongs.py <YYYY>
```

To make a playlist for all years up to (but not including) the current year, run

```
python billboardsongs.py all
```

## Dependencies
Uses the [billboard.py](https://github.com/guoguo12/billboard-charts) and [spotipy](https://spotipy.readthedocs.io/en/2.22.1/) APIs.