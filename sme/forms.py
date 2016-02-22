#!/usr/bin/env python


"""Forms."""

from flask.ext.wtf import Form
from wtforms.fields import TextAreaField, SubmitField
from wtforms.validators import DataRequired


class MainForm(Form):
    """Main form."""
    text_1 = TextAreaField("Text 1", [DataRequired("Text 1 is required.")])
    text_2 = TextAreaField("Text 2", [DataRequired("Text 2 is required.")])
    submit = SubmitField("Check")
