/* ============================================================
   Oracle AI DP Portfolio — Views
   ============================================================ */

---------------------------------------------------------------
-- View: Último score de churn por cliente
---------------------------------------------------------------
CREATE OR REPLACE VIEW VW_CHURN_CLIENTE_ULTIMO_SCORE AS
WITH last_score AS (
  SELECT
    p.customer_id,
    p.churn_score,
    p.model_version,
    p.scored_at,
    ROW_NUMBER() OVER (PARTITION BY p.customer_id ORDER BY p.scored_at DESC) AS rn
  FROM FATO_CHURN_PREDICOES p
)
SELECT
  c.customer_id,
  c.idade,
  c.renda,
  c.plano,
  c.tempo_cliente,
  c.qtd_chamados,
  c.atraso_pagamento,
  c.churn AS churn_real,
  c.faixa_renda,
  ls.churn_score,
  ls.model_version,
  ls.scored_at,
  CASE
    WHEN ls.churn_score IS NULL THEN 'sem_score'
    WHEN ls.churn_score >= 0.80 THEN 'alto'
    WHEN ls.churn_score >= 0.50 THEN 'medio'
    ELSE 'baixo'
  END AS risco_churn
FROM DIM_CLIENTES_CHURN c
LEFT JOIN last_score ls
  ON c.customer_id = ls.customer_id
 AND ls.rn = 1;

---------------------------------------------------------------
-- View: Distribuição de risco por plano (para dashboard)
---------------------------------------------------------------
CREATE OR REPLACE VIEW VW_CHURN_RISCO_POR_PLANO AS
SELECT
  plano,
  risco_churn,
  COUNT(*) AS qtd_clientes
FROM VW_CHURN_CLIENTE_ULTIMO_SCORE
GROUP BY plano, risco_churn;
