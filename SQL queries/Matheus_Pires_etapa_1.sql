--Dado o schema apresentado na figura pharma.png, as seguintes queries foram realizadas 

--Query 1: Quantidade de vendas em unidades por Gerente no tipo de canal ʻFarmácias’;
SELECT Nome_Gerente,
    SUM(Unidades)
    FROM Fato
        LEFT JOIN PDV_dim
            ON Fato.Cod_PDV = PDV_dim.Cod_PDV 
        LEFT JOIN Representantes
            ON PDV_dim.Cod_Representantes = Representantes.Cod_Representantes
        LEFT JOIN Canal_de_Vendas_dm
            ON PDV_dim.Cod_Canal_de_Vendas = Canal_de_Vendas_dm.Cod_Canal
    WHERE Tipo_canal = 'Fármacias'
    GROUP BY Nome_GERENTE

    
-- Query 2: Quais as marcas que venderam mais de 500 unidades por unidade da federação;
'''
Esse enunciado ficou ambíguo para mim.
Não entendi se as marcas precisariam ter mais de 500 em TODAS UFs (ou seja, apenas uma UF com venda inferior a 500 unidades de uma marca
seria suficiente para remover ela da query);
Ou se seriam as marcas que venderam mais de 500 unidades por UF em conjunto com a respeciva UF (e nesse não seria necessário que o produt
tivesse mais de 500 vendas em todas UFs)
Em todo caso, fiz ambas as queries e na ordem eu que eu as apresentei
'''

WITH vendas_abaixo AS (
    SELECT Cod_Produto, 
        Cod_pdv,
        UF,
        SUM(Unidades) AS total_vendas
        FROM Fato
            LEFT JOIN PDV_dim
                ON Fato.Cod_pdv = PDV_dim.Cod_pdv
        WHERE total_vendas < = 500
        GROUP BY Cod_Produto, UF

SELECT Marcas,
    Cod_Produto
    FROM Produto_dim
    WHERE Cod_Produto NOT IN
        (SELECT Cod_Pdv
            FROM vendas_abaixo
        )

WITH vendas_acima AS(
    SELECT Cod_Produto, 
        Cod_pdv,
        UF,
        SUM(Unidades) AS total_vendas
        FROM Fato
            LEFT JOIN PDV_dim
                ON Fato.Cod_pdv = PDV_dim.Cod_pdv
        WHERE total_vendas > 500
        GROUP BY Cod_Produto, UF
    )

SELECT MARCAS,
    UF,
    SUM(Unidades)
    FROM vendas_acima
        LEFT JOIN Produto_dim
            ON vendas_acima.Cod_Produto = Produto_dim.Cod_Produto

--Query 3: Quantidade de vendas e, unidades da marca ʻVi-Ferrin’ do Gerente de código ʻ400’;
SELECT COUNT(Unidades),
    SUM(Unidades)
    FROM Fato
        LEFT JOIN Produto_dim
            ON Fato.Cod_Produto = Produto_dim.Cod_Produto
        LEFT JOIN PDV_dim
            ON Fato.Cod_PDV = PDV_dim.Cod_PDV
        LEFT JOIN Representantes
            ON PDV_dim.Cod_Local = Representantes.Cod_Local
    WHERE Cod_Gerente = '400'
        AND Marca = 'Vi-Ferrin' 