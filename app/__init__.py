from flask import Flask

app = Flask(__name__)
# 解决循环导入问题
from app import routes
