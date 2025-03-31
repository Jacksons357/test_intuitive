from flask import Flask
from controllers import operator_controller
from flask_cors import CORS

class RunApi:
  def __init__(self):
    self.app = Flask(__name__)
    CORS(self.app)
    self.setup_routes()

  def setup_routes(self):
    self.app.add_url_rule('/api', 'list_operators', operator_controller.list_operators, methods=['GET'])
    self.app.add_url_rule('/api/search', 'search_operators', operator_controller.search_operators, methods=['GET'])

  def run(self):
    self.app.run(debug=False)