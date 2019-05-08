import yaml
from setuptools import setup

import versioneer

with open("environment.yml", 'r') as stream:
    out = yaml.load(stream)
    requirements = out['dependencies'][1:]  # we do not return python

setup(
    name='pyoviz',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Pyomeca viz toolkit",
    author="Romain Martinez",
    author_email='martinez.staps@gmail.com',
    url='https://github.com/pyomeca/pyoviz',
    license='Apache 2.0',
    packages=['pyoviz'],
    package_data={'': ['ressources/*.png']},
    include_package_data=True,
    # install_requires=requirements,
    keywords='pyoviz',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
