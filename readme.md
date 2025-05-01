```markdown
# yt-downloader – Download and Convert YouTube Videos to MP4 🎥➡️📦

**yt-downloader** is a simple Python tool that allows you to download YouTube videos and automatically convert them to MP4 format if necessary. It uses `yt-dlp` for downloading and `ffmpeg` for efficient video conversion.

---

## ✨ Features

- Download high-quality YouTube videos with one command  
- Automatically converts MKV files to MP4 using `ffmpeg`  
- Keeps the process fast and simple  
- Optional removal of the original MKV file after conversion  

---

## ⚙️ Requirements

- Python 3.10 or higher  
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)  
- [ffmpeg](https://ffmpeg.org/)  

---

## 🚀 Setup & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/yt-downloader
   ```

2. **Navigate to the project folder**
   ```bash
   cd yt-downloader
   ```

3. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate     # (Linux/macOS)
   .\env\Scripts\activate      # (Windows)
   ```

4. **Run the application**
   ```bash
   python yt_downloader.py
   ```

---

## 📁 Notes

- Make sure `ffmpeg` is installed and available in your system PATH.  
- The script downloads videos as `.mkv` and converts them to `.mp4` automatically.  
- Original `.mkv` files are deleted after conversion to save space (you can disable this by commenting out the relevant line in the code).  

---

## 🛠 Example

```bash
Paste the YouTube video URL: https://www.youtube.com/watch?v=example
Conversion completed: example_video.mp4
```

---

