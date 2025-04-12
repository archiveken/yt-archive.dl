import os
from yt_dlp import YoutubeDL

def download_video(url, output_format="mp3"):
    # Options for yt-dlp
    ydl_opts = {
        "format": "bestaudio/best",  # Get the best audio/video format
        "postprocessors": [{
            "key": "FFmpegExtractAudio",  # Extract audio using ffmpeg
            "preferredcodec": output_format,  # Convert to the desired format
            "preferredquality": "192",  # Set quality (192kbps for MP3)
        }],
        "outtmpl": "%(title)s.%(ext)s",  # Save file as video title
        "quiet": True,  # Suppress output for minimalism
    }

    # Download the video/audio
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    print("=== Minimalist YouTube Converter ===")
    url = input("Enter YouTube URL: ")
    print("Choose output format:")
    print("1. MP3 (Audio)")
    print("2. MP4 (Video)")
    choice = input("Enter choice (1/2): ")

    if choice == "1":
        output_format = "mp3"
    elif choice == "2":
        output_format = "mp4"
    else:
        print("Invalid choice.")
        return

    print("Downloading...")
    try:
        download_video(url, output_format)
        print("Download complete!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
