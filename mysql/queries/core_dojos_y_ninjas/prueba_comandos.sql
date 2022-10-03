INSERT INTO `esquema_dojos_y_ninjas`.`dojos` (`id`, `nombre`) VALUES ('1', 'dojo_a');
INSERT INTO `esquema_dojos_y_ninjas`.`dojos` (`id`, `nombre`) VALUES ('2', 'dojo_b');
INSERT INTO `esquema_dojos_y_ninjas`.`dojos` (`id`, `nombre`) VALUES ('3', 'dojo_c');

DELETE FROM `esquema_dojos_y_ninjas`.`dojos` WHERE (`id` = '1');
DELETE FROM `esquema_dojos_y_ninjas`.`dojos` WHERE (`id` = '2');
DELETE FROM `esquema_dojos_y_ninjas`.`dojos` WHERE (`id` = '3');

INSERT INTO `esquema_dojos_y_ninjas`.`dojos` (`id`, `nombre`) VALUES ('1', 'dojo_a');
INSERT INTO `esquema_dojos_y_ninjas`.`dojos` (`id`, `nombre`) VALUES ('2', 'dojo_b');
INSERT INTO `esquema_dojos_y_ninjas`.`dojos` (`id`, `nombre`) VALUES ('3', 'dojo_c');

INSERT INTO `esquema_dojos_y_ninjas`.`ninjas` (`id`, `nombre`, `apellido`, `edad`, `dojo_id`) VALUES ('1', 'Cristian', 'Yela', '38', '1');
INSERT INTO `esquema_dojos_y_ninjas`.`ninjas` (`id`, `nombre`, `apellido`, `edad`, `dojo_id`) VALUES ('2', 'Andres', 'Garcia', '25', '1');
INSERT INTO `esquema_dojos_y_ninjas`.`ninjas` (`id`, `nombre`, `apellido`, `edad`, `dojo_id`) VALUES ('3', 'Ana', 'Abad', '33', '1');

INSERT INTO `esquema_dojos_y_ninjas`.`ninjas` (`id`, `nombre`, `apellido`, `edad`, `dojo_id`) VALUES ('4', 'Luis', 'Luna', '26', '2');
INSERT INTO `esquema_dojos_y_ninjas`.`ninjas` (`id`, `nombre`, `apellido`, `edad`, `dojo_id`) VALUES ('5', 'Pedro', 'Panesso', '29', '2');
INSERT INTO `esquema_dojos_y_ninjas`.`ninjas` (`id`, `nombre`, `apellido`, `edad`, `dojo_id`) VALUES ('6', 'Carlos', 'Zapata', '23', '2');

INSERT INTO `esquema_dojos_y_ninjas`.`ninjas` (`id`, `nombre`, `apellido`, `edad`, `dojo_id`) VALUES ('7', 'Marta', 'Hazas', '31', '3');
INSERT INTO `esquema_dojos_y_ninjas`.`ninjas` (`id`, `nombre`, `apellido`, `edad`, `dojo_id`) VALUES ('8', 'Paula', 'Carvalho', '29', '3');
INSERT INTO `esquema_dojos_y_ninjas`.`ninjas` (`id`, `nombre`, `apellido`, `edad`, `dojo_id`) VALUES ('9', 'Mariana', 'Bedoya', '24', '3');

-- SELECT * FROM dojos;
-- SELECT * FROM ninjas WHERE dojo_id = 1;
-- SELECT * FROM ninjas WHERE dojo_id = 3;

SELECT  dojo_id, ninjas.id, dojos.nombre AS "Nombre del dojo", ninjas.nombre AS "Nombre del Ninja", ninjas.apellido AS "Apellido del Ninja"
FROM dojos
LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
WHERE dojo_id = 1;

SELECT  dojo_id, ninjas.id, dojos.nombre AS "Nombre del dojo", ninjas.nombre AS "Nombre del Ninja", ninjas.apellido AS "Apellido del Ninja"
FROM dojos
LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
WHERE dojo_id = 3;

SELECT  dojo_id, ninjas.id, dojos.nombre AS "Nombre del dojo", ninjas.nombre AS "Nombre del Ninja", ninjas.apellido AS "Apellido del Ninja"
FROM dojos
LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
WHERE ninjas.id = 3 or ninjas.id = 6 or ninjas.id = 9;


