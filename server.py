#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import cgitb

# Activăm afișarea erorilor în browser dacă ceva nu merge bine
cgitb.enable()

# Spunem serverului că vom afișa o pagină HTML ca răspuns
print("Content-Type: text/html; charset=utf-8\n")

# Preluăm datele trimise din formularul HTML
form = cgi.FieldStorage()

nume = form.getvalue("nume_client")
model = form.getvalue("model_telefon")
cantitate = form.getvalue("cantitate_produse")

# SARCINA PRINCIPALĂ: Salvarea datelor într-un fișier text pe server
# Deschidem fișierul 'comenzi.txt' în modul 'append' (adaugă la sfârșit fără să șteargă)
with open("comenzi.txt", "a", encoding="utf-8") as f:
    f.write(f"Client: {nume} | Produs: {model} | Cantitate: {cantitate}\n")

# Formăm răspunsul HTML care se va întoarce în browserul utilizatorului
print(f"""
<!DOCTYPE html>
<html>
<head>
    <title>Răspuns Server CGI</title>
    <style>
        body {{ font-family: Arial, sans-serif; text-align: center; padding-top: 50px; background-color: #f4f4f9; }}
        .box {{ background: white; padding: 30px; display: inline-block; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }}
        h1 {{ color: #27ae60; }}
        a {{ color: #007bff; text-decoration: none; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="box">
        <h1>✔ Comandă înregistrată pe Server!</h1>
        <p>Mulțumim, <strong>{nume}</strong>. Datele tale au fost salvate cu succes în baza noastră de date (comenzi.txt).</p>
        <p>Produs solicitat: {model} (Cantitate: {cantitate} buc.)</p>
        <br>
        <a href="/index.html">← Înapoi la magazin</a>
    </div>
</body>
</html>
""")