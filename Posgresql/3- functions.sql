
CREATE OR REPLACE FUNCTION func_somar(INTEGER,INTEGER)
RETURNS INTEGER
SECURITY DEFINER
--RETURNS NULL ON NULL INPUT
CALLED ON NULL INPUT
LANGUAGE SQL
AS
$$
	SELECT COALESCE($1,0) + COALESCE($2,0) ;
$$;

SELECT func_somar(1,null);

-----------------------------------------------------------

CREATE OR REPLACE FUNCTION func_add_banco(p_num INTEGER, p_nome VARCHAR, p_ativo BOOLEAN)
RETURNS INTEGER
SECURITY INVOKER
LANGUAGE PLPGSQL
CALLED ON NULL INPUT
AS 
$$
DECLARE variavel_id INTEGER;
BEGIN
	IF p_numero IS NULL OR p_nome IS NULL OR p_ativo IS NULL THEN
		RETURN 0;
	END IF;
	
	SELECT INTO variavel_id numero
	FROM banco
	WHERE numero = p_numero
	
	IF variavel_id IS NULL THEN
		INSERT INTO banco (numero, nome, ativo)
		VALUES (p_numero, p_nome, p_ativo);
	ELSE
		RETURN variavel_id;
	END IF;
	
	RETURN variavel_id;
END;
$$;

SELECT func_add_banco(1,'Banco Novo'FALSE);

-----------------------------------------------------------

/*
---> LANGUAGES
- SQL
- PLPGSQL
- PLJAVA
- PLPY 
- ...

---> SECURITY
- INVOKER : (padrão) eu permito que a função seja executada com as permissões do usuario que esta executando a função.
- DEFINER : o usuário que esta executando a função, execute com as permissões do usuário que criou a função.

---> COMPORTAMENTO
- IMMUTABLE : não permite alterar o banco com insert, update, delete, create...
- STABLE : permite select, current_timestamp e outros tipos de variaveis.
- VOLATILLE : (padrão) aceita todo tipo.

---> RECURSOS
- COST : custo/row em unidades de CPU
- ROWS : numero estimado de linhas que será analisada pelo planner

---> SOBRE NULL
- CALLED ON NULL INPUT : (padrão) Se qualquer um dos parametros/argumentos for NULL, a função será executada.
- RETURNS NULL ON NULL INPUT : se qualquer um dos parametros/argumentos for NULL, a função retornará NULL.

*** NÃO É POSSIVEL UTILIZAR TRANSACOES

*/ 

