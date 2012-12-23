# -*- coding: utf-8 -*- #

from cumulus.utils import MakeResp

def index(seq):
	if not seq.req.session.get('uid'):
		return MakeResp('redirect', seq.conf['builtins']['prefix'])
	return '업로드'
