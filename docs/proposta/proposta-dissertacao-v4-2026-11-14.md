# Proposta de Dissertação de Mestrado — versão 4

## Transferência e recalibração de probabilidades de inadimplência entre carteiras de crédito: disponibilidade de dados, heterogeneidade e viés na mensuração de perdas esperadas em instituições financeiras brasileiras

**Autor:** Arthur. **Programa:** Mestrado em Controladoria e Contabilidade, PPGCONT/UFRGS, linha Usuários Externos.
**Data:** 14 de novembro de 2026. **Estado:** proposta para discussão com a orientação. As pendências que condicionam a qualificação estão reunidas na seção 11.

## Resumo

A provisão para perdas esperadas associadas ao risco de crédito é uma estimativa, e sua utilidade para o usuário externo depende de que a probabilidade de inadimplência (PD) empregada no cálculo seja neutra e de que sua incerteza seja conhecida. Carteiras com pouco histórico próprio podem aproveitar informação de outras carteiras, ao custo de importar viés quando as populações diferem. A pesquisa analisará como a disponibilidade de dados locais e a heterogeneidade entre carteiras de origem e de destino afetam a qualidade de PDs de 12 meses estimadas por transferência com recalibração, em comparação com modelos locais e agrupados. O desenho é preditivo e experimental sobre dados observacionais: a disponibilidade local e a distância entre origem e destino serão manipuladas por sorteio controlado, e seis regimes de estimação serão avaliados em janelas futuras do destino. A qualidade será medida por pontuação probabilística, calibração e viés monetário, este definido como o erro da PD ponderado por exposição e severidade. Um critério de adequação fixado antes do teste classificará cada combinação de disponibilidade e heterogeneidade como adequada, inadequada ou inconclusiva. A contribuição pretendida é empírica e metodológica: delimitar a fronteira de utilidade da transferência e traduzir representação fidedigna em propriedades mensuráveis da estimativa.

**Palavras-chave:** perdas esperadas de crédito; probabilidade de inadimplência; transferência de aprendizado; recalibração; calibração; representação fidedigna; viés de mensuração.

## 1. Introdução

### 1.1 Contexto

A Resolução CMN nº 4.966/2021 substituiu o reconhecimento de perdas incorridas pelo de perdas esperadas nas instituições autorizadas pelo Banco Central do Brasil (Conselho Monetário Nacional [CMN], 2021). A provisão passou a depender de estimativas prospectivas, entre as quais a PD, isto é, a probabilidade de que a operação apresente o evento de inadimplência em um horizonte definido. A estimativa só pode ser verificada depois de decorrido esse horizonte, e quem lê as demonstrações não observa o modelo que a produziu.

A Estrutura Conceitual estabelece que a informação útil representa fidedignamente o fenômeno, o que requer representação completa, neutra e livre de erro, e admite estimativas desde que sua incerteza seja explicitada (Comitê de Pronunciamentos Contábeis [CPC], 2019, itens 2.12–2.19). A literatura sobre contabilidade bancária documenta que a provisão para perdas de crédito é o principal *accrual* dos bancos e concentra a discricionariedade do preparador (Beatty & Liao, 2014). Uma PD enviesada compromete a neutralidade da provisão ainda que nenhuma escolha oportunista tenha ocorrido: o viés nasce do modelo.

O risco de viés aumenta quando a carteira dispõe de pouca informação própria. Três situações ilustram a variedade de casos: a instituição em início de operação, com histórico curto; a carteira nova dentro de uma instituição estabelecida; e a carteira especializada, numerosa, mas diferente das bases externas disponíveis. Nessas situações, estimar a PD apenas com dados locais produz estimativas instáveis, e aproveitar dados de outras carteiras reduz a instabilidade, mas pode deslocar a estimativa em direção a uma população que não é a do destino. O enquadramento prudencial não identifica esses casos: uma instituição do Segmento 5 pode dispor de histórico extenso, e uma do Segmento 3 pode abrir uma carteira sem histórico algum.

### 1.2 Problema e questão de pesquisa

O aproveitamento de informação externa em risco de crédito tem antecedentes. Suryanto *et al.* (2022) aplicam transferência de aprendizado e adaptação de domínio a modelos de crédito; Kiefer (2009) e Blümke (2020) tratam da estimação de PD em carteiras com poucos ou nenhum evento. Permanece em aberto o ponto que interessa à mensuração contábil: em que volume de dados locais e até que grau de diferença entre carteiras a informação transferida melhora a estimativa, e a partir de onde passa a prejudicá-la. A questão de pesquisa é:

> *Como a disponibilidade de dados locais e a heterogeneidade entre carteiras de origem e de destino afetam, em comparação com modelos locais e agrupados, a qualidade das probabilidades de inadimplência de 12 meses estimadas por transferência com recalibração em carteiras de crédito de instituições financeiras brasileiras?*

Qualidade designa três atributos mensuráveis, definidos na seção 6.6: pontuação probabilística, calibração e viés monetário. Disponibilidade e heterogeneidade são as variáveis independentes; a qualidade da PD é a variável dependente.

### 1.3 Justificativa

**Relevância.** A pesquisa interessa a três públicos. O usuário externo (depositantes, credores, investidores, cooperados e o supervisor) depende da provisão para avaliar o risco de crédito da instituição e não tem como auditar a PD. O preparador precisa decidir, com critério defensável, se utiliza um modelo próprio, um modelo de terceiros ou uma combinação. A instituição do Segmento 4 que pleiteia a metodologia completa deve demonstrar ao Banco Central do Brasil (BCB) a qualidade de sua metodologia de avaliação da perda esperada (Banco Central do Brasil [BCB], 2024). Para as instituições que aplicam a metodologia simplificada, a relevância depende de a regulamentação exigir estimativa própria da perda esperada além dos níveis mínimos; esse ponto está registrado como pendência normativa na seção 5.

**Inovação.** O desenho manipula experimentalmente os dois fatores de interesse. A disponibilidade local é reduzida por sorteio de tomadores, e a distância entre origem e destino é variada por subamostragem controlada da origem. A avaliação inclui uma medida monetária do erro da PD e um critério de adequação fixado antes do teste, em lugar de comparações apenas relativas entre modelos.

**Contribuição.** A contribuição é empírica e metodológica. A empírica consiste na fronteira de utilidade: o volume local a partir do qual o modelo próprio iguala o modelo transferido e recalibrado, em função da distância entre carteiras. A metodológica consiste em um protocolo que traduz neutralidade e incerteza de mensuração em propriedades verificáveis de uma PD.

**Impacto.** Os resultados oferecem ao preparador uma regra de decisão documentável, ao auditor e ao supervisor um critério de avaliação e à pesquisa contábil uma operacionalização de representação fidedigna aplicável a outras estimativas baseadas em modelos.

### 1.4 Delimitação

- **Objeto:** PD de primeiro evento em 12 meses, para operações sem o evento na data-base, em carteiras de crédito de instituições financeiras brasileiras.
- **Componente modelado:** somente a PD. A perda dado o evento (LGD) e a exposição no evento (EAD) entram como premissas comuns a todos os regimes.
- **População:** contratos das instituições que autorizarem o acesso; amostra por conveniência.
- **Fora do escopo:** modelagem de LGD e de EAD, perda esperada para a vida inteira do instrumento, alocação em estágios, avaliação de conformidade regulatória e inferência causal sobre decisões de crédito.

## 2. Objetivos

### 2.1 Objetivo geral

Analisar o efeito da disponibilidade de dados locais e da heterogeneidade entre carteiras de origem e de destino sobre a qualidade das probabilidades de inadimplência de 12 meses estimadas por transferência com recalibração, em comparação com modelos locais e agrupados, em carteiras de crédito de instituições financeiras brasileiras.

### 2.2 Objetivos específicos

1. Comparar a pontuação probabilística e a calibração dos regimes de estimação ao longo de uma malha de disponibilidade de dados locais.
2. Mensurar o efeito da heterogeneidade entre origem e destino, induzida e observada, sobre o desempenho relativo dos regimes.
3. Mensurar o viés monetário das PDs de cada regime sob premissas comuns de LGD e EAD.
4. Delimitar as combinações de disponibilidade e heterogeneidade em que cada regime satisfaz o critério de adequação.

## 3. Referencial teórico e lacuna

### 3.1 Representação fidedigna e estimativas baseadas em modelos

A teoria de base é a da qualidade da informação contábil para o usuário externo. A Estrutura Conceitual define o usuário primário como o investidor, o credor por empréstimos e os demais credores, que não podem exigir informação sob medida e dependem do relatório de propósito geral (CPC, 2019). Para esse usuário, uma estimativa é útil quando é relevante e representa fidedignamente o fenômeno. A representação fidedigna tem três atributos: completude, neutralidade e ausência de erro. A ausência de erro refere-se ao processo que produz a estimativa, e não à exatidão do valor; a incerteza de mensuração não impede a utilidade, desde que seja descrita (CPC, 2019, itens 2.18–2.19).

Esses atributos correspondem a propriedades estatísticas de uma PD. A Tabela 1 apresenta a correspondência adotada neste projeto.

**Tabela 1**
*Correspondência entre atributos da informação contábil e propriedades mensuráveis da PD*

| Atributo (CPC, 2019) | Propriedade da estimativa | Medida (seção 6.6) |
|---|---|---|
| Neutralidade | Ausência de sub ou superestimação sistemática | Intercepto de calibração; viés monetário |
| Ausência de erro no processo | Probabilidades coerentes com as frequências observadas ao longo da escala de risco | Inclinação e curva de calibração |
| Incerteza de mensuração | Precisão conhecida das estimativas | Intervalos de confiança; classificação inconclusiva |
| Verificabilidade | Reprodução por terceiro independente | Protocolo e registro de execução (seção 9) |

A correspondência delimita o alcance da pesquisa. Uma PD neutra é condição necessária, e não suficiente, para uma provisão neutra: LGD, EAD, cenários e desconto também a determinam. A literatura sobre discricionariedade na provisão bancária (Beatty & Liao, 2014) trata do viés introduzido por escolhas do preparador; este projeto trata do viés introduzido pelo modelo quando a informação é escassa, que antecede e se soma ao primeiro. As diretrizes do Comitê de Basileia sobre risco de crédito e contabilização de perdas esperadas (Basel Committee on Banking Supervision [BCBS], 2015) situam a validação de modelos nesse contexto de supervisão.

### 3.2 Dilema viés–variância e transferência entre carteiras

O erro de previsão de um modelo decompõe-se em viés (afastamento sistemático) e variância (instabilidade decorrente da amostra). Um modelo estimado apenas com os dados da carteira de destino não importa viés de outras populações, mas sua variância cresce quando a amostra diminui. Um modelo estimado em outra carteira, a origem, tem variância baixa se a origem é numerosa, e viés proporcional à diferença entre as populações. Transferência de aprendizado designa o aproveitamento do modelo da origem no destino; adaptação designa o ajuste desse modelo à população de destino.

A diferença entre populações tem três componentes, com consequências distintas. Na diferença de taxa base, a frequência do evento muda e a relação entre características e risco permanece. Na diferença de composição, muda a distribuição das características dos tomadores. Na diferença de relação condicional, a mesma característica passa a indicar risco diferente. A recalibração de intercepto e inclinação, adotada como forma de adaptação neste projeto, corrige por construção a primeira e parte da segunda, e não corrige a terceira. Denomina-se transferência negativa o caso em que o modelo transferido tem desempenho inferior ao do modelo local.

### 3.3 Calibração e avaliação de probabilidades

Discriminação é a capacidade de ordenar os tomadores por risco; calibração é a concordância entre as probabilidades estimadas e as frequências observadas. A mensuração de perdas esperadas requer a segunda: uma PD que ordena bem os tomadores e superestima o risco de todos produz provisão enviesada. Van Calster *et al.* (2019) distinguem níveis de calibração (média, fraca, moderada e forte) e mostram que modelos com boa discriminação podem apresentar calibração deficiente, em especial quando aplicados a populações diferentes daquela em que foram estimados. Riley *et al.* (2021) demonstram que a estimação precisa da inclinação de calibração é, em geral, o requisito que determina o tamanho mínimo da amostra de validação. Esses trabalhos provêm da pesquisa clínica, e sua transposição ao crédito requer adaptação quanto à dependência entre contratos do mesmo tomador e à maturação dos rótulos.

### 3.4 Antecedentes e lacuna

Os antecedentes identificados estabelecem que a transferência entre carteiras de crédito é praticável e que pode falhar: Suryanto *et al.* (2022) reportam configurações em que a adaptação reduz a discriminação. Há também métodos para estimar PD com poucos ou nenhum evento (Blümke, 2020; Kiefer, 2009). A ocorrência de falha não constitui, por si, a lacuna. A lacuna candidata tem dois pontos. O primeiro é teórico-empírico: não se conhece a fronteira entre transferência útil e transferência negativa como função conjunta do volume local e da distância entre carteiras, avaliada por calibração e não apenas por discriminação. O segundo é contábil: não se conhece a magnitude monetária do viés que cada estratégia introduz na perda esperada.

A lacuna é candidata porque a mini revisão sistemática ainda não foi executada. O [protocolo de mini revisão](../metodologia/mini-revisao-protocolo-wos-2026-11-14.md) especifica bases, consultas, critérios e formulário de extração, e o [adendo da v4](../revisao/protocolo-revisao-literatura.md) define três achados que a refutariam: (a) estudo que estime a fronteira de utilidade da transferência em crédito com avaliação de calibração; (b) estudo que quantifique o efeito monetário do erro de PD sob escassez de dados; (c) evidência de que a distância entre carteiras não se associa ao desempenho da transferência. A ocorrência de (a) ou (b) converte a pesquisa em replicação no contexto brasileiro, com contribuição declarada como tal.

## 4. Hipóteses

As hipóteses referem-se ao algoritmo principal (regressão logística regularizada) e à métrica primária de pontuação probabilística, o *log-loss*, definido na seção 6.6. Em todos os contrastes, valores negativos favorecem o primeiro regime citado. A malha de disponibilidade e os níveis de distância são os da seção 6.4.

**H1 — Disponibilidade.** A vantagem do modelo adaptado sobre o modelo local diminui com o volume de dados locais. Estimando: coeficiente de log2(n local) no contraste *log-loss*(adaptado) − *log-loss*(local); sinal esperado positivo. Fundamento: a variância do modelo local decresce com a amostra, enquanto o viés residual do modelo adaptado não decresce.

**H2 — Heterogeneidade.** A vantagem do modelo adaptado sobre o modelo local diminui com a distância entre origem e destino. Estimando: coeficiente do nível de distância induzida no mesmo contraste; sinal esperado positivo. Fundamento: a recalibração não corrige diferenças que alteram a ordenação dos tomadores.

**H3 — Atenuação pela recalibração.** A deterioração associada à distância é maior no modelo transferido sem adaptação do que no modelo adaptado. Estimando: coeficiente do nível de distância no contraste *log-loss*(transferido) − *log-loss*(adaptado); sinal esperado positivo.

**H4 — Viés monetário.** Nos dois níveis de menor disponibilidade local, o viés monetário absoluto do modelo adaptado é menor que o do modelo local. Estimando: diferença |VM(adaptado)| − |VM(local)|; sinal esperado negativo.

**C1 — Contraste pré-especificado, bilateral.** *log-loss*(adaptado) − *log-loss*(agrupado) nos dois níveis de menor disponibilidade. A teoria não sustenta expectativa direcional: o modelo agrupado aproveita toda a informação em um único ajuste, e o adaptado preserva o nível local.

De H1 e H2 deriva-se a fronteira de utilidade, n\*(d): o volume local em que o contraste entre adaptado e local se anula, para cada nível de distância d. H1 e H2 implicam que n\* diminui quando a distância aumenta. O sinal de H1 decorre da teoria da estimação; o resultado informativo é a magnitude dos coeficientes e a posição de n\* na malha. As hipóteses são contrariadas por coeficientes de sinal oposto ou por intervalos que incluam zero com precisão suficiente para excluir efeitos de magnitude relevante (seção 6.9).

**Tabela 2**
*Matriz de amarração entre objetivos, hipóteses e procedimentos*

| Objetivo específico | Hipótese ou contraste | Variável dependente | Fator | Técnica |
|---|---|---|---|---|
| 1 | H1; C1 | Diferença de *log-loss* | Volume local | Modelo de efeitos fixos por par e janela; reamostragem |
| 2 | H2; H3 | Diferença de *log-loss* | Distância induzida; distância observada (descritiva) | Idem |
| 3 | H4 | Viés monetário absoluto | Regime | Contraste pareado; reamostragem |
| 4 | — | Classificação de adequação | Volume local × distância | Critério da seção 6.6; mapa descritivo |

## 5. Enquadramento normativo

A Resolução CMN nº 4.966/2021 estabelece os critérios contábeis para instrumentos financeiros e para a provisão para perdas esperadas associadas ao risco de crédito, e a Resolução BCB nº 352/2023 dispõe sobre os procedimentos correspondentes (BCB, 2023; CMN, 2021). O art. 50 da Resolução CMN nº 4.966/2021 trata da metodologia simplificada aplicável a instituições dos Segmentos 4 e 5 e da possibilidade de autorização da metodologia completa; a Instrução Normativa BCB nº 487/2024 disciplina o pedido de autorização (BCB, 2024). O enquadramento aplicável será determinado por instituição, instrumento e data-base, conforme a [nota de verificação normativa](../normativo/notas-verificacao-normativa.md).

Três delimitações decorrem desse enquadramento. Segmento prudencial não mede disponibilidade de dados, e a pesquisa classificará as carteiras pelos dados observados. As carteiras regulatórias C1 a C5 atendem à apuração de níveis de provisão e não constituem, por definição, populações homogêneas para modelagem. A estimativa experimental, a provisão calculada pelas regras aplicáveis e a provisão registrada são grandezas distintas: a diferença entre a primeira e as demais não indica insuficiência nem excesso de provisão.

Pendência normativa a resolver antes da qualificação: confirmar, no texto vigente, em que medida a instituição sujeita à metodologia simplificada deve manter estimativa própria da perda esperada além dos níveis mínimos. A resposta delimita o público para o qual os resultados têm aplicação direta (seção 1.3).

## 6. Procedimentos metodológicos

### 6.1 Delineamento

A pesquisa é quantitativa e preditiva. Shmueli (2010) distingue a modelagem explicativa, que testa hipóteses causais sobre construtos teóricos, da modelagem preditiva, que avalia a capacidade de antecipar observações novas, e mostra que a distinção governa a escolha de dados, de validação e de métricas. O problema desta pesquisa é preditivo: pergunta-se pela qualidade de uma estimativa em observações futuras. Quanto aos procedimentos, trata-se de experimento computacional sobre dados observacionais de arquivo. Os fatores disponibilidade e distância são manipulados pelo pesquisador mediante sorteio, o que permite atribuir a eles as diferenças de desempenho dentro das carteiras estudadas. As diferenças observadas entre carteiras reais não são manipuladas e recebem tratamento descritivo.

### 6.2 Unidades e populações

A unidade de previsão é o par contrato–data-base, com identificador pseudonimizado do tomador para controle de dependência. A unidade de comparação é a célula formada por par origem–destino, janela temporal, nível de disponibilidade e nível de distância. Carteira analítica é o conjunto de contratos de mesma modalidade, perfil de tomador e política de crédito, delimitado com dados de desenvolvimento. Origem é a carteira ou o conjunto de carteiras que fornece o modelo transferido; destino é a carteira em que o desempenho futuro é avaliado. Os dados de teste do destino não participam de treino, escolha da origem, recalibração ou seleção de hiperparâmetros.

### 6.3 Evento e horizonte

O evento é a primeira ocorrência de atraso superior a 90 dias em até 12 meses após a data-base, entre contratos sem atraso superior a 90 dias na data-base. Trata-se de uma aproximação da definição regulatória de ativo com problema de recuperação de crédito, que abrange outros indicativos; por isso o termo adotado no texto é evento de inadimplência, e não ativo problemático. Havendo registro confiável da caracterização regulatória, uma segunda definição será avaliada em análise separada.

Contratos com acompanhamento inferior a 12 meses serão tratados como censurados e não como não eventos. Liquidação antecipada, cessão, baixa, renegociação e cura terão regras fixadas no [dicionário de dados](../../data_dictionary/README.md) antes da abertura do teste.

### 6.4 Fatores experimentais

**Disponibilidade de dados locais.** O conjunto de desenvolvimento do destino será reduzido por sorteio de tomadores, sem seleção por classe, em malha candidata de 5%, 10%, 20%, 40%, 70% e 100%, com 20 repetições por nível. O conjunto de teste permanece idêntico em todos os níveis. Cada sorteio será descrito por número de tomadores, contratos, eventos e meses de histórico. A variável n local é o número de tomadores distintos no desenvolvimento.

**Heterogeneidade induzida.** A distância entre origem e destino será variada por subamostragem da origem. Um classificador de domínio, estimado com dados de desenvolvimento, fornece para cada contrato da origem a probabilidade de pertencer ao destino. A origem será reamostrada com probabilidades de inclusão crescentes ou decrescentes nessa probabilidade, em cinco níveis candidatos, de modo a aproximá-la ou afastá-la do destino. O tamanho da origem será mantido constante entre níveis, para que distância e volume não se confundam. O procedimento altera a composição das características e não altera a relação entre características e risco.

**Heterogeneidade observada.** Cada par origem–destino será descrito por três medidas, calculadas com dados de desenvolvimento e rótulos maturados: (a) diferença de taxa base, em escala logito; (b) separabilidade, medida pela área sob a curva ROC do classificador de domínio em validação cruzada, complementada pela média das distâncias de Wasserstein (variáveis numéricas) e de variação total (variáveis categóricas); (c) desajuste condicional, medido pelo excesso de *log-loss* do modelo da origem no desenvolvimento do destino após a correção do intercepto. A medida (c) capta a diferença de relação condicional que as medidas de composição não identificam.

### 6.5 Regimes de estimação

1. **Taxa base:** PD constante igual à frequência do evento no desenvolvimento do destino. Referência ingênua.
2. **Local:** modelo estimado apenas com o desenvolvimento do destino.
3. **Local reduzido:** modelo local restrito a um conjunto pequeno e pré-especificado de variáveis. Controla o efeito de estimar menos parâmetros.
4. **Agrupado:** modelo único estimado com origem e desenvolvimento do destino.
5. **Transferido:** modelo estimado apenas na origem e aplicado ao destino sem ajuste.
6. **Adaptado:** modelo da origem recalibrado com o desenvolvimento do destino: logit(p adaptado) = a + b × logit(p origem), com penalização que mantém (a, b) próximos de (0, 1) quando os dados locais não sustentam afastamento. A intensidade da penalização será escolhida em validação interna.

O algoritmo principal é a regressão logística regularizada, por ser auditável e por exigir poucas decisões de ajuste. O *gradient boosting* em árvores será aplicado aos regimes 2, 4, 5 e 6 como análise de robustez, com orçamento de ajuste equivalente, e não integra a família confirmatória. Quando o desenvolvimento do destino não contiver as duas classes, os regimes 2, 3 e 6 serão registrados como não estimáveis, e a frequência dessas ocorrências será reportada por célula.

### 6.6 Medidas de qualidade e critério de adequação

**Pontuação probabilística.** O *log-loss* é a média do logaritmo negativo da probabilidade atribuída ao resultado observado. É uma regra de pontuação própria: seu valor esperado é mínimo quando a probabilidade estimada coincide com a verdadeira. Constitui a métrica primária das hipóteses H1 a H3 e de C1. O escore de Brier será reportado como complemento.

**Calibração.** O intercepto de calibração é o deslocamento, em escala logito, entre as probabilidades estimadas e as frequências observadas, com inclinação fixada em 1; valor zero indica ausência de sub ou superestimação média. A inclinação de calibração é o coeficiente de logit(p) na regressão logística do evento observado; valor 1 indica que as probabilidades não são extremas demais nem comprimidas demais. Curvas de calibração com intervalos complementam as duas medidas.

**Viés monetário.** VM = Σ (PD − y) × LGD × EAD / Σ EAD, em pontos-base da exposição, em que y indica a ocorrência do evento no horizonte e LGD e EAD são comuns a todos os regimes. A medida compara a perda esperada estimada com a perda que decorreria dos eventos observados sob a mesma premissa de severidade. Difere do intercepto de calibração por ponderar o erro pela exposição: um modelo calibrado em número de contratos pode errar nos contratos de maior valor.

**Discriminação.** A área sob a curva ROC será reportada como medida descritiva.

**Critério de adequação.** Uma PD será classificada como adequada em uma célula quando, no teste, os três requisitos forem atendidos: (i) o intervalo de 95% do intercepto de calibração estiver contido em ±δa; (ii) o intervalo de 95% da inclinação estiver contido em [1 − δb, 1 + δb]; (iii) o limite superior do intervalo de 95% da diferença de *log-loss* em relação à taxa base for negativo. Será classificada como inadequada quando algum intervalo estiver inteiramente fora da faixa correspondente, e como inconclusiva nos demais casos. Os valores candidatos são δa = 0,2 e δb = 0,2; os valores definitivos serão justificados com a literatura de validação e fixados antes da abertura do teste. O critério exige que o intervalo esteja contido na faixa, e não apenas que inclua o valor ideal, para que estimativas imprecisas não sejam aprovadas por falta de evidência em contrário.

### 6.7 Informação prospectiva

Um conjunto parcimonioso de variáveis macroeconômicas, comum a todos os regimes, será incluído com a versão disponível em cada data-base. Para expectativas de mercado, será recuperada a observação histórica vigente na data, e não a série revisada. Uma análise sem variáveis macroeconômicas avaliará a sensibilidade dos resultados.

### 6.8 Validação temporal

As janelas de teste serão formadas por datas-base posteriores ao desenvolvimento, com os 12 meses seguintes integralmente observados. No desenvolvimento, a seleção de hiperparâmetros e de penalização será feita por validação cronológica aninhada, com intervalo de exclusão de 12 meses entre treino e validação para impedir sobreposição de horizontes. Imputação, seleção de variáveis e recalibração serão ajustadas dentro de cada janela de treino. Tomadores presentes na origem e no destino serão atribuídos a um único domínio.

### 6.9 Inferência

A inferência confirmatória é condicional às carteiras estudadas. Os contrastes de H1 a H3 serão estimados por modelo linear da diferença de *log-loss* por célula, com efeitos fixos por par origem–destino e janela, e com log2(n local) e nível de distância como regressores. A incerteza será obtida por reamostragem que combina os sorteios de desenvolvimento com *bootstrap* de tomadores do teste em blocos temporais. H4 e C1 serão estimados por contraste pareado com a mesma reamostragem. Os cinco testes formam uma família, com intervalos de 95% e ajuste de Holm.

A opção por efeitos fixos responde ao número de carteiras disponíveis. Com poucas instituições, não há base para inferir sobre a população de carteiras brasileiras, e repetições de sorteio não criam carteiras independentes. A associação entre heterogeneidade observada e desempenho será reportada de forma descritiva; passará a ser testada, com reamostragem por destino, se o número de destinos independentes atingir o mínimo fixado no protocolo antes do teste. A generalização para outras carteiras será argumentada com base na descrição das carteiras estudadas, e não inferida estatisticamente.

Efeito nulo só será afirmado quando o intervalo estiver contido em margem de irrelevância fixada antes do teste; ausência de significância não será interpretada como equivalência. Os modelos lineares dos contrastes terão resíduos examinados quanto a não linearidade em log2(n), e a especificação alternativa por níveis categóricos será reportada.

### 6.10 Precisão e tamanho da amostra

A precisão-alvo é uma meia-largura de 0,2 para o intervalo de 95% da inclinação de calibração no teste de cada célula, valor compatível com a faixa do critério de adequação. O número de eventos necessário será calculado pelo procedimento de Riley *et al.* (2021) e por simulação com dados de desenvolvimento. Carteiras cujo teste não atinja a precisão-alvo serão mantidas e classificadas como inconclusivas, sem exclusão. A malha de disponibilidade será ajustada, antes do teste, para que os níveis inferiores contenham eventos suficientes para estimar o regime local em parcela relevante dos sorteios.

### 6.11 Validade

**Interna.** As ameaças principais são o vazamento de informação do teste, controlado pela separação temporal e pelo registro prévio das decisões, e a multiplicidade de análises, controlada pela família confirmatória fechada e pela identificação das demais análises como exploratórias.

**De construto.** A disponibilidade manipulada por sorteio reproduz a redução de volume e não reproduz as demais condições de uma instituição com poucos dados, como política de crédito recente, sistemas menos maduros e campos de qualidade inferior. Uma análise com janelas históricas curtas aproximará a condição de início de operação. A distância induzida reproduz a diferença de composição e não a diferença de relação condicional, que só é observada entre carteiras reais.

**Externa.** A amostra é de conveniência. Os resultados descrevem as carteiras estudadas, e sua extensão a outras instituições depende da semelhança de modalidades, políticas e período.

## 7. Do viés da PD à perda esperada

O viés monetário (seção 6.6) é a medida principal do desdobramento contábil. Ele utiliza o resultado observado no teste e, por isso, constitui evidência sobre o erro de mensuração do componente de PD, sob a premissa de severidade adotada. A LGD e a EAD comuns serão documentadas quanto à origem: estimadas com dados da instituição, obtidas de fonte externa ou arbitradas em faixas de sensibilidade.

A grandeza LP12 = PD12 × LGD × EAD será reportada por regime como aproximação da perda esperada associada a eventos em 12 meses. A interpretação como perda esperada de 12 meses, no sentido da IFRS 9 (International Accounting Standards Board [IASB], 2014), requer que a LGD reflita as perdas de fluxos ao longo de toda a recuperação, com desconto coerente; na ausência dessa sustentação, LP12 permanecerá identificada como aproximação. A diferença de LP12 entre regimes é propagação aritmética das PDs e será apresentada como análise de sensibilidade, sem valor de evidência sobre qual regime mede melhor.

O limiar de materialidade para o viés monetário será fixado com a orientação antes do teste, em pontos-base da exposição e, havendo acesso, em proporção da provisão registrada da carteira. A comparação com níveis regulatórios de provisão depende de classificação por ativo, garantias e regras vigentes em cada data-base, e só será realizada se esses dados estiverem disponíveis.

## 8. Dados e cenários

A pesquisa requer microdados de contratos com histórico de atraso. Dados públicos agregados não contêm os rótulos e atributos necessários. O acesso ainda não está confirmado, e três cenários delimitam o alcance das conclusões.

- **Cenário A — várias instituições.** Transferência entre instituições. Conclusões restritas às instituições participantes.
- **Cenário B — uma instituição, várias carteiras.** Transferência entre carteiras internas. O desenho da seção 6 é integralmente executável, pois a inferência é condicional às carteiras e os fatores são induzidos.
- **Cenário C — base pública ou estrangeira.** Demonstração do método. O título e as conclusões serão revistos para excluir a referência a instituições brasileiras, e o desdobramento contábil ficará limitado ao viés monetário sob premissas arbitradas.

Um estudo-piloto em base pública de contratos será executado nos três primeiros meses, em qualquer cenário, para validar o código e calibrar a malha e a precisão-alvo. Seus resultados não integrarão as conclusões. A decisão entre os cenários será registrada até o terceiro mês.

## 9. Reprodutibilidade, governança e ética

O [protocolo experimental](../metodologia/protocolo-experimental-v4.md) especifica as decisões a registrar antes da abertura do teste: versão dos dados, definições de evento, cortes temporais, malha, níveis de distância, faixas do critério de adequação, margem de irrelevância e plano de análise. Alterações posteriores serão registradas como emendas datadas. Código, configuração, sementes e versões de bibliotecas serão versionados; o código será desenvolvido em Python, com os pacotes identificados no repositório.

Dados identificáveis não serão versionados nem enviados a serviços externos. A pseudonimização de identificadores não equivale a anonimização, e o risco de reidentificação será avaliado. Termos de cessão, base legal, sigilo, prazo de retenção e necessidade de apreciação por comitê de ética serão definidos com as instituições e com o programa antes do acesso.

## 10. Entregas e cronograma

**Entregas:** mini revisão sistemática da literatura; protocolo e dicionário de dados fixados; comparação reprodutível dos regimes; fronteira de utilidade e mapa de adequação; análise do viés monetário; relatório de limitações.

**Tabela 3**
*Cronograma indicativo, em meses a contar do início formal*

| Meses | Atividade |
|---|---|
| 1–3 | Mini revisão sistemática; negociação de acesso; estudo-piloto em base pública; decisão de cenário |
| 3–4 | Diagnóstico dos dados; fixação do protocolo |
| 4–6 | Regimes de referência e validação temporal |
| 6–8 | Transferência, adaptação e fatores experimentais |
| 8–9 | Viés monetário e análises de sensibilidade |
| 9–10 | Inferência e robustez |
| 10–12 | Redação e revisão |

## 11. Limitações e pendências

Quatro pendências condicionam a qualificação e não são resolvidas por este documento.

1. **Acesso a dados.** Não há microdados confirmados. Sem acesso a dados brasileiros até o terceiro mês, aplica-se o cenário C, com revisão do título.
2. **Lacuna.** A mini revisão sistemática não foi executada. A lacuna da seção 3.4 é candidata e pode ser refutada pelos achados ali especificados.
3. **Parâmetros do critério.** As faixas de adequação, a margem de irrelevância e o limiar de materialidade são candidatos e dependem de justificação na literatura e de decisão com a orientação.
4. **Base normativa.** A extensão da exigência de estimativa própria sob a metodologia simplificada e a vigência de cada dispositivo nas datas-base precisam de conferência no texto oficial.

As limitações do desenho são as da seção 6.11: amostra de conveniência, escassez e distância induzidas que reproduzem apenas parte das condições reais, e desdobramento contábil restrito ao componente de PD.

## Referências

Banco Central do Brasil. (2023). *Resolução BCB nº 352, de 23 de novembro de 2023*. https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?numero=352&tipo=Resolu%C3%A7%C3%A3o+BCB

Banco Central do Brasil. (2024). *Instrução Normativa BCB nº 487, de 5 de julho de 2024*. https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?numero=487&tipo=Instru%C3%A7%C3%A3o+Normativa+BCB

Basel Committee on Banking Supervision. (2015). *Guidance on credit risk and accounting for expected credit losses*. Bank for International Settlements. https://www.bis.org/bcbs/publ/d350.htm

Beatty, A., & Liao, S. (2014). Financial accounting in the banking industry: A review of the empirical literature. *Journal of Accounting and Economics, 58*(2–3), 339–383. https://doi.org/10.1016/j.jacceco.2014.08.009

Blümke, O. (2020). Estimating the probability of default for no-default and low-default portfolios. *Journal of the Royal Statistical Society: Series C (Applied Statistics), 69*(1), 89–107. https://doi.org/10.1111/rssc.12381

Comitê de Pronunciamentos Contábeis. (2019). *Pronunciamento Técnico CPC 00 (R2): Estrutura conceitual para relatório financeiro*. http://static.cpc.aatb.com.br/Documentos/573_CPC00(R2).pdf

Conselho Monetário Nacional. (2021). *Resolução CMN nº 4.966, de 25 de novembro de 2021*. https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?numero=4966&tipo=RESOLU%C3%87%C3%83O+CMN

International Accounting Standards Board. (2014). *IFRS 9 Financial Instruments*. IFRS Foundation. https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/

Kiefer, N. M. (2009). Default estimation for low-default portfolios. *Journal of Empirical Finance, 16*(1), 164–173. https://doi.org/10.1016/j.jempfin.2008.03.004

Riley, R. D., Debray, T. P. A., Collins, G. S., Archer, L., Ensor, J., van Smeden, M., & Snell, K. I. E. (2021). Minimum sample size for external validation of a clinical prediction model with a binary outcome. *Statistics in Medicine, 40*(19), 4230–4251. https://doi.org/10.1002/sim.9025

Shmueli, G. (2010). To explain or to predict? *Statistical Science, 25*(3), 289–310. https://doi.org/10.1214/10-STS330

Suryanto, H., Mahidadia, A., Bain, M., Guan, C., & Guan, A. (2022). Credit risk modeling using transfer learning and domain adaptation. *Frontiers in Artificial Intelligence, 5*, Article 868232. https://doi.org/10.3389/frai.2022.868232

Van Calster, B., McLernon, D. J., van Smeden, M., Wynants, L., & Steyerberg, E. W. (2019). Calibration: The Achilles heel of predictive analytics. *BMC Medicine, 17*, Article 230. https://doi.org/10.1186/s12916-019-1466-7
