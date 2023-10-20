#! /bin/bash

python3 setup.py sdist bdist_wheel \
	&& pip install ./dist/ft_package-0.0.1-py3-none-any.whl
