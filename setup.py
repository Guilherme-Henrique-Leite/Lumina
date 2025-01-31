from setuptools import setup, find_packages

setup(
    name="customer_management",
    version="0.1.0",
    packages=find_packages(),
    package_data={
        'customer_management': ['database/*.sql']
    },
    install_requires=[
        "streamlit",
        "pandas",
        "sqlalchemy",
        "plotly",
        "openpyxl",
        "pytz"
    ],
    entry_points={
        'console_scripts': [
            'run-app=customer_management.app:main'
        ]
    }
) 