# Copyright (c) 2021 Open Risk (https://www.openriskmanagement.com)
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


from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.timezone import now

from risk_analysis.Workflows import Workflow
from risk_analysis.Objectives import Playbook


class ResultGroup(models.Model):
    """
    Data object holds a group of calculation results
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    creation_date = models.DateTimeField(auto_now_add=True)
    group_type = models.IntegerField(default=0)

    # The number of results include in the group
    # Must be manually augmented whenever there is a result added or deleted
    # mirrors self.runs in Contoller/Results.py
    calculation_count = models.IntegerField(default=0)

    # the playbook that created this result group (if available)
    # ATTN result groups can also be formed in ad-hoc ways (e.g. user defined collections)
    # in that case there is no playbook associated and thus standardardized reports
    # and visualization are not available

    playbook = models.ForeignKey(Playbook, on_delete=models.CASCADE, null=True, blank=True,
                               help_text="Playbook that created this ResultGroup (if any)")


    # TODO Does not make strict sense for a collection
    calculation_timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('admin:results_explorer_result_group_change', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Result Group"
        verbose_name_plural = "Result Groups"


class Calculation(models.Model):
    """
    Data object holds the complete outcome of a workflow calculation as returned by model server

    Includes reference to user initiating calculation and the submitted workflow
    Logfile holds a logstring
    Results is json object with flexible structure. Typical
        'Graph'     : json object (different types)
        'Statistics': json object (tabular)
    """

    result_group = models.ForeignKey(ResultGroup, on_delete=models.CASCADE, null=True, blank=True,
                               help_text="Result Group to which this Calculation belong (if any)")

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    # The Base Workflow object that was used for the calculation
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE, default=1)

    # The final workflow_data used for the calculation
    # In principle starting with the base workflow, performing all the FK embeddings
    # and applying the workflow delta should reproduce the workflow data stored here
    workflow_data = models.JSONField(null=True, blank=True, help_text="Verbatim storage of the calculation input "
                                                              "in JSON format")

    # The result object creation time (may differ from the server execution time)
    creation_date = models.DateTimeField(auto_now_add=True)

    logfile = models.TextField(null=True, blank=True, help_text="Verbatim storage of the calculation logfile")
    results_data = models.JSONField(null=True, blank=True, help_text="Verbatim storage of the calculation results "
                                                              "in JSON format")
    calculation_timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('admin:results_explorer_calculation_change', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Result"
        verbose_name_plural = "Results"


class Visualization(models.Model):
    """
    Data object holds the structural Vega / Vega-Lite specification of a visualization

    Includes reference to user creating the Visualization
    """

    VISUALIZATION_DATA_CHOICES = [(0, 'Load portfolio data from local JSON files'),
                                  (1, 'Fetch portfolio data via REST API'),
                                  (2, 'Create new portfolio from local JSON configuration'),
                                  (3, 'Fetch portfolio configuration via REST API'),
                                  (4, 'Attached portfolio data in JSON format')]

    OBJECTIVE_CHOICE = [(0, 'Portfolio Information'), (1, 'Concentration Risk'), (2, 'Origination'),
                        (3, 'Risk Appetite'), (4, 'Risk Capital'), (5, 'Other')]

    name = models.CharField(max_length=200, help_text="Assigned name to help manage Visualization collections")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1, help_text="The creator of the Visualization")
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    objective = models.IntegerField(default=0, null=True, blank=True, choices=OBJECTIVE_CHOICE,
                                    help_text="Objective fulfilled by the Visualization")

    description = models.TextField(null=True, blank=True, help_text="A description of the main purpose and "
                                                                    "characteristics of the Visualization")

    visualization_data_mode = models.IntegerField(default=1, null=True, blank=True, choices=VISUALIZATION_DATA_CHOICES,
                                                  help_text="Select the mode for portfolio data inputs")

    visualization_data = models.JSONField(null=True, blank=True, help_text="Container for visualization data")
    visualization_data_url = models.URLField(null=True, blank=True, help_text="URL for visualization data")
    results_url = models.CharField(max_length=200, null=True, blank=True, help_text="Where to store the results")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('results_explorer:Visualization_view', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Visualization"
        verbose_name_plural = "Visualizations"
