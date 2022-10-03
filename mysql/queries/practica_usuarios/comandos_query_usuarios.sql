INSERT INTO usuarios (nombre, apellido, email)
VALUES ("Cristian","Yela","cyela@codingdojo.com"),
("Luis","Luna","lluna@outlook.it"),
("Pedro Pablo","Jaramillo","ppj@gmail.com");

SELECT * FROM usuarios;

SELECT * FROM usuarios
WHERE email = 'cyela@codingdojo.com';

SELECT * FROM usuarios
WHERE id = 3;

UPDATE usuarios SET apellido = "Panqueques"
WHERE usuarios.id = 3;

DELETE FROM usuarios
WHERE usuarios.id = 2;

SELECT * FROM usuarios
ORDER BY nombre DESC;