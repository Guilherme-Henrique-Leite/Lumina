"""
Module to outsource table_registry
"""
from customer_management.utils.load_css import load_css

from customer_management.utils.registry import table_registry

from customer_management.utils.check_email import is_valid_email

from customer_management.utils.clean_contact import clean_contact

from customer_management.utils.optimize_data import check_object
from customer_management.utils.optimize_data import optimize_memory

from customer_management.utils.contains_emoji import contains_emoji

from customer_management.utils.clean_data import clean_and_validate_data

from customer_management.controller.layer_controller import run_data_pipeline

from customer_management.utils.transform_excel import convert_df_to_excel

from customer_management.utils.country_mapping import COUNTRY_MAPPING, VALID_COUNTRIES

from customer_management.utils.normalize_country_names import normalize_country_name