from setuptools import setup, find_packages

setup(
    name='employee_dashboard',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'plotly',
        'flask',
        'fastapi',
        'pytest'
    ],
)
