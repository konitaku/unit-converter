from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired
from converter import convert
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")


class ConvertForm(FlaskForm):
    number = StringField(validators=[DataRequired()], render_kw={"placeholder": "数字を入力"})
    unit_select1 = SelectField(
        choices=[("m", "メートル"), ("mile", "マイル"), ("yard", "ヤード"), ("feet", "フィート"), ("inch", "インチ")],
        validators=[DataRequired()]
    )
    unit_select2 = SelectField(
        choices=[("m", "メートル"), ("mile", "マイル"), ("yard", "ヤード"), ("feet", "フィート"), ("inch", "インチ")],
        validators=[DataRequired()]
    )


@app.route("/", methods=["POST", "GET"])
def home():
    form = ConvertForm()
    result = 0
    if form.validate_on_submit():
        result = convert(float(form.number.data), form.unit_select1.data, form.unit_select2.data)

        form = ConvertForm(
            number=form.number.data,
            unit_select1=form.unit_select1.data,
            unit_select2=form.unit_select2.data
        )
    return render_template("index.html", form=form, pagename="home", result=result)


@app.route("/other")
def other():
    return render_template("other.html")


if __name__ == "__main__":
    app.run(debug=True)
