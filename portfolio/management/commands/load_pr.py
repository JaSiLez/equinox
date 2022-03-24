# Copyright (c) 2021 - 2022 Open Risk (https://www.openriskmanagement.com)
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

import pandas as pd
from django.core.management.base import BaseCommand

from portfolio.Project import Project
from portfolio.ProjectCategory import ProjectCategory


class Command(BaseCommand):
    help = 'Imports project data'

    # Delete existing objects
    Project.objects.all().delete()

    # Import data from file
    data = pd.read_csv("pr.csv", header='infer', delimiter=',')

    """
    TITLE,REFERENCE_NUMBER,CPV_CODE,TYPE_CONTRACT,SHORT_DESCR,VAL_TOTAL,CURRENCY

    """
    indata = []
    serial = 10000

    pk1 = ProjectCategory.objects.get(name="SUPPLIES")
    pk2 = ProjectCategory.objects.get(name="WORKS")
    pk3 = ProjectCategory.objects.get(name="SERVICES")

    for index, entry in data.iterrows():

        if entry['TYPE_CONTRACT'] == 'SUPPLIES':
            fk = pk1
        elif entry['TYPE_CONTRACT'] == 'WORKS':
            fk = pk2
        elif entry['TYPE_CONTRACT'] == 'SERVICES':
            fk = pk3

        pr = Project(
            project_identifier=entry['REFERENCE_NUMBER'],
            project_title=entry['TITLE'],
            project_description=entry['SHORT_DESCR'],
            cpv_code=entry['CPV_CODE'],
            project_category=fk,
            project_budget=entry['VAL_TOTAL'],
            project_currency=entry['CURRENCY'])
        serial += 1

        indata.append(pr)

    Project.objects.bulk_create(indata)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully inserted data into db'))
