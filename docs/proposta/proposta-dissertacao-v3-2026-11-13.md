# Proposta de Dissertação de Mestrado — versão 3

## Modelagem adaptativa de perdas esperadas de crédito com Machine Learning: disponibilidade de dados e heterogeneidade entre carteiras de instituições financeiras brasileiras

**Autor:** Arthur. **Programa:** Mestrado em Controladoria e Contabilidade, PPGCONT/UFRGS, linha Usuários Externos.  
**Data:** 13 de novembro de 2026. **Status:** proposta para discussão com a orientação; sem resultados empíricos e sem acesso a microdados confirmado.  
**Versão corrente:** esta versão substitui a v2 como proposta de trabalho. As versões anteriores e o parecer permanecem intactos como referências históricas. As hipóteses e os parâmetros ainda não constituem um protocolo pré-registrado.

## Resumo

A confiabilidade da mensuração de perdas esperadas de crédito (ECL) depende de estimativas de risco representativas das carteiras às quais são aplicadas. Instituições financeiras diferem quanto à extensão do histórico, ao número de eventos de inadimplência, à qualidade das informações e às características de seus tomadores e produtos. Essas dimensões não decorrem automaticamente do enquadramento prudencial em S4 ou S5. A pesquisa investigará em quais condições estratégias adaptativas de Machine Learning, que transferem informações entre carteiras e ajustam as estimativas à população de destino, produzem probabilidades de inadimplência (PD) confiáveis, e quais são as repercussões dessas diferenças na mensuração de ECL. Serão comparados modelos locais, agrupados, transferidos sem adaptação e adaptados, utilizando regressão logística regularizada e gradient boosting. O desenho combinará variação controlada da disponibilidade de dados locais com diferenças observadas entre carteiras, validação temporal e avaliação explícita de transferência negativa. A qualidade das PDs será examinada por regras de pontuação probabilística, calibração, discriminação, estabilidade e incerteza. As repercussões na ECL serão calculadas sob premissas comuns e documentadas de recuperação, exposição, cenários e desconto, separando sensibilidade modelada de validação de perdas monetárias. A contribuição pretendida é identificar condições de utilidade e limites da adaptação entre carteiras. O protótipo reprodutível será instrumento da pesquisa; uma solução comercial constitui desenvolvimento posterior.

**Palavras-chave:** perdas esperadas de crédito; Machine Learning; probabilidade de inadimplência; transferência de aprendizado; adaptação de domínio; heterogeneidade; calibração.

## 1. Introdução, problema e delimitação

### 1.1 Contexto e motivação

A mensuração contábil de ECL exige considerar a possibilidade de inadimplência e suas consequências econômicas, com informações disponíveis na data da avaliação. A Resolução CMN nº 4.966/2021 e os procedimentos complementares do BCB compõem o contexto brasileiro; o enquadramento aplicável precisa ser determinado para cada instituição, instrumento e data. O interesse contábil deste projeto reside na confiabilidade e na incerteza dessa mensuração, não apenas no ordenamento dos tomadores por risco.

Três situações motivam a investigação: uma instituição em início de operação pode ter pouco histórico próprio; uma instituição estabelecida pode dispor de muitos dados e de recursos limitados para modelagem; uma carteira especializada pode apresentar grande volume de dados, mas pouca semelhança com as bases externas disponíveis. São situações possíveis, não caracterizações empíricas comprovadas da população S4/S5. Volume de dados, capacidade operacional e especialização serão tratados separadamente.

Modelos locais dependem da informação disponível na própria carteira. O aproveitamento de dados de outras carteiras pode reduzir a variabilidade das estimativas, mas também introduzir viés se os mecanismos de risco diferirem. Suryanto et al. (2022) já estudam transferência e adaptação em risco de crédito; portanto, o uso dessas técnicas não será apresentado como novidade por si só. Kiefer (2009) e Blümke (2020) oferecem antecedentes para estimação de PD quando há poucos ou nenhum evento. A lacuna específica proposta na seção 4 permanece sujeita à revisão da literatura.

### 1.2 Problema de pesquisa

A disponibilidade de informações próprias e a heterogeneidade entre carteiras condicionam a confiabilidade de modelos de risco de crédito. Informações externas podem ser úteis quando o histórico local é limitado, mas também podem produzir estimativas inadequadas quando a população de origem difere da população de destino. O problema científico consiste em identificar as condições sob as quais a transferência e a adaptação de conhecimento estatístico entre carteiras permitem estimar PDs confiáveis para subsidiar a mensuração de perdas esperadas de crédito.

### 1.3 Questão de pesquisa

> Em que condições de disponibilidade de dados locais e heterogeneidade entre carteiras estratégias adaptativas de Machine Learning produzem estimativas confiáveis de probabilidade de inadimplência, e como essas estimativas se refletem na mensuração de perdas esperadas de crédito em instituições financeiras brasileiras?

A primeira parte é o resultado científico primário; a segunda é seu desdobramento contábil, sob parâmetros explicitados. A avaliação regulatória é uma aplicação condicionada à comparabilidade, e a viabilidade operacional é uma dimensão secundária. Não se formulam problemas independentes sobre construção de plataforma, otimização de orçamento ou reforma dos pisos regulatórios.

### 1.4 Escopo

- **Objeto:** transferência e adaptação entre carteiras analíticas de crédito, inclusive entre instituições se os dados permitirem; a PD é o componente modelado por ML.
- **Contexto institucional:** instituições financeiras brasileiras, com interesse aplicado em S4/S5, sem presumir poucos dados, baixa capacidade ou metodologia contábil uniforme. O segmento não é critério estatístico para classificar escassez.
- **População observada:** contratos elegíveis das instituições que autorizarem acesso; amostra por conveniência, sem representatividade nacional presumida.
- **Horizonte principal:** PD de primeiro evento nos 12 meses seguintes à data-base, para operações sem o evento na origem da previsão. Uma extensão multiperíodo depende de dados e redefinição documentada do protocolo.
- **ECL:** repercussões de mudanças na PD sob LGD, EAD e demais premissas comuns; inferência sobre perdas efetivas depende de recuperações e acompanhamento suficientes.
- **Fora do núcleo:** modelar simultaneamente LGD e EAD por ML, aprendizado federado em produção, plataforma comercial, certificação de conformidade e demonstração causal de efeitos sobre crédito ou resultado contábil.

## 2. Objetivos

### 2.1 Objetivo geral

Avaliar em que condições de disponibilidade de dados locais e heterogeneidade entre carteiras estratégias adaptativas de Machine Learning produzem PDs confiáveis e analisar as repercussões dessas estimativas na mensuração de ECL em instituições financeiras brasileiras.

### 2.2 Objetivos específicos

1. Comparar a qualidade probabilística e a calibração de modelos locais, agrupados, transferidos sem adaptação e adaptados, em diferentes regimes de informação local.
2. Identificar a associação entre heterogeneidade de origem–destino e ganhos ou perdas de desempenho, inclusive transferência negativa e limites da adaptação.
3. Avaliar como a disponibilidade de informação local condiciona a utilidade da adaptação, sua estabilidade temporal e a incerteza das estimativas.
4. Quantificar a propagação das diferenças de PD para a ECL sob premissas controladas, incluindo comparações contábeis e regulatórias somente quando houver dados e horizontes compatíveis.

A revisão da literatura, a construção dos dados e a implementação são procedimentos. Tempo de execução, memória e esforço de manutenção serão descritos como viabilidade secundária, sem promessa de mensurar custo total de adoção.

## 3. Hipóteses e correspondência com o método

As hipóteses são expectativas testáveis, não resultados. Os regimes de informação e heterogeneidade serão definidos apenas com dados de desenvolvimento, antes da abertura do teste final. As mesmas identificações H1–H3 são usadas na configuração e no protocolo.

**H1 — Informação compartilhável.** Nos regimes previamente definidos de menor disponibilidade local e maior compatibilidade origem–destino, a adaptação por recalibração regularizada apresenta menor log-loss no destino do que o treinamento exclusivamente local. Fundamento: o compartilhamento pode reduzir variância quando a informação externa é pertinente. Contraste primário: log-loss(adaptado) − log-loss(local), esperado negativo. Local não estimável é registrado como inviável, não recebe erro artificial nem conta como vitória da adaptação.

**H2 — Heterogeneidade e transferência negativa.** O aumento da distância de distribuição entre origem e destino associa-se a pior desempenho relativo da transferência sem adaptação, comparada ao modelo local, após considerar a disponibilidade local. Contraste primário: coeficiente da distância na diferença log-loss(transferido) − log-loss(local), esperado positivo. Serão divulgadas a magnitude, a incerteza e a proporção de pares com deterioração. Distância entre covariáveis não identifica, sozinha, mudança da relação entre covariáveis e inadimplência.

**H3 — Informação para adaptação.** Na faixa de informação local previamente definida, o ganho do modelo adaptado em relação à transferência sem adaptação aumenta com a quantidade de tomadores locais utilizáveis. Contraste primário: coeficiente de log2(1 + n local), sendo n local o número de tomadores distintos, na diferença log-loss(adaptado) − log-loss(transferido), esperado negativo. O número de eventos e a profundidade temporal serão reportados para caracterizar essa informação. Saturação, ausência de ganho ou piora contradizem a expectativa na faixa examinada; não será alegada monotonicidade universal.

O log-loss é uma regra de pontuação da qualidade probabilística, não uma medida pura de calibração. Intercepto e inclinação de calibração, curvas de confiabilidade e Brier score complementam obrigatoriamente sua interpretação. Melhor log-loss com calibração inadequada não será descrito como PD plenamente validada.

**Encadeamento:** objetivo 1 → H1 → contrastes pareados no destino; objetivo 2 → H2 → análise de distância e transferência negativa; objetivo 3 → H3 → curvas de aprendizagem, estabilidade e incerteza; objetivo 4 → análise contábil derivada, sem hipótese de superioridade nem de insuficiência dos pisos. A viabilidade operacional não cria uma quarta hipótese. As H1–H5 da v2 pertencem ao histórico e não conservam sua numeração ou significado nesta versão.

## 4. Fundamentação e lacuna a verificar

### 4.1 Qualidade da mensuração contábil

A ponte contábil será a representação fidedigna de estimativas, a relevância da informação e a explicitação da incerteza de mensuração. Uma PD bem calibrada é necessária para algumas decomposições de ECL, mas não comprova a qualidade integral da provisão: recuperação, exposição, horizonte, cenários e desconto também importam. Diretrizes de validação e documentação de ECL do Comitê de Basileia ajudam a organizar essa ponte (BCBS, 2015), sem substituir normas brasileiras nem servir como certificação do protótipo.

### 4.2 Aprendizado estatístico, transferência e agrupamento parcial

O dilema viés–variância orienta a comparação entre estimativas locais e compartilhadas. A recalibração regularizada compartilha informação enquanto permite ajuste local de nível e inclinação. Isso não assegura dominância sobre modelos locais ou agrupados em toda distribuição. Transfer learning designa o aproveitamento de conhecimento da origem; domain adaptation enfatiza ajustes às diferenças de domínio. O projeto usará uma implementação simples e auditável antes de ampliar a família de métodos. Modelos hierárquicos bayesianos constituem extensão possível; uma média ponderada heurística não será descrita como inferência bayesiana.

### 4.3 Calibração e incerteza

Discriminação e calibração respondem a perguntas distintas. Van Calster et al. (2019) fornecem referência metodológica sobre calibração, cuja aplicação ao crédito exige adaptação. Intervalos de incerteza, curvas por carteira e períodos sucessivos serão necessários para evitar que o desempenho médio oculte deterioração local. Ausência de eventos não significa PD zero; tampouco permite confirmar calibração individual sem informação adicional e acompanhamento futuro.

### 4.4 Lacuna provisória

Investigar as condições de transferência positiva e negativa, considerando conjuntamente disponibilidade local, heterogeneidade, calibração e repercussões monetárias, pode produzir evidência útil no contexto brasileiro. Essa é uma hipótese de lacuna, não uma afirmação de inexistência de estudos. A revisão deve verificar o que já se sabe sobre cada relação e quais limitações de avaliação permanecem, em vez de reivindicar originalidade apenas por combinar ML, ECL e S4/S5.

## 5. Enquadramento normativo e limites de interpretação

A [nota normativa corrente](../normativo/notas-verificacao-normativa.md) registra fontes, dispositivos, correções da v2 e pendências. A Resolução CMN nº 4.966/2021, art. 50, disciplina a metodologia simplificada para S4/S5 no âmbito aplicável, com autorização para metodologia completa em hipóteses previstas e exceções relativas a sistemas cooperativos. O enquadramento deve ser conferido por instituição; segmento prudencial não mede quantidade de dados.

A Resolução BCB nº 352/2023 inclui procedimentos para instituições financeiras em seu art. 1º, II. Os arts. 76–81 tratam de níveis de provisão e carteiras; a 309/2023 foi revogada. Sua exclusão generalizada da v2 estava incorreta. O experimento separará provisão calculada pelas regras aplicáveis, provisão efetivamente registrada e ECL experimental. As categorias regulatórias C1–C5 não são automaticamente grupos homogêneos para modelagem.

Uma diferença positiva entre ECL experimental e referência regulatória não comprova insuficiência contábil nem determina lançamento. Uma diferença negativa tampouco autoriza redução de provisão. As conclusões dependem de escopo, qualidade dos parâmetros, horizontes e regras vigentes na data-base. A dissertação não homologa uma metodologia nem substitui validação independente. Não se equipara a metodologia simplificada brasileira à abordagem simplificada de recebíveis da IFRS 9.

## 6. Desenho empírico

### 6.1 Natureza, unidade e domínios

Pesquisa quantitativa de finalidade preditiva e avaliativa, com experimentos computacionais sobre dados observacionais e simulações de sensibilidade. A unidade de previsão será contrato–data-base, com identificação pseudonimizada de tomador para controle de dependência. A unidade de comparação será par origem–destino × janela temporal × regime de informação. Repetições de amostragem não criam novas instituições independentes.

Uma carteira analítica será delimitada por modalidade, perfil e política de crédito, com regras definidas no desenvolvimento. A origem reúne carteiras elegíveis; o destino é a população em que se avalia o desempenho futuro. O teste do destino não entra em treino, escolha da origem, adaptação, calibração nem seleção de hiperparâmetros. O compartilhamento pressupõe compatibilidade de definições e autorização de uso, não livre intercâmbio de dados.

### 6.2 Evento e horizonte

O candidato operacional principal é a primeira ocorrência de atraso superior a 90 dias em até 12 meses após a data-base, entre contratos sem esse evento na base. Ele será denominado **proxy de inadimplência** quando não cobrir os demais critérios de ativo problemático. Se houver classificação confiável de ativo com problema de recuperação, será construída e avaliada uma definição alternativa separada, com regras e datas documentadas; não se usa uma união ambígua dos dois rótulos.

Contrato com acompanhamento menor que o horizonte não será classificado automaticamente como não inadimplente. Liquidação, cessão, baixa, renegociação, cura, default recorrente e riscos competitivos terão regras específicas no dicionário. Operações já problemáticas exigem tratamento de recuperação separado; o classificador de primeiro evento não responde pela perda de toda a carteira.

### 6.3 Disponibilidade de dados e heterogeneidade

Disponibilidade será descrita por contratos e tomadores distintos, eventos e não eventos, meses de histórico, maturação dos rótulos e qualidade/completude dos campos. O desenho principal reduzirá aleatoriamente unidades de tomador do desenvolvimento do destino, usando frações preliminares de 10%, 40% e 100%, sem selecionar apenas defaults. As frações e a malha final serão fixadas após diagnóstico, antes do teste. Contagens de eventos são resultados do sorteio, não garantia de poder estatístico.

A simulação de início de operação usará janelas históricas mais curtas em análise separada, porque reduzir linhas não reproduz todos os efeitos de uma instituição nova. Um cenário sem rótulos locais permite avaliar transferência pura, mas não ajustar recalibração supervisionada. O teste futuro permanece igual entre regimes e conserva a distribuição original. Qualquer experimento adicional de amostragem por classe exige probabilidades de inclusão e correção da prevalência.

A heterogeneidade será medida no desenvolvimento por diferenças de modalidade, políticas e composição, além de distância padronizada de covariáveis comuns. A medida principal proposta é a média das distâncias de Wasserstein normalizadas por escala robusta da origem para variáveis numéricas e distâncias de variação total para categorias. Lista de variáveis, pesos, tratamento de escala nula e limites de compatibilidade serão congelados antes do teste. Diferenças de taxas de default serão descritas separadamente, com rótulos já maturados. Grupos de baixa/alta distância serão definidos no desenvolvimento, sem buscar cortes que maximizem o efeito final.

### 6.4 Modelos e regimes

Algoritmos principais: regressão logística regularizada e gradient boosting em árvores, sob orçamento comparável de ajuste. O núcleo tem quatro regimes:

1. **Local:** apenas dados de desenvolvimento disponíveis do destino.
2. **Agrupado (pooled):** origem e o mesmo conjunto disponível do destino, em um único ajuste.
3. **Transferido sem adaptação:** modelo treinado apenas na origem, aplicado diretamente ao destino.
4. **Adaptado:** o modelo da origem é recalibrado com dados locais disponíveis, usando intercepto e inclinação regularizados em direção à transformação identidade.

Modelo conceitual: `logit(p_adaptado) = a_destino + b_destino × logit(p_origem)`. A penalização mantém os parâmetros próximos de `(0, 1)` quando os dados não sustentam desvios, com intensidade escolhida no desenvolvimento. Probabilidades serão limitadas apenas numericamente para avaliação de log-loss, com tolerância registrada. Nenhum ajuste usa o teste. O parâmetro `k=50` do auxiliar histórico é uma heurística, não o método validado da proposta.

Ausência de duas classes ou informação insuficiente resulta em ajuste local/adaptação não estimável ou fallback previamente especificado para o modelo de origem. Serão reportadas cobertura de execução e frequência de fallback. Reponderação de domínio, modelos hierárquicos e ajuste de representações são extensões, não exigências simultâneas. Não há promessa de que ML complexo supere logística.

### 6.5 Informação prospectiva

O conjunto principal de variáveis e cenários prospectivos será parcimonioso e comum aos regimes. Seleção macro específica por carteira será extensão, deixando de ser problema central autônomo. Cada série ou expectativa terá data de referência, publicação e versão disponível na data-base. Focus não elimina automaticamente vazamento: é necessário recuperar a observação histórica correta, respeitar sua publicação e não usar uma previsão atual no lugar da antiga.

Uma ablação sem macro avalia sensibilidade metodológica, mas não é declarada automaticamente suficiente para mensuração contábil prospectiva. Sem histórico de expectativas ou cenários sustentáveis, o exercício será identificado como retrospectivo ou de sensibilidade.

### 6.6 Validação e análise estatística

- Reservar janelas futuras de datas-base com horizonte de rótulo integralmente observado; o teste não corresponde simplesmente aos últimos registros do arquivo.
- Usar validação cronológica aninhada no desenvolvimento, com maturação dos rótulos e purga/embargo coerentes com o horizonte. Ajustar imputação, seleção, regularização e calibração dentro dessas janelas.
- Evitar duplicação de tomadores entre domínios. Para avaliar novos tomadores, separá-los também entre treino e teste; avaliações recorrentes da carteira existente serão identificadas e terão dependência temporal controlada.
- Executar os regimes sobre os mesmos sorteios e teste. Reportar log-loss e Brier, intercepto/inclinação e curvas de calibração com incerteza, ROC-AUC e PR-AUC onde ambas as classes existirem. Métricas indefinidas permanecem ausentes com motivo explícito.
- Estimar contrastes pareados com reamostragem que respeite tomadores e blocos temporais; a escolha final de blocos depende da estrutura de dados. Com poucas instituições, a análise entre elas é descritiva; sementes não serão tratadas como amostras institucionais independentes.
- Usar intervalos de 95% e ajuste de Holm na família H1–H3. Tamanho de efeito e relevância prática acompanham o teste. Nenhuma margem de equivalência será inventada depois dos resultados; não haverá conclusão de equivalência por ausência de significância.
- Registrar variabilidade entre janelas, sensibilidade a fontes e subgrupos, além de limitações de poder. Planejar tamanho amostral pela precisão desejada e simulações de desenvolvimento, sem regra universal de dez eventos por variável.

Transferência negativa será definida como deterioração frente ao comparador previamente escolhido: transferência pura versus local para H2, e adaptação versus transferência pura em análise complementar. O critério incluirá magnitude e intervalo; mero ponto estimado pior não comprova deterioração estatisticamente identificável. Nenhum modelo será selecionado pelo desempenho no teste final para depois reportar esse mesmo teste como validação independente.

## 7. Da PD à ECL

### 7.1 Exercício principal controlado

Para isolar a contribuição da PD, comparar `LP12_i = PD12_i × LGD_i × EAD_i`, com LGD e EAD comuns aos modelos e claramente documentadas. LP12 é aproximação experimental de perda associada a eventos em 12 meses, não um motor completo de ECL. A comparação principal é `ΔLP12 = Σ_i (PD_A,i − PD_B,i) × LGD_i × EAD_i`, em BRL e em pontos-base da exposição. Esse efeito é uma propagação aritmética, não evidência de que o modelo com menor valor mede melhor a perda.

Para interpretar o produto como aproximação de ECL de 12 meses, a LGD precisa refletir perdas de fluxos ao longo da recuperação decorrentes dos defaults possíveis nesse horizonte, inclusive além do mês 12, com desconto coerente. A ECL de 12 meses não é apenas o caixa perdido nos próximos 12 meses, distinção explicada no [resumo oficial da IFRS 9, seção de impairment](https://www.ifrs.org/content/dam/ifrs/project/fi-hedge-accounting/ifrs-standard/project-summary.pdf). Sem essa sustentação, o resultado permanece LP12 ilustrativa.

### 7.2 Extensão multiperíodo e cenários

Se viável, usar `ECL = Σ_s w_s Σ_t q_(t,s) × LGD_(t,s) × EAD_(t,s) × DF_(t,s)`, em que os pesos de cenário somam um e `q` representa probabilidades marginais, não PDs acumuladas repetidas. Taxas condicionais de default exigem conversão por sobrevivência; liquidação/prepagamento requer tratamento consistente. O desconto e o horizonte devem ser compatíveis com o instrumento e o regime contábil aplicável.

PD de 12 meses não será multiplicada pelo prazo para produzir PD vitalícia. Sem estrutura temporal e recuperação adequadas, não haverá alegação de ECL vitalícia, cobertura de todos os estágios ou suficiência da provisão total. Os estágios da metodologia completa não serão automaticamente impostos à simplificada.

### 7.3 Parâmetros, validação e comparação regulatória

LGD será estimada com fluxos, custos e prazos de recuperação quando disponíveis, tratando censura; se ausentes, usar faixas de sensibilidade ou parâmetros externos justificados, identificados como premissas. EAD considera exposição no evento, amortização e desembolsos futuros quando relevantes; saldo corrente é apenas uma aproximação para produtos compatíveis. A análise principal fixa esses parâmetros entre modelos, e análises secundárias variam-nos para avaliar robustez. Intervalos de PD não representarão automaticamente toda a incerteza da ECL.

Erro de perdas monetárias só será reportado quando houver perdas realizadas comparáveis, recuperações maturadas e horizonte consistente. Rótulos de inadimplência sozinhos não validam LGD nem ECL. Para perdas observadas nulas, usar erro absoluto normalizado por exposição, evitando razões indefinidas.

A comparação com níveis normativos requer classificação por ativo, garantias, atraso, regras especiais e versão vigente à data, além do mesmo perímetro da estimativa. A diferença positiva será denominada **diferença experimental positiva**, não provisão complementar a registrar. Antes da vigência de um regime, aplicar suas regras a dados anteriores constitui contrafactual identificado, nunca reconstrução da obrigação histórica. Séries agregadas de inadimplência não substituem esse cálculo.

## 8. Dados, acesso e limites empíricos

O [dicionário corrente](../../data_dictionary/README.md) distingue campos essenciais à PD, campos para transferência, componentes de ECL e classificação regulatória. Não há microdados privados confirmados nesta revisão. Dados públicos agregados não fornecem, por si, os rótulos e atributos contratuais necessários; o uso de registros internos ou SCR depende de acesso autorizado e regras de uso.

**Cenário A — múltiplas instituições:** permite avaliar transferência entre instituições, condicionado à padronização e ao número de unidades independentes. Instituições de um mesmo sistema podem compartilhar políticas e infraestrutura; não representam toda a população brasileira.

**Cenário B — uma instituição, várias carteiras:** permite comparar transferência interna. Título contextual brasileiro permanece, mas amostra, pergunta operacional e conclusões restringem-se às carteiras observadas; não se afirmará validação entre instituições.

**Cenário C — bases estrangeiras ou sintéticas:** permite prova de conceito de mecanismos, com limitações do processo de seleção, jurisdição e definição de evento. Exige revisão expressa do título empírico e das conclusões; suspende conclusões sobre suficiência de provisões brasileiras. Não se substitui essa etapa por séries SGS agregadas.

Até o mês 3, registrar acesso, elegibilidade, contagens, maturação e decisão A/B/C. Se nenhum conjunto permitir contrastes identificáveis, reduzir o escopo com a orientação antes de executar testes, sem preencher lacunas com resultados simulados apresentados como reais. Não se exige um volume fixo universal: a viabilidade depende de precisão, complexidade, prevalência e dependência.

## 9. Reprodutibilidade, governança e viabilidade

O [protocolo operacional](../metodologia/protocolo-experimental-v3.md) especifica o registro de dados, hipóteses e decisões. O arquivo de configuração é declarativo e ilustrativo; não existe executor implementado. O pacote `ecl_suficiencia` mantém seu nome técnico para compatibilidade e contém auxiliares aritméticos e interfaces pendentes. Não constitui motor de produção.

Documentar versões de dados e bibliotecas, sementes, cortes temporais, parâmetros, falhas de estimação, orçamento de ajuste, tempo de treinamento/inferência e memória em equipamento identificado. Requisitos de manutenção serão descritos; medidas de execução não comprovam viabilidade econômica comercial.

Dados identificáveis não serão versionados nem enviados a serviços externos. Hashes de identificadores não garantem anonimização; pseudonimização, controle de acesso e risco de reidentificação devem ser avaliados. Termos de cessão, base legal, sigilo, retenção e eventual avaliação ética serão definidos com os responsáveis institucionais antes de acesso. Não se presume dispensa ética nem autorização de compartilhamento entre instituições pelo simples caráter acadêmico.

## 10. Revisão da literatura e referências

### 10.1 Protocolo de revisão proposto

Buscar Scopus, Web of Science e literatura nacional, complementando com rastreamento de citações e fontes primárias. Registrar data, consulta, filtros, duplicatas, critérios de inclusão/exclusão e motivos de exclusão. Incluir estudos de transferência/adaptação em crédito, PD com informação limitada, calibração e conversão de PD em ECL; distinguir contexto prudencial de mensuração contábil.

Consultas iniciais, a ajustar à sintaxe de cada base:

```text
("credit risk" OR "probability of default" OR "credit scoring") AND
("transfer learning" OR "domain adaptation" OR "partial pooling" OR hierarchical)

("probability of default" OR "credit risk") AND
("low default" OR "limited data" OR "small sample" OR heterogeneity) AND
(calibration OR uncertainty OR "negative transfer")

("expected credit loss" OR "IFRS 9" OR "perdas esperadas") AND
(calibration OR validation OR "machine learning" OR "model risk")
```

Extrair origem/destino, eventos, horizonte, acesso aos dados, definição de default, validação temporal, métricas, incerteza, transferência negativa, tratamento de LGD/EAD e limites de generalização. O produto da revisão será uma síntese crítica das condições estudadas; não há revisão sistemática concluída nesta versão.

### 10.2 Referências iniciais e status

- Suryanto, H., Mahidadia, A., Bain, M., Guan, C., & Guan, A. (2022). Credit risk modeling using transfer learning and domain adaptation. *Frontiers in Artificial Intelligence, 5*, 868232. [Artigo e metadados](https://doi.org/10.3389/frai.2022.868232). Texto consultado nesta revisão; antecedente direto, sem equivalência automática à ECL brasileira.
- Kiefer, N. M. (2009). Default estimation for low-default portfolios. *Journal of Empirical Finance, 16*(1), 164–173. [Registro editorial](https://doi.org/10.1016/j.jempfin.2008.03.004). Resumo e metadados conferidos; leitura integral a aprofundar.
- Blümke, O. (2020). Estimating the probability of default for no-default and low-default portfolios. *Journal of the Royal Statistical Society: Series C (Applied Statistics), 69*(1), 89–107. [Registro editorial](https://doi.org/10.1111/rssc.12381). Resumo e metadados conferidos; referência para atualização bayesiana, não algoritmo já implementado.
- Van Calster, B., et al. (2019). Calibration: The Achilles heel of predictive analytics. *BMC Medicine, 17*, 230. [Artigo](https://doi.org/10.1186/s12916-019-1466-7). Referência metodológica herdada da v2; lista completa de autores e leitura crítica a conferir antes da redação final.
- Basel Committee on Banking Supervision. (2015). *Guidance on credit risk and accounting for expected credit losses*. [Publicação oficial](https://www.bis.org/bcbs/publ/d350.htm). Referência de supervisão e validação; não substitui regulação nacional.
- IFRS Foundation. *IFRS 9 — Financial Instruments*. [Página oficial](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/). Referência conceitual; conferir edição e parágrafos utilizados na redação final.
- CMN e BCB: fontes oficiais e status de verificação na [nota normativa](../normativo/notas-verificacao-normativa.md).

Os demais trabalhos das versões anteriores permanecem disponíveis para revisão, sem serem automaticamente tratados como metadados validados ou evidência da lacuna corrente.

## 11. Entregas, cronograma e aplicação futura

**Entregas científicas:** protocolo e dicionário; comparação reprodutível dos regimes; evidências sobre condições e limites da adaptação; análise da propagação de PD para ECL; relatório de limitações. Resultados nulos ou transferência negativa são resultados válidos.

**Cronograma indicativo a contar do início formal:** meses 1–2, revisão e desenho; meses 2–3, acesso e diagnóstico dos dados; meses 4–5, referências locais/agrupadas e validação; meses 5–7, transferência/adaptação e curvas de aprendizagem; meses 7–8, ECL e sensibilidades compatíveis; meses 9–10, inferência e robustez; meses 10–12, redação e revisão. Datas e prazo serão pactuados com a orientação; a data desta revisão não comprova início da execução.

Um futuro produto poderá apoiar ingestão, escolha/adaptação de estimadores, mensuração e monitoramento. Sua construção dependerá de validação externa, segurança, segregação de dados, governança, integração e enquadramento por cliente. A dissertação não promete uma plataforma pronta, aceitação regulatória, redução obrigatória de provisões ou uma técnica universalmente superior. A utilização comercial posterior de dados ou modelos exige avaliação de direitos e autorizações próprios.

## 12. Decisões a fechar antes dos experimentos

1. Instituições/carteiras acessíveis, direitos de uso e cenário A/B/C.
2. Evento primário, coortes, censura, definição de destino e comparabilidade das fontes.
3. Precisão desejada, malha de informação, distância entre domínios e critérios de inviabilidade.
4. Janelas maturadas, orçamento de ajuste, reamostragem e plano de análise H1–H3.
5. Disponibilidade de recuperações, EAD e cenários; limites do exercício LP12 ou da extensão de ECL.
6. Enquadramento contábil por instituição/data, premissas de uso de dados e avaliação ética.

Essas decisões limitam a execução e as conclusões; não impedem a atualização documental. Nenhuma delas é apresentada como aprovada ou resolvida por esta versão.
