import yt_dlp

def youtube_downloader():
    url = input("Masukkan URL YouTube: ")
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',  # Nama file sesuai dengan judul video
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Video berhasil diunduh!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    youtube_downloader()
