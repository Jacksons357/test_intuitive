-- 10 operadoras com maiores despesas no último trimestre
SELECT o.registro_ans, o.razao_social, SUM(d.vl_saldo_final) AS total_despesas
FROM demonstracoes_contabeis d
JOIN operadoras o ON d.registro_ans = o.registro_ans
WHERE d.descricao ILIKE '%EVENTOS%SINISTROS%CONHECIDOS%OU%AVISADOS%DE%ASSISTÊNCIA%A%SAÚDE%MEDICO%HOSPITALAR%'
AND d.data >= '2024-10-01' AND d.data <= '2024-12-31'
GROUP BY o.registro_ans, o.razao_social
ORDER BY total_despesas DESC
LIMIT 10;

-- 10 operadoras com maiores despesas no último ano
SELECT o.registro_ans, o.razao_social, SUM(d.vl_saldo_final) AS total_despesas
FROM demonstracoes_contabeis d
JOIN operadoras o ON d.registro_ans = o.registro_ans
WHERE d.descricao ILIKE '%EVENTOS%SINISTROS%CONHECIDOS%OU%AVISADOS%DE%ASSISTÊNCIA%A%SAÚDE%MEDICO%HOSPITALAR%'
AND d.data >= '2024-01-01' AND d.data <= '2024-12-31'
GROUP BY o.registro_ans, o.razao_social
ORDER BY total_despesas DESC
LIMIT 10;