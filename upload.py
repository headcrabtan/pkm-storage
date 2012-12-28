# -*- coding: utf-8 -*- #

from cumulus.utils import MakeResp
from cumulus.template import render

from common import menu
context = { 'Menu': menu, 'ActiveMenu': None }

def index(seq):
	uid = seq.req.session.get('uid')
	if not uid: return MakeResp('redirect', '/login')

	context['ActiveMenu'] = '업로드'
	context['UploadResult'] = None

	if seq.req.method == 'POST':
		file = seq.req.post.get('Pkm', {})
		secret = seq.req.post.get('Secret')
		content = file.get('content')

		if content:
			try:
				from hashlib import sha1
				filename = sha1(content).hexdigest()
				file = open('files/%s.pkm' % filename, 'wb')
				file.write(content)
				file.close()

				from parser import PkmLoader
				content = PkmLoader(content)
				content['uid'] = uid
				content['filename'] = filename
				if secret: secret = '1'
				else: secret = '0'
				content['secret'] = secret
				seq.db.InsertRow('upload', content)

				context['UploadResult'] = '.pkm 파일이 성공적으로 저장되었습니다.'
			except:
				context['UploadResult'] = """
					올바른 .pkm이 아니거나 파일을 저장하는 데 오류가 발생했습니다.
				""".strip()
		else:
			context['UploadResult'] = '파일이 선택되지 않았습니다.'

	return render('upload.html', context)
