# -*- coding: utf-8 -*-

class config(object):
	program = [3,4,5]
	department = {
		'3': [33,34],
		'4': [11,12,13,14,15,16,18,19,20,23,31,32,41,42,43,44,61],
		'5': [35,52,53,54,55]
	}
	campus = [0,1,2]
	class_program = ['01',11,12]

	user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1'
	device = {
		'brand': '0x00000000',
		'hardware': '0x00000001',
		'version': '0x00000002',
		'manufacture': '0x00000003',
		'model': '0x00000004',
		'name': '0x00000005',
		'product': '0x00000006',
		'regId': '0x00000007',
		'secureId': '0x00000008',
		'serial': '0x00000009',
		'id': 0
	}
	
	api_endpoint = 'https://sia.mercubuana.ac.id/mobile/index.php/api'
	http_api_path =  {
		'login': '/login'
	}

	etc_http_path = {
		'sia_pc': {
			'login': 'https://sia.mercubuana.ac.id/gate.php/login',
			'biomhs': 'https://sia.mercubuana.ac.id/akad.php/biomhs/lst',
			'editmhs': 'https://sia.mercubuana.ac.id/akad.php/biomhs/editmhs/{NIM}',
		},
		'sso_pc': {
			'login': 'https://sso.mercubuana.ac.id/',
			'updatedata': 'https://sso.mercubuana.ac.id/Users/update',
			'changepasswd': 'https://sso.mercubuana.ac.id/Users/edit'
		}
	}