from flask import Flask, render_template
app = Flask(__name__)
BASE = "https://public.tableau.com/views/Health360ComprehensiveHealthcareRiskDiseaseAnalytics_17929898861220/"
VIEWS = {
    "dashboard": BASE + "Dashboard1?:showVizHome=no&:embed=true&:display_count=n&:language=en-GB",
    "story": BASE + "Story1?:showVizHome=no&:embed=true&:display_count=n&:language=en-GB"
}
@app.route("/")
def home():
    return render_template("index.html", page="home")
@app.route("/about")
def about():
    return render_template("about.html", page="about")
@app.route("/dashboard")
def dashboard():
    return render_template("visualization.html", page="dashboard", title="Dashboard",
        subtitle="Interactive dashboard visualizing our data insights and operational metrics.",
        view_url=VIEWS["dashboard"], view_type="dashboard")
@app.route("/story")
def story():
    return render_template("visualization.html", page="story", title="Story",
        subtitle="Smart Healthcare Analytics: Patient Risk & Lifestyle Insights",
        view_url=VIEWS["story"], view_type="story")
@app.route("/faq")
def faq():
    return render_template("faq.html", page="faq")
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
