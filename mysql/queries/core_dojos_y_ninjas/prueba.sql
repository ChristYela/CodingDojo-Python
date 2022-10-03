CREATE TABLE dojo_a ( id INT PRIMARY KEY, nombre VARCHAR(255) );
CREATE TABLE dojo_b ( id INT PRIMARY KEY, nombre VARCHAR(255) );
CREATE TABLE dojo_c ( id INT PRIMARY KEY, nombre VARCHAR(255) );

DROP TABLE dojo_a;
DROP TABLE dojo_b;
DROP TABLE dojo_c;

CREATE TABLE dojo_a ( id INT PRIMARY KEY, nombre VARCHAR(255) );
CREATE TABLE dojo_b ( id INT PRIMARY KEY, nombre VARCHAR(255) );
CREATE TABLE dojo_c ( id INT PRIMARY KEY, nombre VARCHAR(255) );

INSERT INTO dojo_a VALUES ( 1, 'Hugo' );
INSERT INTO dojo_a VALUES ( 2, 'Paco' );
INSERT INTO dojo_a VALUES ( 3, 'Luis' );

INSERT INTO dojo_b VALUES ( 1, 'Curly' );
INSERT INTO dojo_b VALUES ( 2, 'Larry' );
INSERT INTO dojo_b VALUES ( 3, 'Moe' );

INSERT INTO dojo_c VALUES ( 1, 'Bart' );
INSERT INTO dojo_c VALUES ( 2, 'Lisa' );
INSERT INTO dojo_c VALUES ( 3, 'Maggie' );

SET SQL_SAFE_UPDATES = 0;

SELECT * FROM dojo_a;

SELECT * FROM dojo_b;

SELECT * FROM dojo_c WHERE id='3';

SELECT * FROM dojo_c WHERE nombre = 'Maggie';



