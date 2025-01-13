from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def Home():
    web_title = 'HALAMAN HOME'
    return render_template('index.html', web_title = web_title)

@app.route("/about")
def About():
    web_title = 'HALAMAN ABOUT'
    return render_template('about.html', web_title = web_title)

@app.route("/usia", methods=['GET', 'POST'])
def Usia():
    if request.method == 'POST':
        tahun_lahir = int(request.form["tahun_lahir"])
        tahun_sekarang = 2025
        usia = tahun_sekarang - tahun_lahir
        return render_template('usia.html', usia = usia)

    return render_template('usia.html', usia = None)

if __name__ == "__main__":
    app.run(debug=True)
