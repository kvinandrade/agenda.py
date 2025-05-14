/*CREATE DATABASE agenda_db
CREATE USER 'usuario'@'localhost' IDENTIFIED BY 'senha123';
GRANT ALL PRIVILEGES ON agenda_db.* TO 'usuario'@'localhost';
FLUSH PRIVILEGES;
USE agenda_db;

CREATE TABLE contatos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL
);*/

SELECT * FROM contatos;
