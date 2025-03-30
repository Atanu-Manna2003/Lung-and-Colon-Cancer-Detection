import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


_version_ = "0.0.0"

REPO_NAME = "Lung_and_Colon_Cancer_Detection"
AUTHOR_USER_NAME = "Atanu-Manna2003"
SRC_REPO = "Lung_Cancer_Detection"
AUTHOR_EMAIL = "atanumanna527@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=_version_,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)