# sqlalchemy-challenge.

Files were uploaded to the git repo in the url submitted.

Homework files are located in the SurfsUp directory. The Part 1 Climate Data analysis was completed in a jupyter notebook file entitled "climate_analysis_hw". The Part 2 Design Your Climate App was completed in a python file called "app_hw". 

Review of analyses:
1. SQLAlchemy was used to connect to the Hawaii.sqlite SQLite database. The automap_base function was used to reflect table into classes. References to the classes were saved. Python was linked to the database by creating a SQLAlchemy session; the session was closed at the end of the notebook.
2. Queries were completed for both the Precipitation and Station Analyses using pandas, datetime modules. Graphs were produced using matplotlib. Pictures of the visualizations are saved in the Visualizations directory within the SurfsUp directory.
3. Within the python file, the appropriate dependencies were imported. The database set up mirrored the script within the Jupyter notebook file, reflecting the existing database and tables. A Flask was set up using the Flask module. Flask routes for "/" (welcome), precipitation, stations, tobs and temperature were documented with appropriate queries, results, and jsonification of the output using the jsonify module. 

Unfortunately when using Anaconda Powershell to access the python script and open the url, I could not get this to work. However my code is all complete with the hope that if the connection could be established the API would work. 

Online resources such as github and stack overflow as well as a review of the module activities and class zoom were used to complete the assignment.