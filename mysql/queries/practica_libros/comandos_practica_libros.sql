SELECT * FROM usuarios;
SELECT * FROM libros;
SELECT * FROM favoritos;

INSERT INTO usuarios (nombre)
VALUES ("Jane Austin"),("Emily Dickinson"),("FYodor Dostoevsky"),("William Shakespeare"),("Lau Tzu");

SELECT * FROM usuarios;

INSERT INTO libros (titulo, num_paginas)
VALUES ("C Sharp",200),("Java",200),("Python",200),("PHP",200),("Ruby",200);

SELECT * FROM libros;

UPDATE libros SET titulo = "C#" 
WHERE id= 1;

SELECT * FROM libros;

UPDATE usuarios SET nombre = "Bill Shakespeare"
WHERE id = 4;

SELECT * FROM usuarios;

INSERT INTO favoritos (usuario_id,libro_id)
VALUES (1,1),(1,2),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3),(3,4),(4,1),(4,2),(4,3),(4,4),(4,5);

SELECT * FROM favoritos;

SELECT * FROM libros 
JOIN favoritos on libros.id = favoritos.libro_id
JOIN usuarios on usuarios.id = favoritos.usuario_id
WHERE libros.id = 3;

DELETE FROM favoritos
WHERE libro_id = 3
AND usuario_id = 2;

INSERT INTO favoritos (usuario_id,libro_id)
VALUES (5,2);

SELECT * FROM usuarios
JOIN favoritos ON usuarios.id = favoritos.usuario_id
JOIN libros ON libros.id = favoritos.libro_id
WHERE usuarios.id = 3;

SELECT * FROM libros
JOIN favoritos ON libros.id = favoritos.libro_id
JOIN usuarios ON usuarios.id = favoritos.usuario_id
WHERE libros.id = 5;