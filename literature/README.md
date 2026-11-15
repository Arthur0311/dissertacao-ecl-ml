# Dados bibliográficos da mini RSL

Área exclusiva para bibliografia. `data/` permanece destinada a dados públicos, sintéticos e experimentos quantitativos; sua estrutura não foi alterada.

- [raw](raw/): exportações originais, sem edição.
- [processed](processed/): consolidação, deduplicação e [triagem](processed/triagem_estudos.xlsx).
- [analysis](analysis/): [matriz de extração](analysis/matriz-extracao.xlsx), síntese e avaliação da lacuna.
- [references](references/): BibTeX dos estudos selecionados.

## Execução

1. Fixar configuração e executar consultas do [protocolo Q0–Q6](../docs/revisao/protocolo-busca-wos-q0-q6.md), priorizando Q1–Q2 como núcleo.
2. Preencher a ficha literal no [registro de buscas](../docs/revisao/registro-buscas.md).
3. Salvar originais por consulta e data; registrar lotes, formatos e hashes.
4. Consolidar cópias, preservar todas as origens e deduplicar por DOI normalizado; revisar título, ano e autores quando DOI estiver ausente ou houver conflito.
5. Triar, obter textos e registrar decisões e motivos; manter o mesmo `id_registro` nas duas planilhas.
6. Extrair evidências com página/seção da fonte; produzir síntese e preencher o [fluxo PRISMA](../docs/revisao/fluxo-prisma.md).

As planilhas são modelos vazios derivados do pacote fornecido, ampliados para cobrir todos os campos solicitados. Não existem exportações ou estudos incluídos. Cada tabela tem 150 linhas reservadas, sem resultados; ao ultrapassá-las, expandir tabela e validações. Campos numéricos desconhecidos ficam vazios, nunca zero; explicar ausência em observações. Nos campos textuais, usar `Não informado` ou `Não se aplica` quando apropriado.

## Rastreabilidade

`id_registro` identifica uma publicação; `id_estudo` agrupa publicações do mesmo estudo. `queries_origem` aceita múltiplas Q separadas por ponto e vírgula. `data_busca` é a primeira recuperação; todas as recuperações são vinculadas por `ids_execucao`, pelos arquivos e pela aba `Origens` da triagem (uma linha por registro e ocorrência). A aba preserva query, data, arquivo e identificador WoS para cada ocorrência.

Preservar DOI e UT/WoS literais nas origens. Usar cópia normalizada do DOI (sem prefixo de URL, espaços externos e em minúsculas) somente para comparação; manter valores originais. Registrar fusões e conflitos em `processed/deduplicacao.md` quando houver dados reais. Versões distintas de uma pesquisa não são duplicatas automáticas.

O protocolo inicial v5 e os materiais v3/v4 permanecem como antecedentes. A numeração de queries antiga não é intercambiável com a versão operacional de 15/11/2026.
