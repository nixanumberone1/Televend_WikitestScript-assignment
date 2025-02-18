Requirments:

1. Instalacija Pythona sa official websitea https://www.python.org/downloads/  ili u VSCode pod extenzije -> Python-> install. Nakon toga otvoriti command palletu (CTRL-Shift-X) i Type Python: Select Interpreter and choose the installed Python version.

2. Instalacija Google chrome browsera https://www.google.com/chrome/?brand=YTUH&ds_kid=43700078760035388&gad_source=1&gclid=Cj0KCQiA_NC9BhCkARIsABSnSTYH__yX7GD2L7RbLz-zzBramys63LTMz0laAs2bTdbzTrSJQHWwVPMaAj2_EALw_wcB&gclsrc=aw.ds 

3.Instalacija VS code (Optional)

4. Instalacija ChromeDrivera https://sites.google.com/chromium.org/driver/  ili ako je NodeJs. instaliran, napraviti novi repo i u cmd napisati  "npm install chromedriver@132.0.0" za spremanje webdrivera (verziju 132 ja trenuto imam kao latest) i povezati %PATH% globalu varijablu sa folderom gdje je spremljen webdriver

5. Instalacija Seleniuma, u repo po izboru gdje ce biti spremljen projekt u cmd upisati: "pip install selenium"


Pokretanje skripte u VScode:

1. pozicioniranje u repo gdje se spremljeni testovi sa "cd" naredbom ili run iz glavnog repo-a i run sa naredbom:  "python Py_automaton_scripts/wiki_test.py"

2. Report ispis se sprema nakon izvrsenja svakog testa pod "test_report.txt" u glavnu mapu projekta