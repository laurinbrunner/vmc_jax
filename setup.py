import setuptools

version={}
with open("./jVMC/version.py") as fp:
    exec(fp.read(), version)

with open("README.md", "r") as fh:
    long_description = fh.read()


DEFAULT_DEPENDENCIES = ["setuptools", "wheel", "numpy", "jax>=0.2.11,<=0.3.10", "jaxlib>=0.1.64,<=0.3.10", "flax>=0.3.6,<=0.4.3", "mpi4py", "h5py"]
#CUDA_DEPENDENCIES = ["setuptools", "wheel", "numpy", "jax[cuda]>=0.2.11,<=0.2.25", "flax>=0.3.6,<=0.3.6", "mpi4py", "h5py"]
DEV_DEPENDENCIES = DEFAULT_DEPENDENCIES + ["sphinx", "mock", "sphinx_rtd_theme"]

setuptools.setup(
    name='jVMC',
    version=version['__version__'],
    author="Markus Schmitt, Moritz Reh",
    author_email="markus.schmitt@uni-koeln.de",
    description="jVMC: Versatile and performant variational Monte Carlo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://jvmc.readthedocs.io/en/latest/#",
    packages=setuptools.find_packages(),
    install_requires=DEFAULT_DEPENDENCIES,
    extras_require={
#        "cuda": CUDA_DEPENDENCIES
        "dev": DEV_DEPENDENCIES
    },
    classifiers=[
        "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
    ],
)
