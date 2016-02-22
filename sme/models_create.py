#!/usr/bin/env python


"""Models."""


from sqlalchemy import *
from os import environ
SME_SQLALCHEMY_DATABASE_URI = environ['SME_DEV_SQLALCHEMY_DATABASE_URI']


db = create_engine(SME_SQLALCHEMY_DATABASE_URI)
db.echo = False
metadata = MetaData(db)

text = Table('text', metadata,
    Column('text_id', Integer, primary_key=True),
    Column('text_md5', String),
    Column('text_keywords', String),
    Column('text_fingerprint', String),
    Column('text', String),
)

text.create(checkfirst=True)
