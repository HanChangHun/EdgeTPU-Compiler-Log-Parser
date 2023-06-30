from setuptools import setup, find_packages

setup(
    name="edgetpu_compiler_log_parser",
    version="0.1.1",
    description="Parse EdgeTPU compiler log",
    author="Changhun Han",
    author_email="ehwjs1914@ajou.ac.kr",
    packages=find_packages(exclude=["test"]),
)
