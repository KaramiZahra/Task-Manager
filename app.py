from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"Task {self.id}"


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        current_task = request.form["content"]
        new_task = Task(content=current_task)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            return f"Operation failed: {e}"
    else:
        tasks = Task.query.all()
        return render_template("index.html", tasks=tasks)


@app.route("/delete/<int:id>")
def delete(id: int):
    delete_task = Task.query.get_or_404(id)
    try:
        db.session.delete(delete_task)
        db.session.commit()
        return redirect("/")
    except Exception as e:
        return f"Operation failed: {e}"


@app.route("/edit/<int:id>", methods=["POST", "GET"])
def edit(id: int):
    edit_task = Task.query.get_or_404(id)
    if request.method == "POST":
        edit_task.content = request.form["content"]
        try:
            db.session.commit()
            return redirect("/")
        except Exception as e:
            return f"Operation failed: {e}"
    else:
        return render_template("edit.html", task=edit_task)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
