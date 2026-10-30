HEALTH360 FLASK WEBSITE

Run on Windows:
1. Extract this ZIP and open the Health360_Flask folder in VS Code.
2. Open Terminal > New Terminal.
3. (Recommended) Create a virtual environment:
   py -m venv .venv
4. Activate it:
   .venv\Scripts\activate
5. Install Flask:
   pip install -r requirements.txt
6. Run the website:
   python app.py
7. Open http://127.0.0.1:5000 in your browser.

Project structure:
app.py
requirements.txt
templates/index.html
static/css/style.css
static/js/script.js

An internet connection is needed for Google Fonts and Tableau Public. The original Tableau Dashboard and Story links are embedded, with direct links as a fallback. If Tableau says content is blocked by the owner, Flask cannot override Tableau's embedding permissions; ask the workbook owner to allow embedding or open the views directly.
