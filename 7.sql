CREATE TABLE kontaktlar(
    id INTEGER PRIMARY KEY,
    ism TEXT,
    telefon TEXT
);

INSERT INTO kontaktlar( ism, telefon)
VALUES
    ('Ali','+998901112233'),
    ('Vali ',  ' +998935554433' )
    ('Sardor', '+998977778899 ');

UPDATE kontaktlar SET telefon = '+998900000000' WHERE ism = ' Vali';

DELETE FROM kontaktlar WHERE ism = 'Sardor';
SELECT * FROM kontaktlar;
