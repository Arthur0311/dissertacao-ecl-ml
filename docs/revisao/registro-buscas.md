# Registro auditável de buscas — mini RSL Web of Science

**Estado:** Q1–Q6 executadas e exportadas em 18/11/2026; triagem de título/resumo feita (assistida por IA, validação humana pendente). Q0 sem exportação. Campos marcados **a confirmar** dependem de informação que só quem executou a busca tem.  
**Protocolo:** [Q0–Q6](protocolo-busca-wos-q0-q6.md).  
**Convenção:** um registro **por execução**, mesmo que repita a query em outra data.

## 1. Registro de execuções

| ID | Data/hora e fuso | Base/índices WoS | Query executada e versão | Período | Filtros | Resultados brutos | Exportados | Arquivos em `literature/raw/` | Observações |
|---|---|---|---|---|---|---:|---:|---|---|
| Q0 | Sem exportação em `raw/` | — | Protocolo Q0 | — | — | — | — | — | Mapeamento exploratório; não entrou na triagem |
| Q1-E01 | 2026-11-18, ~14:36 (hora local do arquivo) | A confirmar | Protocolo Q1 de 15/11 (string a confirmar) | Sem filtro aparente (2014–2026 nos registros) | Sem filtro aparente de tipo/idioma | A confirmar | 49 | `Q1.bib`, `Q1.xls` | Núcleo |
| Q2-E01 | 2026-11-18, ~14:38 | A confirmar | Protocolo Q2 (a confirmar) | Sem filtro aparente (desde 1995) | Idem | A confirmar | 199 | `Q2.bib`, `Q2.xls` | Núcleo; 2 duplicatas internas |
| Q3-E01 | 2026-11-18, ~14:40 | A confirmar | Protocolo Q3 (a confirmar) | Sem filtro aparente (desde 1998) | Idem | A confirmar | 456 | `Q3.bib`, `Q3.xls` | Suporte |
| Q4-E01 | 2026-11-18, ~14:42 | A confirmar | Protocolo Q4 (a confirmar) | Sem filtro aparente (desde 2010) | Idem | A confirmar | 67 | `Q4.bib`, `Q4.xls` | Suporte |
| Q5-E01 | 2026-11-18, ~14:43 | A confirmar | Protocolo Q5 (a confirmar) | Sem filtro aparente (desde 2009) | Idem | A confirmar | 80 | `Q5.bib`, `Q5.xls` | Suporte |
| Q6-E01 | 2026-11-18, ~16:02 | A confirmar | Protocolo Q6 (a confirmar) | Sem filtro aparente (desde 1993) | Idem | 500 | 500 | `Q6.bib`, `Q6.xls` | Suporte geral. Total de 500 resultados confirmado pelo autor em 18/11/2026: exportação completa |

**Observações da importação (18/11/2026):**

- Os arquivos não seguem o padrão `wos_Qn_AAAA-MM-DD`; foram mantidos como vieram, porque `raw/` é imutável. A planilha veio em `.xls` (não `.xlsx`) e está fora do Git pelo `.gitignore`.
- BibTeX e XLS de cada consulta trazem os mesmos identificadores WoS (49, 199, 456, 67, 80 e 500), contados uma única vez.
- As exportações incluem anais, outros idiomas e anos anteriores a 2009. Os critérios do protocolo (Article, inglês, 2009–2026) foram aplicados na triagem, como exclusões documentadas (E1, E2, E3).
- Artigos-semente: Suryanto et al. (2022) em Q1 (R0029); Kiefer (2009) em Q2 (R0197); Blümke (2020) em Q2 (R0190). Todos incluídos.
- SHA-256 e data de cada arquivo: `literature/processed/execucoes_raw.csv`, gerado por `literature/scripts/consolidar_wos.py`.

## 2. Histórico das alterações de consultas

| Data/hora | ID | Mudança exata na string ou filtro | Justificativa | Impacto sobre contagem |
|---|---|---|---|---|
| Pendente | — | Nenhuma execução registrada | — | — |

## 3. Fluxo quantitativo consolidado

Preencher com números **reais**, preservando contagens por base/consulta. Deduplicar antes da triagem. Caso a busca inclua recuperação por citações, informar os registros adicionados por essa via separadamente.

- Registros identificados em consultas WoS (somados, ainda com duplicatas): **1.351** (Q1 49, Q2 199, Q3 456, Q4 67, Q5 80, Q6 500).
- Registros adicionais por referências/citações: **0** (via ainda não usada).
- Duplicatas removidas: **55** (por identificador WoS; 2 casos adicionais por DOI/título).
- Registros únicos submetidos à triagem: **1.296**.
- Excluídos por critério formal do protocolo, sem leitura: **317** (E1 tipo documental 234; E2 idioma 14; E3 período 69).
- Lidos em título e resumo: **979**. Excluídos: **775** (M1 34; M2 333; M3 13; M4 315; M5 9; E4 retratado 1; M7 70, dúvidas excluídas na segunda leitura de 21/11/2026).
- Seguem para leitura integral: **204** (181 incluídos na primeira leitura + 23 das 93 dúvidas, resolvidas na segunda leitura).
  - Evidência principal (crédito com transferência/adaptação ou escassez): 66.
  - Suporte: simulação 27; calibração 23; contábil 38; metodológico geral 50.
  - Ordem de leitura: `literature/analysis/lista_estudo_versionada.xlsx` (15 para ler primeiro; 28 na íntegra; 64 em leitura dirigida; 97 só resumo).
- Textos completos procurados e não obtidos: **pendente**.
- Textos completos avaliados e excluídos, por motivo: **pendente**.
- Estudos incluídos na síntese de crédito: **pendente**.

**Limitação a declarar:** a leitura de título e resumo foi feita por IA (Claude), em 16 lotes, com os critérios e códigos de `literature/processed/README.md`. As 93 dúvidas foram resolvidas em 21/11/2026 por uma segunda leitura, também por IA, a pedido do autor. Não houve revisor humano independente. Recomenda-se que o autor confira uma amostra das exclusões (em especial as 70 de código M7) e registre essa conferência antes de fixar os números.

## 4. Regras de integridade

- Nunca alterar conteúdo de `literature/raw/`.
- Manter DOI, título, ano e identificadores WoS quando disponíveis.
- Em artigos retornados por múltiplas queries, guardar **todas** as IDs de origem.
- Não inferir que a fonte foi revisada por pares apenas pelo fato de estar no WoS; verificar o tipo documental e contexto.
- Não registrar seleção final sem preencher motivo e etapa de exclusão quando apropriado.

## 5. Ficha obrigatória por execução

Duplicar a ficha abaixo para cada execução, inclusive reexecuções. As linhas Q0–Q6 acima são agenda, não buscas realizadas.

- ID da execução e query: **pendente**.
- Versão do protocolo e responsável: **pendente**.
- Plataforma, coleção, índices e instituição de acesso: **pendente**.
- Data, horário e fuso (ISO 8601 com deslocamento): **pendente**.
- Período de publicação e cobertura da assinatura: **pendente**.
- Filtros exatos (tipo, idioma, demais) e Exact Search: **pendente**.
- String literalmente executada (colar abaixo, não apenas referenciar o protocolo):

```text
PENDENTE — nenhuma string executada
```

- Quantidade encontrada: **pendente**.
- Quantidade exportada XLSX / BibTeX / outro formato: **pendente**.
- Campos selecionados na exportação e referências citadas disponíveis: **pendente**.
- Caminhos relativos dos arquivos, lotes e intervalos de registros: **pendente**.
- SHA-256 de cada arquivo original: **pendente**.
- Diferenças entre encontrado/exportado e justificativa: **pendente**.
- Alterações frente à string candidata, motivo e efeito observado: **pendente**.
- Teste de estudos-semente (título/DOI conferido, recuperado ou não, ação): **pendente**.

Identificadores antigos Q1–Q5 pertencem ao protocolo de 14/11 baseado na v3/v4 e não são equivalentes aos Q0–Q6 atuais. Sempre guardar versão + ID da consulta. A classificação temática do registro pode diferir de sua consulta de origem.

Buscas por citações ou título exato recebem IDs próprios (`CIT-001`, `TIT-001` etc.), com fonte-semente, direção, data, string quando aplicável e registros recuperados. Não atribuir esses registros artificialmente a uma Q.
