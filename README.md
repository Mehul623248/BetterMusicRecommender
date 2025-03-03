How the Music Recommender works (may add GUI later)

1. First get a playlist of 15 songs max
2. Then using last.fm api, get all tags for each song.
3. Then get top 10 most occuring tags
4. Use ytmusicapi to search for songs using those tags
5. Get the list of songs recommended (about 30)
6. Select 5 (could be more) songs randomly
7. Check the top tags occuring of these songs
8. If 5 or more tags match original tags, then end
9. Else, redo the selection of 5 random songs
   
