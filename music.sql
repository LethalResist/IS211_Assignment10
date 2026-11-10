CREATE TABLE artist (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE album (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    artist_id INTEGER NOT NULL,
    FOREIGN KEY (artist_id) REFERENCES artist (id)
);

CREATE TABLE song (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    album_id INTEGER NOT NULL,
    track_number INTEGER NOT NULL,
    length_seconds INTEGER NOT NULL,
    FOREIGN KEY (album_id) REFERENCES album (id),
    UNIQUE (album_id, track_number)
);
