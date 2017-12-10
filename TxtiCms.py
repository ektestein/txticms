# internal modules
from abc import abstractmethod, abstractstaticmethod
import argparse
from os.path import basename, splitext
from random import random
import webbrowser

# external modules
import requests
from telegraph import Telegraph

# project modules
import settings


class FileHandler(object):
	@abstractmethod
	def __create(self):
		pass

	# @abstractstaticmethod
	def __edit(self):
		pass

	@abstractmethod
	def __delete_page(self):
		pass


class TxtiCms(FileHandler):
	__txti_addr = 'http://txti.es'
	# headers = {'user-agent': 'my-app/0.0.1'}
	headers = {
			'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0',
			'Accept': 'text / css, * / *;q = 0.1',
			'Accept-Language': 'ru - RU, ru;q = 0.8, en - US;q = 0.5, en;q = 0.3',
			'Accept-Encoding': 'gzip, deflate',
			'Referer': 'http://txti.es/',
			'Cookie': 'PHPSESSID = 5g7phh3vom2ggnbav52v8et6l2',
			'Connection': 'keep-alive'}

	def __init__(self):
		pass

	# @staticmethod
	def update(self):
		# __class__.__create(path)
		self.__edit()

	@staticmethod
	def __create(path):
		with open(path) as source:
			text = source.read()

		custom_url = splitext(basename(path))[0] + '-' + str(random()).rsplit('.', 1)[1]  # сделать на uuid
		edit_code = hash(text)

		requests.post(
			TxtiCms.__txti_addr,
			{
				# техническая информация
				'form_level': 3,
				'submit': 'Save+and+done',
				# содержимое полей
				'content': text,
				'custom_url': custom_url,
				# 'custom_edit_code': settings.password,
				'custom_edit_code': edit_code,
				'title': '',
				'author': settings.author,
				'description': settings.description
			},
			headers=TxtiCms.headers)
		print('Page: %s\nPassword: %s' % (custom_url, edit_code))

		webbrowser.open(__class__.__txti_addr + '/' + custom_url)

	# @staticmethod
	def __edit(self):
		ans = requests.post(
			'http://txti.es/testfile-26661296874238893/edit',
			{
				# техническая информация
				'form_level': 3,
				# 'submit': 'Save+and+done',
				'update': 'Save+and+done',
				# содержимое полей
				'content': 'new content',
				'custom_url': 'testfile-26661296874238893',
				# 'custom_edit_code': settings.password,
				'custom_edit_code': '-3269072730032607315',
				'title': '',
				'username': '',
				'author': settings.author,
				'description': settings.description,
				'edit_code': '-3269072730032607315',
				'original_url': 'testfile-26661296874238893'
			},
			headers=TxtiCms.headers)
		print(ans.text)

		webbrowser.open('http://txti.es/testfile-26661296874238893')

	def __delete_page(self):
		pass


class TelegraphCms(FileHandler):
	pass


if __name__ == '__main__':
	argparser = argparse.ArgumentParser()
	argparser.add_argument('path', help='Путь до файла, который требуется залить на сайт')
	path2file = argparser.parse_args().path

	telegraph = Telegraph()

	telegraph.create_account(short_name='1338')

	# response = telegraph.create_page(
	# 	'Hey',
	# 	html_content='<p>Hello, world!</p>'
	# )
	# response = telegraph.edit_page('http://telegra.ph/Hey-12-07-3', 'Hey', 'smth new')
	# print('http://telegra.ph/{}'.format(response['path']))
	# print(111)
	# print(telegraph.get_page('http://telegra.ph/Hey-12-07-3', True))
	# print(telegraph.get_page('api', True))
	print(telegraph.get_page('api', False))


__docformat__ = 'restructuredtext ru'
