from odoo import http
from odoo.http import request

class MyController(http.Controller):
    @http.route('/myurl', auth='public', website=True)
    def my_controller(self):
        my_scope = {'text':'hell to world!'}
        return request.render('controller_template', my_scope)