# Dados processados — consolidação e triagem

Gerados em 18/11/2026 a partir de `raw/Q1–Q6.bib`, pelos scripts em `literature/scripts/`.

| Arquivo | Conteúdo |
|---|---|
| `wos_consolidado.xlsx` | 1.351 linhas: um registro por exportação, com a consulta de origem |
| `wos_deduplicado.xlsx` | 1.296 registros únicos, com todas as consultas de origem |
| `triagem_estudos.xlsx` | Aba `Registros`: decisão de título/resumo, motivo, categoria e justificativa. Aba `Origens`: ligação com `raw/` |
| `registros_unicos.jsonl`, `decisoes_titulo_resumo.csv`, `segunda_leitura.csv`, `execucoes_raw.csv` | Intermediários (resumos, decisões da 1ª e da 2ª leitura, SHA-256 dos originais) |

**Fora do Git:** os `.bib`/`.xls` de `raw/`, `wos_consolidado.xlsx`, `wos_deduplicado.xlsx`, `registros_unicos.jsonl` e os `.csv` ficam só no disco, porque o repositório é público e esses arquivos trazem os registros completos do Web of Science, com resumos. Guarde uma cópia de segurança deles fora do repositório.

Para refazer: `python literature/scripts/consolidar_wos.py`, `python literature/scripts/aplicar_triagem.py` e `python literature/scripts/lista_estudo.py` (este gera em `literature/analysis/` a `lista_estudo_versionada.xlsx`, sem resumos, e a cópia de trabalho `lista_estudo_priorizada.xlsx`, com resumos e fora do Git).

## Deduplicação

Em cascata: identificador WoS; depois DOI normalizado; depois título normalizado + ano. O `id_registro` (R0001…) é estável enquanto os arquivos de `raw/` não mudarem.

## Códigos da triagem de título e resumo

Decisão: `incluir` ou `excluir`. As 93 decisões `duvida` da primeira leitura foram resolvidas na segunda (21/11/2026): 23 incluídas, 70 excluídas com o código **M7**.

- **E1** tipo documental diferente de Article · **E2** idioma diferente de inglês · **E3** fora de 2009–2026 · **E4** artigo retratado. E1–E3 são regra do protocolo, aplicada sem leitura.
- **M1** fora do domínio · **M2** crédito sem pertinência aos eixos · **M3** contábil/regulatório sem modelagem de PD/ECL · **M4** aplicação de outro domínio sem contribuição metodológica transferível · **M5** só fraude, seguros ou outro risco · **M6** informação insuficiente.

Categoria: `principal` (crédito/PD com transferência, adaptação ou escassez informacional), `suporte_simulacao`, `suporte_calibracao`, `suporte_contabil`, `suporte_metodologico`. Revisões de literatura estão marcadas em `observacoes`.

## Prioridade de leitura

A segunda leitura deu a cada incluído de 0 a 100 pontos pela utilidade direta para a dissertação, só com base em título e resumo. Faixas: 1 (85+) ler primeiro; 2 (75–84) ler na íntegra; 3 (55–74) leitura dirigida; 4 (abaixo de 55) só resumo. Desempate por citações por ano no WoS. A ordem é um guia de estudo, não um critério de inclusão.

**Revisor:** Claude (IA), duas leituras. Falta a conferência humana por amostra; ver limitação no [registro de buscas](../../docs/revisao/registro-buscas.md).
