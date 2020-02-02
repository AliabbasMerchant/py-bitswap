# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='py-bitswap',
    version='0.0',
    description="Python implementation of the Bitswap 'data exchange' protocol used by IPFS ",
    long_description_markdown_filename='README.md',
    author='Aliabbas Merchant',
    author_email='merchantaliabbas@gmail.com',
    url='https://github.com/AliabbasMerchant/py-bitswap',
    license='MIT',
    keywords='bitswap ipfs',
    packages=find_packages(include='bitswap'),
    classifiers=[
        'Development Status :: In Progress',
        'Intended Audience :: Developers',
        'License :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],

    include_package_data=True,
    py_modules=['bitswap'],
    # install_requires=install_requires,
    # extras_require=deps,
    # setup_requires=['setuptools-markdown'],
    # zip_safe=False,
)