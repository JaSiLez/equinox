from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from reference.nace_list import NACE_CHOICES
from reference.nuts3_list import NUTS3_CHOICES

"""
Current structure of simplified portfolio data structure
"
"portfolio_id": p, FK
"Obligor_ID": i,
"EAD": EAD,
"LGD": LGD,
"Rating": R,
"Stage": Stage,
"Tenor": T,
"Sector": Sector
"Country": Country
"""

portfolio_attributes = [(0, 'EAD'), (1, 'LGD'), (2, 'Rating'), (3, 'Stage'),
                        (4, 'Tenor'), (5, 'Sector'), (6, 'Country')]


class Portfolio(models.Model):
    """
    Portfolio object holds workflow oriented portfolio data
    The object is read/write
    Includes reference to user creating the data set
    Portfolio is named to facilitate recognition
    Actual Portfolio data stored in the PortfolioData model
    Notes is a user oriented field to allow storing human readable context about the portfolio

    Type is an integer field representing the type of the portfolio
    0 -> Performing Book (default)
    1 -> Non-performing Book


    """

    PORTFOLIO_TYPES = [(0, 'Performing'), (1, 'NPL')]
    GENERATION_TYPES = [(0, 'Actual'), (1, 'Synthetic'), (2, 'External')]

    name = models.CharField(max_length=200, help_text="An assigned name to help identify the portfolio")
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="The user that created the portfolio")
    notes = models.TextField(blank=True, null=True,
                             help_text="Description of the purpose or other relevant information about the portfolio")
    portfolio_type = models.IntegerField(default=0, choices=PORTFOLIO_TYPES, help_text='0=Performing Book, 1=NPL Book')

    generation = models.IntegerField(default=0, choices=GENERATION_TYPES,
                                     help_text='0=Actual, 1=Synthetic')

    # portfolio shape parameters

    max_rating = models.IntegerField(null=True, blank=True, help_text="Maximum rating")
    min_rating = models.IntegerField(null=True, blank=True, help_text="Minimum rating")
    mean_rating = models.IntegerField(null=True, blank=True, help_text="Average rating")

    max_lgd = models.IntegerField(null=True, blank=True, help_text="Maximum LGD")
    min_lgd = models.IntegerField(null=True, blank=True, help_text="Minimum LGD")
    mean_lgd = models.IntegerField(null=True, blank=True, help_text="Average LGD")

    max_ead = models.IntegerField(null=True, blank=True, help_text="Maximum EAD")
    min_ead = models.IntegerField(null=True, blank=True, help_text="Minimum EAD")
    mean_ead = models.IntegerField(null=True, blank=True, help_text="Average EAD")

    max_tenor = models.IntegerField(null=True, blank=True, help_text="Maximum Tenor")
    min_tenor = models.IntegerField(null=True, blank=True, help_text="Minimum Tenor")
    mean_tenor = models.IntegerField(null=True, blank=True, help_text="Average Tenor")

    country_no = models.IntegerField(null=True, blank=True, help_text="Number of Countries")
    sector_no = models.IntegerField(null=True, blank=True, help_text="Number of Sectors")

    # TODO disabled for now
    # Reindroduce JSONField to hold flexible portolio metadata
    # portfolio_data = JSONField()

    # bookkeeping
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('portfolio_explorer:portfolio_view', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolios"


class PortfolioData(models.Model):
    """
    PortfolioData object holds portfolio data in classic table format
    The object is read/write

    """
    # TODO incorporate portfolio type based constraint
    # NPL Assets have Rating=D, Stage=3

    portfolio_id = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

    Obligor_ID = models.CharField(max_length=200)
    EAD = models.FloatField(blank=True, null=True, help_text="Exposure at Default")
    LGD = models.IntegerField(blank=True, null=True, help_text="Loss Given Default Class")
    Tenor = models.IntegerField(blank=True, null=True, help_text="Tenor (integer years)")
    # The field encodes using an integer key a dictionary of business (industry) sectors
    Sector = models.IntegerField(blank=True, null=True, choices=NACE_CHOICES, help_text="Business Sector")
    # The field encodes using an integer key a dictionary of geographical locations
    # Eg. countries, NUTS regions etc.
    Country = models.IntegerField(blank=True, null=True, choices=NUTS3_CHOICES, help_text="NUTS3 Region of Operations")

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('portfolio_explorer:portfolio_data_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Portfolio Data"
        verbose_name_plural = "Portfolio Data"


class LimitStructure(models.Model):
    """
    LimitStructure object holds limitflow oriented limit data
    The object is read/write
    Includes reference to user creating the data set
    LimitStructure is named to facilitate recognition

    """

    name = models.CharField(max_length=200, help_text="An assigned name to help identify the limit structure")
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="The user that created the limit structure")
    notes = models.TextField(blank=True, null=True,
                             help_text="Description of the purpose or other relevant information about the limit structure")

    # limit structure parameters

    # max_rating = models.IntegerField(null=True, blank=True, help_text="Maximum rating")
    min_rating = models.IntegerField(null=True, blank=True, help_text="Minimum rating")

    # max_lgd = models.IntegerField(null=True, blank=True, help_text="Maximum LGD class")
    min_lgd = models.IntegerField(null=True, blank=True, help_text="Minimum LGD class")

    max_ead = models.FloatField(null=True, blank=True, help_text="Maximum EAD")
    # min_ead = models.FloatField(null=True, blank=True, help_text="Minimum EAD")

    max_tenor = models.IntegerField(null=True, blank=True, help_text="Maximum Tenor (Years)")
    # min_tenor = models.IntegerField(null=True, blank=True, help_text="Minimum Tenor")

    # bookkeeping
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('portfolio_explorer:limitstructure_view', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Limit Structure"
        verbose_name_plural = "Limit Structures"
