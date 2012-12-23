# -*- coding: utf-8 -*- #

from cumulus.template import render

def home(seq):
	return render('index.html', {
		'uid': seq.req.session.get('uid', False)
	})
