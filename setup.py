import setuptools
setuptools.setup(
    name='pip-9454-b',
    version='0.1',
    install_requires=['pip-9454-a @ git+ssh://git@github.com/sparkyb/pip-9454-a.git'],
)
