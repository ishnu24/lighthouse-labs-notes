SELECT artists.name FROM artists LEFT OUTER JOIN albums ON artists.artistid=albums.artistid WHERE albumid IS NULL 
