import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(

    name="latestearthquake-ind",

    version="0.2",

    author="dodi ackbar",

    author_email="dodiakbar.tgr@gmail.com",

    description="This package will get the latest info of earquake from BMKG (Meteorological, Climatological, "
                "and Geophysical Agency)",

    long_description=long_description,

    long_description_content_type="text/markdown",

    url="https://github.com/dodevdi/latest-indonesia-earthquake",
    project_urls={
        "Website": "https://github.com/dodevdi/"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable"
    ],
    # package_dir={"": "src"},
    # packages=setuptools.find_packages(),
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
