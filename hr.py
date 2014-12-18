# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, osv

class hr_sanction(osv.osv):
    _name = 'hr.sanction'
    _description = 'HR Employee Sanctions'

    _columns = {
        'employee_id': fields.many2one('hr.employee','id','Employee ID'),
	'sanction_type': fields.selection((('A','Apercibimiento'),
					   ('B','Apercibimiento Severo'),
					   ('C','Suspension')),'Sanction Type'),
        'sanction_date': fields.date('Sanction Date'),
        'comment': fields.text('Additional Information'),
        'signed': fields.boolean('Signed'),
	'job_id': fields.related(
		'employee_id',
		'job_id',
		type="many2one",
		relation="hr.job",
		string="Job",
		store=False
		)
    }

hr_sanction()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
