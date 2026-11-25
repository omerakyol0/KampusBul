from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from pathlib import Path

app = Flask(__name__)

DB_PATH = Path(__file__).resolve().parent / "kampusbul.db"


# Veritabani olusturma
def veritabani_olustur():
    with sqlite3.connect(DB_PATH) as baglanti:
        baglanti.execute("""
            CREATE TABLE IF NOT EXISTS ilanlar (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                esya_adi TEXT NOT NULL,
                aciklama TEXT NOT NULL,
                konum TEXT NOT NULL,
                tur TEXT NOT NULL,
                durum TEXT DEFAULT 'Aktif',
                tarih DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)


# Ana sayfa
@app.route("/")
def ana_sayfa():
    return redirect(url_for("ilan_ekle"))


# Ilan olusturma
@app.route("/ilan-ekle", methods=["GET", "POST"])
def ilan_ekle():

    if request.method == "POST":

        esya_adi = request.form.get("esya_adi", "").strip()
        aciklama = request.form.get("aciklama", "").strip()
        konum = request.form.get("konum", "").strip()
        tur = request.form.get("tur", "")

        # Zorunlu alan kontrolu
        if not all([esya_adi, aciklama, konum]) or tur not in ("Kayıp", "Bulunan"):
            return render_template(
                "ilan_ekle.html",
                hata="Lütfen bütün alanları doldurunuz."
            ), 400

        # Ilani veritabanina kaydet
        with sqlite3.connect(DB_PATH) as baglanti:
            baglanti.execute("""
                INSERT INTO ilanlar
                (esya_adi, aciklama, konum, tur)
                VALUES (?, ?, ?, ?)
            """, (esya_adi, aciklama, konum, tur))

        return redirect(url_for("ilan_ekle", basarili=1))

    return render_template(
        "ilan_ekle.html",
        basarili=request.args.get("basarili") == "1"
    )


veritabani_olustur()

if __name__ == "__main__":
    app.run(debug=True)