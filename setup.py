  
import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="friendlist",
    version="1.0.0",
    author="Shreyas Mohite",
    author_email="shreyasmohite786@gmail.com",
    description="Adding your friends in friends list",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Geeks-Vegeta/wifi-password.git",
    packages=setuptools.find_packages()
)