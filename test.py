import moviepy.editor as mp

#Si\ziphiwe To\po

def extract_part(video_path, start_time, end_time, output_path):
    # Load the video
    video = mp.VideoFileClip(video_path)
    
    # Extract the part
    part = video.subclip(start_time, end_time)
    
   
    part.write_videofile(output_path, codec='libx264')

# Paths to your video and output file
video_path = r'C:\Users\ZZ01MC864\Desktop\Faceless\Demo.mp4'
output_path = r'C:\Users\ZZ01MC864\Desktop\Faceless\extracted_part.mp4'

# Times to extract (in seconds)
start_time = 10  # Start at 10 seconds
end_time = 20    # End at 20 seconds

# Extract the part
extract_part(video_path, start_time, end_time, output_path)

