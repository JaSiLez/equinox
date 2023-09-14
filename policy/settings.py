# Copyright (c) 2020 - 2023 Open Risk (https://www.openriskmanagement.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os
from pathlib import Path

# Directories

EQUINOX_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = os.path.join(EQUINOX_DIR, 'policy/fixtures/policy_data/')
ROOT_DIR = DATA_PATH

# Output files:
dataseries_file = ROOT_DIR + "dataseries.latest.json"
dimensions_file = ROOT_DIR + "dimensions.latest.json"
dataseries_update_file = ROOT_DIR + "dataseries.update.json"
metadata_file = ROOT_DIR + 'wikidata_extract_19_05_2020.json'

DATA_FILE = 'Oxford_Policies_Report_Latest.csv'
# DATA_FILE = 'OxCGRT_latest.csv'

CSV_FILE_PATH = DATA_PATH + DATA_FILE

# Logfile
logfile_path = DATA_PATH + 'Logs/processing.log'

datatypes = {
    'country_region_code': str,
    'country_region': str,
    'sub_region_1': str,
    'sub_region_2': str,
    'retail_and_recreation_percent_change_from_baseline': float,
    'grocery_and_pharmacy_percent_change_from_baseline': float,
    'parks_percent_change_from_baseline': float,
    'transit_stations_percent_change_from_baseline': float,
    'workplaces_percent_change_from_baseline': float,
    'residential_percent_change_from_baseline': float
}

BACKUP_DIR = DATA_PATH + "Backups/"
LOG_DIR = DATA_PATH + "Logs/"
CURRENT_DIR = DATA_PATH + "CURRENT/"

# Input files:
dataflows_file = ROOT_DIR + "dataflows.latest.json"

# Log files
dataflow_update_log = "dataflow_update.log"
download_log = "dataseries_download.log"
parsing_log = "dataseries_parsing.log"
error_log = "error.log"

# Download mode parameters
# TODO If dataflows have changed, using Update mode throws directory error
# Select update mode
# Download_Mode = 'Update'
Download_Mode = 'Clean_Start'

# Select update type (D=Daily, A=All)
Download_Type = 'A'
# Download_Type = 'A'

CUTOFF_CHANGE_RED = 30  # 50% change day-on-day
CUTOFF_CHANGE_ORANGE = 20  # 25% change day-on-day
CUTOFF_CHANGE_YELLOW = 10  # 10% change day-on-day

# Statistics Strings
stat_strings = {
    'Max': 'Maximum',
    'Min': 'Minimum',
    'T': 'Latest',
    'Mean': 'Average'
}

# Activity names in sequence
activities = ['Retail and Recreation', 'Grocery and Pharmacy', 'Parks', 'Transit Stations', 'Workplaces',
              'Residential']

activities_short = ['RR', 'GP', 'PA', 'TS', 'WO', 'RE']

dataflows = ['AE', 'AF', 'AG', 'AO', 'AR', 'AT', 'AU', 'AW', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG',
             'BH', 'BJ', 'BO', 'BR', 'BS',
             'BW', 'BY', 'BZ', 'CA', 'CH', 'CI', 'CL', 'CM', 'CO',
             'CR', 'CV', 'CZ', 'DE', 'DK', 'DO', 'EC', 'EE', 'EG', 'ES',
             'FI', 'FJ', 'FR', 'GA',
             'GB', 'GE', 'GH', 'GR', 'GT', 'GW', 'HK', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL',
             'IN', 'IQ',
             'IT', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KR', 'KW', 'KZ', 'LA', 'LB',
             'LI', 'LK', 'LT', 'LU', 'LV', 'LY', 'MD',
             'MK', 'ML', 'MM', 'MN', 'MT', 'MU', 'MX',
             'MY', 'MZ', 'NA', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NZ', 'OM', 'PA',
             'PE', 'PG', 'PH',
             'PK', 'PL', 'PR', 'PT', 'PY', 'QA', 'RE', 'RO', 'RW', 'SA', 'SE', 'SG', 'SI', 'SK',
             'SN', 'SV', 'TG',
             'TH', 'TJ', 'TR', 'TT', 'TW', 'TZ', 'UG', 'US', 'UY', 'VE', 'VN',
             'YE', 'ZA', 'ZM', 'ZW']

country_dict = {'AE': 'United Arab Emirates', 'AF': 'Afghanistan', 'AG': 'Antigua and Barbuda', 'AO': 'Angola',
                'AR': 'Argentina', 'AT': 'Austria', 'AU': 'Australia', 'AW': 'Aruba', 'BA': 'Bosnia and Herzegovina',
                'BB': 'Barbados', 'BD': 'Bangladesh', 'BE': 'Belgium', 'BF': 'Burkina Faso', 'BG': 'Bulgaria',
                'BH': 'Bahrain', 'BJ': 'Benin', 'BO': 'Bolivia', 'BR': 'Brazil', 'BS': 'The Bahamas', 'BW': 'Botswana',
                'BY': 'Belarus', 'BZ': 'Belize', 'CA': 'Canada', 'CH': 'Switzerland', 'CI': "Côte d'Ivoire",
                'CL': 'Chile', 'CM': 'Cameroon', 'CO': 'Colombia', 'CR': 'Costa Rica', 'CV': 'Cape Verde',
                'CZ': 'Czechia', 'DE': 'Germany', 'DK': 'Denmark', 'DO': 'Dominican Republic', 'EC': 'Ecuador',
                'EE': 'Estonia', 'EG': 'Egypt', 'ES': 'Spain', 'FI': 'Finland', 'FJ': 'Fiji', 'FR': 'France',
                'GA': 'Gabon', 'GB': 'United Kingdom', 'GE': 'Georgia', 'GH': 'Ghana', 'GR': 'Greece',
                'GT': 'Guatemala', 'GW': 'Guinea-Bissau', 'HK': 'Hong Kong', 'HN': 'Honduras', 'HR': 'Croatia',
                'HT': 'Haiti', 'HU': 'Hungary', 'ID': 'Indonesia', 'IE': 'Ireland', 'IL': 'Israel', 'IN': 'India',
                'IQ': 'Iraq', 'IT': 'Italy', 'JM': 'Jamaica', 'JO': 'Jordan', 'JP': 'Japan', 'KE': 'Kenya',
                'KG': 'Kyrgyzstan', 'KH': 'Cambodia', 'KR': 'South Korea', 'KW': 'Kuwait', 'KZ': 'Kazakhstan',
                'LA': 'Laos', 'LB': 'Lebanon', 'LI': 'Liechtenstein', 'LK': 'Sri Lanka', 'LT': 'Lithuania',
                'LU': 'Luxembourg', 'LV': 'Latvia', 'LY': 'Libya', 'MD': 'Moldova', 'MK': 'North Macedonia',
                'ML': 'Mali', 'MM': 'Myanmar (Burma)', 'MN': 'Mongolia', 'MT': 'Malta', 'MU': 'Mauritius',
                'MX': 'Mexico', 'MY': 'Malaysia', 'MZ': 'Mozambique', 'NA': 'Namibia', 'NE': 'Niger', 'NG': 'Nigeria',
                'NI': 'Nicaragua', 'NL': 'Netherlands', 'NO': 'Norway', 'NP': 'Nepal', 'NZ': 'New Zealand',
                'OM': 'Oman', 'PA': 'Panama', 'PE': 'Peru', 'PG': 'Papua New Guinea', 'PH': 'Philippines',
                'PK': 'Pakistan', 'PL': 'Poland', 'PR': 'Puerto Rico', 'PT': 'Portugal', 'PY': 'Paraguay',
                'QA': 'Qatar', 'RE': 'Réunion', 'RO': 'Romania', 'RW': 'Rwanda', 'SA': 'Saudi Arabia', 'SE': 'Sweden',
                'SG': 'Singapore', 'SI': 'Slovenia', 'SK': 'Slovakia', 'SN': 'Senegal', 'SV': 'El Salvador',
                'TG': 'Togo', 'TH': 'Thailand', 'TJ': 'Tajikistan', 'TR': 'Turkey', 'TT': 'Trinidad and Tobago',
                'TW': 'Taiwan', 'TZ': 'Tanzania', 'UG': 'Uganda', 'US': 'United States', 'UY': 'Uruguay',
                'VE': 'Venezuela', 'VN': 'Vietnam', 'YE': 'Yemen', 'ZA': 'South Africa', 'ZM': 'Zambia',
                'ZW': 'Zimbabwe', 'RS': 'Serbia'}

# the 28 countries of EU (keeping UK in)
eu_geolocations = {
    "AT": "Austria",
    "BE": "Belgium",
    "BG": "Bulgaria",
    "CY": "Cyprus",
    "CZ": "Czech Republic",
    "DE": "Germany",
    "DK": "Denmark",
    "EE": "Estonia",
    "ES": "Spain",
    "FI": "Finland",
    "FR": "France",
    "GB": "United Kingdom",
    "GR": "Greece",
    "HR": "Croatia",
    "HU": "Hungary",
    "IE": "Ireland",
    "IT": "Italy",
    "LT": "Lithuania",
    "LU": "Luxembourg",
    "LV": "Latvia",
    "MT": "Malta",
    "NL": "Netherlands",
    "PL": "Poland",
    "PT": "Portugal",
    "RO": "Romania",
    "SE": "Sweden",
    "SI": "Slovenia",
    "SK": "Slovakia",
}

countryISOMapping = {
    "AFG": "AF",
    "ALA": "AX",
    "ALB": "AL",
    "DZA": "DZ",
    "ASM": "AS",
    "AND": "AD",
    "AGO": "AO",
    "AIA": "AI",
    "ATA": "AQ",
    "ATG": "AG",
    "ARG": "AR",
    "ARM": "AM",
    "ABW": "AW",
    "AUS": "AU",
    "AUT": "AT",
    "AZE": "AZ",
    "BHS": "BS",
    "BHR": "BH",
    "BGD": "BD",
    "BRB": "BB",
    "BLR": "BY",
    "BEL": "BE",
    "BLZ": "BZ",
    "BEN": "BJ",
    "BMU": "BM",
    "BTN": "BT",
    "BOL": "BO",
    "BIH": "BA",
    "BWA": "BW",
    "BVT": "BV",
    "BRA": "BR",
    "VGB": "VG",
    "IOT": "IO",
    "BRN": "BN",
    "BGR": "BG",
    "BFA": "BF",
    "BDI": "BI",
    "KHM": "KH",
    "CMR": "CM",
    "CAN": "CA",
    "CPV": "CV",
    "CYM": "KY",
    "CAF": "CF",
    "TCD": "TD",
    "CHL": "CL",
    "CHN": "CN",
    "HKG": "HK",
    "MAC": "MO",
    "CXR": "CX",
    "CCK": "CC",
    "COL": "CO",
    "COM": "KM",
    "COG": "CG",
    "COD": "CD",
    "COK": "CK",
    "CRI": "CR",
    "CIV": "CI",
    "HRV": "HR",
    "CUB": "CU",
    "CYP": "CY",
    "CZE": "CZ",
    "DNK": "DK",
    "DJI": "DJ",
    "DMA": "DM",
    "DOM": "DO",
    "ECU": "EC",
    "EGY": "EG",
    "SLV": "SV",
    "GNQ": "GQ",
    "ERI": "ER",
    "EST": "EE",
    "ETH": "ET",
    "FLK": "FK",
    "FRO": "FO",
    "FJI": "FJ",
    "FIN": "FI",
    "FRA": "FR",
    "GUF": "GF",
    "PYF": "PF",
    "ATF": "TF",
    "GAB": "GA",
    "GMB": "GM",
    "GEO": "GE",
    "DEU": "DE",
    "GHA": "GH",
    "GIB": "GI",
    "GRC": "GR",
    "GRL": "GL",
    "GRD": "GD",
    "GLP": "GP",
    "GUM": "GU",
    "GTM": "GT",
    "GGY": "GG",
    "GIN": "GN",
    "GNB": "GW",
    "GUY": "GY",
    "HTI": "HT",
    "HMD": "HM",
    "VAT": "VA",
    "HND": "HN",
    "HUN": "HU",
    "ISL": "IS",
    "IND": "IN",
    "IDN": "ID",
    "IRN": "IR",
    "IRQ": "IQ",
    "IRL": "IE",
    "IMN": "IM",
    "ISR": "IL",
    "ITA": "IT",
    "JAM": "JM",
    "JPN": "JP",
    "JEY": "JE",
    "JOR": "JO",
    "KAZ": "KZ",
    "KEN": "KE",
    "KIR": "KI",
    "PRK": "KP",
    "KOR": "KR",
    "KWT": "KW",
    "KGZ": "KG",
    "LAO": "LA",
    "LVA": "LV",
    "LBN": "LB",
    "LSO": "LS",
    "LBR": "LR",
    "LBY": "LY",
    "LIE": "LI",
    "LTU": "LT",
    "LUX": "LU",
    "MKD": "MK",
    "MDG": "MG",
    "MWI": "MW",
    "MYS": "MY",
    "MDV": "MV",
    "MLI": "ML",
    "MLT": "MT",
    "MHL": "MH",
    "MTQ": "MQ",
    "MRT": "MR",
    "MUS": "MU",
    "MYT": "YT",
    "MEX": "MX",
    "FSM": "FM",
    "MDA": "MD",
    "MCO": "MC",
    "MNG": "MN",
    "MNE": "ME",
    "MSR": "MS",
    "MAR": "MA",
    "MOZ": "MZ",
    "MMR": "MM",
    "NAM": "NA",
    "NRU": "NR",
    "NPL": "NP",
    "NLD": "NL",
    "ANT": "AN",
    "NCL": "NC",
    "NZL": "NZ",
    "NIC": "NI",
    "NER": "NE",
    "NGA": "NG",
    "NIU": "NU",
    "NFK": "NF",
    "MNP": "MP",
    "NOR": "NO",
    "OMN": "OM",
    "PAK": "PK",
    "PLW": "PW",
    "PSE": "PS",
    "PAN": "PA",
    "PNG": "PG",
    "PRY": "PY",
    "PER": "PE",
    "PHL": "PH",
    "PCN": "PN",
    "POL": "PL",
    "PRT": "PT",
    "PRI": "PR",
    "QAT": "QA",
    "REU": "RE",
    "ROU": "RO",
    "RUS": "RU",
    "RWA": "RW",
    "BLM": "BL",
    "SHN": "SH",
    "KNA": "KN",
    "LCA": "LC",
    "MAF": "MF",
    "SPM": "PM",
    "VCT": "VC",
    "WSM": "WS",
    "SMR": "SM",
    "STP": "ST",
    "SAU": "SA",
    "SEN": "SN",
    "SRB": "RS",
    "SYC": "SC",
    "SLE": "SL",
    "SGP": "SG",
    "SVK": "SK",
    "SVN": "SI",
    "SLB": "SB",
    "SOM": "SO",
    "ZAF": "ZA",
    "SGS": "GS",
    "SSD": "SS",
    "ESP": "ES",
    "LKA": "LK",
    "SDN": "SD",
    "SUR": "SR",
    "SJM": "SJ",
    "SWZ": "SZ",
    "SWE": "SE",
    "CHE": "CH",
    "SYR": "SY",
    "TWN": "TW",
    "TJK": "TJ",
    "TZA": "TZ",
    "THA": "TH",
    "TLS": "TL",
    "TGO": "TG",
    "TKL": "TK",
    "TON": "TO",
    "TTO": "TT",
    "TUN": "TN",
    "TUR": "TR",
    "TKM": "TM",
    "TCA": "TC",
    "TUV": "TV",
    "UGA": "UG",
    "UKR": "UA",
    "ARE": "AE",
    "GBR": "GB",
    "USA": "US",
    "UMI": "UM",
    "URY": "UY",
    "UZB": "UZ",
    "VUT": "VU",
    "VEN": "VE",
    "VNM": "VN",
    "VIR": "VI",
    "WLF": "WF",
    "ESH": "EH",
    "YEM": "YE",
    "ZMB": "ZM",
    "ZWE": "ZW",
    "XKX": "XK",
    "RKS": "XK"
}

"""
 head -1 policy/policy_data/Oxford_Policies_Report_Latest.csv

CountryName,CountryCode,RegionName,RegionCode,Jurisdiction,Date,C1_School closing,C1_Flag,C2_Workplace closing,C2_Flag,C3_Cancel public events,C3_Flag,C4_Restrictions on gatherings,C4_Flag,C5_Close public transport,C5_Flag,C6_Stay at home requirements,C6_Flag,C7_Restrictions on internal movement,C7_Flag,C8_International travel controls,E1_Income support,E1_Flag,E2_Debt/contract relief,E3_Fiscal measures,E4_International support,H1_Public information campaigns,H1_Flag,H2_Testing policy,H3_Contact tracing,H4_Emergency investment in healthcare,H5_Investment in vaccines,

H6_Facial Coverings,

H6_Flag,

H7_Vaccination policy,

H7_Flag,

M1_Wildcard,

ConfirmedCases,ConfirmedDeaths,StringencyIndex,StringencyIndexForDisplay,StringencyLegacyIndex,StringencyLegacyIndexForDisplay,GovernmentResponseIndex,GovernmentResponseIndexForDisplay,ContainmentHealthIndex,ContainmentHealthIndexForDisplay,EconomicSupportIndex,EconomicSupportIndexForDisplay


"""

# The field names as they are in the CSV header
field_names = ['C1_School closing',
               'C1_Flag',
               'C2_Workplace closing',
               'C2_Flag',
               'C3_Cancel public events',
               'C3_Flag',
               'C4_Restrictions on gatherings',
               'C4_Flag',
               'C5_Close public transport',
               'C5_Flag',
               'C6_Stay at home requirements',
               'C6_Flag',
               'C7_Restrictions on internal movement',
               'C7_Flag',
               'C8_International travel controls',
               'E1_Income support', 'E1_Flag',
               'E2_Debt/contract relief',
               'E3_Fiscal measures',
               'E4_International support',
               'H1_Public information campaigns',
               'H1_Flag',
               'H2_Testing policy',
               'H3_Contact tracing',
               'H4_Emergency investment in healthcare',
               'H5_Investment in vaccines',
               'H6_Facial Coverings',
               'H6_Flag',
               'H7_Vaccination policy',
               'H7_Flag',
               'M1_Wildcard',
               'ConfirmedCases',
               'ConfirmedDeaths',
               'StringencyIndex',
               'StringencyIndexForDisplay',
               'StringencyLegacyIndex',
               'StringencyLegacyIndexForDisplay',
               'GovernmentResponseIndex',
               'GovernmentResponseIndexForDisplay',
               'ContainmentHealthIndex',
               'ContainmentHealthIndexForDisplay',
               'EconomicSupportIndex',
               'EconomicSupportIndexForDisplay'
               ]

# Field codes as constructed / simplified from the CSV headers
field_codes = ['C1',
               'C1F',
               'C2',
               'C2F',
               'C3',
               'C3F',
               'C4',
               'C4F',
               'C5',
               'C5F',
               'C6',
               'C6F',
               'C7',
               'C7F',
               'C8',
               'E1',
               'E1F',
               'E2',
               'E3',
               'E4',
               'H1',
               'H1F',
               'H2',
               'H3',
               'H4',
               'H5',
               'H6',
               'H6F',
               'H7',
               'H7F',
               'M1',
               'AUX1',
               'AUX2',
               'I1',
               'I1D',
               'I2',
               'I2D',
               'I3',
               'I3D',
               'I4',
               'I4D',
               'I5',
               'I5D'
               ]

# field description (from CSV headers)
field_description = ['School closing',
                     'School closing Flag',
                     'Workplace closing',
                     'Workplace closing Flag',
                     'Cancel public events',
                     'Cancel public events Flag',
                     'Restrictions on gatherings',
                     'Restrictions on gatherings Flag',
                     'Close public transport',
                     'Close public transport Flag',
                     'Stay at home requirements',
                     'Stay at home requirements Flag',
                     'Restrictions on internal movement',
                     'Restrictions on internal movement Flag',
                     'International travel controls',
                     'Income support',
                     'Income support Flag',
                     'Debt/contract relief',
                     'Fiscal measures',
                     'International support',
                     'Public information campaigns',
                     'Public information campaigns_Flag',
                     'Testing policy',
                     'Contact tracing',
                     'Emergency investment in healthcare',
                     'Investment in vaccines',
                     'Facial Coverings',
                     'Facial Coverings Flag',
                     'Vaccination Policy',
                     'Vaccination Policy Flag',
                     'Wildcard',
                     'Confirmed Cases',
                     'Confirmed Deaths',
                     'Stringency Index',
                     'Stringency Index For Display',
                     'Stringency Legacy Index',
                     'Stringency Legacy Index For Display',
                     'Government Response Index',
                     'Government Response Index For Display',
                     'Containment Health Index',
                     'Containment Health Index For Display',
                     'Economic Support Index',
                     'Economic Support Index For Display'
                     ]

# from codebook
field_description_long = ['Record closings of schools and universities',
                          'School closing Flag',
                          'Record closings of workplaces',
                          'Workplace closing Flag',
                          'Record cancelling public events',
                          'Cancel public events Flag',
                          'Record limits on private gatherings',
                          'Restrictions on gatherings Flag',
                          'Record closing of public transport',
                          'Close public transport Flag',
                          'Record orders to "shelter-in-place" and otherwise confine to the home',
                          'Stay at home requirements Flag',
                          'Record restrictions on internal movement between cities/regions',
                          'Restrictions on internal movement Flag',
                          'Record restrictions on international travel (for foreign travellers, not citizens)',
                          'Record if the government is providing direct cash payments to people who lose their jobs or cannot work. Note: only includes payments to firms if explicitly linked to payroll/salaries',
                          'Income support Flag',
                          'Record if the government is freezing financial obligations for households (eg stopping loan repayments, preventing services like water from stopping, or banning evictions)',
                          'Announced economic stimulus spending. Note: only records amount additional to previously announced spending',
                          'Announced offers of Covid-19 related aid spending to other countries. Note: only record amount additional to previously announced spending',
                          'Record presence of public info campaigns',
                          'Public information campaigns Flag',
                          'Record government policy on who has access to testing. Note: this records policies about testing for current infection (PCR tests) not testing for immunity (antibody test)',
                          'Record government policy on contact tracing after a positive diagnosis. Note: we are looking for policies that would identify all people potentially exposed to Covid-19; voluntary bluetooth apps are unlikely to achieve this',
                          'Announced short term spending on healthcare system, eg hospitals, masks, etc. Note: only records amount additional to previously announced spending',
                          'Announced public spending on Covid-19 vaccine development. Note: only record amount additional to previously announced spending',
                          'Record policies on the use of facial coverings outside the home',
                          'Facial Coverings Flag',
                          'Record policies for vaccine delivery for different groups',
                          'Vaccine Policies Flag',
                          'Wildcard',
                          'Confirmed Cases',
                          'Confirmed Deaths',
                          'Stringency Index',
                          'Stringency Index For Display',
                          'Stringency Legacy Index',
                          'Stringency Legacy Index For Display',
                          'Government Response Index',
                          'Government Response Index For Display',
                          'Containment Health Index',
                          'Containment Health Index For Display',
                          'Economic Support Index',
                          'Economic Support Index For Display'
                          ]

# code list from codebook.md
field_code_list = {'C1': {'0': 'no measures',
                          '1': 'recommend closing',
                          '2': 'require closing (only some levels or categories, eg just high school, or just public schools)',
                          '3': 'require closing all levels'},
                   'C1F': {'0': 'no measures'},
                   'C2': {'0': 'no measures',
                          '1': 'recommend closing (or recommend work from home)',
                          '2': 'require closing (or work from home) for some sectors or categories of workers',
                          '3': 'require closing (or work from home) for all-but-essential workplaces (eg grocery stores, doctors)'},
                   'C2F': {'0': 'targeted', '1': 'general'},
                   'C3': {'0': 'no measures',
                          '1': 'recommend cancelling',
                          '2': 'require cancelling'},
                   'C3F': {'0': 'targeted', '1': 'general'},
                   'C4': {'0': 'no restrictions',
                          '1': 'restrictions on very large gatherings (the limit is above 1000 people)',
                          '2': 'restrictions on gatherings between 101-1000 people',
                          '3': 'restrictions on gatherings between 11-100 people',
                          '4': 'restrictions on gatherings of 10 people or less'},
                   'C4F': {'0': 'targeted', '1': 'general'},
                   'C5': {'0': 'no measures',
                          '1': 'recommend closing (or significantly reduce volume/route/means of transport available)',
                          '2': 'require closing (or prohibit most citizens from using it)'},
                   'C5F': {'0': 'targeted', '1': 'general'},
                   'C6': {'0': 'no measures',
                          '1': 'recommend not leaving house',
                          '2': 'require not leaving house with exceptions for daily exercise, grocery shopping, and essential trips',
                          '3': 'require not leaving house with minimal exceptions (eg allowed to leave once a week, or only one person can leave at a time, etc)'},
                   'C6F': {'0': 'targeted', '1': 'general'},
                   'C7': {'0': 'no measures',
                          '1': 'recommend not to travel between regions/cities',
                          '2': 'internal movement restrictions in place'},
                   'C7F': {'0': 'targeted', '1': 'general'},
                   'C8': {'0': 'no restrictions',
                          '1': 'screening arrivals',
                          '2': 'quarantine arrivals from some or all regions',
                          '3': 'ban arrivals from some regions',
                          '4': 'ban on all regions or total border closure'},
                   'E1': {'0': 'no income support',
                          '1': 'government is replacing less than 50% of lost salary (or if a flat sum, it is less than 50% median salary)',
                          '2': 'government is replacing 50% or more of lost salary (or if a flat sum, it is greater than 50% median salary)'},
                   'E1F': {'0': 'formal sector workers only', '1': 'transfers to informal sector workers too'},
                   'E2': {'0': 'no',
                          '1': 'Narrow relief, specific to one kind of contract',
                          '2': 'broad debt/contract relief'},
                   'E3': {'0': 'numerical variable (USD)'},
                   'E4': {'0': 'numerical variable (USD)'},
                   'H1': {'0': 'No COVID-19 public information campaign',
                          '1': 'public officials urging caution about COVID-19',
                          '2': 'coordinated public information campaign (e.g. across traditional and social media)'},
                   'H1F': {'0': 'targeted', '1': 'general'},
                   'H2': {'0': 'no testing policy',
                          '1': 'only those who both (a) have symptoms AND (b) meet specific criteria (eg key workers, admitted to hospital, came into contact with a known case, returned from overseas)',
                          '2': 'testing of anyone showing Covid-19 symptoms',
                          '3': 'open public testing (eg "drive through" testing available to asymptomatic people)'},
                   'H3': {'0': 'no contact tracing',
                          '1': 'limited contact tracing; not done for all cases',
                          '2': 'comprehensive contact tracing; done for all identified cases'},
                   'H4': {'0': 'numerical variable'},
                   'H5': {'0': 'numerical variable'},
                   'H6': {'0': 'No policy', '1': 'Recommended',
                          '2': 'Required in some specified shared/public spaces outside the home with other people present, or some situations when social distancing not possible',
                          '3': 'Required in all shared/public spaces outside the home with other people present or all situations when social distancing not possible',
                          '4': 'Required outside the home at all times regardless of location or presence of other people'},
                   'H6F': {'0': 'targeted', '1': 'general'},
                   'H7': {'0': 'No availability',
                          '1': 'Availability for ONE of following: key workers/ clinically vulnerable groups / elderly groups',
                          '2':
                              'Availability for TWO of following: key workers/ clinically vulnerable groups / elderly groups',
                          '3': 'Availability for ALL of following: key workers/ clinically vulnerable groups / elderly groups',
                          '4': 'Availability for all three plus partial additional availability (select broad groups/ages)',
                          '5': 'Universal availability'},
                   'H7F': {'0': 'At cost to individual (or funded by NGO, insurance, or partially government funded)',
                           '1': 'No or minimal cost to individual (government funded or subsidised)'},
                   'M1': {'0': 'numerical variable'},
                   'AUX1': {'0': 'numerical variable'},
                   'AUX2': {'0': 'numerical variable'},
                   'I1': {'0': 'numerical variable'},
                   'I1D': {'0': 'numerical variable'},
                   'I2': {'0': 'numerical variable'},
                   'I2D': {'0': 'numerical variable'},
                   'I3': {'0': 'numerical variable'},
                   'I3D': {'0': 'numerical variable'},
                   'I4': {'0': 'numerical variable'},
                   'I4D': {'0': 'numerical variable'},
                   'I5': {'0': 'numerical variable'},
                   'I5D': {'0': 'numerical variable'}
                   }

field_type = ['ordinal',
              'binary',
              'ordinal',
              'binary',
              'ordinal',
              'binary',
              'ordinal',
              'binary',
              'ordinal',
              'binary',
              'ordinal',
              'binary',
              'ordinal',
              'binary',
              'ordinal',
              'ordinal',
              'binary',
              'ordinal',
              'numerical',
              'numerical',
              'ordinal',
              'binary',
              'ordinal',
              'ordinal',
              'numerical',
              'numerical',
              'text',
              'ordinal',
              'ordinal',
              'ordinal',
              'ordinal',
              'numerical',
              'numerical',
              'numerical',
              'numerical',
              'numerical',
              'numerical',
              'numerical',
              'numerical',
              'numerical',
              'numerical',
              'numerical',
              'numerical'
              ]
