from setuptools import setup

setup(
    name='medmij',
    install_requires=['lxml'],
    packages=['medmij'],
    zip_safe=True,
    setup_requires=['nose'],
    test_suite='nose.collector',
    tests_require=['nose'],
    python_require=">=3.7",
    package_data={'medmij': ['*.xsd']}
)
