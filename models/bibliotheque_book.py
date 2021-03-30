from odoo import fields, models ,api

class Book(models.Model):
	_inherit = 'bibliotheque.book'
	is_available = fields.Boolean('Is Available?')
	isbn = fields.Char(help="Use a valid ISBN-13 or ISBN-10.")
	publisher_id = fields.Many2one(index=True)

	@api.multi
	def _check_isbn(self):
		self.ensure_one()
		digits =[int(x) for x in self.isbn if x.isdigit()]
		if len(digits) == 10:
		    _sum = 0
		    for i in range(9):
		        if 0 <= int(digits[i]) <= 9:
		            _sum += int(digits[i]) * (10 - i)
		        else:
		            return False
		          
		    if(digits[9] != 'X' and 0 <= int(digits[9]) <= 9):
		        return False
		     
		    _sum += 10 if digits[9] == 'X' else int(digits[9])
		      	  
		    return (_sum % 11 == 0)	


		# 	ponderations = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		# 	total = sum(a* b for a,b in zip(digits[:9], ponderations))
		# 	check = total % 11
		# 	return digits[-1] == check
		# else:
		# 	return super()._check_isbn()	


      