"""

Created Wed Jun 10 12:48:51 CEST 2020

dataflow = {
    "CATEGORY_LIST": {
        "OXFORD": 1
    },
    "NAME": name,
    "IDENTIFIER": key,
    "SHORT_DESC": key + " Policy Data",
    "LONG_DESC": "Policy Data for " + dataflow_dict[key] + " and its regions.",
    "ID": index,
    "SELECTORS": {
        "key": "all"
    },
    "TRACKED": True,
    "UPDATE": "W",
    "GEO": 1
}

dataflow['OXFORD_N'] = oxford_count
dataflow['DASHBOARD_N'] = dashboard_count\

"""

import json
import pickle
from django.core.management.base import BaseCommand

import policy.settings as settings
from policy.settings import dataflows_file, country_dict


class Command(BaseCommand):
    help = 'Create policy dataflow catalog'
    Debug = True

    datapath = settings.DATA_PATH

    dataflow_dict = pickle.load(open(datapath + '/dataflow_dict' + '.pkl', 'rb'))
    print(dataflow_dict)

    dataflow_list = []
    index = 0

    dataflow_list_file = dataflows_file

    dataseries_list_file = settings.dataseries_file
    series_list = json.load(open("./policy/policy_data/dataseries.latest.json"))

    dataseries_updated_file =  settings.dataseries_update_file
    updated_list = json.load(open("./policy/policy_data/dataseries.update.json"))

    for key in dataflow_dict:
        print(key, dataflow_dict[key])
        index += 1
        # TODO mobility data and policy data not the same country dict
        name = dataflow_dict[key]
        name = name.replace(" ", "_")
        name = name.replace("'", "")
        name = name.replace(",", "")
        name = name.replace(".", "_")
        name = name.replace("-", "_")
        name = name.replace("__", "_")

        dataflow = {
            "CATEGORY_LIST": {
                "OXFORD": 1
            },
            "NAME": name,
            "IDENTIFIER": key,
            "SHORT_DESC": key + " Policy Data",
            "LONG_DESC": "Policy Data for " + dataflow_dict[key] + " and its regions.",
            "ID": index,
            "SELECTORS": {
                "key": "all"
            },
            "TRACKED": True,
            "UPDATE": "W",
            "GEO": 1
        }

        # Calculate available timeseries
        oxford_count = 0
        for series in series_list:
            if series['DF_NAME'] == key:
                oxford_count += 1
        dataflow['OXFORD_N'] = oxford_count

        # Calculate valid (full data) timeseries
        dashboard_count = 0
        for series in updated_list:
            if series['DF_NAME'] == key and series['Status'] == "Valid":
                dashboard_count += 1
        dataflow['DASHBOARD_N'] = dashboard_count

        # Calculate number of regions and subregions (if any)
        regions_n = 0
        subregions_n = 0

        dataflow['REGIONS_N'] = regions_n
        dataflow['SUBREGIONS_N'] = subregions_n

        dataflow_list.append(dataflow)
        if Debug:
            print(key, regions_n, subregions_n)

    # store an updated list of dataseries dicts
    json.dump(dataflow_list, open(dataflow_list_file, 'w'), sort_keys=True, indent=4,
              separators=(',', ': '))

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully created policy dataflow catalog'))