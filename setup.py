from setuptools import find_packages, setup
setup(
    name='pythaiterminology',
    version='0.1.0',
    description='Thai terminology corpus library',
    author='Chayoot Kosiwanich',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)