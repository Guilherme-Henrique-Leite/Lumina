from setuptools import setup, find_packages

setup(
    name="customer_management",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "streamlit",
        "pandas",
        "sqlalchemy",
        "plotly",
        "openpyxl",
        "pytz"
    ],
) 