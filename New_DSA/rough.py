# from pytube import YouTube
# import os
# # YouTube video URL
# video_url = 'https://www.youtube.com/watch?v=CHSnz0bCaUk&t=137s'

# # Output directory to save the downloaded video
# save_path = 'D:/'

# # Create a YouTube object
# video = YouTube(video_url)

# # Get streams with 4K resolution and includes both video and audio tracks
# streams = video.streams.filter(res='2160p', only_video=True)

# if streams:
#     # Select the first stream from the filtered streams
#     stream = streams.first()

#     # Download the selected stream along with audio
#     audio_stream = video.streams.get_audio_only()
#     stream.download(output_path=save_path, filename='video')
#     audio_stream.download(output_path=save_path, filename='audio')

#     # Merge video and audio into a single file
#     video_file = save_path + 'video.mp4'
#     audio_file = save_path + 'audio.mp4'
#     merged_file = save_path + 'merged.mp4'
#     os.system(f'ffmpeg -i {video_file} -i {audio_file} -c copy {merged_file}')

#     # Optional: Delete video and audio files
   

#     print("Video Downloaded Successfully")
# else:
#     print("No 4K video with audio available for download.")


# print(10/10)


# for i in range(ord('A'), ord('Z') + 1):
#     print(chr(i), end=" ")


print(ord('A'))