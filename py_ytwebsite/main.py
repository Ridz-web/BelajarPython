import yt_dlp
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def yt_downloader():
    massage = ""
    yt_url = request.form.get('yt_url')
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',  # Nama file sesuai dengan judul video
    }
    try:
        if request.method == "POST":
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([yt_url])
            massage = "Video berhasil diunduh!"
    except Exception as e:
        massage = f"Terjadi kesalahan: {e}"

    return render_template("index.html", massage = massage)



if __name__ == "__main__":
     app.run(debug=True)
