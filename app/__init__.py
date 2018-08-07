from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# 解决循环导入问题
from app import routes
