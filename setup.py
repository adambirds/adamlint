from setuptools import find_packages, setup

VERSION="1.0.0"

REQUIRED = [
    'pyflakes',
    'pycodestyle',
    'typing-extensions',
]

def long_description() -> str:
    with open('README.md', encoding='utf8') as f:
        return f.read()

setup(
    name='adamlint',
    version=VERSION,
    author='ADB Web Designs',
    description='A linter launcher for projects that have multiple source languages.',
    long_description=long_description(),
    long_description_content_type='text/markdown',
    author_email='enquiries@adbwebdesigns.co.uk',
    python_requires='>=3.5',
    url='https://github.com/adambirds/adamlint',
    packages=find_packages(exclude=('tests',)),
    package_data={
        'zulint': ["py.typed"],
    },
    install_requires=REQUIRED,
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',

        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
