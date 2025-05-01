import yt_dlp
import subprocess
import os

def download_and_convert():
    url = input("Paste the YouTube video URL: ")

    output_template = "%(title)s.%(ext)s"

    ydl_opts = {
        'outtmpl': output_template,
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mkv'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        downloaded_file = ydl.prepare_filename(info)

        if not downloaded_file.endswith('.mkv'):
            print("The file is already in MP4 or another format. No conversion needed.")
            return

    mp4_file = os.path.splitext(downloaded_file)[0] + ".mp4"

    cmd = [
        "ffmpeg",
        "-i", downloaded_file,
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "192k",
        "-strict", "experimental",
        mp4_file
    ]

    subprocess.run(cmd)

    print("Conversion completed:", mp4_file)

    # Optional: delete original MKV file
    os.remove(downloaded_file)

if __name__ == "__main__":
    download_and_convert()