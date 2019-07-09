
import numpy as np
import datetime
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, request

#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
#session = Session(engine)

### Routes
#`/`
# * Home page.
# * List all routes that are available.

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/?start=YYYY-MM-DD (Example:/api/v1.0/?start=2012-02-28)<br/>"
        f"/api/v1.0/?start=YYYY-MM-DD&end=YYYY-MM-DD (Example:/api/v1.0/?start=2012-02-28&end=2012-03-05)"
    )

@app.route("/api/v1.0/precipitation")
def precip():
    session = Session(engine)
    """Return a list of precipitation data over time in Hawaii"""
    # Query all station precipitation 
    results = session.query(Measurement.station, Measurement.date, Measurement.prcp).all()

    # Create a dictionary from the row data and append to a list of all_precip
    all_precip = []
    for station, date, prcp in results:
        precip_dict = {}
        precip_dict["station"] = station
        precip_dict["date"] = date
        precip_dict["prcp"] = prcp
        all_precip.append(precip_dict)

    return jsonify(all_precip)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    """Return a list of stations from the measurement datasets"""
    # Query distinct stations
    results = session.query(Measurement.station).distinct().all()
    distinct_stations = list(np.ravel(results))

    return jsonify(distinct_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    """Return tobs data for last year of data in the measurement datasets"""
    # Query station tobs for date range
    #results = session.query(Measurement.station, Measurement.date, Measurement.tobs).all()
    results = session.execute("SELECT date, station, tobs FROM measurement\
               WHERE date >= datetime((Select max(date) from measurement), 'start of month', '-12 month') \
               AND date < datetime((Select max(date) from measurement), 'start of month','+1 month') \
               ORDER BY date DESC")
    # Create a dictionary from the row data and append to a list of all_precip
    all_tobs = []
    for station, date, tobs in results:
        tobs_dict = {}
        tobs_dict["station"] = station
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        all_tobs.append(tobs_dict)

    return jsonify(all_tobs)

@app.route("/api/v1.0/")
def start_dt():
    session = Session(engine)
    """Return min, max, avg tobs for dates greater than or equal to the start date"""
    # Query station tobs for date range
    if 'start' in request.args:
        try:
            start_date = str(request.args['start'])
            datetime.datetime.strptime(start_date, '%Y-%m-%d')
            results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
            filter(Measurement.date >= start_date).all()
        except ValueError:
            return "Incorrect data format (start date), should be YYYY-MM-DD"
        if 'end' in request.args:
            try: 
                end_date = str(request.args['end'])
                datetime.datetime.strptime(end_date, '%Y-%m-%d')
                results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
            except ValueError:
                return "Incorrect data format (end date), should be YYYY-MM-DD"
    else:
        return "Error: Arguments unknown"

    stats = list(np.ravel(results))
    return jsonify(stats)

   

if __name__ == '__main__':
    app.run(debug=True)

