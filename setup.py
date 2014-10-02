from distutils.core import setup

setup(
    name="less.web.py",
    version="0.1.0",
    author="Pavan Mishra",
    author_email="pavanmishra@gmail.com",
    py_modules=["lessweb"],
    include_package_data=True,
    url="http://pypi.python.org/pypi/less.web.py_v010/",
    license="LICENSE",
    description="Masking the web.py magic",
	long_description=open("README.md").read(),
    install_requires=[
        "web.py",
    ],
)
