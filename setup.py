import setuptools

setuptools.setup(
    name = 'ojcalc',
    version = '0.0.1',
    description = 'nice calculator',
    author = 'ojkwon',
    url = 'https://github.com/Kwon-Oh-Jae/package.git',
    download_url = 'https://github.com/Kwon-Oh-Jae/package.git',
    packages = ['mycalc'],
    install_requires=[
    'pandas',
    'numpy',
    'matplotlib',
    'scipy',
  ],
    classifiers= [
      "Programming Language :: Python :: 3"
    ]
 )
