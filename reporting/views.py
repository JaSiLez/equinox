import json

import pandas as pd
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from django.http import Http404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.urls import reverse_lazy

from model_server.models import ReportingModeDescription, ReportingModeMatch, \
    ReportingModeName, ModelModes, ModelModesShort
from portfolio.ProjectEvent import ProjectEvent
from portfolio.Asset import ProjectAsset
from portfolio.Contractor import Contractor
from portfolio.EmissionsSource import GPCEmissionsSource, BuildingEmissionsSource
from portfolio.EmissionsSource import GPPEmissionsSource
from portfolio.PortfolioManager import PortfolioManager
from portfolio.Portfolios import ProjectPortfolio
from portfolio.Project import Project
from portfolio.ProjectActivity import ProjectActivity
from portfolio.models import MultiAreaSource
from reference.NUTS3Data import NUTS3PointData
from reporting.forms import CustomPortfolioAggregatesForm, portfolio_attributes, aggregation_choices
from reporting.models import Calculation, Visualization

"""

## other

*  Project Asset
*  Building
*  Point Source
*  Area Source
*  Multi Area Source
*  Portfolio Snapshot
*  Portfolio Data
*  Limit Structure
*  Emissions Source
*  GPC Emissions Source
*  Building Emissions Source
*  Borrower
*  Loan
*  Mortgage
*  Operator
*  Project Category
*  Project Company
*  Revenue
*  Primary Effect
*  Secondary Effect
*  Sponsor
*  Stakeholder
*  Swap

"""


@login_required(login_url='/login/')
def portfolio_overview(request):
    t = loader.get_template('portfolio_overview.html')
    context = RequestContext(request, {})

    """
    Compile a global portfolio overview of all data sets available the database

    ## Focus of this view is on procurement data
    
    *  Portfolio Manager
    *  Project Portfolio
    *  GPP Emissions Source
    *  Contractor
    *  Project Activity
    *  Project

    """

    pm_count = PortfolioManager.objects.count()
    po_count = ProjectPortfolio.objects.count()
    pr_count = Project.objects.count()
    pe_count = ProjectEvent.objects.count()
    pa_count = ProjectActivity.objects.count()
    co_count = Contractor.objects.count()
    gpp_count = GPPEmissionsSource.objects.count()
    as_count = ProjectAsset.objects.count()
    geo_count = MultiAreaSource.objects.count()

    context.update({'pm_count': pm_count,
                    'po_count': po_count,
                    'gpp_count': gpp_count,
                    'pe_count': pe_count,
                    'co_count': co_count,
                    'as_count': as_count,
                    'pa_count': pa_count,
                    'geo_count': geo_count,
                    'pr_count': pr_count})

    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def portfolio_summary(request, pk):
    """
    TODO

    Display an individual :model:`portfolio.Portfolio`.
    Fetch additional data associated with the portfolio
    Invoke function to Compute Portfolio statistics
    - Total number of rows
    - Total exposure
    - Average rating etc.

    **Context**

    ``Portfolio``
        An instance of :model:`portfolio.Portfolio`.

    **Template:**

    :template:`portfolio_explorer/portfolio_summary.html`
    """

    portfolio_queryset = None
    try:
        p = ProjectPortfolio.objects.get(pk=pk)
    except ProjectPortfolio.DoesNotExist:
        raise Http404("Portfolio does not exist")

    try:
        project_queryset = ProjectPortfolio.objects.filter(portfolio_id=pk)
    except ProjectPortfolio.DoesNotExist:
        raise Http404("PortfolioData does not exist")

    # Insert into dataframe for statistics
    portfolio_dataframe = pd.DataFrame.from_records(portfolio_queryset.values())

    # Aggregates
    obligor_count = portfolio_dataframe.shape[0]
    total_exposure = portfolio_dataframe['EAD'].sum()

    # TODO Round digits
    pstats = portfolio_dataframe[['EAD', 'LGD', 'Tenor', 'Sector', 'Rating', 'Country', 'Stage']].describe().to_html()

    t = loader.get_template('portfolio_summary.html')
    context = RequestContext(request, {})
    context.update({'portfolio': p, 'pstats': pstats})
    context.update({'obligor_count': obligor_count, 'total_exposure': total_exposure})
    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def portfolio_aggregates(request):
    """
    TODO

    Create a custom aggregation report on the basis of form input fields
    Aggregation Function to Apply
    Field to Aggregate

    :param request:
    :return:
    """
    success_url = reverse_lazy('portfolio_list')

    result_data = {}
    result_label = {}

    if request.method == 'POST':

        form = CustomPortfolioAggregatesForm(request.POST)
        form.is_valid()
        Attribute = portfolio_attributes[int(form.cleaned_data['attribute'])][1]
        Aggregator_Function = aggregation_choices[int(form.cleaned_data['aggregator_function'])][1]
        print('GLOBALS: ', globals())

        # convert the aggregator function string to a class object
        Method = globals()[Aggregator_Function]
        # result_data = Portfolio.objects.aggregate(Avg('portfoliodata__EAD'))
        #
        aggregation_string = 'portfoliodata__' + Attribute
        result_data = ProjectPortfolio.objects.annotate(aggregated=Method(aggregation_string))
        result_label = Aggregator_Function + ' ' + Attribute

    else:
        form = CustomPortfolioAggregatesForm()


@login_required(login_url='/login/')
def portfolio_stats_view(request, pk):
    """
    TODO

    Generate aggregate statistics about the portfolio.
    """

    try:
        p = ProjectPortfolio.objects.get(pk=pk)
    except ProjectPortfolio.DoesNotExist:
        raise Http404("Portfolio does not exist")

    try:
        portfolio_queryset = ProjectPortfolio.objects.filter(portfolio_id=pk)
    except ProjectPortfolio.DoesNotExist:
        raise Http404("PortfolioData does not exist")

    portfolio_dataframe = pd.DataFrame.from_records(portfolio_queryset.values())

    # TODO Improve headers
    stats_view = {}
    for attr in ['Tenor', 'LGD', 'Rating', 'Stage', 'Country', 'Sector']:
        # Group Count by attribute
        pstats = portfolio_dataframe.groupby([attr], as_index=True).size().reset_index(name='Count')
        N = pstats['Count'].sum()
        # Calculate Percentage
        pstats['%'] = pstats['Count'] / N
        pstats.set_index(attr)
        stats_view[attr] = pstats.to_html(index=False)

    t = loader.get_template('portfolio_stats_view.html')
    context = RequestContext(request, {})
    context.update({'portfolio': p, 'stats_view': stats_view, 'portfolio_data': portfolio_queryset})
    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def pcaf_mortgage_report(request):
    t = loader.get_template('pcaf_mortgage_report.html')
    context = RequestContext(request, {})

    """ Construct a PCAF Mortgage Emissions report and a Portfolio Carbon Footprint
    
    Select Emissions Sources where the asset is Residential Building
    asset.asset_class = 0
    
    Aggregate total emission per asset (sum of emissions sources, weighted average DQ score)
    
    
    Select Loans that are 
    - Residential Mortgages (asset_class == 0)
    - with total_balance > 0

    """

    for be in BuildingEmissionsSource.objects.all():
        print(80 * '=')
        print(be.asset.loan_identifier.counterparty_identifier)
        print(be.asset.loan_identifier)
        print(be.asset.loan_identifier.legal_balance)
        print(be.asset.initial_valuation_amount)
        print(be.asset.building_area_m2)
        print(be.emissions_factor.Emission_factor)

    table_header = []
    table_header.append('Borrower')
    table_header.append('Loan')
    table_header.append('Legal Balance')
    table_header.append('Building')
    table_header.append('Initial Valuation')
    table_header.append('Area')
    table_header.append('Emission Factor')
    table_header.append('Attribution Factor')
    table_header.append('Financed Emissions')

    table_rows = {}
    key = 0
    for be in BuildingEmissionsSource.objects.all():
        value = []
        value.append(be.asset.loan_identifier.counterparty_identifier)
        value.append(be.asset.loan_identifier)
        value.append(be.asset.loan_identifier.legal_balance)
        value.append(be.asset_id)
        value.append(be.asset.initial_valuation_amount)
        value.append(be.asset.building_area_m2)
        value.append(be.emissions_factor.Emission_factor)
        value.append(be.asset.loan_identifier.legal_balance / be.asset.initial_valuation_amount)
        value.append(be.asset.building_area_m2 * be.emissions_factor.Emission_factor)
        table_rows[key] = value
        key += 1
        print(key, value)

    context.update({'TableHeader': table_header})
    context.update({'TableRows': table_rows})
    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def ghg_reduction(request):
    t = loader.get_template('ghg_reduction.html')
    context = RequestContext(request, {})

    activities = ProjectActivity.objects.all()

    table_header = []
    table_header.append('Project')
    table_header.append('Project Activity')
    table_header.append('Activity Emissions')
    table_header.append('Baseline Emissions')
    table_header.append('GHG Reduction')

    table_rows = {}
    key = 0

    if len(activities) > 0:
        for pa in ProjectActivity.objects.all():
            value = []
            if pa.project:
                value.append(pa.project.project_identifier)
            else:
                value.append(None)
            value.append(pa.project_activity_identifier)
            value.append(pa.project_activity_emissions)
            value.append(pa.baseline_activity_emissions)
            if pa.baseline_activity_emissions and pa.project_activity_emissions:
                value.append(pa.baseline_activity_emissions - pa.project_activity_emissions)
            else:
                value.append(None)
            table_rows[key] = value
            key += 1
            # print(key, value)

    context.update({'TableHeader': table_header})
    context.update({'TableRows': table_rows})
    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def manager_nuts3_map(request):
    t = loader.get_template('portfolio_map.html')
    context = RequestContext(request, {})

    """
    Compile a global portfolio map of portfolio managing entities using their NUTS3 representative point geometries

    """

    portfolio_data = PortfolioManager.objects.all()
    nuts_data = []
    iter = 1
    for co in portfolio_data.iterator():
        nuts = co.region
        if iter < 100:
            try:
                nuts_data.append(NUTS3PointData.objects.get(nuts_id=nuts))
            except:
                pass
            iter += 1
        else:
            break
    geodata = json.loads(serialize("geojson", nuts_data))
    context.update({'geodata': geodata})

    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def contractor_nuts3_map(request):
    t = loader.get_template('portfolio_map.html')
    context = RequestContext(request, {})

    """
    Compile a global portfolio map of contractor entities using their NUTS3 representative point geometries

    """

    # geometry = json.loads(serialize("geojson", PointSource.objects.all()))
    # geometry = json.loads(serialize("geojson", AreaSource.objects.all()))
    # geodata = json.loads(serialize("geojson", NUTS3PointData.objects.all()))
    portfolio_data = Contractor.objects.all()
    nuts_data = []
    iter = 1
    for co in portfolio_data.iterator():
        nuts = co.region
        if iter < 100:
            try:
                nuts_data.append(NUTS3PointData.objects.get(nuts_id=nuts))
            except:
                pass
            iter += 1
        else:
            break
    geodata = json.loads(serialize("geojson", nuts_data))
    context.update({'geodata': geodata})

    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def gpp_report(request):
    t = loader.get_template('gpp_report.html')
    context = RequestContext(request, {})

    """

    """

    table_header = []
    table_header.append('Project Title')
    table_header.append('Budget (EUR)')
    table_header.append('CPV')
    table_header.append('CO2 (Tonnes)')

    table_rows = {}
    key = 0
    for source in GPPEmissionsSource.objects.all():
        pr = source.project
        value = []
        value.append(pr.project_title)
        value.append(pr.project_budget)
        value.append(pr.cpv_code)
        value.append(source.co2_amount)
        table_rows[key] = value
        key += 1

    context.update({'TableHeader': table_header})
    context.update({'TableRows': table_rows})
    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def gpc_report(request):
    t = loader.get_template('gpc_report.html')
    context = RequestContext(request, {})

    """
    1. GPC Reference Number in the format: I.X.X which identifies the GHG Emissions Sources at the level of granularity required by the GPC
    2. Applicable GHG Emission Scope (Numerical: 1, 2, 3). This is linked to the GPC Reference Number (Emissions) Sector/Subsector classifying GHG Emissions Sources according the GPC GHG Emissions Taxonomy (Stationary Energy, Transportation, etc)
    3. GHG Notation Keys (NO, IE, etc. providing context for the included or missing data)
    4. Mass of Greenhouse Gas Emissions per Gas Species (and total CO2e)
    CO2, CH4,  N2O,  HFC,  PFC,  SF6,  NF3, Total CO2e,  CO2(b)
    5. Data Quality assessment for both Activity Data and GHG Emission Factor (H, M, L Scale), AD,  EFD
    6. Explanatory comments (i.e. description of methods or notation keys used)
    
    """

    table_header = []
    table_header.append('GPC Ref No')
    table_header.append('Scope')
    table_header.append('Name')
    table_header.append('Notation Key')
    table_header.append('GHG Reduction')

    table_rows = {}
    key = 0
    for pa in GPCEmissionsSource.objects.all():
        value = []
        value.append(pa.gpc_subsector.gpc_ref_no)
        value.append(pa.gpc_subsector.gpc_scope)
        value.append(pa.gpc_subsector.name)
        value.append(pa.notation_key)
        value.append(pa.co2_amount)
        value.append(pa.ch4_amount)
        value.append(pa.n2o_amount)
        value.append(pa.hfc_amount)
        value.append(pa.pfc_amount)
        value.append(pa.sf6_amount)
        value.append(pa.nf3_amount)
        value.append(pa.tco2e_amount)
        value.append(pa.co2b_amount)
        value.append(pa.AD_DQ)
        value.append(pa.EF_DQ)
        value.append(pa.comments)
        table_rows[key] = value
        key += 1
        print(key, value)

    context.update({'TableHeader': table_header})
    context.update({'TableRows': table_rows})
    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def result_types(request):
    t = loader.get_template('result_types.html')
    context = RequestContext(request, {})

    # create a table with model result mode information
    # header row
    table_header = []
    table_header.append('Result Type ID')
    table_header.append('Name')
    for key, entry in ModelModesShort.items():
        table_header.append(entry)
    table_header.append('Description')

    table_rows = {}
    for key, entry in ReportingModeName.items():
        value = []
        value.append(key)
        value.append(ReportingModeName[key])
        matched_modes = ReportingModeMatch[key]
        for i in range(len(matched_modes)):
            if matched_modes[i] == 0:
                value.append('N')
            elif matched_modes[i] == 1:
                value.append('Y')
            else:
                print('ERROR in MODE')
        value.append(ReportingModeDescription[key])
        table_rows[key] = value

    context.update({'ModelModes': ModelModes})
    context.update({'TableRows': table_rows})
    context.update({'TableHeader': table_header})
    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def results_view(request, pk):
    try:
        R = Calculation.objects.get(pk=pk)
    except Calculation.DoesNotExist:
        raise Http404("Calculation does not exist")

    t = loader.get_template('result_view.html')
    context = RequestContext(request, {})
    context.update({'Result': json.dumps(R.results_data)})
    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def visualization_view(request, pk):
    """
    Interactive modification / calculation of Visualizations using Ajax calls

    **Context**

    ``Visualization``
        An instance of :model:`reporting.Visualization`.

    **Template:**

    :template:`reporting/Visualization_interactive.html`
    """

    # get the Visualization object
    visualization = Visualization.objects.get(pk=pk)
    t = loader.get_template('visualization.html')
    context = RequestContext(request, {})
    context.update({'object': visualization})
    return HttpResponse(t.template.render(context))
