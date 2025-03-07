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
    return cleaned_list


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
 