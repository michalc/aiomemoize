import setuptools


def long_description():
    with open('README.md', 'r') as file:
        return file.read()


setuptools.setup(
    name='aiomemoize',
    version='0.0.3',
    author='Michal Charemza',
    author_email='michal@charemza.name',
    description='Memoize asyncio Python function calls',
    long_description=long_description(),
    long_description_content_type='text/markdown',
    url='https://github.com/michalc/aiomemoize',
    py_modules=[
        'aiomemoize',
    ],
    python_requires='~=3.5',
    test_suite='test',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Framework :: AsyncIO',
    ],
)
