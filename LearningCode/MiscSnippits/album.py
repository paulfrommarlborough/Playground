# album.py

def make_album(album_title, album_artist, album_label, album_songs):
    album_info = { 'title': album_title,
                    'artist': album_artist,
                    'label': album_label,
                    'song_count': album_songs
    } 
    return album_info


def print_albums(recs):
    for rec in recs:
        msg = f"record: {rec['title']}" 
        print(msg)

records = []

record = make_album('revolver', 'beatles', 'apple', 12)
records.append(record)

record = make_album('darkside of the moon', 'pink floyd', 'electra',4)
records.append(record)

userinput=""
while userinput != 'q':
    userinput = input('album name [q]: ')
    if (userinput=='q'):
        break
    al_name = userinput
    
    userinput = input('album artist [q]: ')
    if (userinput=='q'):
        break
    al_artist = userinput
    
    userinput = input('album label [q]: ')
    if (userinput=='q'):
        break
    al_label = userinput
    
    userinput = input('album song count [q]: ')
    if (userinput=='q'):
        break
    al_songcount = int(userinput)
    
    record = make_album(al_name, al_artist, al_label, al_songcount)
    records.append(record)

print(f"records are...")
print(records)


print_albums(records)