
--------------- Instalação postgresql

-- Para baixar acessar pagina e seguir instruções
https://www.postgresql.org/download/

-- Após instalado, vamos criar um cluster no ubuntu
pg_createcluster -d /home/postgres/aula 13 aula --start

/*
/home/postgres/aula :: <diretorio>
13 :: <versao_postgres> 
aula :: <nome_do_cluster> 
--start "comando para assim que criar o cluster ele ser iniciado"
*/

-- Consultar clusters existentes
pg_lsclusters

-- mudar para o usuario postgres
su - postgres

-- acessar o bd
psql

-- sair do bd
\q

-- sair do usuario postgres no ubuntu
logout


--------------- Instalação pgadmin

-- Para baixar acessar pagina e seguir instruções
https://www.pgadmin.org/download/

-- Após ser instalado podemos chamar via terminal, 
-- e será disponibilizado um endereço que podemos acessar via navegador web
pgadmin4


