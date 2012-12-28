# -*- coding: utf-8 -*- #

from cumulus.utils import MakeResp
from cumulus.template import render

from common import menu
context = { 'Menu': menu, 'ActiveMenu': None }

def home(seq):
	context['ActiveMenu'] = '홈'

	session = seq.req.session.get
	context['user'] = {
		'Uid': session('uid'),
		'Img': session('img')
	}

	return render('index.html', context)

def login(seq):
	if seq.req.session.get('uid'):
		return MakeResp('redirect', '/')

	context['LoginError'] = None

	if seq.req.method == 'POST':
		uid = seq.req.post.get('Id')
		upw = seq.req.post.get('Pw')

		if uid and upw:
			from hashlib import sha1
			select = seq.db.SelectRow(
				'member', ['img'],
				"`uid`='%s' AND `pw`='%s'" % (
					uid, sha1(upw.encode()).hexdigest()
				)
			)

			if len(select) == 1:
				resp = MakeResp('redirect', '/')
				resp['header']['session'] = {
					'uid': uid,
					'img': select[0]['img']
				}
				return resp

			else:
				context['LoginError'] = 'ID 또는 비밀번호가 올바르지 않습니다.'

		else:
			context['LoginError'] = '모든 항목을 입력해 주십시오.'

	return render('login.html', context)

def logout(seq):
	resp = MakeResp('redirect', '/')
	resp['header']['session'] = None
	return resp
