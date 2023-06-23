import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "CNNClassifier"
AUTHOR_USER_NAME = "Samargithubb"
SRC_REPO = "CNNClassifier"
AUTHOR_EMAIL = "samarrana407@gmail.com"
description = "A python package for CNN app"
long_description = long_description
long_description_content = "text/markdown"
url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}"
project_urls = {
    "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
}
package_dir = {"": "src"}
packages = setuptools.find_packages(where="src")

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description=description,
    long_description=long_description,
    long_description_content_type=long_description_content,
    url=url,
    project_urls=project_urls,
    package_dir=package_dir,
    packages=packages,
)
