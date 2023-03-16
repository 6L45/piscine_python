from setuptools import setup, find_packages

setup(
    name='ft_package',
    version='0.0.1',
    author='eagle',
    author_email='eagle@42.fr',
    description='A sample test package',
    url='https://github.com/eagle/ft_package',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    python_requires='>=3.7',
)

