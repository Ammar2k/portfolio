from flask import Flask, abort, render_template

app = Flask(__name__)

projects = [
    {
        "name": "Final Year Project: Autonomous Mobile Robot",
        "thumb": "img/AMR.jpg",
        "hero": "img/AMR.jpg",
        "categories": ["FYP", "Robotics"],
        "slug": "amr",
        "prod": "https://openaccess.cms-conferences.org/publications/book/978-1-958651-11-7/article/978-1-958651-11-7_5",
    },
    {
        "name": "Highway Lane Detection using OpenCV",
        "thumb": "img/lane_detection.png",
        "hero": "img/lane_detection.png",
        "categories": ["Computer Vision"],
        "slug": "highway_lane_detection",
        "prod": "https://github.com/Ammar2k/CV-Projects/tree/master/Highway_Lanes",
    },
    {
        "name": "Traffic Sign Classification",
        "thumb": "img/road_work.png",
        "hero": "img/road_work.png",
        "categories": ["Deep Learning", "CNN"],
        "slug": "traffic_sign_classification",
        "prod": "https://github.com/Ammar2k/CV-Projects/tree/master/traffic_sign_classification",
    },
    # {
    #     "name": "Habit tracking app with Python and MongoDB",
    #     "thumb": "img/habit-tracking.png",
    #     "hero": "img/habit-tracking-hero.png",
    #     "categories": ["python", "web"],
    #     "slug": "habit-tracking",
    #     "prod": "https://udemy.com",
    # },
]

slug_to_project = {project["slug"]: project for project in projects}


@app.route("/")
def home():
    return render_template("projects.html", projects=projects)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(
        f"project_{slug}.html",
        project=slug_to_project[slug],
    )


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404
