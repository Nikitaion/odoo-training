from odoo import http
from odoo.http import request
import json

class MyController(http.Controller):
    @http.route('/myurl', auth='public', methods=['POST'], type='json')
    def my_controller(self):
        my_json={'text':'Hello json!'}
        return json.dumps(my_json)