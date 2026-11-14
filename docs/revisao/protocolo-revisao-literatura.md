# Revisão da literatura — adendo da proposta v4 e situação das referências

**Estado em 14/11/2026:** revisão não executada. A lacuna da seção 3.4 da [proposta v4](../proposta/proposta-dissertacao-v4-2026-11-14.md) é candidata até a conclusão da revisão.

O protocolo operativo de busca, seleção, extração e síntese é o da [mini revisão sistemática](../metodologia/mini-revisao-protocolo-wos-2026-11-14.md), com as [consultas para a Web of Science](../metodologia/mini-revisao-queries-wos-2026-11-14.txt). Aquele protocolo foi elaborado com base na proposta v3. Este adendo registra apenas o que a v4 acrescenta ou altera; não o substitui nem o modifica.

## 1. Correspondência entre o protocolo e a v4

| Item do protocolo de mini revisão | Leitura sob a v4 |
|---|---|
| Pergunta principal ("qualidade probabilística das PDs" e "repercussões na mensuração de ECL") | Mantida. A variável dependente da v4 tem três atributos: pontuação probabilística, calibração e viés monetário |
| Quatro regimes (local, agrupado, transferido, adaptado) | Seis regimes: acrescentam-se taxa base e local reduzido |
| Formulário de extração, item 12 ("relevância para H1, H2, H3") | Hipóteses H1–H4 e contraste C1 da v4; a numeração da v3 não se conserva |
| Formulário de extração, item 10 (ECL) | Acrescentar: o estudo reporta erro monetário da PD com base em eventos observados, ou apenas propaga premissas? |
| Formulário de extração, item 5 (domínios) | Acrescentar: a distância entre domínios é observada ou manipulada? Qual componente (taxa base, composição, relação condicional)? |
| Síntese ("implicações para os quatro regimes e H1–H3 da v3") | Implicações para a fronteira de utilidade e para o critério de adequação da v4 |
| Rota Q5 (capacidade operacional) | Fora do núcleo da v4; manter como complementar, sem objetivo correspondente |

## 2. Rota adicional requerida pela v4

A v4 adota como teoria de base a representação fidedigna e a qualidade da provisão para o usuário externo. As rotas Q1 a Q4 não cobrem essa literatura. Consulta candidata para a Web of Science, a submeter ao mesmo piloto e às mesmas regras de registro:

```text
TS=("expected credit loss" OR "expected credit losses" OR "loan loss provision" OR "loan loss provisions" OR "loan loss provisioning" OR "allowance for loan losses")
AND TS=("measurement uncertainty" OR "estimation uncertainty" OR "faithful representation" OR discretion* OR "estimation error" OR "model risk" OR neutralit* OR "earnings management")
```

Na SPELL e na SciELO: `("perdas esperadas" OR "provisão para créditos" OR "PCLD") AND (mensuração OR discricionariedade OR "gerenciamento de resultados" OR "Resolução 4.966")`.

Referências metodológicas de outros campos (calibração, tamanho de amostra para validação, modelagem preditiva) entram por rastreamento dirigido, como o protocolo de mini revisão já prevê.

## 3. Achados que refutam a lacuna candidata

1. Estudo que estime, em crédito, o volume local em que o modelo próprio iguala o modelo transferido, com avaliação de calibração.
2. Estudo que quantifique o efeito monetário do erro de PD sob escassez de dados.
3. Evidência de que a distância entre carteiras não se associa ao desempenho da transferência.

A ocorrência de (1) ou (2) converte a pesquisa em replicação no contexto brasileiro; a de (3) exige rever H2 e H3. O protocolo de mini revisão registra que Suryanto et al. (2022) já reportam configurações em que a adaptação reduz a discriminação: a ocorrência de falha da adaptação não é, por si, a lacuna.

## 4. Situação de leitura das referências da proposta v4

Os metadados foram conferidos em fontes editoriais ou repositórios em 14/11/2026. A leitura integral pelo autor é requisito para a versão de qualificação.

| Referência | Metadados | Leitura pelo autor | Uso na proposta |
|---|---|---|---|
| Suryanto et al. (2022) | Conferidos | Texto consultado | Antecedente direto; conferir métricas e desenho de validação |
| Kiefer (2009) | Conferidos | Resumo; leitura integral pendente | Antecedente: carteiras com poucos eventos |
| Blümke (2020) | Conferidos | Resumo; leitura integral pendente | Antecedente: carteiras sem eventos |
| Van Calster et al. (2019) | Conferidos; cinco autores e grupo STRATOS | Pendente | Níveis e avaliação de calibração |
| Riley et al. (2021) | Conferidos | Pendente | Tamanho de amostra para validação; base da precisão-alvo |
| Shmueli (2010) | Conferidos | Pendente | Justificativa do delineamento preditivo |
| Beatty e Liao (2014) | Conferidos | Pendente | Provisão bancária e discricionariedade; conferir no texto as afirmações da seção 1.1 |
| CPC 00 (R2) (2019) | Conferidos | Conferir a numeração dos itens 2.12–2.19 | Representação fidedigna e incerteza de mensuração |
| BCBS (2015) | Conferidos | Pendente | Contexto de supervisão |
| IASB (2014), IFRS 9 | Edição a conferir | Pendente | Definição de perda esperada de 12 meses |
| CMN (2021); BCB (2023, 2024) | Datas conferidas | Ver [nota normativa](../normativo/notas-verificacao-normativa.md) | Enquadramento |

As referências das propostas v1 e v2 não foram reaproveitadas sem conferência e não sustentam a lacuna corrente.
