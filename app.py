import os
from os.path import join, dirname
from dotenv import load_dotenv

from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from pymongo import MongoClient
from datetime import datetime

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME = os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

connection_string = 'mongodb+srv://ahnafb:nanaf2730@cluster0.qzd2yiy.mongodb.net/?retryWrites=true&w=majority'

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')