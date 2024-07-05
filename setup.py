import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()



__version__ = "0.0.0"

REPO_NAME = "Cancer-Detection"
AUTHOR_USER_NAME = "saishridhar"
SRC_REPO = "Cancer-Detection"
AUTHOR_EMAIL = "saishridhar.16@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description = "Upload X-ray image to know whether you have cancer or not",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
)