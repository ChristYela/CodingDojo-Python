SELECT * FROM nombres;

INSERT INTO nombres (nombre)
VALUES ("Cristian"), ("Andres");

SELECT * FROM nombres;

UPDATE `nombres`.`nombres` SET `nombre` = 'Heberth' WHERE (`id` = '2');

SELECT * FROM nombres;

DELETE FROM `nombres`.`nombres` WHERE (`id` = '2');

SELECT * FROM nombres;