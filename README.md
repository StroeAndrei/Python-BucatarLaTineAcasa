# Bucatar la tine acasa
### Tehnologii folosite: python, flask, javascript, html, css
Un website construit pentru un bucatar care ofera servicii personalizate de "bucatar la tine acasa". Aplicatia foloseste un template obtinut de la [Mashup](http://www.mashup-template.com/)<br/><br/>

### Instructiuni
- Descarcam aplicatia si extragem fisierele intr-un dosar. 
- Din linia de comanda ne deplasam in dosarul aplicatiei si instalam mediul virtual pentru Python 
(este necesar ca Python sa fie instalat in sistem) executand comanda "py -3 -m venv venv" dupa care activam 
mediul virtual tot din linia de comanda "venv\Scripts\activate" (pentru SO Windows).
- Extensiile folosite in aplicatie se regasesc in fiserul requirements.txt. Pentru instalare, se executa din 
dosarul aplicatiei (dupa ce am activat mediul virtual) comanda "pip install -r requirements.txt". 
- Se seteaza variabila FLASK_APP din linia de comanda astfel "set FLASK_APP=server.py" (pentru SO Windows). 
Pentru extensia Flask-Mail sunt necesare doua variabile de mediu, una pentru adresa de email si cealalta 
pentru parola cu denumirile: GMAIL_ADDR_AFU si GMAIL_PASS_AFU.
- Pentru a porni server-ul local si a rula aplicatia vom executa din linia de comanda "flask run".

Homepage
![homepage](https://github.com/StroeAndrei/Python-BucatarLaTineAcasa/blob/master/screenshots/homepage.PNG)<br/>

Servicii
![servicii](https://github.com/StroeAndrei/Python-BucatarLaTineAcasa/blob/master/screenshots/servicii.PNG)<br/>

Contact
![contact](https://github.com/StroeAndrei/Python-BucatarLaTineAcasa/blob/master/screenshots/contact.PNG)<br/>

Odata utilizat formularul de contact, bucatarul va primi pe adresa de email mesajele corespunzatoare
![mesaje](https://github.com/StroeAndrei/Python-BucatarLaTineAcasa/blob/master/screenshots/mesaje_primite.PNG)<br/>

De asemenea datele vor fi salvate pentru o utilizare ulterioara (extragere adrese de email) intr-un fisier Excel
![mesaje](https://github.com/StroeAndrei/Python-BucatarLaTineAcasa/blob/master/screenshots/mesaje_excel.PNG)<br/>








