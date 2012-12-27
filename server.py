# -*- coding: utf-8 -*- #

from cumulus.engine import Cumulus
application = Cumulus({
	'urls': [
		('^/(home)?$', 'main.home'),
		('^/login/?$', 'main.login'),
		('^/logout/?$', 'main.logout'),
		('^/upload/?$', 'upload.index')
	],
	'db': {
		'location': 'mysql://localhost/pkm',
		'username': 'headcrabtan',
		'password': '1234'
	},
	'server': { 'KeyPhrase': 'Za2A?haT-q6gudR?7!SE7%p#' },
	'path': { 'AppRoot': '/srv/private/headcrabtan/pkm' },
	'builtins': {
		'prefix': '/pkm/',
		'static': 'InternalStatic'
	},
	'error': {
		'debug': True,
		'template': 'error/default.html'
	},
	'status': {
		404: ['Not Found', 'URL에 해당하는 페이지 또는 자원을 찾을 수 없습니다.'],
		500: ['Internal Server Error', '내부 오류가 발생했습니다.']
	}
}).WSGIApp
