# Import the dependencies.
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    
    return (
        f"Welcome to Hawaii!<br>/"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start"
        f"/api/v1.0/start/end"
    )

@app.route("/api/v1.0/preciptation")
def precipitation():
    
    #Query precipitation scores for 12 month period
    results = session.query(Measurement.date, Measurement.prcp).\
     filter(Measurement.date >= '2016-08-23').filter(Measurement.date <= '2017-08-23').all()

    session.close()

    precipitation_data = []
    for date in results: 
        precip_dict = {}
        precip_dict["date"]= prcp
        precipitation_data.append(precip_dict)

    return jsonify(precipitation_data)

@app.route("/api/v1.0/stations")
def stations():

    #Query stations
    results = session.query(Station.name).all()

    session.close()

    # Convert list of tuples into normal list
    station_names = list(np.ravel(results))

    return jsonify(station_names)

@app.route("/api/v1.0/tobs")
def tobs():

    #Query the temperatures for the most active station identified through prior analysis (USC00519281) over the past year
    results = session.query(Measurement.tobs).\
    filter(Measurement.date >= '2016-08-23').filter(Measurement.date <= '2017-08-23').filter(Measurement.station == "USC00519281").all()

    session.close()

    temp_data = []
    for date in results: 
        temp_dict = {}
        temp_dict["date"]= tobs
        temp_data.append(temp_dict)

    return jsonify(temp_data)

@app.route("/api/v1.0/<start>")
def start(date):

    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= date).all()
    
    session.close()

    return jsonify(results)

@app.route("/api/v1.0/<start>/<end>")
def start_end(startdate, enddate):
    
 
     results = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)).filter(Measurement.date >= startdate).filter(Measurement.date <= enddate).all()
     
    session.close()

    return jsonify(results)
    