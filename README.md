# Plato-Movie-Matrix

Python Scripts for Loading to Database:
      - /theMatrix/theMatrix/dbLoader.py // Original parser from textfile input to Mongo
      - /theMatrix/theMatrix/formal.py // Manipulates and Aggregates relevant entries from main database and saves them as refined entries. Puts entries in format ready for display in django                                            web views templates.

Python Scripts for Additional Graph Gen:
      - /theMatrix/theMatrix/assignment3.py //For underprovision helps generate larger graphs for visualization that were difficult to perform using Google Chart API

Database Model Format:
      - /theMatrix/theMatrix/Plato/models.py // Defines format of database entries

Data bridge to HTML:
     - /theMatrix/theMatrix/Plato/views.py // defines URL templates and injects data into views      

View HTML and Javascript:
     - /theMatrix/theMatrix/Plato/templates/ *contents* //Frontend display and visualization code

Report:
    - /TheMatrix/IntroCMAssignment3DataAnalysis.pdf