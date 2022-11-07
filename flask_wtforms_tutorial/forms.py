"""Form class declaration."""
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (
    DateField,
    PasswordField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
)
from datetime import date
from wtforms.fields.html5 import DateField
from wtforms.validators import URL, DataRequired, Email, EqualTo, Length

class StockForm(FlaskForm):
    """Generate Your Graph."""
    
    #THIS IS WHERE YOU WILL IMPLEMENT CODE TO POPULATE THE SYMBOL FIELD WITH STOCK OPTIONS
    symbol = SelectField("Choose Stock Symbol",[DataRequired()],
        choices=[
            ("IBM", "IBM"),
            ("GOOGL", "GOOGL"),
        ],
    )

    chart_type = SelectField("Select Chart Type",[DataRequired()],
        choices=[
            ("Bar", "1. Bar"),
            ("Line", "2. Line"),
        ],
    )

    time_series = SelectField("Select Time Series",[DataRequired()],
        choices=[
            ("Intraday", "1. Intraday"),
            ("Daily", "2. Daily"),
            ("Weekly", "3. Weekly"),
            ("Monthly", "4. Monthly"),
        ],
    )

    start_date = DateField("Enter Start Date")
    end_date = DateField("Enter End Date")
    submit = SubmitField("Submit")



