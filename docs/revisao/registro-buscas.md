# Registro auditável de buscas — mini RSL Web of Science

**Estado:** PENDENTE — nenhuma execução da Web of Science foi importada neste pacote.  
**Protocolo:** [Q0–Q6](protocolo-busca-wos-q0-q6.md).  
**Convenção:** um registro **por execução**, mesmo que repita a query em outra data.

## 1. Registro de execuções

| ID | Data/hora e fuso | Base/índices WoS | Query executada e versão | Período | Filtros | Resultados brutos | Exportados | Arquivos em `literature/raw/` | Observações |
|---|---|---|---|---|---|---:|---:|---|---|
| Q0 | Pendente | A confirmar | Protocolo Q0 — a validar | A definir | A definir | — | — | — | Mapeamento exploratório |
| Q1 | Pendente | A confirmar | Protocolo Q1 — a validar | A definir | A definir | — | — | — | Núcleo |
| Q2 | Pendente | A confirmar | Protocolo Q2 — a validar | A definir | A definir | — | — | — | Núcleo |
| Q3 | Pendente | A confirmar | Protocolo Q3 — a validar | A definir | A definir | — | — | — | Suporte |
| Q4 | Pendente | A confirmar | Protocolo Q4 — a validar | A definir | A definir | — | — | — | Suporte |
| Q5 | Pendente | A confirmar | Protocolo Q5 — a validar | A definir | A definir | — | — | — | Suporte |
| Q6 | Pendente | A confirmar | Protocolo Q6 — a validar | A definir | A definir | — | — | — | Suporte geral |

## 2. Histórico das alterações de consultas

| Data/hora | ID | Mudança exata na string ou filtro | Justificativa | Impacto sobre contagem |
|---|---|---|---|---|
| Pendente | — | Nenhuma execução registrada | — | — |

## 3. Fluxo quantitativo consolidado

Preencher com números **reais**, preservando contagens por base/consulta. Deduplicar antes da triagem. Caso a busca inclua recuperação por citações, informar os registros adicionados por essa via separadamente.

- Registros identificados em consultas WoS (somados, ainda com duplicatas): **pendente**.
- Registros adicionais por referências/citações: **pendente**.
- Duplicatas removidas: **pendente**.
- Registros únicos submetidos à triagem: **pendente**.
- Registros excluídos por título/resumo: **pendente**.
- Textos completos procurados e não obtidos: **pendente**.
- Textos completos avaliados e excluídos, por motivo: **pendente**.
- Estudos incluídos na síntese de crédito: **pendente**.
- Fontes metodológicas de apoio (separadas): **pendente**.

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
