
-- connectando no bd via terminal
postgres$psql -h <host> -p 5432 -U <nomeusuario> <bancodados>


-- criando um bd a partir do bd-postgres
CREATE DATABASE auladb;


-- criando uma role
CREATE ROLE professores NOCREATEDB NOCREATEROLE INHERIT NOLOGIN NOBYPASSRLS CONNECTION LIMIT 5;


-- consultando roles criadas
\du -- pelo terminal
SELECT * FROM pg_roles; -- pelo pgadmin

-- realizar alguma alteração na role
ALTER ROLE professores PASSWORD '';

-- criando uma role e atribuindo uma role existente para a nova role:
CREATE ROLE aline INHERIT LOGIN PASSWORD '123' IN role professores;

-- criando uma role e atribuindo ela para uma role existente:
CREATE ROLE aline LOGIN PASSWORD '123' role professores;
