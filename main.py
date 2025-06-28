# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: base
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Imports

# %%
from pathlib import Path
import pandas as pd
import numpy as np

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import seaborn as sns
from tqdm import tqdm
import powerlaw
import random

from scipy.stats import fisher_exact
from collections import defaultdict
import scipy.stats as stats

from scipy.stats import entropy
from collections import Counter
from typing import Optional





# %% [markdown]
# # Top-line Variables + Settings

# %%
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

PLOTS_PATH = Path("./writing/images/")
TABLES_PATH = Path("./writing/tables/")

# %% [markdown]
# # Loading in  ICIJ

# %%
icij_data_path = Path("datasets/ICIJ/data")

addresses_path = icij_data_path / "nodes-addresses.csv"
officers_path = icij_data_path / "nodes-officers.csv"
entities_path = icij_data_path / "nodes-entities.csv"
intermediaries_path = icij_data_path / "nodes-intermediaries.csv"
others_path = icij_data_path / "nodes-others.csv"
relationships_path = icij_data_path / "relationships.csv"

officers_df = pd.read_csv(officers_path)
entities_df = pd.read_csv(entities_path)
intermediaries_df = pd.read_csv(intermediaries_path)
others_df = pd.read_csv(others_path)
relationships_df = pd.read_csv(relationships_path)
addresses_df = pd.read_csv(addresses_path)

# %% [markdown]
# # Exploratory, each major dataset
#
#
# 1. Clarifying "country" vs. "jurisidction" for entities:
# 2. Clarifying different "entity_types"
# 3. Time Series of entities_df and incorporation dates of them
#
#
# Jurisdiction is the country under whose laws entity is incorporated and governed, 
#
# Country instead: The nation-state associated with an address, officer, or activity of the entity

# %%
officers_df.head()

# %%
officers_df["name"].value_counts().head(20)

# %% [markdown]
# ### Entities_df description

# %%
entities_df.head()

# %%
entities_df["company_type"].value_counts().head(30)

# %% [markdown]
# Entity Type	Description
# | Entity Type | Description |
# |-------------|-------------|
# | Standard International Company | A generic offshore company formed under international business company (IBC) laws, typically used for asset holding, trade, or tax planning. |
# | Standard Company under IBC Act | An offshore company set up specifically under an International Business Companies Act, common in jurisdictions like the British Virgin Islands (BVI) and Seychelles. Used for international business, often with tax and privacy benefits. |
# | Business Company Limited by Shares | A company whose capital is divided into shares owned by shareholders. Liability is limited to the amount unpaid on shares. Common in many offshore jurisdictions. |
# | Regular (Local) Company | A company incorporated to operate primarily within the local jurisdiction, as opposed to international business companies which are meant for overseas operations. |
# | Business Corporation | A general term for a company formed to conduct business, often used interchangeably with "company" or "corporation." May be used in both local and offshore contexts. |
# | Client Sundry Account | An account or entity used by intermediaries to hold or manage funds or assets on behalf of multiple clients, often for administrative or pooling purposes. |
# | International Trust | A trust established under international trust laws, usually for asset protection, estate planning, or confidentiality. |
# | Cook Islands Asset Protection Trust | A trust specifically formed in the Cook Islands, known for strong asset protection features and privacy. Used to shield assets from creditors or legal claims. |
# | Domestic Company | A company incorporated and operating in its country of registration, as opposed to an offshore or international company. |
# | Cook Islands Asset Protection Trust - 3520A | A variant of the Cook Islands Asset Protection Trust, possibly referencing a specific trust structure or compliance form (such as IRS Form 3520-A for U.S. taxpayers). |
# | International Company | A broad term for a company registered in an offshore jurisdiction for the purpose of conducting international business. |
# | Sundry Account | Similar to "Client Sundry Account," used to manage miscellaneous or pooled client funds/assets. |
# | Cook Islands Trust | A trust registered in the Cook Islands, used for asset protection and privacy. |
# | International Business Corporation | A specific type of offshore company, usually with tax and regulatory benefits, common in jurisdictions like BVI and Panama. |
# | BVI Trust | A trust established in the British Virgin Islands, often used for estate planning, privacy, and asset protection. |
# | The GRA group of Companies for express Co. | Likely refers to a group structure or holding company arrangement, possibly managed by a specific intermediary or service provider. |
# | Nominee Only Entity | An entity where only nominee directors or shareholders are listed, obscuring the identity of the real (beneficial) owners. |
# | Mutual Fund Manager | A company licensed to manage mutual funds, often set up offshore for regulatory or tax reasons. |
# | Mutual Fund | An investment vehicle that pools money from multiple investors to invest in securities, sometimes established offshore for tax efficiency. |
# | Foreign Company Transfer | Refers to the transfer or registration of a foreign company within the offshore jurisdiction, possibly as part of a re-domiciliation or restructuring. |
#
#
# Note, we can easily join to addresses using address as well

# %%
for date_col in ["incorporation_date", "inactivation_date", "struck_off_date"]:
    entities_df[date_col] = pd.to_datetime(entities_df[date_col], format="%d-%b-%Y", errors="coerce")
    entities_df.loc[entities_df[date_col].dt.year > 2100, date_col] = pd.NaT
    print(f"Min date for {date_col}: {entities_df[date_col].min()}")
    print(f"Max date for {date_col}: {entities_df[date_col].max()}")

# %%
source_mapping = {
    'Panama Papers': 'Panama Papers',
    'Paradise Papers': 'Paradise Papers',
    'Paradise Papers - Malta corporate registry': 'Paradise Papers',
    'Paradise Papers - Nevis corporate registry': 'Paradise Papers',
    'Paradise Papers - Aruba corporate registry': 'Paradise Papers',
    'Paradise Papers - Barbados corporate registry': 'Paradise Papers',
    'Paradise Papers - Bahamas corporate registry': 'Paradise Papers',
    'Paradise Papers - Samoa corporate registry': 'Paradise Papers',
    'Paradise Papers - Cook Islands corporate registry': 'Paradise Papers',
    'Paradise Papers - Lebanon corporate registry': 'Paradise Papers',
    'Pandora Papers - Alemán, Cordero, Galindo & Lee (Alcogal)': 'Pandora Papers',
    'Pandora Papers - SFM Corporate Services': 'Pandora Papers',
    'Pandora Papers - Commence Overseas': 'Pandora Papers',
    'Pandora Papers - Alpha Consulting': 'Pandora Papers',
    'Pandora Papers - Fidelity Corporate Services': 'Pandora Papers',
    'Pandora Papers - Trident Trust': 'Pandora Papers',
    'Pandora Papers - CILTrust International': 'Pandora Papers',
    'Pandora Papers - Il Shin Corporate Consulting Limited': 'Pandora Papers',
    'Pandora Papers - Overseas Management Company (OMC)': 'Pandora Papers',
    'Pandora Papers - Asiaciti Trust': 'Pandora Papers',
    'Bahamas Leaks': 'Bahamas Leaks',
    'Offshore Leaks': 'Offshore Leaks'
}

entities_df['source'] = entities_df['sourceID'].map(source_mapping)

print(entities_df['source'].value_counts())

# %% [markdown]
# # Enriching relationships_df
#
# 1. Getting the type of node on each side, `node_type_start` and `node_type_end`
# 2. Flipping usch that intermediaries are always node_starts

# %%
relationships_df.head()

# %%
# Sets of node IDs for faster lookups
address_ids = set(addresses_df['node_id'])
entity_ids = set(entities_df['node_id'])
officer_ids = set(officers_df['node_id'])
intermediary_ids = set(intermediaries_df['node_id'])
other_ids = set(others_df['node_id']) 

def get_node_type(node_id):
    if node_id in entity_ids:
        return 'entity'
    elif node_id in officer_ids:
        return 'officer'
    elif node_id in intermediary_ids:
        return 'intermediary'
    elif node_id in address_ids:
        return 'address'
    elif node_id in other_ids:
        return 'other'
    else:
        return 'unknown' 

relationships_df['node_type_start'] = relationships_df['node_id_start'].map(get_node_type)
relationships_df['node_type_end'] = relationships_df['node_id_end'].map(get_node_type)

# %%
relationships_df["node_type_end"].value_counts()

# %% [markdown]
# A bidirectonial graph, so for convenience we transform all relations to always start with the intermediary for convenience. Only ones that will remain with intermediary as node_type_end are the relations between intermediaries themselves

# %%
rows_to_flip = (relationships_df['node_type_end'] == 'intermediary') 

# store original values for swapping
start_nodes_temp = relationships_df.loc[rows_to_flip, 'node_id_start'].copy()
start_types_temp = relationships_df.loc[rows_to_flip, 'node_type_start'].copy()

# perform the swap for node IDs
relationships_df.loc[rows_to_flip, 'node_id_start'] = relationships_df.loc[rows_to_flip, 'node_id_end']
relationships_df.loc[rows_to_flip, 'node_id_end'] = start_nodes_temp

# perform the swap for node types
relationships_df.loc[rows_to_flip, 'node_type_start'] = relationships_df.loc[rows_to_flip, 'node_type_end']
relationships_df.loc[rows_to_flip, 'node_type_end'] = start_types_temp

relationships_df["node_type_end"].value_counts()

# %%
intermediaries_relationships = relationships_df[
    (relationships_df["node_type_start"] == "intermediary")
]
intermediaries_relationships["node_type_end"].value_counts()

# %% [markdown]
# What are the types of relationsships between each node type?

# %%
intermediaries_relationships[intermediaries_relationships["node_type_end"] == "entity"].rel_type.value_counts()

# %%
intermediaries_relationships[intermediaries_relationships["node_type_end"] == "address"].rel_type.value_counts()

# %%
intermediaries_relationships[intermediaries_relationships["node_type_end"] == "officer"].rel_type.value_counts()

# %%
# and also checking hte weird ones between entities - all of which seem to indicate that we're talking about the same intermediaries
intermediaries_relationships[intermediaries_relationships["node_type_end"] == "intermediary"].rel_type.value_counts()

# %% [markdown]
# # Enriching entities_df
#
# 1. Aligning different names for Bearer instruments and replacing them with just "Bearer" 
# 2. Counting the number of bearer instruments tied to each intermediary, `bearer_count`
# 3. Aligning jursidiction with iso3 standard
# 4. Enriching with Lafitte data and brief description of legal technologies on jurisdiction
# 5. Enriching with democracy index scores on country_codes

# %% [markdown]
# Bearer names (including "THE BEARER," "EL PORTADOR," etc.) are placeholders for anonymous ownership through bearer shares, meaning the true owner is not recorded and can be changed simply by transferring the physical certificate.
#
# Individual names are real people who serve as officers of offshore entities.
#
# Corporate names are typically nominee companies or service providers that act as officers, often to provide anonymity for the real owners.
#
# From Harrington (2016):
#
# *In addition, a few offshore jurisdictions allow the use of “bearer shares,” which are a way of issuing corporate stock without specifying a particular owner. Rather, the owner of a bearer share is literally whoever happens to be holding the stock certificate at any moment in time. This provides strong privacy protections, because as long as one does not have the shares in hand, one can say truthfully under oath, “I do not own that firm.” And if any officers of the firm are ever questioned about its ownership, they can also truthfully say, “I don’t know who owns the company, because bearer shares were issued.” In other words, bearer shares make it impossible to know who owns a company, and that makes it impossible to assign legal responsibility for any taxes, fines, or debts the company incurs.*
#

# %%
# 1. Standardizing bearer names

bearer_variations = [
    'THE BEARER',
    'EL PORTADOR',
    'Bearer 1',
    'Bearer',
    'The Bearer',
    'BEARER'
]

# Create a function to standardize bearer names
def standardize_bearer(name):
    if name in bearer_variations:
        return 'Bearer'
    return name

officers_df['name'] = officers_df['name'].apply(standardize_bearer)

print(officers_df['name'].value_counts().head(10))

# %%
# 2. Counting number of bearers tied to these entities

bearer_officers_ids = officers_df[officers_df['name'] == 'Bearer']['node_id'].unique()

bearer_relationships = relationships_df[
    (
        (relationships_df['node_type_start'] == 'entity') & 
        (relationships_df['node_id_end'].isin(bearer_officers_ids))
    ) 
        |
    (
        (relationships_df['node_type_end'] == 'entity') & 
        (relationships_df['node_id_start'].isin(bearer_officers_ids))
    ) 
]
bearer_relationships["node_type_start"].value_counts()

# %%
bearer_relationships["node_type_end"].value_counts()

# %%
# always the node_id_end, so grouping by that
bearers_by_officers = bearer_relationships.groupby('node_id_end').size().reset_index(name='bearer_count')
bearers_by_officers.head()

entities_df = entities_df.merge(
    bearers_by_officers, left_on='node_id', right_on='node_id_end', how='left'
)
entities_df.head()
entities_df["bearer_count"] = entities_df["bearer_count"].fillna(0).astype(int)
entities_df["bearer_count"].value_counts()

# %%
entities_df.head()

# %%
# 3. Aligning jurisdiction field with iso3_standard
# All credit goes to Gemini...

entities_df.jurisdiction.unique()
def map_country_codes_to_iso3(series: pd.Series) -> pd.Series:
    mapping = {
        'SAM': 'WSM',   # Samoa (often abbreviated as Sam) - Assuming this is Samoa
        'PMA': 'PAN',   # Panama (PMA is sometimes used, though PAN is standard)
        'NEV': 'USA',   # Nevada, USA (Assuming a US state, mapping to USA)
        'UK': 'GBR',    # United Kingdom
        'SGP': 'SGP',   # Singapore (already ISO3)
        'RAK': 'ARE',   # Ras Al Khaimah, UAE (Assuming an Emirate, mapping to UAE)
        'IOM': 'IMN',   # Isle of Man
        'BAH': 'BHS',   # Bahamas
        'ANG': 'AGO',   # Angola (Assuming Angola, could be Anguilla AIA) - Going with Angola as it's a more common country. If it's Anguilla, change to 'AIA'.
        'SEY': 'SYC',   # Seychelles
        'NIUE': 'NIU',  # Niue
        'UY': 'URY',    # Uruguay
        'BVI': 'VGB',   # British Virgin Islands
        'HK': 'HKG',    # Hong Kong
        'NZL': 'NZL',   # New Zealand (already ISO3)
        'CYP': 'CYP',   # Cyprus (already ISO3)
        'MLT': 'MLT',   # Malta (already ISO3)
        'BLZ': 'BLZ',   # Belize (already ISO3)
        'JSY': 'JEY',   # Jersey
        'WYO': 'USA',   # Wyoming, USA (Assuming a US state, mapping to USA)
        'CRI': 'CRI',   # Costa Rica (already ISO3)
        'XXX': 'XXX',   # Unknown or unidentifiable
        'CAYMN': 'CYM', # Cayman Islands
        'LABUA': 'MYS', # Labuan, Malaysia (Assuming a territory, mapping to Malaysia)
        'MARSH': 'MHL', # Marshall Islands
        'MAURI': 'MUS', # Mauritius
        'STLU': 'LCA',  # Saint Lucia
        'MALAY': 'MYS', # Malaysia
        'DUBAI': 'ARE', # Dubai, UAE (Assuming an Emirate, mapping to UAE)
        'VANU': 'VUT',  # Vanuatu
        'COOK': 'COK',  # Cook Islands
        'BERMU': 'BMU', # Bermuda
        'BRUN': 'BRN',  # Brunei Darussalam
        'LIBER': 'LBR', # Liberia
        'USA': 'USA',   # United States (already ISO3)
        'CHINA': 'CHN', # China
        'THAIL': 'THA', # Thailand
        'NETH': 'NLD',  # Netherlands
        'IRELD': 'IRL', # Ireland
        'AW': 'ABW',    # Aruba
        'XX': 'XXX',    # Unknown or unidentifiable
        'AE': 'ARE',    # United Arab Emirates (ISO2, mapping to ISO3)
        'AG': 'ATG',    # Antigua and Barbuda (ISO2, mapping to ISO3)
        'AI': 'AIA',    # Anguilla (ISO2, mapping to ISO3)
        'AN': 'ANT',    # Netherlands Antilles (Though dissolved, keeping for mapping historical data) - Note: NLD is the modern mapping.
        'BB': 'BRB',    # Barbados (ISO2, mapping to ISO3)
        'BM': 'BMU',    # Bermuda (ISO2, mapping to ISO3)
        'BS': 'BHS',    # Bahamas (ISO2, mapping to ISO3)
        'BZ': 'BLZ',    # Belize (ISO2, mapping to ISO3)
        'CK': 'COK',    # Cook Islands (ISO2, mapping to ISO3)
        'CY': 'CYP',    # Cyprus (ISO2, mapping to ISO3)
        'BRB': 'BRB',   # Barbados (already ISO3)
        'LBN': 'LBN',   # Lebanon (already ISO3)
        'CYM': 'CYM',   # Cayman Islands (already ISO3)
        'GHA': 'GHA',   # Ghana (already ISO3)
        'GD': 'GRD',    # Grenada (ISO2, mapping to ISO3)
        'GG': 'GGY',    # Guernsey (ISO2, mapping to ISO3)
        'GI': 'GIB',    # Gibraltar (ISO2, mapping to ISO3)
        'IM': 'IMN',    # Isle of Man (ISO2, mapping to ISO3)
        'JE': 'JEY',    # Jersey (ISO2, mapping to ISO3)
        'KN': 'KNA',    # Saint Kitts and Nevis (ISO2, mapping to ISO3)
        'KY': 'CYM',    # Cayman Islands (ISO2, mapping to ISO3)
        'LI': 'LIE',    # Liechtenstein (ISO2, mapping to ISO3)
        'LR': 'LBR',    # Liberia (ISO2, mapping to ISO3)
        'LU': 'LUX',    # Luxembourg (ISO2, mapping to ISO3)
        'MH': 'MHL',    # Marshall Islands (ISO2, mapping to ISO3)
        'MT': 'MLT',    # Malta (ISO2, mapping to ISO3)
        'MU': 'MUS',    # Mauritius (ISO2, mapping to ISO3)
        'NL': 'NLD',    # Netherlands (ISO2, mapping to ISO3)
        'NZ': 'NZL',    # New Zealand (ISO2, mapping to ISO3)
        'PA': 'PAN',    # Panama (ISO2, mapping to ISO3)
        'SC': 'SYC',    # Seychelles (ISO2, mapping to ISO3)
        'SG': 'SGP',    # Singapore (ISO2, mapping to ISO3)
        'TC': 'TCA',    # Turks and Caicos Islands (ISO2, mapping to ISO3)
        'US': 'USA',    # United States (ISO2, mapping to ISO3)
        'USDE': 'USA',  # Delaware, USA (Assuming a US state, mapping to USA)
        'VC': 'VCT',    # Saint Vincent and the Grenadines (ISO2, mapping to ISO3)
        'VG': 'VGB',    # British Virgin Islands (ISO2, mapping to ISO3)
        'VI': 'VIR',    # U.S. Virgin Islands (ISO2, mapping to ISO3)
        'KNA': 'KNA',   # Saint Kitts and Nevis (already ISO3)
        np.nan: 'XXX',  # Map NaN values to 'XXX' (like country_codes)
        'HKG': 'HKG',   # Hong Kong (already ISO3)
        'COK': 'COK',   # Cook Islands (already ISO3)
        'VGB': 'VGB',   # British Virgin Islands (already ISO3)
        'WSM': 'WSM',   # Samoa (already ISO3)
        'SYC': 'SYC',   # Seychelles (already ISO3)
        'GGY': 'GGY',   # Guernsey (already ISO3)
        'BHS': 'BHS',   # Bahamas (already ISO3)
        'PAN': 'PAN',   # Panama (already ISO3)
        'MCO': 'MCO',   # Monaco (already ISO3)
        'JEY': 'JEY',   # Jersey (already ISO3)
        'IMN': 'IMN',   # Isle of Man (already ISO3)
        'GBR': 'GBR',   # United Kingdom (already ISO3)
        'ARE': 'ARE',   # United Arab Emirates (already ISO3)
        'AIA': 'AIA',   # Anguilla (already ISO3)
        'VCT': 'VCT',   # Saint Vincent and the Grenadines (already ISO3)
        'MUS': 'MUS',   # Mauritius (already ISO3)
        'MHL': 'MHL',   # Marshall Islands (already ISO3)
        'GIB': 'GIB',   # Gibraltar (already ISO3)
        'LVA': 'LVA',   # Latvia (already ISO3)
        'CHE': 'CHE',   # Switzerland (already ISO3)
        'LCA': 'LCA',   # Saint Lucia (already ISO3)
        'VUT': 'VUT',   # Vanuatu (already ISO3)
    }
    return series.map(mapping)

entities_df["jurisdiction"] = map_country_codes_to_iso3(entities_df["jurisdiction"])

# %%
# 3. Enriching with Lafitte on jurisdiction

hthd_path = Path("datasets/legal_innovations_history/HTHD.csv")
hthd = pd.read_csv(hthd_path)

# jurisdiction in entities_df and iso3 in hthd both. 
# need to join on iso3 and jurisidction + incorporation_year = year

# %%
# Only goes up until 2000, but we have incorporation dates all the way until ~2020
# Solution: Forward-filling the last entry

all_countries = hthd['iso3'].unique()
all_years = range(1850, 2021)
expanded_df = pd.DataFrame([(country, year) for country in all_countries for year in all_years], 
                         columns=['iso3', 'year'])

expanded_hthd = expanded_df.merge(hthd, on=['iso3', 'year'], how='left')

cumul_cols = [col for col in expanded_hthd.columns if col.endswith('_cumul')]
expanded_hthd[cumul_cols] = expanded_hthd.groupby('iso3')[cumul_cols].ffill()

expanded_hthd = expanded_hthd.fillna(0)

expanded_hthd[expanded_hthd["iso3"] == "PAN"].sample(10)

# %%
# Define the mapping from column names to the primary Lafitte categories
legal_tech_category_mapping = {
    "Banking_cumul": "Banking",
    "Holding_cumul": "Corporate",
    "IBC_cumul": "Dual-Purpose",
    "Insurance_cumul": "Corporate",
    "Corporate_cumul": "Corporate",
    "Ship_cumul": "Corporate",
    "Exempt_cumul": "Dual-Purpose",
    "Individual_cumul": "Personal",
    "Treaty_cumul": "Other Technologies",
    "Other_cumul": "Other Technologies",
}
# List of the specific cumul columns to check
specific_tech_columns = list(legal_tech_category_mapping.keys())

def categorize_jurisdiction_by_tech(row):
    """
    Assigns a jurisdiction to one or more of the five Lafitte categories.
    If multiple distinct categories apply, returns them joined by '/' in
    alphabetical order of their names. If none apply, returns
    'No Legal Technologies'.
    """
    # Gather all active categories for this row
    active_categories = {
        legal_tech_category_mapping[col]
        for col in specific_tech_columns
        if row.get(col, 0)
    }

    if not active_categories:
        return "No Legal Technologies"
    if len(active_categories) == 1:
        # Single category
        return next(iter(active_categories))
    # Multiple categories: join in alphabetical order
    return "/".join(sorted(active_categories))

expanded_hthd["jurisdiction_legal_technology"] = expanded_hthd.apply(
    categorize_jurisdiction_by_tech, axis=1
)
expanded_hthd["jurisdiction_legal_technology"].value_counts()

# %%
# calculating overlap
jurisdiction_unique = entities_df["jurisdiction"].unique()
iso3_unique = hthd.iso3.unique()

jurisdiction_set = set(jurisdiction_unique)
iso3_set = set(iso3_unique)

overlap_elements = jurisdiction_set.intersection(iso3_set)

num_overlap = len(overlap_elements)

num_jurisdiction_unique = len(jurisdiction_set)
num_iso3_unique = len(iso3_set)


print(f"Number of overlapping jurisdictions: {num_overlap}")
print(f"Number of unique jurisdictions in entities_df: {num_jurisdiction_unique}")
print(f"Number of unique ISO3 codes in hthd: {num_iso3_unique}")


# %% [markdown]
# ## Legal Technologies in Tax Havens
#
# ### 1. Trust Laws & Other (Personal)
# Legal technologies designed to directly circumvent personal taxation.
# - **Trust Laws**: Allow legal disconnection between asset use and ownership
#   - Example: Turks and Caicos Islands' Trust Ordinance of 1990
# - **Other Personal Technologies**: Include measures like tax abolition
#   - Example: Monaco's abolition of personal income taxes in 1869
#
# ### 2. Corporate Technologies
# Technologies targeting firms to enable corporate tax avoidance.
#
# - **MNE-specific Laws**: Attract multinational enterprise activities and profits
#   - Example: Ireland's Export Profits Tax Relief of 1956
# - **Holding Company Laws**: Create special regimes for holding companies
#   - Example: Luxembourg's 1929 law on financial participation societies
# - **Offshore Insurance & Captives**: Enable revenue transfers via self-insurance
#   - Example: Barbados' Exempt Insurance Act of 1983
# - **Flag of Convenience Laws**: Offer limited regulations for ship registration
#   - Example: Panama's Law/63 on foreign ships registration
#
# ### 3. Dual-Purpose Technologies (IBC & Exempt Companies)
# Used to circumvent both corporate and personal taxation.
#
# - **International Business Companies (IBCs)**: Tax-neutral companies with:
#   - No domestic activities
#   - Limited legal/administrative requirements
#   - Minimal reporting
#   - No disclosure of ultimate owners
#   - Example: British Virgin Islands' International Business Companies Act of 1984
# - **Other Exempt Companies**: Similar to IBCs
#   - Example: Jersey's 1940 Corporation Tax Law
#
# ### 4. Banking Technologies
# Complementary technologies enabling secrecy and offshore holdings.
#
# - **Offshore Banking Laws**: Facilitate unregulated banks with limited requirements
#   - Example: Anguilla's Banking Ordinance of 1991
# - **Bank Secrecy Laws**: Protect account holders from investigations
#   - Example: Switzerland's Banking Act of 1934
#
# ### 5. Other Technologies
# Diverse regulations not fitting other categories.
#
# - **Tax Treaties**: Limit bilateral taxation and enable conduit entities
#   - Example: Netherlands Antilles' tax treaty with Netherlands (1964)
# - **Specific Regulations**: Country-specific rules
#   - Example: Bahamas' Hawksbill Creek Agreement of 1955
#
#
# And at the dataset level by each column:
# ### Banking_cumul
# Legal Technology: Directly refers to reforms related to 'Offshore banking' and 'Bank secrecy'.
# Category: Banking
#
# ### Holding_cumul  
# Legal Technology: Corresponds to reforms establishing special regimes for 'Holding' companies.
# Category: Corporate
#
# ### IBC_cumul
# Legal Technology: Refers to reforms for 'IBC' (International Business Companies) - tax-neutral companies with limited domestic activities and legal requirements.
# Category: Dual (used to circumvent both personal and corporate taxation)
#
# ### Insurance_cumul
# Legal Technology: Corresponds to reforms related to 'Offshore Insurance and Captives', allowing for self-insurance and revenue transfers to tax havens.
# Category: Corporate
#
# ### Corporate_cumul
# Legal Technology: While broadly named, likely captures reforms specifically aimed at attracting MNE activities and profits, distinct from other corporate reforms that have their own columns (Holding, Insurance, Ship).
# Category: Corporate
#
# ### Ship_cumul
# Legal Technology: Refers to reforms establishing a 'Flag of convenience', offering limited regulations and tax rates for ships registered in an offshore maritime registry.
# Category: Corporate
#
# ### Exempt_cumul
# Legal Technology: Refers to 'Other exempt companies' which are similar to IBCs.
# Category: Dual
#
# ### Individual_cumul
# Legal Technology: Refers to reforms like 'Trust laws' (allowing legal disconnection between asset use and ownership) and 'Other' personal tax circumvention methods.
# Category: Individual
#
# ### Treaty_cumul
# Legal Technology: Refers to reforms related to 'Tax treaties' that can limit bilateral taxation.
# Category: Other
#
# ### Multiple_cumul
# Legal Technology: Captures reforms that are classified under more than one specific legal technology type.
# Category: Cross-cutting (spans multiple categories)
#
# ### Other_cumul
# Legal Technology: Likely refers to 'Specific regulations' or other reforms within the broader "Other" category that aren't tax treaties.
# Category: Other

# %%
# Calculate mean incorporation year, excluding 0 values which are likely missing/invalid
# to fill in where we have NaN's otherwise. Imputing so we can get a guess at the legal technologies

entities_df['incorporation_year'] = (
    pd.to_datetime(entities_df['incorporation_date'], errors='coerce')
      .dt.year
)
MEAN_INCORPORATION_YEAR = entities_df[entities_df['incorporation_year'] > 0]['incorporation_year'].mean().round(0)
MEAN_INCORPORATION_YEAR
entities_df['incorporation_year'] = entities_df['incorporation_year'].fillna(MEAN_INCORPORATION_YEAR).astype(int)
entities_df[entities_df["jurisdiction"] == "PAN"][["incorporation_year", "country_codes", "jurisdiction"]].sample(10)


# %%
# Merge on jurisdiction and year
entities_df = entities_df.merge(
    expanded_hthd,
    left_on=['jurisdiction', 'incorporation_year'],
    right_on=['iso3', 'year'],
    how='left'
)
entities_df.sample(5)

# %%
entities_df["jurisdiction_legal_technology"].value_counts()

# %%
entities_df[entities_df["jurisdiction"] == "PAN"][["incorporation_year", "jurisdiction", "Individual_cumul"]].sample(10)

# %%
legal_tech_columns = ['Banking_cumul', 'Holding_cumul', 'IBC_cumul', 'Insurance_cumul', 
                     'Corporate_cumul', 'Ship_cumul', 'Exempt_cumul', 'Individual_cumul',
                     'Treaty_cumul', 'Multiple_cumul', 'Other_cumul']

tech_counts = entities_df[legal_tech_columns].gt(0).sum(axis=1)

entities_multiple_tech = (tech_counts > 1).sum()

print(f"Number of entities with multiple legal technologies: {entities_multiple_tech}")
print(f"\nDistribution of number of legal technologies per entity:")
tech_counts.value_counts().sort_index()


# %%
# 4. Enriching with regime type
vdem_core_path = Path("datasets/vdem_core/vdem_core.csv")
vdem_core = pd.read_csv(vdem_core_path)

# trimming the dataset to what we need: regime classification on iso3-year level
vdem_core = vdem_core[vdem_core["year"] >= 1900]
vdem_core = vdem_core[["country_text_id", "year", "v2x_regime"]]
vdem_core.head(10)

# %%
vdem_core["v2x_regime"].value_counts()

# %% [markdown]
# ### v2x_regime score meaning:
#
# 0 – Closed Autocracy: No meaningful, multi-party elections are held for either the executive or the legislature. Political power is concentrated, and rulers are not accountable to the electorate in any significant way.
#
# 1 – Electoral Autocracy: Multi-party elections exist for the legislature and chief executive, but these elections are not free and fair, or there are significant infringements on political and civil freedoms. The regime retains authoritarian characteristics despite the presence of elections.
#
# 2 – Electoral Democracy: Multi-party elections are both present and meaningfully free and fair, allowing for real competition. However, the rule of law, checks and balances, and protection of civil liberties may be weaker than in liberal democracies.
#
# 3 – Liberal Democracy: Meets all criteria for electoral democracy and, in addition, has strong protections for civil liberties, rule of law, judicial and legislative constraints on the executive, and effective checks and balances.

# %%
# Handling several country_codes by exploding and grouping back together
entities_df_exploded = entities_df.copy()
entities_df_exploded['country_codes'] = entities_df_exploded['country_codes'].str.split(';')
entities_df_exploded = entities_df_exploded.explode('country_codes')

entities_df_exploded = entities_df_exploded.merge(
    vdem_core,
    left_on=['country_codes', 'incorporation_year'],
    right_on=['country_text_id', 'year'],
    how='left'
)

# takign floor of the mean regime score, ignoring NaNs
regime_scores = entities_df_exploded.groupby(entities_df_exploded.index)['v2x_regime'].agg(
    lambda x: np.floor(x.mean()) if not x.isna().all() else np.nan
)

entities_df['v2x_regime'] = regime_scores
entities_df["v2x_regime"] = entities_df["v2x_regime"].fillna("Unknown").map({
    0.0: "Closed Autocracy",
    1.0: "Electoral Autocracy", 
    2.0: "Electoral Democracy",
    3.0: "Liberal Democracy",
    "Unknown": "Micro-state"
})

entities_df['v2x_regime'].value_counts()

# %% [markdown]
# # Enriching intermediaries_df
#
# 1. Getting the degrees of intermediaries
# 2. Going through all the entities they're connected to, getting dict object for:
#     * a. countries: n_entities (explode out on ;-separated entries and count both)
#     * b. jurisdictions: n_entities
#     * c. regime-type: n_entities (also include NaNs)
#     * d. jurisdiction-type: n_entities (Note, using cumulative column for each legal tech. If a jursidiction has multiple elgal technologies we count them multiple places)
# 3. Counting number of entities of which connected, having bearer instruments
# 4. Calculating entropy - standardized and HHI

# %%
# 1. Get degree of each intermediary
intermediary_entities_connections = relationships_df[
    (relationships_df['node_type_start'] == 'intermediary') & 
    (relationships_df['node_type_end'] == 'entity')
]

entities_per_intermediary = intermediary_entities_connections.groupby('node_id_start').size()
intermediaries_df['degree'] = intermediaries_df['node_id'].map(entities_per_intermediary)
intermediaries_df['log_degree'] = np.log10(intermediaries_df['degree'])

# %%
intermediaries_df.head()

# %%
# 2. Going through all the entities they're connected to, getting dict object for:
#     * countries: n_entities (explode out on ;-separated entries and count both)
#     * jurisdictions: n_entities
#     * regime-type: n_entities (also include NaNs)
#     * jurisdiction-type: n_entities (Note, using cumulative column for each legal tech. If a jursidiction has multiple elgal technologies we count them multiple places)

intermediary_entities_connections_enriched = intermediary_entities_connections.merge(
    entities_df[[
        "node_id", "country_codes", "jurisdiction", "v2x_regime", "bearer_count",
        "Banking_cumul", "Holding_cumul", "IBC_cumul", "Insurance_cumul", "Corporate_cumul", "Ship_cumul",
        "Exempt_cumul", "Individual_cumul", "Treaty_cumul", "Multiple_cumul", "Other_cumul"]],
    left_on="node_id_end",
    right_on="node_id",
    how="left"
)
# objective: create new column storing dictionary of this structure: dict(country_code=number_of_entities_in_country, ...)
# will make calculations easier

# %%
# a. country codes
# Note: Complication arising by virtue of there sometimes being multiple country codes per entity

# country_codes is semi-colon separated list form, so we need to handle that using a split first

country_codes_exploded = intermediary_entities_connections_enriched.dropna(subset=['country_codes']).copy()
country_codes_exploded['country_codes'] = country_codes_exploded['country_codes'].str.split(';')
country_codes_exploded = country_codes_exploded.explode('country_codes')
country_codes_exploded['country_codes'] = country_codes_exploded['country_codes'].str.strip()
country_codes_exploded = country_codes_exploded[country_codes_exploded['country_codes'] != '']

# count countries per intermediary using value_counts
country_counts = country_codes_exploded.groupby('node_id_start')['country_codes'].value_counts().unstack(fill_value=0)

# store as dictionary for easy lookup
country_counts_dict = country_counts.apply(lambda x: x[x > 0].to_dict(), axis=1).to_dict()

# Add the country counts dictionary to intermediaries_df
intermediaries_df['country_counts'] = intermediaries_df['node_id'].map(country_counts_dict)
intermediaries_df['country_counts'] = intermediaries_df['country_counts'].fillna({}).apply(lambda x: x if isinstance(x, dict) else {})

intermediaries_df['country_count'] = intermediaries_df['country_counts'].apply(len)
intermediaries_df.head()

# %%
# b. jurisdictions map

jurisdiction_exploded = intermediary_entities_connections_enriched.dropna(subset=['jurisdiction']).copy()
jurisdiction_exploded = jurisdiction_exploded[jurisdiction_exploded['jurisdiction'] != '']

# count jurisdictions per intermediary using value_counts
jurisdiction_counts = jurisdiction_exploded.groupby('node_id_start')['jurisdiction'].value_counts().unstack(fill_value=0)

# store as dictionary for easy lookup
jurisdiction_counts_dict = jurisdiction_counts.apply(lambda x: x[x > 0].to_dict(), axis=1).to_dict()

intermediaries_df['jurisdiction_counts'] = intermediaries_df['node_id'].map(jurisdiction_counts_dict)
intermediaries_df['jurisdiction_counts'] = intermediaries_df['jurisdiction_counts'].fillna({}).apply(lambda x: x if isinstance(x, dict) else {})

intermediaries_df['jurisdiction_count'] = intermediaries_df['jurisdiction_counts'].apply(len)


# %%
intermediaries_df.head()

# %%
# c. regime-type map

regime_exploded = intermediary_entities_connections_enriched.dropna(subset=['v2x_regime']).copy()
regime_exploded = regime_exploded[regime_exploded['v2x_regime'] != '']

regime_counts = regime_exploded.groupby('node_id_start')['v2x_regime'].value_counts().unstack(fill_value=0)

regime_counts_dict = regime_counts.apply(lambda x: x[x > 0].to_dict(), axis=1).to_dict()

intermediaries_df['regime_counts'] = intermediaries_df['node_id'].map(regime_counts_dict)
intermediaries_df['regime_counts'] = intermediaries_df['regime_counts'].fillna({}).apply(lambda x: x if isinstance(x, dict) else {})

intermediaries_df['regime_count'] = intermediaries_df['regime_counts'].apply(len)
intermediaries_df.head()

# %%
# d. legal technology map

legal_tech_columns = ['Banking_cumul', 'Holding_cumul', 'IBC_cumul', 'Insurance_cumul', 
                     'Corporate_cumul', 'Ship_cumul', 'Exempt_cumul', 'Individual_cumul',
                     'Treaty_cumul', 'Multiple_cumul', 'Other_cumul']

legal_tech_exploded = intermediary_entities_connections_enriched.dropna(subset=legal_tech_columns).copy()

column_mapping = {col: col.replace('_cumul', '') for col in legal_tech_columns}

legal_tech_counts = {}
for _, row in legal_tech_exploded.iterrows():
    intermediary_id = row['node_id_start']
    if intermediary_id not in legal_tech_counts:
        legal_tech_counts[intermediary_id] = {}
    
    for old_col, new_col in column_mapping.items():
        if row[old_col] > 0:  # Only count positive values
            if new_col not in legal_tech_counts[intermediary_id]:
                legal_tech_counts[intermediary_id][new_col] = 0
            legal_tech_counts[intermediary_id][new_col] += 1

intermediaries_df['legal_tech_counts'] = intermediaries_df['node_id'].map(legal_tech_counts)
intermediaries_df['legal_tech_counts'] = intermediaries_df['legal_tech_counts'].fillna({}).apply(lambda x: x if isinstance(x, dict) else {})

intermediaries_df['legal_tech_count'] = intermediaries_df['legal_tech_counts'].apply(len)
intermediaries_df.head()

# %%
intermediaries_df[intermediaries_df["legal_tech_count"] > 0].sample(5)

# %%
# 3. Counting number of entities of which connected, having bearer instruments

bearer_counts = intermediary_entities_connections_enriched[intermediary_entities_connections_enriched['bearer_count'] > 0].groupby('node_id_start').size()
intermediaries_df['bearers_connected'] = intermediaries_df['node_id'].map(bearer_counts)
intermediaries_df['bearers_connected'] = intermediaries_df['bearers_connected'].fillna(0)

intermediaries_df["bearer_share"] = intermediaries_df["bearers_connected"] / intermediaries_df["degree"]


# %%
# 4. Calculating standardized entropy

def calculate_normalized_entropy(counts_dict):
    if not counts_dict:
        return 0
    total = sum(counts_dict.values())
    probabilities = [count/total for count in counts_dict.values()]

    entropy = -sum(p * np.log2(p) for p in probabilities)

    max_entropy = np.log2(len(counts_dict))
    return entropy / max_entropy if max_entropy > 0 else 0

intermediaries_df['legal_tech_entropy'] = intermediaries_df['legal_tech_counts'].apply(calculate_normalized_entropy)

intermediaries_df['jurisdiction_entropy'] = intermediaries_df['jurisdiction_counts'].apply(calculate_normalized_entropy)

intermediaries_df['regime_entropy'] = intermediaries_df['regime_counts'].apply(calculate_normalized_entropy)

intermediaries_df['country_entropy'] = intermediaries_df['country_counts'].apply(calculate_normalized_entropy)

intermediaries_df.head()

# %%
# filtering all irrelevant ones away - don't have any entities incorporated
intermediaries_df = intermediaries_df[intermediaries_df["country_count"] != 0]

# %% [markdown]
# # Joining in Enrichment Data Into Intermediaries Dataframe

# %%
enriched_random_sample_500_path = Path("enrichment_data/enriched_random_sample_500.csv")
enriched_top_5_percent_intermediaries_path = Path("enrichment_data/enriched_top_5_percent_intermediaries.csv")

random_sample = pd.read_csv(enriched_random_sample_500_path)
top_5_percent = pd.read_csv(enriched_top_5_percent_intermediaries_path)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

def create_donut_chart(data, ax, title):
    total = len(data)
    filtered = len(data[
        (data["confidence"] == "High") & 
        (data["classification"] != "ERROR")
    ])
    
    wedges, texts, autotexts = ax.pie(
        [filtered, total - filtered],
        labels=['High Confidence', 'Excluded'],
        colors=['#2ecc71', '#e74c3c'],
        autopct='%1.1f%%',
        pctdistance=0.85,
        labeldistance=1.1,
        wedgeprops={'width': 0.5}
    )
    
    ax.set_title(f'{title}\nBefore Filtering: n={total:,}', pad=10)
    ax.text(0, 0, f'Kept: n={filtered:,}', 
            ha='center', va='center', fontsize=12, fontweight='bold')
    
    plt.setp(autotexts, size=9, weight="bold")
    plt.setp(texts, size=10)

create_donut_chart(random_sample, ax1, 'Random Sample')
create_donut_chart(top_5_percent, ax2, 'Top ~1.5% of Intermediaries (by degree)')

plt.tight_layout()
plt.savefig(PLOTS_PATH / 'Appendix_Filtering_of_Enrichment.png')

plt.show()

intermediaries_df_enriched_random_sample_500 = random_sample[
    (random_sample["confidence"] == "High") & 
    (random_sample["classification"] != "ERROR")
]

# Then deduplicate the top 5% data
intermediaries_df_enriched_top_5_percent_intermediaries = top_5_percent[
    (top_5_percent["confidence"] == "High") & 
    (top_5_percent["classification"] != "ERROR")
]

intermediaries_df_enriched_random_sample_500.shape

# %%
# Add type column to filtered dataframes
intermediaries_df_enriched_top_5_percent_intermediaries["type"] = "Top 5% Intermediaries"
intermediaries_df_enriched_random_sample_500["type"] = "Random Sample"

to_merge = pd.concat([intermediaries_df_enriched_top_5_percent_intermediaries, intermediaries_df_enriched_random_sample_500])
to_merge.value_counts("type")

# %%
# Merging onto
intermediaries_df = intermediaries_df.merge(
    to_merge, 
    on="name", 
    how="left"
)

# %% [markdown]
# # Preliminary and Overview Figures

# %% [markdown]
# ## Timeline of Incorporations

# %%
entities_df['incorporation_year'] = entities_df['incorporation_date'].dt.year
entities_valid = entities_df.dropna(subset=['incorporation_year', 'country_codes'])
entities_valid['incorporation_year'] = entities_valid['incorporation_year'].astype(int)

agg_counts = (
    entities_valid.groupby(['incorporation_year', 'source'])
    .size().reset_index(name='count')
)

plt.figure(figsize=(15, 8))
ax = sns.lineplot(x='incorporation_year', y='count', data=agg_counts, hue='source', linewidth=3)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.xlim([1980, 2020])

plt.axvline(x=MEAN_INCORPORATION_YEAR, color='gray', linestyle='--', alpha=0.7, label="Mean Incorporation Year", linewidth=2)

plt.xlabel('Year of Incorporation', fontsize=12)
plt.ylabel('Number of Entities', fontsize=12)
plt.title('Entity Incorporations Over Time by Source in ICIJ Data', fontsize=18, pad=20, fontweight="bold")

plt.legend(loc='upper left', fontsize=17)

ax.yaxis.grid(True, linestyle='-', alpha=0.5)
ax.xaxis.grid(False)

plt.tight_layout()
plt.savefig(PLOTS_PATH / "Preliminary_Incorporations_over_Time.png")

# %% [markdown]
# ## Degree Distribution of Intermediaries:
#
# * Show power-alw distribution fits well
# * Use MLE to fit power law
# * Goodness-of-fit using Kolmogorov-Smirnov statistics. ISSUE: assumes we know parameter a priori - not fitting it a posterriori like here with MLE. Recall Lillefors correction in the context of wehn we test against normal distributions. If this is what we want, this is the seminal paper:
# * Clauset, A., Shalizi, C. R., & Newman, M. E. J. (2009). Power-law distributions in empirical data. SIAM Review, 51(4), 661-703. This paper provides a rigorous statistical framework for identifying and validating power-law distributions. 
# * An alternative to this is just comparing the fit of the power-law distribution to the fit of a log-normal distribution. Exponential makes no sense. Likelihood ratio test to confirm this 
# * Note, we already have Kejriwal \& Dang (2020) showing this, so we can just use their results if need be
#
#

# %%
data = intermediaries_df["degree"].dropna() 
fit = powerlaw.Fit(data, xmin=1, verbose=False) 

R_lognorm, p_lognorm = fit.distribution_compare('power_law', 'lognormal_positive', normalized_ratio=True)
print(f"\nLog-likelihood ratio (Power Law vs. Log-normal): R = {R_lognorm:.4f}, p-value = {p_lognorm:.4f}")

fig = plt.figure(figsize=(10, 6))
ax = plt.gca()

fit.plot_pdf(color='b', label='Intermediaries\' degree', linewidth=2)
fit.power_law.plot_pdf(color='r', linestyle='--', label=f'Fitted Power Law ($\\alpha$={fit.alpha:.2f})', linewidth=1) 
fit.lognormal_positive.plot_pdf(ax=ax, color='m', linestyle='-.', label=f'Fitted Log-Normal ($\\mu$={fit.lognormal_positive.mu:.2f}, $\\sigma$={fit.lognormal_positive.sigma:.2f})') 

plt.title('Log-Log Plot of PDF of Intermediaries\' Entities Incorporated', fontweight='bold', fontsize=14, pad=20)
plt.ylabel('Frequency (log scale)', fontsize=12)
plt.xlabel('Degree (log-scale)', fontsize=12)
plt.legend(fontsize=10)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.xaxis.grid(False)

plt.tight_layout()
plt.savefig(PLOTS_PATH / "Preliminary_Powerlaw_Fit.png")
plt.show()

# %% [markdown]
# ## Which Countries are Intermediaries/Officers/Entities in?
#
# Bar plots in 2x2 subplot across,
# * Officers
# * Intermediaries
# * Entities (both countries they are active in, as well as the jurisdictions they are incorporated in)

# %%
entities_df.head()

# %%
fig, axes = plt.subplots(2, 2, figsize=(20, 14))
axes = axes.flatten()

def create_barplot(ax, data, title, color, total_count):
    ax = sns.barplot(
        data=data,
        y='country',
        x='percentage',
        color=color,
        edgecolor='black',
        ax=ax
    )
    
    ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
    ax.tick_params(axis='y', labelsize=10)
    ax.tick_params(axis='x', labelsize=10)
    
    for i, v in enumerate(data['percentage']):
        ax.text(v + 0.5, i, f'{v:.1f}%',
                ha='left', va='center', fontsize=8, color='black', fontweight='medium')
    
    ax.set_xlabel('Percentage', fontsize=10)
    ax.set_ylabel('')
    ax.grid(axis='x', linestyle='--', alpha=0.6, color='gray')
    sns.despine(ax=ax, trim=False)
    
    # Add coverage text
    top_15_percentage = (data['count'].sum() / total_count) * 100
    coverage_text = (
        f'Coverage   \n\n'
        f'Top 15: {top_15_percentage:.1f}%\n'
        f'Rest: {100-top_15_percentage:.1f}%'
    )
    props = dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='gray', pad=1.5)
    ax.text(0.80, 0.2, coverage_text,
            transform=ax.transAxes,
            verticalalignment='bottom',
            horizontalalignment='right',
            bbox=props,
            fontsize=20,
            fontweight='medium',
            color='#333333')
    
    return ax

# Plot 1: Jurisdictions
country_counts = entities_df['jurisdiction_description'].dropna().value_counts().reset_index()
country_counts.columns = ['country', 'count']
top_15_countries = country_counts.head(15)
total_count = country_counts['count'].sum()
top_15_countries['percentage'] = (top_15_countries['count'] / total_count) * 100

ax1 = create_barplot(axes[0], top_15_countries, 
                    'Top 15 Jurisdictions by Percentage of Entities Located There',
                    '#9b59b6', total_count)

# Plot 2: Entity Countries
country_counts = entities_df['countries'].dropna().value_counts().reset_index()
country_counts.columns = ['country', 'count']
top_15_countries = country_counts.head(15)
total_count = country_counts['count'].sum()
top_15_countries['percentage'] = (top_15_countries['count'] / total_count) * 100

ax2 = create_barplot(axes[1], top_15_countries,
                    'Top 15 Countries by Percentage of Entities Active There',
                    '#3498db', total_count)

# Plot 3: Intermediary Countries
country_counts = intermediaries_df['countries'].dropna().value_counts().reset_index()
country_counts.columns = ['country', 'count']
top_15_countries = country_counts.head(15)
total_count = country_counts['count'].sum()
top_15_countries['percentage'] = (top_15_countries['count'] / total_count) * 100

ax3 = create_barplot(axes[2], top_15_countries,
                    'Top 15 Countries by Percentage of Intermediaries Based There',
                    '#2ecc71', total_count)

# Plot 4: Officer Countries
country_counts = officers_df['countries'].dropna().value_counts().reset_index()
country_counts.columns = ['country', 'count']
top_15_countries = country_counts.head(15)
total_count = country_counts['count'].sum()
top_15_countries['percentage'] = (top_15_countries['count'] / total_count) * 100

ax4 = create_barplot(axes[3], top_15_countries,
                    'Top 15 Countries by Percentage of Officers Based There',
                    '#e74c3c', total_count)


plt.tight_layout()
plt.savefig(PLOTS_PATH / "Preliminary_Geography_Overview.png", dpi=300)
plt.show()

# %% [markdown]
# # Geographical Specialisation

# %% [markdown]
# ## How many Countries do Intermediaries Incorporate Entities in And Which?
# * Distribution of the number of countries they incorporate in
#
# Transition: Doesn't account for the fact that some just incorporate more!
# * Distirbution of entropy scores
#
# Transition: Groups of countries they incorporate in
#
# Graph of the countries they incorporate in approach: 
# * Edge weight increases, if an intermediary incorporates in ocuntries in common. E.g. if he has entities in Singapore and Hong kong they are proivded one more to their weight.
# * When visualising, only showing edge to reduce space from about ~125 countries according to rule of some minimum lift OR Cooccurrence threshold (E.g. minimum lift of 1.5 or minimum cooccurence of 10%)
# a. Colouring in according to regime type
# b. Colouring in according to louvain community detection
# * Reporting highest in-betweenness scores 
# * Reporting associations with highest lift scores + Fisher exact test to confirm statistical significance
#

# %%
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

sns.histplot(data=intermediaries_df, x='country_count', ax=ax1, 
             color='#3498db', alpha=0.7, edgecolor='black', binwidth=0.5)
ax1.set_xlabel('Number of Countries', labelpad=10)
ax1.set_xlim(1, 10)
ax1.set_ylabel('Count', labelpad=10)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

y = intermediaries_df['country_count'].value_counts().sort_index()
ax1.grid(axis='x')
ax1.set_title('Countries Entities Active in per Intermediary', pad=15, weight='bold')

sns.scatterplot(data=intermediaries_df, x='country_count', y='log_degree', 
                ax=ax2, alpha=0.4, color='#3498db', s=50)
ax2.set_xlabel('Countries with Entities Active', labelpad=10)
ax2.set_ylabel('Log-Degree', labelpad=10)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.grid(axis='x')
ax2.set_title('Country-count vs Degree of Intermediaries', pad=15, weight='bold')

plt.tight_layout()
plt.savefig(PLOTS_PATH / "Geography_Distribution_of_Countries_by_Intermediary.png")
plt.show()


# %%
def create_intermediary_network(df, count_column):
    """ Edge weight increases if an intermediary incorporates in countries in common. """
    G = nx.Graph()
    for counts in df[count_column]:
        locs = [loc for loc in counts.keys() if loc != "XXX"]
        for i in range(len(locs)):
            for j in range(i + 1, len(locs)):
                u, v = locs[i], locs[j]
                if not G.has_node(u): G.add_node(u)
                if not G.has_node(v): G.add_node(v)
                if G.has_edge(u, v):
                    G[u][v]['weight'] += 1
                else:
                    G.add_edge(u, v, weight=1)
    return G

def get_node_stats(df, count_column):
    node_appearances = {}
    for counts in df[count_column]:
        for node in counts:
            node_appearances[node] = node_appearances.get(node, 0) + 1
    return node_appearances

def filter_graph_for_visualization(G_original, node_counts_per_location,
                                   total_intermediaries, lift_threshold,
                                   support_threshold, min_loc_appearances):
    """ Filters by lift & support and minimum node appearances. """
    Gf = nx.Graph()
    # add nodes meeting appearance threshold
    valid_nodes = {n for n, c in node_counts_per_location.items() if c >= min_loc_appearances}
    Gf.add_nodes_from(valid_nodes)
    kept = []
    for u, v, data in G_original.edges(data=True):
        if u not in valid_nodes or v not in valid_nodes:
            continue
        N_uv = data['weight']
        N_u = node_counts_per_location.get(u, 0)
        N_v = node_counts_per_location.get(v, 0)
        support = N_uv / total_intermediaries if total_intermediaries else 0
        lift = (N_uv * total_intermediaries) / (N_u * N_v) if N_u and N_v else 0
        if lift >= lift_threshold and support >= support_threshold:
            Gf.add_edge(u, v, weight=N_uv, lift=lift, support=support)
            kept.append((u, v))
    Gf.remove_nodes_from(list(nx.isolates(Gf)))
    print(f"Kept {len(kept)} edges after filtering.")
    return Gf

def plot_network(G, ax, title="Network Visualization",
                 k_spring=0.1, node_size=300, font_size=8, color_by='regime'):
    if not G.nodes:
        ax.set_title(f"{title} (Empty)")
        ax.axis('off')
        return
    pos = nx.spring_layout(G, k=k_spring, iterations=50, seed=42)
    if color_by == 'regime':
        regime_colors = {
            'Liberal Democracy': 'green',
            'Electoral Democracy': 'lightgreen',
            'Electoral Autocracy': 'orange',
            'Closed Autocracy': 'red',
            'Micro-state': 'purple'
        }
        node_colors = []
        for node in G.nodes():
            sub = entities_df[entities_df['country_codes'] == node]
            regime = sub['v2x_regime'].iloc[0] if not sub.empty else 'Unknown'
            node_colors.append(regime_colors.get(regime, 'grey'))
        legend_elems = [
            plt.Line2D([0], [0], marker='o', color='w',
                       markerfacecolor=color, label=regime, markersize=8)
            for regime, color in regime_colors.items()
        ]
    elif color_by == 'legal_technology':
        # Determine which legal technologies are actually used by nodes in the graph
        techs_used = set()
        for node in G.nodes():
            sub = entities_df[entities_df['country_codes'] == node]
            if not sub.empty:
                tech = sub['jurisdiction_legal_technology'].iloc[0]
                if pd.notna(tech):
                    techs_used.add(tech)
        unique_techs = sorted(techs_used)
        # Build a colormap only as large as the number of used technologies
        cmap = plt.cm.get_cmap('tab10', len(unique_techs))
        tech_to_idx = {tech: idx for idx, tech in enumerate(unique_techs)}
        # Assign colors to nodes based on their technology
        node_colors = []
        for node in G.nodes():
            sub = entities_df[entities_df['country_codes'] == node]
            tech = sub['jurisdiction_legal_technology'].iloc[0] if not sub.empty else None
            idx = tech_to_idx.get(tech)
            node_colors.append(cmap(idx) if idx is not None else 'grey')
        # Legend entries only for technologies present in the graph
        legend_elems = [
            plt.Line2D([0], [0], marker='o', color='w',
                       markerfacecolor=cmap(tech_to_idx[tech]), label=tech, markersize=8)
            for tech in unique_techs
        ]
    else:  
        comms = nx.community.greedy_modularity_communities(G)
        cmap = plt.cm.get_cmap('tab20', len(comms))
        comm_map = {n: i for i, com in enumerate(comms) for n in com}
        node_colors = [cmap(comm_map[n]) for n in G.nodes()]
        legend_elems = [
            plt.Line2D([0], [0], marker='o', color='w',
                       markerfacecolor=cmap(i), label=f'Comm {i}', markersize=8)
            for i in range(len(comms))
        ]
    nx.draw_networkx_nodes(G, pos, node_size=node_size, node_color=node_colors, ax=ax, alpha=0.8)
    weights = [G[u][v]['weight'] for u,v in G.edges()]
    mx = max(weights) if weights else 1
    widths = [max(0.5, min(5, w/(mx/10))) for w in weights]
    nx.draw_networkx_edges(G, pos, width=widths, ax=ax, alpha=0.6, edge_color='slategrey')
    nx.draw_networkx_labels(G, pos, font_size=font_size, ax=ax)
    ax.legend(handles=legend_elems, loc='center left', bbox_to_anchor=(1,0.5))
    ax.set_title(title)
    ax.axis('off')


# %%
# 1. Build full graph and node stats
total_intermediaries_count = intermediaries_df.shape[0]
G_full_countries = create_intermediary_network(intermediaries_df, "country_counts")

with open(TABLES_PATH / "country_network_stats.txt", "w") as f:
    f.write(f"Full country network: {G_full_countries.number_of_nodes()} nodes, {G_full_countries.number_of_edges()} edges\n")
    f.write(f"Network density: {nx.density(G_full_countries):.4f}\n")
    f.write(f"Average degree: {sum(dict(G_full_countries.degree()).values())/G_full_countries.number_of_nodes():.2f}\n")
    f.write(f"Average clustering coefficient: {nx.average_clustering(G_full_countries):.4f}\n")
    f.write(f"Number of connected components: {nx.number_connected_components(G_full_countries)}\n")

    singletons = [n for n, d in G_full_countries.degree() if d == 0]
    f.write(f"Number of singletons: {len(singletons)}\n")
    f.write(f"Percentage of singletons: {(len(singletons)/G_full_countries.number_of_nodes())*100:.2f}%\n")

    node_loc_appearances = get_node_stats(intermediaries_df, "country_counts")
    f.write("\nCountry node appearances:\n")
    f.write(str(node_loc_appearances) + "\n")

    # Get regime mapping from entities_df
    regime_mapping = entities_df.groupby('country_codes')['v2x_regime'].first().to_dict()
    exclude_nodes = {'XXX'}

    # 2. Top 10 central nodes by betweenness and eigenvector centrality (excluding XXX)
    betw = nx.betweenness_centrality(G_full_countries, normalized=True)
    eig = nx.eigenvector_centrality(G_full_countries, max_iter=1000)

    top10_betw = pd.DataFrame(
        sorted(betw.items(), key=lambda x: x[1], reverse=True),
        columns=['node', 'betweenness']
    )
    top10_betw = top10_betw[~top10_betw['node'].isin(exclude_nodes)].head(10)
    top10_betw['eigenvector'] = top10_betw['node'].map(lambda n: eig.get(n, 0))
    top10_betw['appearances'] = top10_betw['node'].map(node_loc_appearances)
    top10_betw['regime'] = top10_betw['node'].map(lambda n: regime_mapping.get(n, 'Unknown'))
    f.write("\nTop 10 countries by betweenness centrality (excluding XXX):\n")
    f.write(top10_betw.to_string() + "\n")

    top10_eig = pd.DataFrame(
        sorted(eig.items(), key=lambda x: x[1], reverse=True),
        columns=['node', 'eigenvector']
    )
    top10_eig = top10_eig[~top10_eig['node'].isin(exclude_nodes)].head(10)
    top10_eig['betweenness'] = top10_eig['node'].map(lambda n: betw.get(n, 0))
    top10_eig['appearances'] = top10_eig['node'].map(node_loc_appearances)
    top10_eig['regime'] = top10_eig['node'].map(lambda n: regime_mapping.get(n, 'Unknown'))
    f.write("\nTop 10 countries by eigenvector centrality (excluding XXX):\n")
    f.write(top10_eig.to_string() + "\n")

    # 3. Top 20 significant associations via Fisher's exact test (excluding XXX)
    records = []
    for u, v, data in G_full_countries.edges(data=True):
        if u in exclude_nodes or v in exclude_nodes:
            continue
        N_uv = data['weight']
        N_u = node_loc_appearances.get(u, 0)
        N_v = node_loc_appearances.get(v, 0)
        a = N_uv
        b = N_u - N_uv
        c = N_v - N_uv
        d = total_intermediaries_count - (N_u + N_v - N_uv)
        oddsratio, pval = fisher_exact([[a, b], [c, d]], alternative='greater')
        support = N_uv / total_intermediaries_count if total_intermediaries_count else 0
        lift = (N_uv * total_intermediaries_count) / (N_u * N_v) if N_u and N_v else 0
        
        u_regime = regime_mapping.get(u, 'Unknown')
        v_regime = regime_mapping.get(v, 'Unknown')
        
        records.append({
            'u': u, 'v': v, 'weight': N_uv,
            'support': support, 'lift': lift,
            'odds_ratio': oddsratio, 'p_value': pval,
            'u_regime': u_regime,
            'v_regime': v_regime
        })

    fisher_df = pd.DataFrame(records)
    n_nodes = G_full_countries.number_of_nodes()
    m_tests = int(n_nodes * (n_nodes - 1) / 2)
    alpha = 0.05
    bonferroni_threshold = alpha / m_tests

    significant_pairs = fisher_df[fisher_df['p_value'] < bonferroni_threshold].sort_values('p_value')

    f.write(f"\nNumber of nodes: {n_nodes}, hypothesis tests (pairs): {m_tests}\n")
    f.write(f"Bonferroni p-value threshold (@α={alpha}): {bonferroni_threshold:.2e}\n")
    f.write(f"Number of significant associations after Bonferroni correction: {len(significant_pairs)}\n")
    f.write("\nSignificant country associations after Bonferroni correction (excluding XXX):\n")
    f.write(significant_pairs[['u', 'v', 'u_regime', 'v_regime', 'weight', 'support', 'lift', 'odds_ratio', 'p_value']].to_string() + "\n")

# 4. Filter the graph
G_filtered_countries = filter_graph_for_visualization(
    G_original=G_full_countries,
    node_counts_per_location=node_loc_appearances,
    total_intermediaries=total_intermediaries_count,
    lift_threshold=1.5,
    support_threshold=0.0008,
    min_loc_appearances=1
)

nx.set_node_attributes(G_filtered_countries,
                      {node: {'regime': regime_mapping.get(node, 'Unknown')}
                       for node in G_filtered_countries.nodes()})

with open(TABLES_PATH / "country_network_stats.txt", "a") as f:
    f.write(f"\nFiltered graph: {G_filtered_countries.number_of_nodes()} nodes, {G_filtered_countries.number_of_edges()} edges\n")

# 5. Plot the filtered network
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20,10))
plot_network(G_filtered_countries, ax1, title="By Regime (VDem)",
                k_spring=2, node_size=1500, font_size=12, color_by="regime")
plot_network(G_filtered_countries, ax2, title="By Community (Louvain Method)",
                k_spring=2, node_size=1500, font_size=12, color_by="community")
plt.tight_layout()
plt.savefig(PLOTS_PATH / "Geography_Cross_Country_Network.png")
plt.show()

# %% [markdown]
# Just as interesting to note which ones are left out! Notice, Malta, Switzerland, Luxembourg all very represented! but not here!

# %% [markdown]
# ## Which Jurisidctions do they Incorporate in?
# * Power-law distribution of how many they incorporate
# * Distribution of the number of jurisdictions they incorporate in
#
# Same transition:
# * Distirbution of entropy scores
#
# Same approach as above with the jurisdictions they incorporate in.
# * EXCEPT: Colouring in according to legal technology types
# * Reporting highest in-betweenness scores
# * Reporting associations with highest lift scores + Fisher exact test to confirm statistical significance

# %%
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

sns.histplot(data=intermediaries_df, x='jurisdiction_count', ax=ax1, 
             color='#9b59b6', alpha=0.7, edgecolor='black', binwidth=0.5)
ax1.set_xlabel('Number of Jurisdictions', labelpad=10)
ax1.set_xlim(1, 10)
ax1.set_ylabel('Count', labelpad=10)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

y = intermediaries_df['jurisdiction_count'].value_counts().sort_index()
ax1.grid(axis='x')
ax1.set_title('Jurisdictions per Intermediary', pad=15, weight='bold')

sns.scatterplot(data=intermediaries_df, x='jurisdiction_count', y='log_degree', 
                ax=ax2, alpha=0.4, color='#9b59b6', s=50)
ax2.set_xlabel('Number of Jurisdictions', labelpad=10)
ax2.set_ylabel('Log-Degree', labelpad=10)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.grid(axis='x')
ax2.set_title('Jurisdiction-count vs Degree of Intermediaries', pad=15, weight='bold')

plt.tight_layout()
plt.savefig(PLOTS_PATH / "Geography_Distribution_of_Jurisdictions_by_Intermediary.png")
plt.show()

# %%
# 1. Build full graph and node stats using jurisdiction_counts
total_intermediaries_count = intermediaries_df.shape[0]
G_full_jurisdictions = create_intermediary_network(intermediaries_df, "jurisdiction_counts")

with open(TABLES_PATH / "jurisdiction_network_stats.txt", "w") as f:
    f.write(f"Full jurisdiction network: {G_full_jurisdictions.number_of_nodes()} nodes, {G_full_jurisdictions.number_of_edges()} edges\n")
    f.write(f"Network density: {nx.density(G_full_jurisdictions):.4f}\n")
    f.write(f"Average degree: {sum(dict(G_full_jurisdictions.degree()).values())/G_full_jurisdictions.number_of_nodes():.2f}\n")
    f.write(f"Average clustering coefficient: {nx.average_clustering(G_full_jurisdictions):.4f}\n")
    f.write(f"Number of connected components: {nx.number_connected_components(G_full_jurisdictions)}\n")

    singletons = [n for n, d in G_full_jurisdictions.degree() if d == 0]
    f.write(f"Number of singletons: {len(singletons)}\n")
    f.write(f"Percentage of singletons: {(len(singletons)/G_full_jurisdictions.number_of_nodes())*100:.2f}%\n")

    node_jurisd_appearances = get_node_stats(intermediaries_df, "jurisdiction_counts")
    f.write("\nJurisdiction node appearances:\n")
    f.write(str(node_jurisd_appearances) + "\n")

    jurisdiction_tech_mapping = entities_df.groupby('jurisdiction')['jurisdiction_legal_technology'].first().to_dict()
    exclude_nodes = {'XXX'}

    # 2. Top 10 central nodes by betweenness and eigenvector centrality (excluding XXX)
    betw = nx.betweenness_centrality(G_full_jurisdictions, normalized=True)
    eig = nx.eigenvector_centrality(G_full_jurisdictions, max_iter=1000)

    top10_betw = pd.DataFrame(
        sorted(betw.items(), key=lambda x: x[1], reverse=True),
        columns=['node', 'betweenness']
    )
    top10_betw = top10_betw[~top10_betw['node'].isin(exclude_nodes)].head(10)
    top10_betw['eigenvector'] = top10_betw['node'].map(lambda n: eig.get(n, 0))
    top10_betw['appearances'] = top10_betw['node'].map(node_jurisd_appearances)
    top10_betw['jurisdiction_legal_technology'] = top10_betw['node'].map(lambda n: jurisdiction_tech_mapping.get(n, 'Unknown'))
    f.write("\nTop 10 jurisdictions by betweenness centrality (excluding XXX):\n")
    f.write(top10_betw.to_string() + "\n")

    top10_eig = pd.DataFrame(
        sorted(eig.items(), key=lambda x: x[1], reverse=True),
        columns=['node', 'eigenvector']
    )
    top10_eig = top10_eig[~top10_eig['node'].isin(exclude_nodes)].head(10)
    top10_eig['betweenness'] = top10_eig['node'].map(lambda n: betw.get(n, 0))
    top10_eig['appearances'] = top10_eig['node'].map(node_jurisd_appearances)
    top10_eig['jurisdiction_legal_technology'] = top10_eig['node'].map(lambda n: jurisdiction_tech_mapping.get(n, 'Unknown'))
    f.write("\nTop 10 jurisdictions by eigenvector centrality (excluding XXX):\n")
    f.write(top10_eig.to_string() + "\n")

    # 3. Top 20 significant jurisdiction associations via Fisher's exact test (excluding XXX)
    records = []
    for u, v, data in G_full_jurisdictions.edges(data=True):
        if u in exclude_nodes or v in exclude_nodes:
            continue
        N_uv = data['weight']
        N_u = node_jurisd_appearances.get(u, 0)
        N_v = node_jurisd_appearances.get(v, 0)
        a = N_uv
        b = N_u - N_uv
        c = N_v - N_uv
        d = total_intermediaries_count - (N_u + N_v - N_uv)
        oddsratio, pval = fisher_exact([[a, b], [c, d]], alternative='greater')
        support = N_uv / total_intermediaries_count if total_intermediaries_count else 0
        lift = (N_uv * total_intermediaries_count) / (N_u * N_v) if N_u and N_v else 0
        
        u_tech = jurisdiction_tech_mapping.get(u, 'Unknown')
        v_tech = jurisdiction_tech_mapping.get(v, 'Unknown')
        
        records.append({
            'u': u, 'v': v, 'weight': N_uv,
            'support': support, 'lift': lift,
            'odds_ratio': oddsratio, 'p_value': pval,
            'u_jurisdiction_legal_technology': u_tech,
            'v_jurisdiction_legal_technology': v_tech
        })

    fisher_df = pd.DataFrame(records)
    n_nodes = G_full_jurisdictions.number_of_nodes()
    m_tests = int(n_nodes * (n_nodes - 1) / 2)
    alpha = 0.05
    bonferroni_threshold = alpha / m_tests

    significant_pairs = fisher_df[fisher_df['p_value'] < bonferroni_threshold].sort_values('p_value')

    f.write(f"\nNumber of nodes: {n_nodes}, hypothesis tests (pairs): {m_tests}\n")
    f.write(f"Bonferroni p-value threshold (@α={alpha}): {bonferroni_threshold:.2e}\n")
    f.write(f"Number of significant associations after Bonferroni correction: {len(significant_pairs)}\n")
    f.write("\nSignificant jurisdiction associations after Bonferroni correction (excluding XXX):\n")
    f.write(significant_pairs[['u', 'v', 'u_jurisdiction_legal_technology', 'v_jurisdiction_legal_technology', 'weight', 'support', 'lift', 'odds_ratio', 'p_value']].to_string() + "\n")

# 4. Filter the jurisdiction graph
G_filtered_jurisdictions = filter_graph_for_visualization(
    G_original=G_full_jurisdictions,
    node_counts_per_location=node_jurisd_appearances,
    total_intermediaries=total_intermediaries_count,
    lift_threshold=1.5, support_threshold=0.0008,
    min_loc_appearances=1
)

nx.set_node_attributes(G_filtered_jurisdictions, 
                      {node: {'jurisdiction_legal_technology': jurisdiction_tech_mapping.get(node, 'Unknown')} 
                       for node in G_filtered_jurisdictions.nodes()})

with open(PLOTS_PATH / "jurisdiction_network_stats.txt", "a") as f:
    f.write(f"\nFiltered graph: {G_filtered_jurisdictions.number_of_nodes()} nodes, {G_filtered_jurisdictions.number_of_edges()} edges\n")

# 5. Plot the filtered network colored by legal technology category and community
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20,10))
plot_network(
    G_filtered_jurisdictions, ax1,
    title="By Legal Technology (Lafitte Dataset)",
    k_spring=2, node_size=1500, font_size=12,
    color_by="legal_technology"
)
plot_network(
    G_filtered_jurisdictions, ax2,
    title="By Community (Louvain Method)",
    k_spring=2, node_size=1500, font_size=12,
    color_by="community"
)
plt.tight_layout()
plt.savefig(PLOTS_PATH / "Geography_Cross_Jurisdiction_Network.png")
plt.show()


# %% [markdown]
# ## What are the most common intermediary-country to entity-country/jurisdiction pair? 
# * Bipartite graph too difficult to visualise, so 
# * Using country_codes associated to intermediaries (taking 15 most common ones), and then using their country_counts object to create heatmap. Recall, object structure: country_counts_ex = {"ZAM": n_entities_in_ZAM, "SGP": n_entities_in_SGP, ....}
# * we just show the distribution of two countries: Cyprean intermediaries and Singaporean, for example
# * And Heatmap of 15 or so biggest entities by cooccurence (e.g. row sums to 1)
# * Also, computing kde of country_entropy and jurisdictoin_entropy

# %%
# Map v2x_regime to broader regime categories
regime_mapping = {
    'Closed Autocracy': 'Autocracy',
    'Electoral Autocracy': 'Autocracy',
    'Electoral Democracy': 'Democracy',
    'Liberal Democracy': 'Democracy',
    'Micro-state': 'Micro-state'
}

entities_df['regime_broad'] = entities_df['v2x_regime'].map(regime_mapping)


# %%
def compute_country_stats(country):
    """
    Compute regime, entropies, and proportion DataFrames for a given country code.
    """
    subset = intermediaries_df[
        intermediaries_df['country_codes_split'].apply(
            lambda x: country in x if isinstance(x, list) else False
        )
    ]

    ent_df = entities_df[entities_df['country_codes'] == country]
    regime_broad = ent_df['regime_broad'].iloc[0] if not ent_df.empty else None

    total_country_counts = Counter()
    total_jurisdiction_counts = Counter()
    for d in subset['country_counts'].dropna():
        if isinstance(d, dict):
            filtered = {k: v for k, v in d.items() if k != 'XXX'}
            total_country_counts.update(filtered)
    for d in subset['jurisdiction_counts'].dropna():
        if isinstance(d, dict):
            filtered = {k: v for k, v in d.items() if k != 'XXX'}
            total_jurisdiction_counts.update(filtered)

    entropy_countries = calculate_normalized_entropy(total_country_counts)
    entropy_jurisdictions = calculate_normalized_entropy(total_jurisdiction_counts)

    def build_prop_df(counter_obj):
        top_keys = [k for k, _ in counter_obj.most_common(5)]
        counts = [counter_obj[k] for k in top_keys]
        residual = sum(counter_obj.values()) - sum(counts)
        counts.append(residual)
        cols = top_keys + ['Other']
        df = pd.DataFrame([counts], columns=cols)
        return df.div(df.sum(axis=1), axis=0)

    country_prop_df = build_prop_df(total_country_counts)
    jurisdiction_prop_df = build_prop_df(total_jurisdiction_counts)

    return {
        'country': country,
        'regime_broad': regime_broad,
        'entropy_countries': entropy_countries,
        'entropy_jurisdictions': entropy_jurisdictions,
        'country_prop_df': country_prop_df,
        'jurisdiction_prop_df': jurisdiction_prop_df
    }

intermediaries_df['country_codes_split'] = intermediaries_df['country_codes'].str.split(';')
intermediaries_df_exploded = intermediaries_df.explode('country_codes_split')

valid_countries = (
    intermediaries_df_exploded['country_codes_split']
      .dropna()
      .loc[lambda s: s != 'XXX']
      .unique()
      .tolist()
)

stats_all = [compute_country_stats(code) for code in valid_countries]

countries_intermediaries = pd.DataFrame.from_records(
    [
        {
            'country': d['country'],
            'regime_broad': d['regime_broad'],
            'entropy_countries': d['entropy_countries'],
            'entropy_jurisdictions': d['entropy_jurisdictions']
        }
        for d in stats_all
    ]
).set_index('country')

# %%
import seaborn as sns
import numpy as np


def plot_country_heatmaps(stats_list, path_to_save_to: Optional[Path] = None):
    """Plot country and jurisdiction heatmaps for 1 to N countries (up to 5)."""
    n = len(stats_list)
    # create a 2 x n grid of subplots, ensure axes is always 2D
    fig, axes = plt.subplots(
        2, n,
        figsize=(4 * n, 3),
        squeeze=False,
        gridspec_kw={'hspace': 0.3}
    )
    for i, stats in enumerate(stats_list):
        country = stats['country']
        ax1, ax2 = axes[0, i], axes[1, i]

        # country proportion heatmap
        sns.heatmap(
            stats['country_prop_df'],
            ax=ax1,
            annot=True,
            fmt=".2f",
            cbar=False,
            cmap='Blues',
            yticklabels=False
        )
        ax1.set_title(
            f"$\\mathbf{{{country}}}$\n"
            f"$H_c$={stats['entropy_countries']:.2f}, "
            f"$H_j$={stats['entropy_jurisdictions']:.2f}"
        )
        ax1.set_xlabel('')
        ax1.set_ylabel('Countries')

        # jurisdiction proportion heatmap
        sns.heatmap(
            stats['jurisdiction_prop_df'],
            ax=ax2,
            annot=True,
            fmt=".2f",
            cbar=False,
            cmap='Purples',
            yticklabels=False
        )
        ax2.set_xlabel('')
        ax2.set_ylabel('Jurisdictions')

    # adjust layout to prevent cropping when saving
    fig.tight_layout()
    if path_to_save_to:
        # save with tight bounding box to avoid truncation
        fig.savefig(path_to_save_to, bbox_inches='tight', pad_inches=0.1)
    plt.show()

# plotting heatmaps for top 15 countries
country_counts = (
    intermediaries_df_exploded
      .loc[intermediaries_df_exploded['country_codes_split'] != 'XXX', 'country_codes_split']
      .value_counts()
)
top15_countries = country_counts.head(15).index.tolist()
stats_top15 = [compute_country_stats(code) for code in top15_countries]


paths_to_save_to = [
    PLOTS_PATH / "Geography_Country_Heatmaps_Top5.png",
    PLOTS_PATH / "Geography_Country_Heatmaps_Top6_10.png",
    PLOTS_PATH / "Geography_Country_Heatmaps_Top11_15.png",
]
paths_to_save_cyprus = PLOTS_PATH / "Geography_Country_Heatmaps_Cyprus.png"

for i in range(0, len(stats_top15), 5):
    batch = stats_top15[i:i+5]
    plot_country_heatmaps(batch, paths_to_save_to[i//5])

# plot Cyprus separately for fun
stats_cyprus = compute_country_stats('CYP')
plot_country_heatmaps([stats_cyprus], paths_to_save_cyprus)


# %%
country_counts = (
    intermediaries_df_exploded
    .loc[intermediaries_df_exploded['country_codes_split'] != 'XXX', 'country_codes_split']
    .value_counts()
)
countries_intermediaries= (
    pd.DataFrame([
        {
            'country': s['country'],
            'entropy_country': s['entropy_countries'],
            'entropy_jurisdiction': s['entropy_jurisdictions'],
            'count': country_counts.get(s['country'], 0)
        }
        for s in stats_all
    ])
    .query('count > 100')
)

# Perform KS test
from scipy import stats as scipy_stats
ks_stat, p_value = scipy_stats.ks_2samp(
    countries_intermediaries['entropy_country'],
    countries_intermediaries['entropy_jurisdiction']
)

countries_intermediaries_long = (
    pd.DataFrame([
        {
            'country': s['country'],
            'entropy_country': s['entropy_countries'],
            'entropy_jurisdiction': s['entropy_jurisdictions'],
            'count': country_counts.get(s['country'], 0)
        }
        for s in stats_all
    ])
    .query('count > 100')
    .melt(
        id_vars=['country'],
        value_vars=['entropy_country', 'entropy_jurisdiction'],
        var_name='entropy_type',
        value_name='entropy'
    )
)

plt.figure(figsize=(10, 6))
ax = sns.kdeplot(
    data=countries_intermediaries_long,
    x='entropy',
    hue='entropy_type',
    fill=True,
    alpha=0.7,
    palette=['#3498db', '#9b59b6'],
    label='Country Entropy', 
    clip=(0, 1)  
)

country_mean = countries_intermediaries.entropy_country.mean()
jurisdiction_mean = countries_intermediaries.entropy_jurisdiction.mean()

plt.axvline(x=country_mean, color='#3498db', linestyle='--', alpha=0.7)
plt.axvline(x=jurisdiction_mean, color='#9b59b6', linestyle='--', alpha=0.7)

plt.title('Distribution of Country vs Jurisdiction Entropy', fontweight='bold')
plt.xlabel('Normalised Entropy')
plt.ylabel('Density')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.legend(
    title='Entropy Type',
    labels=[
        f'Jurisdiction Entropy (mean: {jurisdiction_mean:.2f})',
        f'Country Entropy (mean: {country_mean:.2f})'
    ]
)

# Add KS test results to plot
plt.annotate(
    f'KS test: p={p_value:.7f}',
    xy=(0.02, 0.95),
    xycoords='axes fraction',
    bbox=dict(boxstyle='round', facecolor='white', alpha=0.8)
)

plt.tight_layout()
plt.savefig(PLOTS_PATH / "Geography_Country_Level_Entropy_Distribution.png")
plt.show()

# %% [markdown]
# # Functional Specialisation

# %% [markdown]
# ## Differences in Entropies + Bearer Shares
# Looking across the different types of entropy scores and the share of entities whom use bearer instruments.
# HOW TO TEST SIGNIFICANCE HERE?
#  

# %%
random_sample = intermediaries_df[intermediaries_df['type'] == 'Random Sample']

random_sample['bearer_dummy'] = (random_sample['bearer_share'] > 0).astype(int)

entropy_means = random_sample.groupby('classification')[['legal_tech_entropy', 'jurisdiction_entropy', 'regime_entropy', 'country_entropy', 'bearer_dummy']].mean()
entropy_means = entropy_means.sort_values('legal_tech_entropy', ascending=False)

plt.figure(figsize=(15, 8))
ax = entropy_means[['legal_tech_entropy', 'jurisdiction_entropy', 'regime_entropy', 'country_entropy', 'bearer_dummy']].plot(
    kind='bar',
    stacked=False,
    colormap='Set2',
    width=0.6,
    edgecolor='black',
    linewidth=1
)

plt.axvline(x=1.5, color='black', linestyle=':', alpha=0.8, linewidth=2, label='_nolegend_')

plt.title('Average Entropy and Bearer Usage by Classification', fontweight='bold', pad=20)
plt.ylabel('', labelpad=10)
plt.xlabel('')

plt.xticks(rotation=45, ha='right')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.grid(axis='y', linestyle='--', alpha=0.3)

for spine in ax.spines.values():
    spine.set_color('black')
    spine.set_linewidth(0.8)

legend_labels = {
    'legal_tech_entropy': 'Legal Technology Diversity',
    'jurisdiction_entropy': 'Jurisdiction Diversity',
    'regime_entropy': 'Political Regime Diversity',
    'country_entropy': 'Country Diversity',
    'bearer_dummy': 'Bearer Share Usage'
}

plt.legend(
    title='Metric',
    labels=[legend_labels[col] for col in entropy_means.columns],
    frameon=True,
    edgecolor='black'
)

plt.tight_layout()
plt.ylabel('Mean')
plt.savefig(PLOTS_PATH / "Specialisation_Average_Entropy_and_Bearer_Usage_by_Classification.png")
plt.show()

# Statistical tests for each metric with Bonferroni correction
# Fisher's exact test for bearer_dummy
# Mann-Whitney U test for the rest (entropy is continuous - and not normally distributed)
from scipy.stats import mannwhitneyu, fisher_exact

metrics = ['legal_tech_entropy', 'jurisdiction_entropy', 'regime_entropy', 'country_entropy', 'bearer_dummy']
classifications = entropy_means.index.tolist()  

# Bonferoni correction
n_classifications = len(classifications)
n_pairs = (n_classifications * (n_classifications - 1)) // 2
n_metrics = len(metrics)
total_comparisons = n_pairs * n_metrics
bonferroni_alpha = 0.05 / total_comparisons

print("\nStatistical Test Results (with Bonferroni correction):")
print("-" * 70)
print(f"Total comparisons: {total_comparisons}")
print(f"Bonferroni-corrected alpha: {bonferroni_alpha:.6f}")
print("-" * 70)

for metric in metrics:
    print(f"\n{metric.upper()}:")
    print("-" * 30)

    for i, class1 in enumerate(classifications):
        for class2 in classifications[i+1:]:
            group1 = random_sample[random_sample['classification'] == class1][metric]
            group2 = random_sample[random_sample['classification'] == class2][metric]
            
            if metric == 'bearer_dummy':
                # Create contingency table for Fisher's exact test
                table = np.array([
                    [sum(group1 == 1), sum(group1 == 0)],
                    [sum(group2 == 1), sum(group2 == 0)]
                ])
                stat, pval = fisher_exact(table)
                print(f"{class1} vs {class2}:")
                print(f"Odds ratio: {stat:.2f}")
            else:
                stat, pval = mannwhitneyu(group1, group2, alternative='two-sided')
                print(f"{class1} vs {class2}:")
                print(f"U-statistic: {stat:.2f}")
            
            print(f"p-value: {pval:.6f}")
            print(f"Significant: {'Yes' if pval < bonferroni_alpha else 'No'}")
            print()


# %% [markdown]
# ## Differences in Degrees:
# * CDF of the different types showing it.
# * Comparison of random smaple vs. the the ones in the top 500 - e.g. administrators the ones that have an incredibly high degree, whereas we tax experts and legal experts more personal advisory. Not connected to as many.
#
#

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kruskal, ks_2samp
from statsmodels.stats.multitest import multipletests # For p-value correction
import itertools # For generating pairs


fig, ax = plt.subplots(figsize=(12, 7)) 

random_sample_df = intermediaries_df[intermediaries_df["type"] == "Random Sample"].copy()

classifications = sorted(random_sample_df['classification'].unique()) 

print("\nDegree Statistics by Classification (Random Sample):")
degrees_by_classification_dict = {} 

for classification in classifications:
    mask = random_sample_df['classification'] == classification
    degrees = random_sample_df[mask]['degree']
    
    if degrees.empty:
        print(f"\nNo data for {classification} in Random Sample. Skipping.")
        continue
    
    degrees_by_classification_dict[classification] = degrees.values 

    stats = degrees.describe()
    print(f"\n{classification}:")
    print(f"  Count: {stats['count']:.0f}")
    print(f"  Mean: {stats['mean']:.2f}")
    print(f"  Median: {stats['50%']:.2f}")
    print(f"  Std Dev: {stats['std']:.2f}")
    print(f"  Min: {stats['min']:.0f}")
    print(f"  Max: {stats['max']:.0f}")
    
    sorted_degrees = np.sort(degrees)
    cdf = np.arange(1, len(sorted_degrees) + 1) / len(sorted_degrees)
    ax.plot(sorted_degrees, cdf, label=classification, linewidth=2.5, alpha=0.8)

ax.set_title(f'CDF of Degrees by Classification (Random Sample)', pad=20, fontsize=16, fontweight='bold')
ax.set_xlabel('Degree (log-scale)', fontsize=14)
ax.set_ylabel('CDF', fontsize=14)
ax.set_xscale('log')
ax.tick_params(axis='both', which='major', labelsize=12)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', linestyle='--', alpha=0.6)
ax.legend(title="Classification", frameon=True, framealpha=0.9, fontsize=11, title_fontsize=12)

plt.tight_layout()
plt.savefig(PLOTS_PATH / "Specialisation_CDF_of_Degrees_by_Classification_Random_Sample.png")
plt.show()

degrees_for_kruskal = [degrees_by_classification_dict[c] for c in classifications if c in degrees_by_classification_dict]

# 1. Omnibus Test: Kruskal-Wallis H Test
if len(degrees_for_kruskal) >= 2:
    valid_degrees_for_kruskal = [arr for arr in degrees_for_kruskal if len(arr) > 0]
    if len(valid_degrees_for_kruskal) >= 2:
        H_statistic, p_value_kruskal = kruskal(*valid_degrees_for_kruskal)
        print(f"\nKruskal-Wallis Test: H={H_statistic:.3f}, p={p_value_kruskal:.4f}")
        print("Significant difference detected" if p_value_kruskal < 0.05 else "No significant difference detected")
    else:
        print("\nNot enough groups for Kruskal-Wallis test")
else:
    print("\nNot enough groups for Kruskal-Wallis test")

# 2. Pairwise Comparisons: Two-Sample Kolmogorov-Smirnov (KS) Test
print("\nPairwise KS Tests (Bonferroni corrected):")
classifications_with_data = [c for c in classifications if c in degrees_by_classification_dict and len(degrees_by_classification_dict[c]) > 0]

if len(classifications_with_data) < 2:
    print("Not enough classifications for pairwise comparisons")
else:
    ks_results_raw_list = [] 
    
    for class1, class2 in itertools.combinations(classifications_with_data, 2):
        degrees1 = degrees_by_classification_dict[class1]
        degrees2 = degrees_by_classification_dict[class2]
        
        ks_stat, p_val_ks = ks_2samp(degrees1, degrees2)
        ks_results_raw_list.append({
            'pair': (class1, class2), 
            'KS_statistic': ks_stat, 
            'p_value_raw': p_val_ks
        })

    if not ks_results_raw_list:
        print("No valid pairs for KS testing")
    else:
        raw_p_values = [res['p_value_raw'] for res in ks_results_raw_list]
        reject, pvals_corrected, _, _ = multipletests(raw_p_values, alpha=0.05, method='bonferroni')
        
        n_comparisons = len(raw_p_values)
        bonferroni_alpha = 0.05 / n_comparisons
        print(f"\nBonferroni-corrected alpha level: {bonferroni_alpha:.6f}")

        significant_pairs = 0
        for i, result_dict in enumerate(ks_results_raw_list):
            pair_str = f"{result_dict['pair'][0]} vs {result_dict['pair'][1]}"
            print(f"{pair_str}: KS={result_dict['KS_statistic']:.3f}, p={pvals_corrected[i]:.4f}")
            if reject[i]:
                significant_pairs += 1
                print("  *Significant difference*")
        
        if significant_pairs == 0 and (p_value_kruskal >= 0.05 if 'p_value_kruskal' in locals() else True):
            print("\nNo significant differences found in pairwise comparisons")
        else:
            print(f"\nFound {significant_pairs} significantly different pair(s)")

# %%
# Comparison of random sample vs. ones in top 500
random_sample_data = intermediaries_df_enriched_random_sample_500['classification'].value_counts(normalize=True).mul(100)
top_5_percent_data = intermediaries_df_enriched_top_5_percent_intermediaries['classification'].value_counts(normalize=True).mul(100)

plt.figure(figsize=(12, 6))

x = np.arange(len(random_sample_data))
width = 0.35

for i, classification in enumerate(random_sample_data.index):
    plt.bar(x[i] - width/2, random_sample_data[classification], width, 
            label=f'Random Sample (n={len(intermediaries_df_enriched_random_sample_500)})' if i == 0 else "", 
            color='#2ecc71', edgecolor='black')
    plt.bar(x[i] + width/2, top_5_percent_data[classification], width, 
            label=f'Top 5% Intermediaries (n={len(intermediaries_df_enriched_top_5_percent_intermediaries)})' if i == 0 else "", 
            color='#3498db', edgecolor='black')
    
    plt.text(x[i] - width/2, random_sample_data[classification], 
             f'{random_sample_data[classification]:.1f}%', 
             ha='center', va='bottom')
    plt.text(x[i] + width/2, top_5_percent_data[classification], 
             f'{top_5_percent_data[classification]:.1f}%', 
             ha='center', va='bottom')

plt.title('Classification Distribution Comparison', pad=20, fontsize=14, fontweight='bold')
plt.ylabel('Percentage (%)', fontsize=12)
plt.xticks(x, random_sample_data.index, rotation=0)
plt.legend(frameon=True, framealpha=0.95)

plt.grid(axis='y', linestyle='--', alpha=0.7, color='gray')

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.margins(y=0.1)

plt.tight_layout()
plt.savefig(PLOTS_PATH / "Specialisation_Classification_Distribution_Comparison.png")
plt.show()

# %% [markdown]
# ## Case studies of one of each type (in the appendix)
# having the case study of each of those revealed into the appendix
#

# %%
random_sample = intermediaries_df[intermediaries_df["type"] == "Random Sample"]
stratified_sample = pd.concat([
    random_sample[random_sample['classification'] == 'Administrator'].sample(n=1, random_state=42),
    random_sample[random_sample['classification'] == 'Investment Advisor'].sample(n=1, random_state=42),
    random_sample[random_sample['classification'] == 'Legal Expert'].sample(n=1, random_state=42),
    random_sample[random_sample['classification'] == 'Tax Expert'].sample(n=1, random_state=42)
])

stratified_sample.head()

# %% [markdown]
# Note: XXX just means that country could not be identified from the documents that ICIJ had in their possession
#
# Administrator: Bourque Mary Ellen M.. Through Primex, a liability-limiting organisation for companies specialising within some sort of chemistry. Under this one of the service providers they note is Bourque Mary Ellen M. associated with `The Corporate Secretary Limited` listed as the primary contact perosn. Firm based in Barbados.
# (Likewise, we can confirm this from a filing found from the SEC with incorporation documents as the LLM has done)
# Note: LLM confuses it a bit. Thinks she's directly associated with Primex Ltd.
# Don't have infomration on where she's based (though the llm has found it's Barbados - but not in ICIJ which is the source we use for htis information)
# Incorporating in Barbados, and this seems to be her primary responsibility to help from offshore to do this)
# Entirely concentrated in Barbados, and the one incorproation she has is also here.
#
#
# Investment Advisor: Platinum Management Services Limited.
# Hong-kong based Insureance Broker Company, providing financial advice.
# 13 entities connected to it. 
# Mostly clients from British Virgin Islands, one from Hong Kong and 3 unknown ones 
# Incorporating mostyl in British Virgin Isalnd as wel, as well as Hong Kong. Notably, none of them have any particular legal technologies
#
#
# Legal Expert: Maitre Maya Obegi
# Dicey classification.... Because of the name with Maitre fro lawyers in french-speaking countries, consistent with client in Lebanon, but no concrete sources on it.
# Client in Lebanon
# Incorporating in British Virgin Islands
# Autocratic country, and we see there's some bearer instruments connected to hwat she did there.
# (Funny enough ICIJ classifies country as United Kingdom as where she's based. Probably.)
#
# And the officers connected to that entity: One officer from Bahrain, that's a shareholder and that one bearer instrument
#
#
# Tax Expert: Martin & Davidoff
# Tax attorney and general CPA firm.
# Clients exclusively from swtizerland. 
# Incorporating in Bahamas, British virgin Islands, Niue and Panama -> high jursidiction entropy of 0.86
# A lot of bearer instruments... 10 of the 29
