from odoo import http
from odoo.http import request

class MyController(odoo.http.Controller):
    @route('/myurl', auth='public')
    def my_controller(self):
        my_scope = {'text':'hell to world!'}
        return request.render('views/qweb_template_for_controller.xml', my_scope)