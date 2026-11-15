# Protocolo inicial de mini revisão sistematizada — Web of Science

**Atualização de 15/11/2026:** este documento é o antecedente do [protocolo operacional Q0–Q6](revisao/protocolo-busca-wos-q0-q6.md). Para novas buscas, usar esse protocolo, o [registro](revisao/registro-buscas.md), o [fluxo](revisao/fluxo-prisma.md) e as [planilhas em literature](../literature/README.md). Os produtos e caminhos abaixo são a proposta inicial; os caminhos correntes estão nos links acima. Nenhuma busca foi executada.

**Projeto-base:** `proposta-dissertacao-v5-2026-11-14.md`.  
**Articulação operacional:** `roadmap-dissertacao-ecl-ml-v5.md`, etapa E02.  
**Elaboração da estratégia:** 14/11/2026. **Estado:** strings candidatas, ainda não executadas nem testadas diretamente no WoS.  
**Base principal:** Web of Science Core Collection, consulta **Advanced Search / Query Builder**.

> **Decisão de desenho:** não usar uma única string que exija simultaneamente *Machine Learning*, *transfer learning*, ECL, simulação, 3040, IFRS 9 e Brasil. Essa interseção provavelmente excluiria pesquisas metodológicas indispensáveis. Executar buscas em **blocos complementares**, registrar os resultados de cada bloco e eliminar duplicatas somente depois da exportação.

---

## 1. Questão e propósito da mini RSL

**Pergunta orientadora:** Quais são as evidências sobre condições em que métodos de transferência/adaptação entre populações de crédito melhoram ou prejudicam a qualidade de estimativas de probabilidade de inadimplência, especialmente sob escassez informacional, heterogeneidade entre carteiras e diferentes estruturas de modelo, e como a literatura avalia calibração, simulação e implicações para ECL?

A mini RSL deverá esclarecer:

1. Quais estratégias de **transferência**, adaptação de domínio, agrupamento ou recalibração foram aplicadas ao risco de crédito e com quais resultados?
2. Como os estudos tratam carteiras com poucos ou nenhum evento de inadimplência? Comparam modelos locais, agrupados e transferidos?
3. Como são avaliadas **calibração e qualidade probabilística**, além da discriminação (AUC)? Há medidas de transferência negativa?
4. Quais trabalhos utilizam **dados sintéticos, simulações de Monte Carlo ou DGPs** para testar propriedades de modelos de PD?
5. Há avaliação da repercussão de erros da PD para **ECL, perda monetária ou provisões**? As hipóteses de LGD/EAD e desconto são explícitas?
6. Quais lacunas permanecem após considerar estudos metodologicamente semelhantes, ainda que não focalizem instituições brasileiras?

**Não confundir:** mini revisão sistematizada de escopo delimitado com revisão sistemática exaustiva. PRISMA 2020 é diretriz de **relato transparente**, não certificação automática da qualidade de uma busca.

---

## 2. Consulta principal: transferência/adaptação no risco de crédito (Q1)

**Esta é a primeira query a executar no campo de busca avançada do WoS:**

```text
TS=(
  ("credit risk" OR "credit scor*" OR "loan default*" OR
   "credit default" OR "probability of default" OR
   "default prediction" OR "expected credit loss*")
  AND
  ("transfer learning" OR "domain adaptation" OR
   "domain shift" OR "covariate shift" OR
   "cross-domain" OR "cross-portfolio" OR
   "negative transfer" OR "multi-task learning" OR
   "model transportability" OR "model transfer*")
)
```

**Por que esta estrutura?** O primeiro bloco recupera estudos sobre previsão de inadimplência, *credit scoring* e perda esperada. O segundo seleciona técnicas ou problemas de transferência entre populações. Não exige explicitamente o termo *machine learning*, pois diversos artigos de adaptação e transferência não o repetem nos metadados.

**Cuidados:** termos de busca dentro de aspas e com `*` são propostos conforme regras de busca do WoS, mas a combinação deve ser testada no ambiente de acesso da instituição. Se a interface rejeitar determinada frase com coringa, substitua por formas explícitas (ex.: `"credit scoring" OR "credit score"`) e documente a alteração.

---

## 3. Consultas complementares — não fundir obrigatoriamente com Q1

### Q2 — Carteiras com poucos eventos / ausência de histórico

```text
TS=(
  ("credit risk" OR "credit scor*" OR "probability of default" OR
   "loan default*" OR "default estimation")
  AND
  ("low-default" OR "low default" OR "no-default" OR
   "no default" OR "rare event*" OR "small sample*" OR
   "few-shot" OR "data scarc*" OR "data spars*" OR
   "cold start" OR "limited data")
)
```

**Função:** localizar métodos de PD em carteiras de baixa inadimplência, regressão penalizada, abordagens bayesianas e modelos que funcionem com pouco histórico. Não exigir transferência como critério de inclusão neste bloco.

### Q3 — Dados sintéticos e simulações em risco de crédito

```text
TS=(
  ("credit risk" OR "credit scor*" OR "loan default*" OR
   "probability of default" OR "expected credit loss*")
  AND
  ("synthetic data" OR "simulated data" OR
   "simulation stud*" OR "Monte Carlo" OR
   "data-generating process*" OR "data generation" OR
   "synthetic portfolio*" OR "credit portfolio simulation")
)
```

**Função:** fundamentar escolha de DGPs, viés de especificação, plausibilidade de dados simulados, cenários e avaliação de métodos. Não presumir que todo resultado seja estudo de Monte Carlo completo.

### Q4 — Calibração e avaliação probabilística dos modelos de crédito

```text
TS=(
  ("credit risk" OR "credit scor*" OR "loan default*" OR
   "probability of default" OR "default prediction")
  AND
  ("probability calibration" OR "model calibration" OR
   "calibration slope" OR "calibration intercept" OR
   "Brier score" OR "log-loss" OR "logarithmic loss" OR
   "proper scoring rule*" OR "calibration curve*")
)
```

**Função:** recuperar técnicas e critérios de validação que não necessariamente são apresentados como transferência de aprendizado. Se o volume for excessivo, restringir após o registro da contagem inicial, e não introduzir filtros arbitrários na query sem documentação.

### Q5 — PD, ECL, contabilidade e Machine Learning

```text
TS=(
  ("expected credit loss*" OR "IFRS 9" OR
   "loan loss provision*" OR "credit loss provision*" OR
   "credit impairment")
  AND
  ("machine learning" OR "probability of default" OR
   "predictive model*" OR "credit risk model*" OR
   "default forecast*" OR "model calibration")
)
```

**Função:** avaliar a conexão contábil entre modelos de PD, ECL, mensuração prospectiva, provisões e eventual impacto monetário. Não usar `S4`, `S5`, `3040` ou `Brasil` como termos obrigatórios.

### Q6 — Apoio metodológico geral (busca auxiliar, não núcleo empírico)

```text
TS=(
  ("transfer learning" OR "domain adaptation" OR
   "covariate shift" OR "negative transfer")
  AND
  ("simulation stud*" OR "Monte Carlo" OR
   "model calibration" OR "probabilistic prediction")
)
```

**Função:** localizar trabalhos metodológicos de outras áreas (por exemplo, pesquisa clínica ou estatística) que ajudem a definir condições de transportabilidade, calibração, amostras pequenas e DGPs. Os artigos sem aplicação ao crédito **não entram automaticamente** na síntese de evidências empíricas sobre risco de crédito; podem sustentar o referencial metodológico.

---

## 4. Sintaxe do WoS e configuração inicial

- **`TS=`** busca no campo *Topic*: título, resumo, palavras-chave de autor e *Keywords Plus* no Web of Science Core Collection.
- **`AND`** exige ambos os blocos; **`OR`** combina sinônimos. Parênteses mantêm a precedência desejada.
- **`"frase"`** indica frase; **`*`** permite variantes de terminações. O WoS também emprega lematização e *stemming* quando a opção *Exact Search* está desligada.
- **`NEAR/x`**, se necessário na etapa de refinamento, exige termos a uma distância máxima de `x` palavras (ex.: `credit NEAR/3 default*`). Não é necessário introduzir esse operador na primeira execução.
- Usar **Core Collection** e registrar explicitamente os índices habilitados (SCI-EXPANDED, SSCI, ESCI, CPCI etc. conforme a assinatura). A disponibilidade varia por instituição.
- **Período inicial recomendado:** 2009–2026, para cobrir literatura de *low-default portfolios* e trabalhos contemporâneos; se a amostra for demasiada, registrar uma segunda análise 2015–2026. Não descartar artigos sem verificar relevância.
- **Tipos documentais:** iniciar com *Article*, *Review Article* e, se disponíveis, *Proceedings Paper*, porque métodos de ML podem aparecer em conferências. Registrar opções exatas e não pressupor equivalência dos índices.
- **Idiomas:** inglês e português como candidatos; justificar qualquer exclusão. Não exigir Brasil/IFRS 9 em Q1–Q4.
- **Status:** resultados e contagens estão **pendentes**. As strings foram fundamentadas pela proposta e pela documentação do WoS, mas **não foram executadas na conta institucional**.

Fontes para as regras: [Clarivate — Search Rules](https://webofscience.zendesk.com/hc/en-us/articles/25350084904721-Search-Rules), [Clarivate — Topic/Search Fields](https://webofscience.zendesk.com/hc/en-us/articles/26916258216209-Web-of-Science-Core-Collection-Search-Fields), [Clarivate — Advanced Search Query Builder](https://webofscience.zendesk.com/hc/en-us/articles/20130361503249-Advanced-Search-Query-Builder).

---

## 5. Teste de sensibilidade da estratégia

**Antes de consolidar a string**, verificar se o conjunto de buscas recupera trabalhos-semente conhecidos:

| Estudo-semente | Papel | Busca em que deve ser procurado | Decisão se não recuperado |
|---|---|---|---|
| Suryanto et al. (2022), *Credit risk modeling using transfer learning and domain adaptation* | Transferência em crédito | Q1 | Verificar termos/índice; buscar título exato e ajustar vocabulário se apropriado |
| Kiefer (2009), *Default estimation for low-default portfolios* | Estimação com poucos eventos | Q2 | Buscar título exato; testar variantes de `low-default` |
| Blümke (2020), *Estimating the probability of default for no-default and low-default portfolios* | Ausência de eventos | Q2 | Verificar separação de expressões com hífen |
| Morris et al. (2019), *Using simulation studies to evaluate statistical methods* | ADEMP e planejamento Monte Carlo | Referencial, recuperação por título/citações | Não esperar inclusão em Q1–Q5: não é estudo de crédito |
| Van Calster et al. (2019), *Calibration: The Achilles heel of predictive analytics* | Conceitos de calibração | Referencial, recuperação por título/citações | Não esperar inclusão em Q4: não é estudo de crédito |

**Cuidado metodológico:** um artigo relevante pode estar ausente da Core Collection, indexado com termos diferentes ou não disponível na assinatura. Não aumentar artificialmente a sensibilidade a ponto de inviabilizar a triagem apenas para forçar a recuperação de todos os artigos.

---

## 6. Critérios iniciais de seleção

### Incluir na **síntese empírica principal**

- Estudos que investiguem predição/estimação de inadimplência, PD ou risco de crédito e que sejam relevantes a pelo menos uma dimensão da pesquisa: transferência, adaptação, escassez, calibração, simulação ou repercussão em ECL.
- Métodos descritos com informação suficiente para identificar dados, unidades de análise, avaliação e principais resultados.
- Pesquisa revisada por pares ou publicações científicas indexadas, conforme regras do protocolo. Revisões entram para mapear literatura, não como observações independentes de desempenho de modelos.

### Incluir como **suporte teórico/metodológico**, fora do conjunto de resultados empíricos de crédito

- Diretrizes de simulação, calibração, transportabilidade e elaboração de revisões, ainda que em outros domínios.
- Normativos e documentos institucionais (CPC, IASB, BCBS, BCB) para enquadramento, **não** contabilizados como estudos empíricos.

### Excluir, com razão documentada

- Trabalhos sem relação com crédito/PD ou cujas menções a ML/transferência sejam incidentais.
- Trabalhos somente sobre detecção de fraude, marketing, telecomunicações ou inadimplência de pagamentos não financeiros, sem justificativa direta para transferência metodológica.
- Trabalhos sem informações suficientes para julgar desenho e resultados, quando não houver texto completo acessível; documentar limitações de acesso.
- Registros duplicados da mesma publicação (manter versão mais completa, citando diferenças se necessárias).

**Evitar exclusões automáticas indevidas:** não exigir que o estudo use especificamente `3040`, S4/S5, Brasil, IFRS 9, instituições virtuais ou PD de 12 meses. São contextos do projeto, não requisitos universais de sua fundamentação.

---

## 7. Extração padronizada e avaliação da qualidade metodológica

### Campos propostos da matriz de extração

`id;doi;titulo;autores;ano;revista_ou_evento;base;tipo_documento;setor_pais;tipo_credito;unidade_analise;dados_publicos_ou_proprietarios;dados_sinteticos;origem_destino;dimensao_amostra;eventos_default;horizonte;estrategias_comparadas;algoritmos;heterogeneidade;tratamento_zero_eventos;validacao_temporal;controle_vazamento;calibracao;metricas_probabilisticas;metricas_discriminacao;transferencia_negativa;dgp;replicacoes_mc;erro_padrao_mc;lgd_ead_ecl;resultados_principais;limitacoes;aderencia_0a2;qualidade_metodologica;decisao;motivo_exclusao;observacoes`

### Verificação crítica sugerida (não confundir com escala validada)

- **Desenho e dados:** tipo de amostragem, generalização, dados de origem e destino efetivamente independentes e acessíveis.
- **Transferência:** diferença entre populações explicitada; tratamento de *covariate shift* versus *concept shift*; presença de *negative transfer*.
- **Métricas:** apenas AUC ou também calibração, *log-loss* e Brier? Comparadores coerentes?
- **Validação:** teste externo/temporal verdadeiro? Hiperparâmetros selecionados em treino? Risco de *data leakage*?
- **Simulação:** DGP explicitado, valores verdadeiros conhecidos, DGPs alternativos, número de replicações e erro de Monte Carlo?
- **Contabilidade:** distinção PD e ECL, horizontes e premissas de LGD/EAD/desconto? Evita inferir provisão de modelos somente preditivos?

**Pontuação de aderência (uso para priorização, não como medida de qualidade):** `0 = periférico`, `1 = parcialmente aderente`, `2 = diretamente aderente`. Avaliar separadamente **rigor metodológico** e **aderência temática**; estudo muito citado não é automaticamente mais rigoroso.

---

## 8. Passo a passo de execução no WoS

1. Abrir **Web of Science Core Collection → Advanced Search / Query Builder**.
2. Registrar a data, a instituição de acesso, o conjunto de índices habilitados, o período de cobertura e os filtros iniciais.
3. Colar **Q1** sem a marcação Markdown. Testar a sintaxe e salvar string exatamente executada.
4. Repetir **Q2–Q5**; executar **Q6** apenas como busca auxiliar e registrar seus resultados separadamente.
5. Para cada consulta, registrar `N encontrados` **sem inventar números**; exportar resultados completos com DOI e referências citadas quando permitido.
6. Eliminar duplicatas por DOI e por normalização de título/ano; registrar `N removidos`.
7. Triar títulos/resumos, depois textos completos; manter razão de exclusão e versão do processo.
8. Fazer busca reversa e prospectiva em artigos-centrais. Registrar estudos adicionados por essas vias.
9. Completar matriz de extração e avaliação crítica; separar resultados empíricos de fundamentos metodológicos.
10. Elaborar quadro de lacunas e confrontar cada alegação de novidade da v5 com evidência encontrada.
11. Produzir diagrama de fluxo de seleção inspirado em PRISMA 2020 com números reais e registrar a versão final das buscas.
12. Reexecutar uma busca de atualização próxima à redação final e registrar eventuais novos estudos.

### Modelo de log de buscas (preencher após execução)

| ID | Data e hora | Base/índices | Query exata | Período | Filtros | N bruto | N exportado | Observações |
|---|---|---|---|---|---|---|---|---|
| Q1 | Pendente | WoS Core Collection | Seção 2 | 2009–2026 candidato | A definir | — | — | Não executada |
| Q2 | Pendente | WoS Core Collection | Seção 3 | 2009–2026 candidato | A definir | — | — | Não executada |
| Q3 | Pendente | WoS Core Collection | Seção 3 | 2009–2026 candidato | A definir | — | — | Não executada |
| Q4 | Pendente | WoS Core Collection | Seção 3 | 2009–2026 candidato | A definir | — | — | Não executada |
| Q5 | Pendente | WoS Core Collection | Seção 3 | 2009–2026 candidato | A definir | — | — | Não executada |
| Q6 | Pendente | WoS Core Collection | Seção 3 | Conforme relevância | A definir | — | — | Apoio metodológico |

---

## 9. Produtos esperados da mini RSL e decisão sobre a lacuna

**Documentos resultantes:**

- `registro-buscas.md`: consultas executadas, cobertura, datas, filtros, N e alterações.
- `matriz-extracao.csv`: evidências por estudo.
- `diagrama-fluxo-prisma.md` ou imagem gerada do fluxo, com contagens reais.
- `sintese-mini-rsl.md`: mapa de métodos, dados, DGPs, resultados contraditórios e limitações.
- `tabela-lacunas.md`: argumento explícito sobre o que já é conhecido e o que o estudo acrescentará.

**Critério de passagem G1:** concluir uma das três decisões abaixo, fundamentada pela revisão:

- **Lacuna sustentada:** manter comparação de transferência por disponibilidade, heterogeneidade e DGPs com calibração/erro monetário.
- **Lacuna parcialmente coberta:** restringir contribuição a replicação metodológica transparente e/ou ao domínio brasileiro **sintético**; evitar linguagem de ineditismo.
- **Lacuna amplamente coberta:** reformular hipótese, DGP ou contribuição antes do estudo confirmatório, com registro de decisão e aprovação do orientador.

---

## 10. Referências de método e documentação de busca

- Clarivate. *Search Rules*. https://webofscience.zendesk.com/hc/en-us/articles/25350084904721-Search-Rules
- Clarivate. *Web of Science Core Collection Search Fields*. https://webofscience.zendesk.com/hc/en-us/articles/26916258216209-Web-of-Science-Core-Collection-Search-Fields
- Clarivate. *Advanced Search Query Builder*. https://webofscience.zendesk.com/hc/en-us/articles/20130361503249-Advanced-Search-Query-Builder
- Page, M. J., et al. (2021). The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. *BMJ, 372*, n71. https://doi.org/10.1136/bmj.n71
- Morris, T. P., White, I. R., & Crowther, M. J. (2019). Using simulation studies to evaluate statistical methods. *Statistics in Medicine, 38*(11), 2074–2102. https://doi.org/10.1002/sim.8086
- Kiefer, N. M. (2009). Default estimation for low-default portfolios. *Journal of Empirical Finance, 16*(1), 164–173. https://doi.org/10.1016/j.jempfin.2008.03.004
- Blümke, O. (2020). Estimating the probability of default for no-default and low-default portfolios. *Journal of the Royal Statistical Society: Series C (Applied Statistics), 69*(1), 89–107. https://doi.org/10.1111/rssc.12381
- Suryanto, H., et al. (2022). Credit risk modeling using transfer learning and domain adaptation. *Frontiers in Artificial Intelligence, 5*, 868232. https://doi.org/10.3389/frai.2022.868232

**Rigor:** nenhuma query foi executada nesta resposta contra a base WoS da universidade; nenhuma contagem, cobertura de assinatura ou taxa de recuperação está sendo alegada.
