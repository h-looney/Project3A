"""Form class declaration."""
import csv
import requests 

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
    
    CSV_URL = 'https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=AU4UXQO6WFYENR4J'

    choices = []

    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        for row in my_list:
            choices.append((row[0], row[0]))
    
    #THIS IS WHERE YOU WILL IMPLEMENT CODE TO POPULATE THE SYMBOL FIELD WITH STOCK OPTIONS
    symbol = SelectField("Choose Stock Symbol",[DataRequired()],
         choices=choices,
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



