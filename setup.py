# -*- coding: utf-8 -*-

import save_the_change


try:
	from setuptools import setup

except ImportError:
	from distutils.core import setup

install_requires = []
for line in open('requirements.txt', 'r').readlines():
	if line and line != '\n' and not line.startswith(('#', '-')):
		install_requires.append(line.replace('\n', ''))

setup(
	name="save_the_change",
	version=save_the_change.__version__,
	description="Automatically save only changed model data.",
	long_description="\n\n".join([open('README.rst', 'r').read(), open('HISTORY.rst', 'r').read()]),
	author=save_the_change.__author__,
	author_email=save_the_change.__contact__,
	url=save_the_change.__homepage__,
	license=open('LICENSE', 'r').read(),
	packages=['save_the_change'],
	package_dir={'save_the_change': 'save_the_change'},
	package_data={'': ['README.rst', 'HISTORY.rst', 'LICENSE']},
	include_package_data=True,
	install_requires=install_requires,
	zip_safe=False,
	classifiers=(
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'Natural Language :: English',
		'License :: OSI Approved :: Apache Software License',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
	),
	test_suite='tests.test.run_tests',
)
