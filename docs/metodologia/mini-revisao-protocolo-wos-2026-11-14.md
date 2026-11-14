# Mini revisão sistemática — protocolo proposto e consultas Web of Science

**Projeto:** Modelagem adaptativa de perdas esperadas de crédito com Machine Learning.  
**Base:** proposta de dissertação v3, de 13/11/2026, especialmente seções 1–4, 6–7 e 10.  
**Data deste documento:** 14/11/2026.  
**Status:** proposta de protocolo para discussão; buscas bibliográficas ainda não executadas na WoS, sem contagens, corpus selecionado ou lacuna confirmada. A sintaxe foi conferida na documentação oficial da Clarivate; sua aceitação na sessão institucional e sua capacidade de recuperar os estudos de referência ainda dependem de um piloto.

## 1. Finalidade e recorte

Recomendo uma **revisão sistematizada de escopo delimitado, com síntese narrativa crítica**, que pode ser apresentada como mini revisão sistemática desde que o método e suas simplificações sejam explícitos. “Mini” descreve o escopo e os recursos; não dispensa rastreabilidade nem permite afirmar exaustividade.

A v3 tem um resultado científico primário: qualidade de PDs obtidas por transferência/adaptação sob diferentes condições de informação local e heterogeneidade. A mensuração de ECL é o desdobramento contábil; capacidade operacional é uma dimensão secundária. A revisão deve preservar essa hierarquia.

**Pergunta principal da revisão:**

> Em carteiras de crédito com diferentes quantidades de informação local e graus de heterogeneidade entre origem e destino, em que condições a transferência, a adaptação ou o compartilhamento de informação melhoram ou deterioram a qualidade probabilística das PDs, e que evidências existem sobre suas repercussões na mensuração de ECL?

**Perguntas auxiliares:**

1. Como os estudos definem escassez: número de tomadores, contratos, defaults, meses de histórico, rótulos disponíveis ou qualidade dos dados?
2. Como medem heterogeneidade e comparam modelos locais, agrupados, transferidos e adaptados?
3. Avaliam calibração, incerteza e estabilidade temporal, além da discriminação? Identificam transferência negativa?
4. Ligam PD a perdas monetárias? Estimam ou assumem LGD/EAD, horizonte, cenários e desconto? Validam perdas realizadas ou apenas propagam premissas?
5. Que custos computacionais, requisitos de manutenção e restrições operacionais são efetivamente medidos?

Não equiparar pequeno porte/S4/S5 a escassez de dados. Não confundir instituições pequenas com tomadores pequenos: “small business lending” pode descrever a carteira de um grande credor. Desbalanceamento de classes também não demonstra, isoladamente, poucos eventos absolutos.

## 2. Estrutura da busca

Usar quatro rotas principais, reunidas por **união**:

- **Q1:** transferência, adaptação, atualização e diferenças de domínio.
- **Q2:** PD com poucos eventos ou informação limitada, incluindo métodos estatísticos tradicionais.
- **Q3:** calibração e qualidade probabilística em crédito.
- **Q4:** modelagem, validação e incerteza na mensuração de ECL.

Q5 e Q6 são rotas complementares para capacidade operacional e contexto brasileiro. Um estudo pode pertencer a várias rotas, mas deve ser contado uma vez após a deduplicação.

Não exigir simultaneamente ECL, ML, poucos dados, pequenas instituições, Brasil e transferência: conceitos relevantes frequentemente aparecem em literaturas distintas. A identificação das interseções ocorrerá na leitura e extração. “Machine learning” também não será obrigatório em Q1–Q3, preservando antecedentes de estimação, recalibração e agrupamento parcial.

**Cobertura proposta:**

- Fonte inicial: Web of Science Core Collection.
- Registrar os índices efetivamente disponíveis e selecionados; considerar SSCI, SCI-EXPANDED, ESCI e índices de anais disponíveis. Não presumir que todos integram a assinatura.
- Sem corte inicial de ano, para preservar antecedentes de PD em carteiras de baixo default. Encerramento na data real da execução; registrar a cobertura histórica oferecida pela assinatura.
- Não filtrar inicialmente por país, área temática, acesso aberto, citações ou quartil.
- Idiomas elegíveis propostos: inglês, português e espanhol; registrar eventual exclusão por idioma. Evitar filtro na interface durante o piloto.
- Literatura principal: artigos e trabalhos completos em anais. Revisões ajudam no mapeamento e no rastreamento; não contam como experimentos primários adicionais.
- Complementar com Scopus, se acessível, e literatura nacional em SciELO e BDTD, com consultas traduzidas para cada interface. As consultas abaixo são específicas da WoS.
- Registrar documentos de IFRS Foundation, BCBS e BCB/CMN como fontes conceituais/normativas, em conjunto separado. Conferir sua versão aplicável quando usados; este protocolo não reavalia o enquadramento normativo.

Se a execução se limitar à WoS e ao rastreamento de citações, declarar essa cobertura e a limitação. Não afirmar que se executou a busca em Scopus ou em fontes nacionais antes de fazê-lo.

## 3. Sintaxe conferida e configuração na WoS

Selecionar **Web of Science Core Collection → Advanced Search → Query Builder**. Colar cada consulta completa separadamente. Não colar os títulos Q1–Q6 nem inserir tudo num único campo básico de Topic. O Query Builder aceita etiquetas de campo e permite combinar os conjuntos gerados; os números reais dependem do histórico da sessão. [Documentação do Query Builder](https://webofscience.zendesk.com/hc/en-us/articles/20130361503249-Advanced-Search-Query-Builder).

- `TS=(...)` pesquisa Topic: título, resumo, palavras-chave do autor e Keywords Plus; não pesquisa o texto integral. [Etiquetas de campo da Core Collection](https://webofscience.zendesk.com/hc/en-us/articles/26916347018257-Web-of-Science-Core-Collection-Advanced-Search-Field-Tags).
- Aspas retas delimitam frases. Como elas restringem a expansão linguística, as expressões principais incluem singular/plural explícitos, como “expected credit loss” e “expected credit losses”.
- `*` admite terminações variáveis; `calibrat*` cobre, por exemplo, calibration/calibrated. Os truncamentos usados têm ao menos três caracteres antes do asterisco. Manter **Exact Search desligado** e registrar essa configuração; aspas e curingas já afetam a expansão dos respectivos termos. [Search Rules](https://webofscience.zendesk.com/hc/en-us/articles/25350084904721-Search-Rules).
- `AND` exige os blocos; `OR` reúne alternativas. `NEAR/n` procura termos próximos, sem impor a ordem da frase. Aqui, Q4 e Q5 usam proximidade em Topic. Não inserir `AND` dentro de um operando agrupado de `NEAR/n`; as alternativas internas usam `OR`. Os parênteses explicitam as relações. [Search Operators](https://webofscience.zendesk.com/hc/en-us/articles/20016122409105-Search-Operators).

Não usar `TITLE-ABS-KEY`, que pertence a outra base. Não usar ECL, PD ou ML isoladamente como termos principais, devido à ambiguidade. CECL aparece acompanhado de termos de crédito/perda/provisão; sua literatura deve ser identificada por regime contábil, sem equipará-la à IFRS 9.

**Limite da validação:** houve conferência documental de etiquetas, operadores, aspas, truncamentos e agrupamento. Não houve submissão das consultas ao mecanismo de busca autenticado, teste de indexação ou estimativa da quantidade de resultados.

## 4. Consultas prontas para colar

### Q1 — Transferência, adaptação e compartilhamento de informação

```text
TS=("credit risk" OR "credit scoring" OR "credit score" OR "credit scores" OR "probability of default" OR "probabilities of default" OR "default probability" OR "default probabilities" OR "default prediction" OR "default estimation" OR "loan default" OR "loan defaults")
AND TS=("transfer learning" OR "domain adaptation" OR "negative transfer" OR "multi task learning" OR "multitask learning" OR "partial pooling" OR "hierarchical model" OR "hierarchical models" OR "hierarchical Bayesian" OR recalibrat* OR "model updating" OR "model transfer" OR "dataset shift" OR "covariate shift" OR "domain shift" OR "distribution shift")
```

### Q2 — PD com poucos dados, poucos eventos ou pouco histórico

```text
TS=("credit risk" OR "credit scoring" OR "credit score" OR "credit scores" OR "probability of default" OR "probabilities of default" OR "default probability" OR "default probabilities" OR "default prediction" OR "default estimation" OR "loan default" OR "loan defaults")
AND TS=("low default" OR "no default" OR "zero default" OR "rare event" OR "rare events" OR "small sample" OR "small samples" OR "limited data" OR "data scarcity" OR "sparse data" OR "scarce data" OR "few shot" OR "cold start" OR "short history" OR "short histories" OR "limited history" OR "limited historical data" OR "limited labeled data" OR "limited labelled data")
```

### Q3 — Calibração e qualidade probabilística em crédito

```text
TS=("credit risk" OR "credit scoring" OR "credit score" OR "credit scores" OR "probability of default" OR "probabilities of default" OR "default probability" OR "default probabilities" OR "default prediction" OR "default estimation" OR "loan default" OR "loan defaults")
AND TS=(calibrat* OR recalibrat* OR "Brier score" OR "Brier scores" OR "log loss" OR "logloss" OR "logarithmic loss" OR "probability estimation" OR "probabilistic prediction" OR "probabilistic predictions")
```

### Q4 — Ponte entre modelos de risco e mensuração de ECL

```text
TS=("expected credit loss" OR "expected credit losses" OR "IFRS 9" OR IFRS9 OR "current expected credit loss" OR "current expected credit losses" OR (CECL NEAR/5 (credit OR loss* OR provision*)))
AND TS=("machine learning" OR "statistical learning" OR "artificial intelligence" OR "gradient boosting" OR "logistic regression" OR "probability of default" OR "probabilities of default" OR "default probability" OR "default probabilities" OR calibrat* OR validat* OR "model risk" OR "estimation uncertainty" OR "measurement uncertainty")
```

### Q5 — Busca complementar: capacidade operacional

```text
TS=("credit risk" OR "credit scoring" OR "credit score" OR "credit scores" OR "probability of default" OR "probabilities of default" OR "default probability" OR "default probabilities" OR "default prediction" OR "default estimation" OR "loan default" OR "loan defaults")
AND TS=("machine learning" OR "statistical learning" OR "gradient boosting" OR "logistic regression" OR "transfer learning")
AND TS=((computation* NEAR/3 (cost* OR budget* OR efficien* OR resource*)) OR "training time" OR "inference time" OR "memory usage" OR "resource constrained" OR "resource constraints" OR "model maintenance" OR "model governance" OR "implementation cost" OR "implementation costs")
```

### Q6 — Busca complementar: contexto brasileiro e termos em português

```text
TS=("risco de credito" OR "risco de crédito" OR "probabilidade de inadimplencia" OR "probabilidade de inadimplência" OR "perdas esperadas de credito" OR "perdas esperadas de crédito" OR "perdas de credito esperadas" OR "perdas de crédito esperadas")
OR (TS=(Brazil* OR Brasil*) AND TS=("expected credit loss" OR "expected credit losses" OR "credit risk" OR "probability of default") AND TS=("machine learning" OR "transfer learning" OR "domain adaptation" OR "IFRS 9" OR IFRS9 OR calibrat* OR "low default"))
```

**Como reunir:** executar Q1–Q4 e usar a combinação OR dos respectivos conjuntos no histórico. Exportar também as rotas separadas, preservando a informação de procedência, ou reconstruí-la antes de deduplicar. Q5/Q6 acrescentam registros elegíveis ao conjunto final; todos passam pelos mesmos critérios. Não combinar Q1 AND Q2 AND Q3 AND Q4 como corpus principal.

Q3 é deliberadamente sensível e pode recuperar validação de PD sem transferência. Q6 também pode recuperar discussões contábeis sem modelagem. A elegibilidade é decidida por conteúdo. Se houver volume excessivo no piloto, delimitar a pergunta e revisar os critérios de modo documentado, preservando versões; não selecionar apenas os primeiros resultados ou os mais citados.

## 5. Piloto e congelamento do protocolo

1. Rodar as quatro rotas principais; guardar texto exato, data/hora, coleção, índices, cobertura, filtros, Exact Search, identificador do conjunto e número retornado.
2. Inspecionar uma amostra variada de cerca de 30–50 títulos/resumos, distribuída entre as rotas. É calibração do procedimento, não a seleção final nem um limite de tamanho da revisão.
3. Testar recuperação de referências já presentes na v3: Suryanto et al. (2022) para Q1; Kiefer (2009) e Blümke (2020) para Q2. Pesquisar separadamente por DOI/título para verificar se estão indexados e cobertos pela assinatura antes de atribuir sua ausência à consulta.
4. Se um estudo elegível e indexado não aparecer, examinar seus termos e ajustar a rota correspondente. Uma recuperação bem-sucedida desses estudos é um teste de plausibilidade; não prova sensibilidade completa.
5. Registrar cada alteração e sua razão. Congelar consultas, critérios e formulário antes da triagem integral. Alterações posteriores continuam possíveis, mas devem ser identificadas e aplicadas consistentemente.
6. Exportar registros com resumo, DOI, identificador WoS e referências citadas, quando disponíveis. Conservar os arquivos brutos; deduplicar uma cópia.
7. Fazer rastreamento retrospectivo e prospectivo dos estudos incluídos e das referências metodológicas selecionadas. Registrar artigo-semente, plataforma, data e resultados. Para conter o escopo, planejar uma rodada sobre todos os incluídos após a busca inicial; novas rodadas exigem registro.
8. Atualizar a busca perto da entrega da dissertação, deduplicando com o corpus anterior.

Referências metodológicas de outros campos, como Van Calster et al. (2019), podem entrar no apoio conceitual por rastreamento dirigido. Não é esperado que uma consulta obrigatoriamente ancorada em crédito recupere um artigo de medicina.

## 6. Inclusão, exclusão e seleção

**Incluir no corpus principal** estudos empíricos ou metodológicos com avaliação em crédito/PD/ECL e contribuição para pelo menos uma das rotas: transferência/compartilhamento, escassez informacional, qualidade probabilística/calibração ou mensuração de ECL. Estudos com dados reais, simulações e demonstrações teóricas pertinentes podem entrar, mas devem ser classificados separadamente. Trabalhos conceituais que não atendam ao critério de avaliação permanecem no apoio teórico.

Não exigir ECL para incluir um estudo de PD; não exigir ML para incluir antecedentes estatísticos; não excluir um estudo pertinente apenas por apresentar somente AUC. A ausência de calibração pode ser precisamente uma limitação a documentar.

**Excluir do corpus principal:**

- Uso de “credit” ou “default” fora de risco de crédito financeiro.
- Aplicação genérica de ML a ações, fraude, marketing ou risco operacional sem relação substantiva com PD/ECL.
- Comparação de classificadores que só reporta discriminação e não aborda nenhuma das rotas substantivas.
- Estudo apenas sobre LGD/EAD, sem conexão com a contribuição da PD ou mensuração conjunta relevante ao objetivo.
- Resumo de congresso sem trabalho completo, editorial, material promocional ou apresentação sem método examinável.
- Versão redundante do mesmo estudo; vincular preprint e artigo, usando a versão mais completa pertinente.
- Idioma fora do recorte, com motivo registrado.

**Triagem:** primeiro título/resumo; depois texto completo. Na dúvida no primeiro estágio, manter para leitura. Registrar uma razão principal de exclusão no texto completo, usando uma ordem predefinida: escopo → tipo de documento/idioma → ausência de contribuição elegível → redundância.

Texto integral não localizado deve ser contabilizado como **relatório não recuperado**, após tentativas registradas, e não como evidência de baixa qualidade. Não adotar disponibilidade em acesso aberto como critério científico.

Preferir dois avaliadores independentes quando possível. Para a escala de mestrado, uma alternativa explícita é Arthur realizar a triagem e a extração, com segunda pessoa verificando todos os casos duvidosos, as exclusões em texto completo e uma amostra predefinida de 20% dos demais registros. Essa verificação é uma escolha pragmática, não uma regra PRISMA nem equivalente a dupla triagem integral. Se houver apenas um avaliador, informar a limitação.

## 7. Formulário de extração

Usar um identificador por estudo e linhas adicionais para cada experimento ou par origem–destino relevante, mantendo o vínculo. Extrair:

1. **Identificação:** autores, ano, DOI/ID, versão, rota de entrada, país e regime contábil.
2. **Contexto:** instituição, tipo de tomador/produto, dados públicos/privados/sintéticos e limites de acesso.
3. **Informação local:** tomadores e contratos distintos, eventos, prevalência, meses de histórico, dados rotulados e campos ausentes; registrar “não reportado” sem inferir.
4. **Evento e horizonte:** definição de default, PD de 12 meses ou outro horizonte, maturação dos rótulos, censura e tratamento de operações já inadimplentes.
5. **Domínios:** definição de origem/destino, diferenças entre carteiras, distância de distribuição e possíveis mudanças temporais.
6. **Métodos e comparadores:** local, pooled, origem sem adaptação, adaptado; algoritmo, regularização, recalibração, dados usados para ajustar e selecionar modelos.
7. **Validação:** separação temporal, separação por tomador, teste externo/no destino, prevenção de vazamento e orçamento de ajuste.
8. **Resultados:** log-loss/Brier; intercepto, inclinação e curva de calibração; ROC-AUC/PR-AUC; intervalos, estabilidade entre janelas e subgrupos.
9. **Transferência negativa:** comparador exato, magnitude, incerteza, cenários de piora, falhas de estimação e fallback.
10. **ECL:** fórmula, horizonte, LGD/EAD estimadas ou assumidas, cenários, desconto, recuperação, perdas realizadas comparáveis e natureza da validação.
11. **Operação:** hardware, tempo, memória, manutenção e governança; separar valores medidos de alegações.
12. **Leitura crítica:** limitações reconhecidas, limitações identificadas pelo revisor e relevância para H1, H2, H3 ou objetivo contábil.

Guardar página/seção/tabela para cada resultado relevante. Distinguir números extraídos do artigo, cálculos do revisor e interpretações. Não inferir ausência de procedimento apenas porque não foi descrito.

## 8. Avaliação crítica e síntese

Adotar uma ficha qualitativa criada para esta revisão, sem apresentá-la como instrumento validado. Para cada domínio registrar **adequado / preocupação / informação insuficiente / não aplicável**, com justificativa:

- Coerência entre evento, horizonte e uso pretendido.
- Qualidade e representatividade dos dados, incluindo eventos efetivos.
- Independência do teste e prevenção de vazamento, inclusive na adaptação.
- Comparabilidade dos modelos e recursos de ajuste.
- Calibração, incerteza e estabilidade avaliadas de modo suficiente.
- Evidência das diferenças de domínio e dos casos de deterioração.
- Sustentação da ponte entre PD e perdas monetárias.
- Reprodutibilidade e limites de generalização.

Ajustar a aplicação ao tipo de estudo: demonstrações teóricas e simulações não recebem automaticamente avaliação negativa por não usarem uma amostra institucional real. Evidência insuficiente sobre um domínio limita a conclusão correspondente.

A síntese deve seguir as perguntas, e não uma sequência de resumos de autores:

- Condições em que compartilhar informação ajuda, não ajuda ou prejudica.
- Papel separado de quantidade de dados, eventos, histórico e heterogeneidade.
- O que se sabe sobre probabilidades calibradas, além de discriminação.
- Evidências sobre ECL versus simples propagação de PD sob parâmetros fixos.
- Viabilidade operacional medida e dimensões ainda não avaliadas.
- Implicações para os quatro regimes e H1–H3 da v3.

Não combinar médias de AUC/log-loss de bases, prevalências e horizontes diferentes como efeito único. Não contar repetições sobre a mesma base pública como validações institucionais independentes. Para esta mini revisão, a síntese narrativa é o desenho inicial; eventual meta-análise dependeria de comparabilidade efetiva e protocolo adicional.

**Exemplo de por que examinar limites:** Suryanto et al. (2022) estudam transferência entre carteiras e apresentam configurações em que a adaptação reduz a AUC, inclusive ao adaptar todas as variáveis. Isso impede formular a novidade como mera identificação de que a adaptação pode falhar. É preciso verificar como a literatura avalia as condições de falha, a qualidade probabilística e a ligação com ECL. [Artigo original, seção 5.4 e tabelas 5–8](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2022.868232/full).

## 9. Registros mínimos e relatório final

Usar PRISMA 2020 como referência de relato e fluxograma e PRISMA-S para documentar as buscas. São diretrizes de transparência do relato; não certificam a qualidade da revisão nem substituem critérios e avaliação crítica. [PRISMA 2020](https://www.prisma-statement.org/prisma-2020-statement); [PRISMA-S](https://www.prisma-statement.org/prisma-search).

**Registro de busca — um por execução:**

- ID da busca e versão da consulta:
- Base, plataforma, coleção e índices:
- Cobertura temporal disponível e intervalo selecionado:
- Data/hora e fuso:
- Consulta completa e estado de Exact Search:
- Filtros e justificativas:
- Número retornado e identificador/link do conjunto:
- Arquivo exportado, intervalo/lotes e campos exportados:
- Responsável e observações:

**Registro de seleção — um por relatório:**

- ID do registro, ID do estudo, DOI/título e fontes de entrada:
- Duplicata/versão vinculada:
- Decisão em título/resumo:
- Texto recuperado e tentativas:
- Decisão em texto completo e razão principal:
- Avaliador, data e verificação:
- Localização da ficha de extração:

**Registro de mudança de protocolo:**

- Data, versão anterior/nova, decisão alterada, motivo e efeito sobre buscas/seleção.

O fluxo deve distinguir registros identificados, duplicatas removidas, registros triados, relatórios procurados/não recuperados, textos avaliados, exclusões por motivo e estudos incluídos. Relatórios distintos de um mesmo estudo não viram automaticamente estudos distintos. Separar entradas pelas bases e por rastreamento/fontes adicionais.

**Estrutura sugerida para a seção da dissertação:**

1. Objetivo, pergunta e recorte da revisão.
2. Fontes, consultas, critérios, seleção e avaliação crítica.
3. Caracterização do corpus e fluxo.
4. Síntese por informação local, heterogeneidade, calibração e ECL.
5. Limitações da evidência e da própria revisão.
6. Lacuna delimitada e consequências para o desenho empírico.

Uma formulação de lacuna a testar é: “Até que ponto os estudos avaliam conjuntamente a disponibilidade local, a heterogeneidade, a calibração fora do tempo e a propagação para ECL sob premissas comparáveis?”. Só transformar essa pergunta em afirmação depois da síntese. Ausência de resultados numa consulta não demonstra ausência de literatura.

## 10. Sequência de trabalho proposta

- **Etapa 1:** piloto, discussão do recorte, teste das referências conhecidas e congelamento.
- **Etapa 2:** buscas completas, exportação, deduplicação e triagem.
- **Etapa 3:** leitura integral, rastreamento, extração e avaliação crítica.
- **Etapa 4:** síntese, fluxograma e revisão da lacuna/H1–H3 com a orientação.

O número final de estudos deve decorrer dos critérios, sem quota arbitrária de 20 ou 30 artigos. A redução de esforço deve vir de uma pergunta delimitada e de cobertura declarada. Este documento organiza a revisão; não constitui sua execução ou uma confirmação da contribuição original.

