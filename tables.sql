CREATE DATABASE bookmanager DEFAULT CHARACTER SET utf8;

CREATE TABLE books(
    id int(11) NOT NULL PRIMARY KEY,
    user_id int(11) NOT NULL,
    image_url varchar(45) DEFAULT NULL,
    name varchar(45) DEFAULT NULL,
    price decimal(10,0) DEFAULT NULL,
    purchase_date datetime DEFAULT NULL,
    created timestamp NULL DEFAULT NULL,
    updated timestamp NULL DEFAULT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE users(
    user_id int(11) NOT NULL PRIMARY KEY,
    mail_address varchar(45) DEFAULT NULL,
    password varchar(45) DEFAULT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
