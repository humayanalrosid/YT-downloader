from pytube import YouTube

link = input("Enter Youtube Video Link : ")

Video_details = YouTube(link)

print("""\n--------------------------------\n\tInstruction 
Type 1 for Title Name 
Type 2 For Thumbnail Download 
Type 3 For Audio Download
Type 4 For Video Download
--------------------------------""")

user_choice = int(input("Enter Your Choice : "))

if user_choice == 1:
    print(f"Video Title Is : {Video_details.title}")
elif user_choice == 2:
    print(f"To Download Thumbnail Click This Link : {Video_details.thumbnail_url} ")
elif user_choice == 3:
    audio = Video_details.streams.filter(only_audio=True)
    audio_quality = list(enumerate(audio))

    for songs in audio_quality:
        print(songs)

    download_audio = int(input("Choose a number from above list : "))
    audio[download_audio].download()
    print("Hurrah!!! Audio Download Successfully.........")

else:
    video = Video_details.streams.filter(file_extension="mp4", progressive=True)
    video_quality = list(enumerate(video))

    for videos in video_quality:
        print(videos)

    download_video = int(input("Choose a number from above list : "))
    video_quality[download_video].download()
    print("Hurrah!!! Video Download Successfully.........")




