import calendar
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button, RangeSlider, SelectInput, PlotlyView
from django.http import JsonResponse
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, extract, or_
import pprint as pp
import datetime
import plotly.graph_objs as go


contOptions = None


def units(argument):

    switcher = {'ug/l': .001,
                'ppb': .001}
    return switcher.get(argument, 1)


def mcl(argument):

    mcl = {'Arsenic': 0.010,
           'Nitrate': 45,
           'Total Nitrate/Nitrite (as N)': 10,
           'Chromium': 0.050,
           'Uranium': 0.030,
           'Selenium': 0.050,
           'Fluoride': 2,
           'Total dissolved solids': 500,
           'Manganese': 0.05,
           'Iron': 0.3,
           'Lead': 0.015}

    return mcl.get(argument, 1)


def connect_to_db():
    Base = automap_base()

    # engine, suppose it has two tables 'user' and 'address' set up
    engine = create_engine(
        'postgresql://tethys_super:zpwt49x3@tethys.byu.edu:5435/waterHackWeek')
    # reflect the tables
    Base.prepare(engine, reflect=True)

    # mapped classes are now created with names by default
    # matching that of the table name.
    Result = Base.classes.results
    Station = Base.classes.stations

    session = Session(engine)

    return [Result, Station, session]


def getContaminantOptions():
    dbConnection = connect_to_db()
    session = dbConnection[2]
    Result = dbConnection[0]

    records = session.query(Result).distinct(Result.characteristicname).all()

    dataRecords = []

    for record_result in records:
        dataRecords.append((record_result.characteristicname,
                            record_result.characteristicname))

    return dataRecords


def getValues(siteID, variables):
    dbConnection = connect_to_db()
    session = dbConnection[2]
    Result = dbConnection[0]

    records = session.query(Result).filter(
        Result.monitoringlocationidentifier == siteID).filter(or_(*[Result.characteristicname.like(name) for name in variables])
                                                              ).filter(
        Result.resultmeasuremeasureunitcode != 'MPN/100ml').filter(
        Result.resultmeasuremeasureunitcode != 'mg/l as N').filter(
        Result.resultmeasurevalue != 'ND').filter(
        Result.resultmeasurevalue != None).all()
    dataRecords = {}

    for record_result in records:

        variable = record_result.characteristicname

        if variable in dataRecords:
            dataRecords[variable].append({
                'date_val': record_result.activitystartdate,
                'value': float(record_result.resultmeasurevalue) * units(record_result.resultmeasuremeasureunitcode) / mcl(record_result.characteristicname)
            })
        else:
            dataRecords[variable] = [{
                'date_val': record_result.activitystartdate,
                'value': float(record_result.resultmeasurevalue) * units(record_result.resultmeasuremeasureunitcode) / mcl(record_result.characteristicname)
            }]

    return dataRecords


@login_required()
def details(request):

    siteid = request.GET.get('siteid')
    variables = request.GET.get('variables').split(',')

    vals = getValues(siteid, variables)

    series_collection = []

    for key, variable in vals.items():
        series_collection.append(go.Scatter(
            mode="markers",
            name=key,
            x=[o['date_val'] for o in variable],
            y=[o['value'] for o in variable]
        ))

    layout = go.Layout(
        title="Chemical Data<br><sub>{0} : {1}</sub>".format(
            siteid, request.GET.get('variables')),
        xaxis=dict(
            title='Date',
        ),
        yaxis=dict(
            title='Normalized Concentration to MCL'
        )
    )

    chart_obj = PlotlyView(
        go.Figure(data=series_collection,
                  layout=layout)
    )

    context = {
        'gizmo_object': chart_obj,
    }

    return render(request, 'gw_contaminants/gizmo_ajax.html', context)

    # context = {
    #     'vals': vals,
    # }

    # return JsonResponse(context)


@login_required()
def home(request):
    global contOptions
    if not contOptions:
        contOptions = getContaminantOptions()

    cont_selector = SelectInput(display_text='Select Contaminants',
                                name='cont_selector',
                                multiple=True,
                                options=contOptions,
                                initial=[])

    search_button = Button(
        display_text='Search',
        name='search-button',
        icon='glyphicon glyphicon-search',
        style='primary',
        attributes={"onclick": "perform_search();"}
    )

    context = {
        'cont_selector': cont_selector,
        'search_button': search_button
    }

    return render(request, 'gw_contaminants/home.html', context)


def get_points(request):

    dbConnection = connect_to_db()
    session = dbConnection[2]
    Result = dbConnection[0]
    Station = dbConnection[1]
    year = int(request.GET.get('year'))
    variables = request.GET.get('variables').split(',')

    recordResults = []

    for var_name in variables:
        records = session.query(Result, Station).distinct(Result.monitoringlocationidentifier).filter(
            extract('year', Result.activitystartdate) == year).filter(Result.monitoringlocationidentifier == Station.monitoringlocationidentifier
                                                                      ).filter(Result.characteristicname == var_name
                                                                               ).filter(Result.resultmeasuremeasureunitcode != 'MPN/100ml').filter(
            Result.resultmeasurevalue != 'ND').filter(
            Result.resultmeasurevalue != None).all()

        dataRecords = {}

        for (record_result, station_result) in records:
            dataRecords[record_result.monitoringlocationidentifier] = {
                'stationID': record_result.monitoringlocationidentifier,
                'name': station_result.monitoringlocationname,
                'lat': station_result.latitudemeasure,
                'long': float(station_result.longitudemeasure)
            }

        recordResults.append(dataRecords)

    combinedKeys = recordResults[0].keys()

    for returncordResult in recordResults:
        combinedKeys = combinedKeys & returncordResult.keys()

    finalResults = []

    for site in recordResults[0]:
        current_site = recordResults[0][site]
        if current_site['stationID'] in combinedKeys:
            finalResults.append(current_site)

    context = {
        'success': True,
        'result': finalResults}

    return JsonResponse(context)
