# -*- coding: utf-8 -*- #

from cumulus.engine import Cumulus
application = Cumulus({
	'urls': [],
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
	'error': { 'debug': True }
}).WSGIApp
