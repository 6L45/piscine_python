from setuptools import setup, find_packages

setup(
    name='ft_package',
    version='0.0.1',
    author='mberengu',
    author_email='mberengu@42.fr',
    description='A sample test package',
    url='https://github.com/mberengu/ft_package',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MOF License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.10',
)
