-- user database
CREATE USER usr_motorock with encrypted PASSWORD '@W9q4x6r1';
GRANT ALL PRIVILEGES ON database motorock TO usr_motorock;

-- user schema
GRANT ALL PRIVILEGES ON SCHEMA vendas TO usr_motorock;

-- tables 
GRANT ALL PRIVILEGES ON TABLE vendas.tb_vendas TO usr_motorock;