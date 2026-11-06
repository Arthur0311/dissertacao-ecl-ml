# Dicionário de dados (modelo)

Preencher uma linha por campo. Campos obrigatórios por camada conforme a seção 7 da proposta.

| Camada | Campo | Tipo | Unidade/domínio | Granularidade | Disponível na data-base? | Fonte | Observações de qualidade |
|---|---|---|---|---|---|---|---|
| operacao | id_contrato | string (hash) | — | contrato | sim | core banking / doc. 3040 | chave; anonimizada |
| operacao | modalidade | categórica | lista do SCR | contrato | sim | doc. 3040 | mapear para carteira analítica |
| operacao | carteira_regulatoria | categórica | C1–C5 | contrato-mês | sim | classificação interna | critério da Res. BCB 309 |
| operacao | saldo_devedor | numérico | BRL | contrato-mês | sim | core banking | EAD |
| operacao | dias_atraso | inteiro | dias | contrato-mês | sim | core banking | faixa para níveis mínimos |
| operacao | evento_default_12m | binário | 0/1 | contrato-mês | não (rótulo) | derivado | definido no dicionário de eventos |
| tomador | natureza | categórica | PF/PJ | tomador | sim | cadastro | |
| macro | selic_focus_12m | numérico | % a.a. | mês | sim (vintage por construção) | BCB/Focus | data de referência da expectativa |
| regulatorio | pct_minimo | numérico | % | carteira × faixa × data | sim | Res. BCB 309 | versão vigente à data |

## Dicionário de eventos

| Evento | Definição operacional | Tratamento |
|---|---|---|
| Inadimplência | atraso > 90 dias ou ativo com problema de recuperação | rótulo em 12 meses |
| Cura | retorno a atraso ≤ 30 dias por n meses | documentar n |
| Renegociação | alteração contratual com atraso | marcar e não apagar o evento original |
| Baixa | baixa para prejuízo | encerra observação |
| Cessão | cessão de carteira | censura |
