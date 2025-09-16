from setuptools import setup, find_packages

setup(
    name="bayesian-network",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'numpy>=1.21.0',
        'scipy>=1.7.0',
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A Bayesian Network implementation for rain-maintenance-train-appointment scenario",
    long_description=open('docs/README.md').read(),
    long_description_content_type='text/markdown',
    keywords="bayesian-network, probability, inference",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
