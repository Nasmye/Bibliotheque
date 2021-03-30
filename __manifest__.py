{
	'name': 'Bibliotheque members',
	'description': 'Manage people who will be able to borrow books',
	'author':'Yasmine C',
	'depends': ['bibliotheque' ,'mail'],

	'data': [
        'views/book_views.xml',
        'security/ir.model.access.csv',
        'views/member_views.xml',
        
    ],

}