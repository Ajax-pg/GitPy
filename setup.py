from setuptools import setup

with open("README.md", encoding="utf-8") as arq:
    readme = arq.read()


setup(name='GitPy',
    version='0.0.1',
    license='MIT License',
    author='João Victor',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='ajaxbytestudio@gmail.com',
    keywords='GitPy',
    description=u'Serve não oficial do GitHub',
    packages=['GitPy'],
    install_requires=['github', 'pandas'],)