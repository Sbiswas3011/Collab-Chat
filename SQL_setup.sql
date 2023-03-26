CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE Chat_Accounts (
	id uuid DEFAULT uuid_generate_v4 (),
	username VARCHAR NOT NULL,
	password VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
	phno VARCHAR NOT NULL,
	PRIMARY KEY (id)
);

INSERT INTO Chat_Accounts (username, password, email, phno) VALUES ('Admin', 'Admin', 'Admin@amdin.com','8888852754');
