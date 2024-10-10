from setuptools import setup, find_packages

setup(
    name='normalizer_usps',  # Unique package name
    version='0.1.0',         # Update version number appropriately
    description='A library for normalizing US addresses.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  # This ensures that PyPI renders your README correctly
    url='https://github.com/larissabeatrizlima/normalizer_usps',  # Replace with your repository URL
    author='Larissa Lima',
    author_email='larissabeatrizlima@outlook    .com',
    license='MIT',  # Choose an appropriate license
    packages=find_packages(),
    include_package_data=True,
    package_data={'normalizer_usps': ['data/*.json']},
    install_requires=[
        'pandas',
        'importlib_resources; python_version < "3.9"',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        # Add other classifiers from https://pypi.org/classifiers/
    ],
    python_requires='>=3.6',
)
