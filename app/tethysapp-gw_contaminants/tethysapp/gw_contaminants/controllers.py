import calendar
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button, RangeSlider, SelectInput
from django.http import JsonResponse
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, extract, or_
import pprint as pp
import datetime


contOptions = None


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

    records = session.query(Result, Station).distinct(Result.monitoringlocationidentifier).filter(
        extract('year', Result.activitystartdate) == year).filter(Result.monitoringlocationidentifier == Station.monitoringlocationidentifier
                                                                  ).filter(or_(*[Result.characteristicname.like(name) for name in variables])).all()

    dataRecords = []

    for (record_result, station_result) in records:
        dataRecords.append({
            'stationID': record_result.monitoringlocationidentifier,
            'name': station_result.monitoringlocationname,
            'lat': station_result.latitudemeasure,
            'long': float(station_result.longitudemeasure)
        })

    context = {
        'success': True,
        'result': dataRecords}

    return JsonResponse(context)
