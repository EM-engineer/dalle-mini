#from setuptools import setup

#if __name__ == "__main__":
#    setup()
from setuptools import setup, find_packages

setup(
    name="dalle-mini",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "jax>=0.4.8",  # Modify the JAX version range according to your needs
        "transformers",
        "vqgan-jax",
        "wandb",
    ],
)
