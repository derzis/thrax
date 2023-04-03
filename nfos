import os

# specify the directory where the music and music video files are stored
dir_path = "/path/to/music/files"
video_dir_path = "/path/to/music/videos"
artist_thumb_dir_path = "/path/to/artist/thumbnails"
artist_poster_dir_path = "/path/to/artist/posters"

# iterate over all files in the directory
for filepath in os.listdir(dir_path):
    if filepath.endswith(".mp3"):
        # extract artist and title from filename
        artist, title = filepath[:-4].split(" - ")

        # handle the case where the title contains " & " before " - "
        if " & " in artist:
            artists = artist.split(" & ")
        else:
            artists = [artist]

        # create NFO file with same name as music file
        nfo_filename = f"{filepath[:-4]}.nfo"
        nfo_filepath = os.path.join(dir_path, nfo_filename)
        with open(nfo_filepath, "w") as nfo_file:
            nfo_file.write(f"<music>\n  <title>{title}</title>\n")
            for a in artists:
                nfo_file.write(f"  <artist>\n    <name>{a}</name>\n")
                artist_thumb_path = os.path.join(artist_thumb_dir_path, f"{a}.jpg")
                nfo_file.write(f"    <thumb>{artist_thumb_path}</thumb>\n")
                artist_poster_path = os.path.join(artist_poster_dir_path, f"{a}.jpg")
                nfo_file.write(f"    <poster>{artist_poster_path}</poster>\n")
                nfo_file.write("  </artist>\n")
            nfo_file.write(f"  <thumb>/path/to/album/{artist}.jpg</thumb>\n")
            nfo_file.write("</music>")

for filepath in os.listdir(video_dir_path):
    if filepath.endswith(".mp4"):
        # extract artist and title from filename
        artist, title = filepath[:-4].split(" - ")

        # handle the case where the title contains " & " before " - "
        if " & " in artist:
            artists = artist.split(" & ")
        else:
            artists = [artist]

        # create NFO file with same name as music video file
        nfo_filename = f"{filepath[:-4]}.nfo"
        nfo_filepath = os.path.join(video_dir_path, nfo_filename)
        with open(nfo_filepath, "w") as nfo_file:
            nfo_file.write(f"<musicvideo>\n  <title>{title}</title>\n")
            for a in artists:
                nfo_file.write(f"  <artist>\n    <name>{a}</name>\n")
                artist_thumb_path = os.path.join(artist_thumb_dir_path, f"{a}.jpg")
                nfo_file.write(f"    <thumb>{artist_thumb_path}</thumb>\n")
                artist_poster_path = os.path.join(artist_poster_dir_path, f"{a}.jpg")
                nfo_file.write(f"    <poster>{artist_poster_path}</poster>\n")
                nfo_file.write("  </artist>\n")
            nfo_file.write(f"  <thumb>/path/to/album/{artist}.jpg</thumb>\n")
            nfo_file.write("</musicvideo>")
