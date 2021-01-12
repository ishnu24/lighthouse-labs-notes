SELECT playlists.name 
  FROM playlists JOIN playlist_track 
    ON playlists.playlistid= playlist_track.playlistid 
   JOIN tracks ON playlist_track.trackid=tracks.trackid
  WHERE genreid != (SELECT genreid FROM genres WHERE name ='Latin')
