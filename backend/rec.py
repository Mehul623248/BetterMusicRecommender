import re
import requests
import config
import os
import json
import random
from collections import Counter
#so for this playlist we get max 100 * n songs recs that gets filtered to just 10 songs
playlist = [ "93 'Til Infinity; Souls Of Mischief",
            "Renegade; JAY-Z",
            "Hit 'em Up; 2Pac",
            "Moment of Clarity; JAY-Z",
            "Survival of the Fittest; Mobb Deep",
            "It Was A Good Day; Ice Cube",
            "Halftime; Nas"
            ]

# playlist = [
#             "Feet Don't Fail Me Now; Joy Crookes",
#             "Coffee; beabadoobee",
#             "Crown; Stormzy",
#             "PRIDE.; Kendrick Lamar",
#             "Gila; Beach House",
#             "Slide; Calvin Harris",
#             "Passionfruit; Drake"

# ]

def youTube(lis):
    from ytmusicapi import YTMusic
    ytmusic = YTMusic()
    quest = ' '.join(lis)
    txt = ytmusic.search(query=quest, filter="songs", limit=30)
    with open(os.path.join("backend", "songs.txt"), "w") as f:
          for i in range(30):
            f.write(txt[i]["title"] +"; " +txt[i]["artists"][0]['name']+ "\n")  
    return txt[19]["title"]

def recs():
    songs= []
    with open(os.path.join("backend", "songs.txt"), "r") as f:
        # seen = set()
        for line in f:
            # line_lower = line.lower()
            # if line_lower in seen:
                songs.append(line)
            # else:
            #     seen.add(line_lower)

    # for song in playlist:
    #     while (song+"\n") in songs:
    #         songs.remove(song+"\n")
            
    seenAlready = set()
    for song in songs:
        if song in seenAlready or "Diddy" in song or "Instrumental" in song or "&" in song:
            continue
        else:
            seenAlready.add(song)

    # print(seenAlready)
    return seenAlready

def realRecs(seenAlready, origTags):
    reccommended= random.sample(list(seenAlready), 5)
    cleaned_list = [element.strip() for element in reccommended]
    # print(cleaned_list)
    getPlaylistInfo(cleaned_list)
    x =  moreProcessTags()
    common_elements = list(set(x) & set(origTags))
   
    while(len(common_elements) < 5):
        reccommended= random.sample(list(seenAlready), 5)
        cleaned_list = [element.strip() for element in reccommended]
        getPlaylistInfo(cleaned_list)
        x1=  moreProcessTags()
        common_elements = list(set(x1) & set(origTags))

    print(len(common_elements))
    print(cleaned_list)
    return 0


#for now hard-code a list, but eventually import playlists and liked album, songs from Spotify or something
def getPlaylistInfo(playlist1):
    total = []
    moreTags = []
    for song in playlist1:
        song = song.strip()
        title = song.split(';')[0]
        title = re.sub(r"\(.*?\)", "", title)
        artist= song.split(';')[1].strip()
        artist = getRidOfSpaces(artist)
        title = getRidOfSpaces(title)
        realJSON= getTags(artist, title)
        processedTags =processTags(realJSON)
        for tag in processedTags:
            moreTags.append(tag)
        # lister = oneTag(processedTags)
        # total.append(getSongs(lister))
    # with open(os.path.join("backend", "actualTracks.txt"), "a") as f:
    #      for item in total:
    #        for it in item:
    #         f.write(it + "\n")
        #  f.write(total)
    with open(os.path.join("backend", "actualTags.txt"), "w") as f:
            for tag in moreTags:
                    f.write(tag+"\n")
    # print(moreTags)
    return 0

def getTags(artist, title):
    artist = getRidOfSpaces(artist)
    title = getRidOfSpaces(title)
    data = requests.get("http://ws.audioscrobbler.com/2.0/?method=track.gettoptags&artist=" + artist +"&track=" + title + "&api_key="+ config.API_key+"&format=json" )
    return data.json()

tagJSON={"toptags":{"tag":[{"count":100,"name":"pop","url":"https://www.last.fm/tag/pop"},{"count":89,"name":"80s","url":"https://www.last.fm/tag/80s"},{"count":64,"name":"michael jackson","url":"https://www.last.fm/tag/michael+jackson"},{"count":46,"name":"dance","url":"https://www.last.fm/tag/dance"},{"count":28,"name":"Disco","url":"https://www.last.fm/tag/Disco"},{"count":14,"name":"funk","url":"https://www.last.fm/tag/funk"},{"count":11,"name":"billie jean","url":"https://www.last.fm/tag/billie+jean"},{"count":10,"name":"king of pop","url":"https://www.last.fm/tag/king+of+pop"},{"count":9,"name":"soul","url":"https://www.last.fm/tag/soul"},{"count":7,"name":"rnb","url":"https://www.last.fm/tag/rnb"},{"count":7,"name":"rock","url":"https://www.last.fm/tag/rock"},{"count":7,"name":"male vocalists","url":"https://www.last.fm/tag/male+vocalists"},{"count":7,"name":"classic","url":"https://www.last.fm/tag/classic"},{"count":6,"name":"american","url":"https://www.last.fm/tag/american"},{"count":5,"name":"favorites","url":"https://www.last.fm/tag/favorites"},{"count":4,"name":"legend","url":"https://www.last.fm/tag/legend"},{"count":4,"name":"80s Pop","url":"https://www.last.fm/tag/80s+Pop"},{"count":4,"name":"oldies","url":"https://www.last.fm/tag/oldies"},{"count":4,"name":"party","url":"https://www.last.fm/tag/party"},{"count":4,"name":"Awesome","url":"https://www.last.fm/tag/Awesome"},{"count":4,"name":"1983","url":"https://www.last.fm/tag/1983"},{"count":4,"name":"thriller","url":"https://www.last.fm/tag/thriller"},{"count":3,"name":"1982","url":"https://www.last.fm/tag/1982"},{"count":3,"name":"Jackson","url":"https://www.last.fm/tag/Jackson"},{"count":3,"name":"mj","url":"https://www.last.fm/tag/mj"},{"count":3,"name":"motown","url":"https://www.last.fm/tag/motown"},{"count":3,"name":"favorite songs","url":"https://www.last.fm/tag/favorite+songs"},{"count":3,"name":"dance pop","url":"https://www.last.fm/tag/dance+pop"},{"count":2,"name":"funky","url":"https://www.last.fm/tag/funky"},{"count":2,"name":"r&b","url":"https://www.last.fm/tag/r&b"},{"count":2,"name":"Michael Jackson - billie jean","url":"https://www.last.fm/tag/Michael+Jackson+-+billie+jean"},{"count":2,"name":"classic rock","url":"https://www.last.fm/tag/classic+rock"},{"count":2,"name":"groovy","url":"https://www.last.fm/tag/groovy"},{"count":2,"name":"male vocalist","url":"https://www.last.fm/tag/male+vocalist"},{"count":2,"name":"USA","url":"https://www.last.fm/tag/USA"},{"count":2,"name":"pop rock","url":"https://www.last.fm/tag/pop+rock"},{"count":2,"name":"dance-pop","url":"https://www.last.fm/tag/dance-pop"},{"count":2,"name":"Favourites","url":"https://www.last.fm/tag/Favourites"},{"count":2,"name":"classics","url":"https://www.last.fm/tag/classics"},{"count":2,"name":"best songs ever","url":"https://www.last.fm/tag/best+songs+ever"},{"count":2,"name":"electronic","url":"https://www.last.fm/tag/electronic"},{"count":2,"name":"catchy","url":"https://www.last.fm/tag/catchy"},{"count":2,"name":"90s","url":"https://www.last.fm/tag/90s"},{"count":2,"name":"fun","url":"https://www.last.fm/tag/fun"},{"count":2,"name":"80's","url":"https://www.last.fm/tag/80%27s"},{"count":2,"name":"Michael","url":"https://www.last.fm/tag/Michael"},{"count":2,"name":"singer-songwriter","url":"https://www.last.fm/tag/singer-songwriter"},{"count":2,"name":"Love","url":"https://www.last.fm/tag/Love"},{"count":2,"name":"cool","url":"https://www.last.fm/tag/cool"},{"count":2,"name":"danceable","url":"https://www.last.fm/tag/danceable"},{"count":1,"name":"alternative","url":"https://www.last.fm/tag/alternative"},{"count":1,"name":"sexy","url":"https://www.last.fm/tag/sexy"},{"count":1,"name":"Retro","url":"https://www.last.fm/tag/Retro"},{"count":1,"name":"amazing","url":"https://www.last.fm/tag/amazing"},{"count":1,"name":"1980s","url":"https://www.last.fm/tag/1980s"},{"count":1,"name":"post-disco","url":"https://www.last.fm/tag/post-disco"},{"count":1,"name":"RB","url":"https://www.last.fm/tag/RB"},{"count":1,"name":"Energetic","url":"https://www.last.fm/tag/Energetic"},{"count":1,"name":"best","url":"https://www.last.fm/tag/best"},{"count":1,"name":"makes me wanna dance","url":"https://www.last.fm/tag/makes+me+wanna+dance"},{"count":1,"name":"Moonwalk","url":"https://www.last.fm/tag/Moonwalk"},{"count":1,"name":"The Best of 80s","url":"https://www.last.fm/tag/The+Best+of+80s"}],"@attr":{"artist":"Michael Jackson","track":"Billie Jean"}}}

def processTags(jsons):
    i = 0
    allTags = []
    while i < len(jsons["toptags"]["tag"]) and i < 10:
       allTags.append(jsons["toptags"]["tag"][i]["name"])
       i+=1
    allTags= list(filter(("MySpotigramBot").__ne__, allTags))
    #print(allTags)
    return allTags

def moreProcessTags():
    allTags = []
    with open(os.path.join("backend", "actualTags.txt"), "r") as f:
            for item in f:
                allTags.append(item)
    
    counter = Counter(allTags)  # Count occurrences
    actual =  [item.strip() for item, _ in counter.most_common(10)]       
    print(actual)
    return actual
    
#outputs all songs that fit each tag so 10 songs per 10 tags makes 100 songs
# #but this oneTag function is for only one song's tags
# def oneTag(allTags):
#     listOfJsons = []
#     for tag in allTags: 
#         stringer = requests.get("http://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag="+tag+"&limit=10&api_key="+config.API_key+"&format=json")
#         listOfJsons.append(stringer.json())
#     return listOfJsons

# def getSongs(listOfJsons):
#     #initially code is just for one of the JSONs
#     # js = {"tracks":{"track":[{"name":"Billie Jean","duration":"293","mbid":"f980fc14-e29b-481d-ad3a-5ed9b4ab6340","url":"https://www.last.fm/music/Michael+Jackson/_/Billie+Jean","streamable":{"#text":"0","fulltrack":"0"},"artist":{"name":"Michael Jackson","mbid":"f27ec8db-af05-4f36-916e-3d57f91ecf5e","url":"https://www.last.fm/music/Michael+Jackson"},"image":[{"#text":"https://lastfm.freetls.fastly.net/i/u/34s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"small"},{"#text":"https://lastfm.freetls.fastly.net/i/u/64s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"medium"},{"#text":"https://lastfm.freetls.fastly.net/i/u/174s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"large"},{"#text":"https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png","size":"extralarge"}],"@attr":{"rank":"1"}},{"name":"Take on Me","duration":"227","mbid":"c9bf13e6-619e-4cca-ae0f-512e9a478930","url":"https://www.last.fm/music/a-ha/_/Take+on+Me","streamable":{"#text":"0","fulltrack":"0"},"artist":{"name":"a-ha","mbid":"7364dea6-ca9a-48e3-be01-b44ad0d19897","url":"https://www.last.fm/music/a-ha"},"image":[{"#text":"https://lastfm.freetls.fastly.net/i/u/34s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"small"},{"#text":"https://lastfm.freetls.fastly.net/i/u/64s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"medium"},{"#text":"https://lastfm.freetls.fastly.net/i/u/174s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"large"},{"#text":"https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png","size":"extralarge"}],"@attr":{"rank":"2"}},{"name":"Sweet Child o' Mine","duration":"356","mbid":"","url":"https://www.last.fm/music/Guns+N%27+Roses/_/Sweet+Child+o%27+Mine","streamable":{"#text":"0","fulltrack":"0"},"artist":{"name":"Guns N' Roses","mbid":"eeb1195b-f213-4ce1-b28c-8565211f8e43","url":"https://www.last.fm/music/Guns+N%27+Roses"},"image":[{"#text":"https://lastfm.freetls.fastly.net/i/u/34s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"small"},{"#text":"https://lastfm.freetls.fastly.net/i/u/64s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"medium"},{"#text":"https://lastfm.freetls.fastly.net/i/u/174s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"large"},{"#text":"https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png","size":"extralarge"}],"@attr":{"rank":"3"}},{"name":"Everybody Wants to Rule the World","duration":"250","mbid":"e4b347be-ecb2-44ff-aaa8-3d4c517d7ea5","url":"https://www.last.fm/music/Tears+for+Fears/_/Everybody+Wants+to+Rule+the+World","streamable":{"#text":"0","fulltrack":"0"},"artist":{"name":"Tears for Fears","mbid":"7c7f9c94-dee8-4903-892b-6cf44652e2de","url":"https://www.last.fm/music/Tears+for+Fears"},"image":[{"#text":"https://lastfm.freetls.fastly.net/i/u/34s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"small"},{"#text":"https://lastfm.freetls.fastly.net/i/u/64s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"medium"},{"#text":"https://lastfm.freetls.fastly.net/i/u/174s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"large"},{"#text":"https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png","size":"extralarge"}],"@attr":{"rank":"4"}},{"name":"Every Breath You Take","duration":"253","mbid":"4bd93e75-bc94-46b8-854f-8c7cea071823","url":"https://www.last.fm/music/The+Police/_/Every+Breath+You+Take","streamable":{"#text":"0","fulltrack":"0"},"artist":{"name":"The Police","mbid":"9e0e2b01-41db-4008-bd8b-988977d6019a","url":"https://www.last.fm/music/The+Police"},"image":[{"#text":"https://lastfm.freetls.fastly.net/i/u/34s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"small"},{"#text":"https://lastfm.freetls.fastly.net/i/u/64s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"medium"},{"#text":"https://lastfm.freetls.fastly.net/i/u/174s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"large"},{"#text":"https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png","size":"extralarge"}],"@attr":{"rank":"5"}},{"name":"Beat It","duration":"258","mbid":"6d0c3f07-afbc-422d-94f3-fb3644cf65e0","url":"https://www.last.fm/music/Michael+Jackson/_/Beat+It","streamable":{"#text":"0","fulltrack":"0"},"artist":{"name":"Michael Jackson","mbid":"f27ec8db-af05-4f36-916e-3d57f91ecf5e","url":"https://www.last.fm/music/Michael+Jackson"},"image":[{"#text":"https://lastfm.freetls.fastly.net/i/u/34s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"small"},{"#text":"https://lastfm.freetls.fastly.net/i/u/64s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"medium"},{"#text":"https://lastfm.freetls.fastly.net/i/u/174s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"large"},{"#text":"https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png","size":"extralarge"}],"@attr":{"rank":"6"}},{"name":"Bohemian Rhapsody","duration":"359","mbid":"ecfa6746-7bc4-4088-ace6-d209477bd63f","url":"https://www.last.fm/music/Queen/_/Bohemian+Rhapsody","streamable":{"#text":"0","fulltrack":"0"},"artist":{"name":"Queen","mbid":"420ca290-76c5-41af-999e-564d7c71f1a7","url":"https://www.last.fm/music/Queen"},"image":[{"#text":"https://lastfm.freetls.fastly.net/i/u/34s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"small"},{"#text":"https://lastfm.freetls.fastly.net/i/u/64s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"medium"},{"#text":"https://lastfm.freetls.fastly.net/i/u/174s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"large"},{"#text":"https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png","size":"extralarge"}],"@attr":{"rank":"7"}},{"name":"Friday I'm in Love","duration":"214","mbid":"8d9104c6-7d8e-460b-8c3d-2d797f79953d","url":"https://www.last.fm/music/The+Cure/_/Friday+I%27m+in+Love","streamable":{"#text":"0","fulltrack":"0"},"artist":{"name":"The Cure","mbid":"69ee3720-a7cb-4402-b48d-a02c366f2bcf","url":"https://www.last.fm/music/The+Cure"},"image":[{"#text":"https://lastfm.freetls.fastly.net/i/u/34s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"small"},{"#text":"https://lastfm.freetls.fastly.net/i/u/64s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"medium"},{"#text":"https://lastfm.freetls.fastly.net/i/u/174s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"large"},{"#text":"https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png","size":"extralarge"}],"@attr":{"rank":"8"}},{"name":"Welcome to the Jungle","duration":"273","mbid":"","url":"https://www.last.fm/music/Guns+N%27+Roses/_/Welcome+to+the+Jungle","streamable":{"#text":"0","fulltrack":"0"},"artist":{"name":"Guns N' Roses","mbid":"eeb1195b-f213-4ce1-b28c-8565211f8e43","url":"https://www.last.fm/music/Guns+N%27+Roses"},"image":[{"#text":"https://lastfm.freetls.fastly.net/i/u/34s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"small"},{"#text":"https://lastfm.freetls.fastly.net/i/u/64s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"medium"},{"#text":"https://lastfm.freetls.fastly.net/i/u/174s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"large"},{"#text":"https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png","size":"extralarge"}],"@attr":{"rank":"9"}},{"name":"Boys Don't Cry","duration":"139","mbid":"fa1cf5a0-b942-46ed-9ca0-3773fb52cbb6","url":"https://www.last.fm/music/The+Cure/_/Boys+Don%27t+Cry","streamable":{"#text":"0","fulltrack":"0"},"artist":{"name":"The Cure","mbid":"69ee3720-a7cb-4402-b48d-a02c366f2bcf","url":"https://www.last.fm/music/The+Cure"},"image":[{"#text":"https://lastfm.freetls.fastly.net/i/u/34s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"small"},{"#text":"https://lastfm.freetls.fastly.net/i/u/64s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"medium"},{"#text":"https://lastfm.freetls.fastly.net/i/u/174s/2a96cbd8b46e442fc41c2b86b821562f.png","size":"large"},{"#text":"https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png","size":"extralarge"}],"@attr":{"rank":"10"}}],"@attr":{"tag":"80s","page":"1","perPage":"10","totalPages":"9187","total":"91862"}}}
#     listOfSongs = []
#     for i in range( len (listOfJsons)):
#         for ii in range( len (listOfJsons[i]["tracks"]["track"])):
#              listOfSongs.append(listOfJsons[i]["tracks"]["track"][ii]["name"]+"; "+ listOfJsons[i]["tracks"]["track"][ii]["artist"]["name"])
#     print(len(listOfSongs))
#     return listOfSongs

# def oneTrack(artist, title):
#     artist = getRidOfSpaces(artist)
#     title = getRidOfSpaces(title)
#     stringer = "http://ws.audioscrobbler.com/2.0/?method=track.getsimilar&artist="+ artist +"&track="+ title+"&api_key="+ config.API_key +"&format=json"

def getRidOfSpaces(name):
     name = name.strip() #just to be safe about trailing spaces
     newName = ""
     for i in range(len(name)):
        if name[i] == " " and name[i+1] != " ":
            newName = newName + "+"           
        elif name[i] == " ":
           newName = newName
        else:
            newName = newName + name[i]
      
     name = newName

     return name

if __name__ == '__main__':
      getPlaylistInfo(playlist)
      x=  moreProcessTags()
      youTube(x)
      y= recs()
      realRecs(y, x)
    # realJSON= getTags("Michael Jackson", "Billie Jean")
    # processedTags =processTags(realJSON)
    # lister = oneTag(processedTags)
    # getSongs(lister)
    # with open(os.path.join("backend", "tracks.txt"), "a") as f:
    #     f.write(lister[1])
        # for section in lister:
        #     f.write(section)
    #getRidOfSpaces("high  for this ")