# Proposta de Dissertação de Mestrado — versão 5

## Modelagem adaptativa de probabilidades de inadimplência com Machine Learning: experimentos de transferência entre carteiras sintéticas e implicações para a mensuração de perdas esperadas de crédito

**Programa:** Mestrado em Controladoria e Contabilidade — PPGCONT/UFRGS.  
**Linha de pesquisa:** Informações para Usuários Externos.  
**Data da reformulação:** 14 de novembro de 2026.  
**Última revisão:** 22 de novembro de 2026 (questão de pesquisa, objetivos, regimes de estimação e seção 10.3).  
**Situação:** proposta de pesquisa para discussão com a orientação; parâmetros operacionais e lacuna de literatura ainda sujeitos à revisão.  
**Documento de origem:** `proposta-dissertacao-v4-2026-11-14.md`. A versão 4 permanece como registro histórico; este texto propõe a substituição do desenho baseado primordialmente em microdados reais por simulações de Monte Carlo calibradas, quando possível, com estatísticas públicas brasileiras.

> **Delimitação fundamental.** A pesquisa avalia métodos de estimação de probabilidade de inadimplência (PD) em ambientes *sintéticos*, cujas condições de geração são conhecidas. O leiaute do Documento 3040 orienta a representação estrutural das operações; os dados públicos do **SCR.data** ajudam a calibrar *distribuições e estatísticas agregadas*. Nem o leiaute nem os agregados do SCR revelam, isoladamente, a verdadeira PD de cada tomador. Os resultados **não** comprovarão, sem validação externa, que um modelo é adequado para qualquer instituição financeira real ou para fins de constituição regulatória de provisão.

## Resumo

A mensuração de perdas esperadas de crédito depende de estimativas de risco capazes de representar, com incerteza conhecida, a probabilidade de inadimplência das operações. Instituições financeiras podem enfrentar diferentes condições informacionais: carteiras recém-originadas, poucas ocorrências de inadimplência, públicos especializados ou dados extensos, mas pouco comparáveis aos de outras populações. O aproveitamento de modelos estimados com dados de carteiras de referência pode reduzir a instabilidade das estimativas locais; contudo, pode introduzir viés quando as populações diferem. Esta dissertação investigará em que condições a disponibilidade de dados locais, a heterogeneidade entre carteiras de origem e destino e a complexidade dos algoritmos afetam a qualidade das estimativas de probabilidade de inadimplência (PD) em 12 meses obtidas com e sem transferência de aprendizado. Será adotado estudo quantitativo de simulação de Monte Carlo, com mecanismos geradores de dados explicitados e diferentes perfis de instituições financeiras virtuais. A estrutura analítica das operações tomará o leiaute do Documento 3040 do Sistema de Informações de Créditos (SCR) como referência, sem utilizar arquivos individuais de instituições reais. Estatísticas públicas do SCR.data apoiarão a calibração de características observáveis das carteiras, sendo explicitadas as dimensões não identificáveis a partir de agregados. Serão comparados modelos locais, agrupados, transferidos e recalibrados, utilizando regressão logística regularizada e *gradient boosting*. Os desfechos principais incluirão pontuação probabilística, calibração, erro em relação às probabilidades verdadeiras do simulador e frequência de transferência negativa. A análise contábil mensurará como erros de PD se propagam à perda esperada simulada, mantendo explícitas as premissas de severidade, exposição e desconto. Os resultados pretendem delimitar condições de utilidade da transferência e fundamentar um procedimento reproduzível de escolha de estratégias; sua aplicação a carteiras reais dependerá de validação posterior.

**Palavras-chave:** perdas esperadas de crédito; probabilidade de inadimplência; Machine Learning; simulação de Monte Carlo; transferência de aprendizado; dados sintéticos; calibração; SCR.

---

## 1. Introdução

### 1.1 Contextualização

A adoção do arcabouço de perdas esperadas de crédito nas instituições abrangidas pela Resolução CMN nº 4.966/2021 e pelas normas complementares do Banco Central do Brasil (BCB) ampliou a importância de estimativas prospectivas de risco. A probabilidade de inadimplência (*probability of default*, PD) é um componente relevante da mensuração baseada em parâmetros de risco, mas não se confunde com a perda esperada de crédito (*expected credit loss*, ECL), que depende também da exposição, da recuperação dos fluxos de caixa, do horizonte relevante e do desconto, conforme a metodologia aplicável. A qualidade da estimativa contábil depende, entre outros aspectos, da confiabilidade e da documentação do processo que a produz.

A Estrutura Conceitual para Relatório Financeiro (CPC 00 [R2]) oferece a fundamentação contábil: relevância e representação fidedigna são características fundamentais de uma informação útil aos usuários externos. Neutralidade, completude e ausência de erro no processo de mensuração são atributos conceituais que motivam a avaliação de modelos; métricas estatísticas de PD representam apenas **evidências parciais**, e não provas diretas de conformidade com esses atributos. A literatura contábil reconhece a importância da provisão de crédito como estimativa e seus possíveis efeitos sobre a qualidade da informação financeira (Beatty & Liao, 2014).

As carteiras de crédito diferem em tamanho, histórico disponível, composição de tomadores, políticas de concessão e resposta às condições macroeconômicas. Essas características não decorrem automaticamente do enquadramento prudencial: instituições S4 e S5 podem possuir dados extensos, enquanto carteiras novas de instituições maiores podem contar com poucos eventos de inadimplência. Também podem existir limitações de equipe, orçamento e infraestrutura que afetam a operacionalização de modelos. A pesquisa distinguirá **restrição informacional**, tratada experimentalmente, de **restrição operacional**, caracterizada de forma complementar.

O aproveitamento de modelos estimados em outras populações constitui uma alternativa à estimação inteiramente local. Todavia, o compartilhamento de informação pode ser prejudicial quando as características da população de origem não representam as da carteira de destino. Uma dificuldade empírica importante é separar os efeitos da quantidade de observações, da heterogeneidade entre populações e da complexidade do modelo, pois essas condições se combinam em carteiras reais e os dados individuais frequentemente não estão disponíveis para investigação acadêmica.

### 1.2 Problema científico

A literatura já investiga estimação de PD em carteiras de poucos eventos e transferência de aprendizado aplicada a risco de crédito (Kiefer, 2009; Blümke, 2020; Suryanto et al., 2022). Portanto, nem a utilização de Machine Learning nem a possibilidade de transferência negativa constituem, isoladamente, uma lacuna científica. O problema específico consiste em determinar **sob quais condições a transferência de informação entre carteiras melhora ou prejudica a qualidade das estimativas de PD**, distinguindo restrição informacional, diferença entre populações e complexidade do estimador. O experimento simulado permitirá observar, além dos eventos realizados, as probabilidades verdadeiras estipuladas pelo mecanismo gerador e a influência de diferentes especificações desse mecanismo. Para uma instituição recém-constituída, o acesso a um modelo externo é uma condição do experimento. Na sua ausência, interessa saber com que histórico o treinamento local passa a melhorar a previsão em relação a uma referência simples disponível.

**Questão de pesquisa**

> **Como a disponibilidade de dados locais, a heterogeneidade entre carteiras e a complexidade dos algoritmos influenciam a qualidade das estimativas de probabilidade de inadimplência em 12 meses obtidas por estratégias de Machine Learning com e sem transferência de aprendizado?**

A **qualidade da PD** é o desfecho central. O cálculo de perdas esperadas a partir dessas probabilidades constitui um desdobramento contábil subordinado ao problema principal. A pesquisa não pretende investigar, como problema independente, a conformidade de instituições reais com o provisionamento regulatório, nem desenvolver uma plataforma comercial completa.

### 1.3 Justificativa e relevância

A **relevância científica** reside na avaliação controlada de modelos sob combinações de disponibilidade e heterogeneidade que não são facilmente isoláveis em dados observacionais. O uso de múltiplos mecanismos geradores — e não apenas de uma função logística — também permitirá investigar se as conclusões dependem da especificação da realidade sintética. O resultado pretendido é condicional: evidenciar fronteiras de utilidade, regiões de transferência negativa e situações em que dados insuficientes impedem conclusões precisas.

A **relevância contábil** decorre de a PD, quando utilizada em metodologias de perdas esperadas, afetar o montante estimado da perda. Uma PD estatisticamente mal calibrada pode introduzir desvios na mensuração, mesmo na ausência de discricionariedade gerencial oportunista. A comparação com a perda esperada verdadeira do experimento permitirá identificar a parcela do erro atribuível à PD sob hipóteses controladas sobre os demais componentes. Isso não equivale a demonstrar insuficiência de provisão de uma instituição real.

A **relevância aplicada** está relacionada à possibilidade de desenvolver posteriormente uma ferramenta que selecione estratégias de estimação conforme a quantidade de dados, a semelhança entre populações e as restrições operacionais. O protótipo científico poderá testar métodos sem expor operações verdadeiras, mas modelos destinados a uso comercial e regulatório deverão ser recalibrados, validados e governados com dados da instituição ou de fontes legitimamente utilizáveis.

### 1.4 Delimitação

- **Objeto estatístico:** PD do primeiro evento definido como atraso superior a 90 dias dentro de 12 meses após a data-base, para contratos elegíveis sem esse evento na data-base. É um *proxy* operacional, não uma equivalência integral à classificação regulatória de ativo com problema de recuperação de crédito.
- **Horizonte principal:** 12 meses, para permitir uma comparação uniforme; horizontes de 3 e 6 meses serão considerados em análises de sensibilidade se o simulador e o cronograma permitirem. ECL de 12 meses não se limita às prestações vencíveis nesse período: perdas decorrentes dos eventos que ocorram nesse horizonte podem envolver recuperações posteriores.
- **População analisada:** instituições financeiras e carteiras **virtuais**, com perfis estilizados do mercado brasileiro, e não uma amostra representativa de instituições brasileiras.
- **Componente estimado por ML:** PD. LGD, EAD, cronogramas de recuperação e desconto terão mecanismos explícitos para o cálculo sintético de ECL; sua modelagem por ML ficará fora do escopo.
- **Fontes:** leiaute/instruções públicas do Documento 3040, estatísticas públicas do SCR.data, informações macroeconômicas públicas e referências científicas para as hipóteses de geração. Arquivos individuais reais do 3040 **não são necessários**.
- **Exclusões:** validação regulatória de modelos para instituições concretas, estimação completa de ECL por toda a vida contratual em dados reais, simulação integral do balanço patrimonial, determinação de piso de provisão por carteira C1–C5, inferência sobre decisões gerenciais reais e desenvolvimento de produto comercial.

## 2. Objetivos

### 2.1 Objetivo geral

Avaliar, por meio de simulações de Monte Carlo com carteiras de crédito sintéticas, como a disponibilidade de dados locais, a heterogeneidade entre carteiras e a complexidade dos algoritmos influenciam a qualidade das estimativas de probabilidade de inadimplência em 12 meses obtidas por estratégias de Machine Learning com e sem transferência de aprendizado, examinando a repercussão dessas estimativas na perda esperada simulada.

### 2.2 Objetivos específicos

1. Construir cenários de carteiras sintéticas com diferentes históricos, perfis de tomadores e relações de risco, utilizando estatísticas públicas brasileiras para fundamentar características agregadas selecionadas.
2. Comparar as estimativas de PD de 12 meses de modelos locais, transferidos e recalibrados com as referências disponíveis em cada cenário, avaliando também o treinamento agrupado quando houver acesso aos dados individuais da origem.
3. Examinar como o número de tomadores, a extensão do histórico e a quantidade de eventos locais observados afetam a viabilidade e o desempenho de cada estratégia.
4. Analisar como diferenças de composição, nível de risco e relação entre os atributos e a inadimplência afetam a transferência entre carteiras.
5. Avaliar como a complexidade do algoritmo interage com a disponibilidade de dados e a estrutura do risco, comparando regressão logística regularizada e *gradient boosting* sob diferentes mecanismos geradores.
6. Identificar as condições em que cada estratégia produz melhores probabilidades na carteira de destino, considerando desempenho preditivo, calibração, erro em relação à PD de referência e estabilidade entre replicações.
7. Quantificar a repercussão dos erros de PD sobre a perda esperada simulada, sob premissas comuns de exposição, recuperação e desconto.

## 3. Referencial teórico e lacuna

### 3.1 Qualidade da informação contábil e incerteza de estimação

A Estrutura Conceitual do CPC 00 (R2) define critérios para a utilidade da informação financeira. A mensuração de perdas esperadas se apoia em estimativas sujeitas à incerteza, motivo pelo qual processos documentados, premissas justificáveis e informações relevantes são essenciais. Neste estudo, a calibração, o erro probabilístico e o desvio monetário serão utilizados como **indicadores operacionais parciais** de propriedades relevantes à qualidade da mensuração; não serão tratados como equivalentes diretos dos conceitos normativos de neutralidade ou ausência de erro.

A relação empírica de interesse será examinada em uma etapa controlada: mantendo constantes as regras de EAD, recuperação e desconto, diferenças entre PDs estimadas se traduzirão em diferenças de perda esperada simulada. Em exercícios complementares, a heterogeneidade de EAD e LGD será alterada para investigar se modelos com desempenho semelhante em número de contratos produzem erros monetários distintos.

### 3.2 Transferência de aprendizado, calibração e heterogeneidade

A regressão logística regularizada fornecerá uma referência estatística transparente. Algoritmos de *gradient boosting* permitirão captar relações não lineares e interações. A comparação não pressupõe superioridade do algoritmo flexível: quando o processo gerador é aproximadamente logístico, a regressão pode ser suficiente; quando existem interações relevantes, modelos de árvores podem apresentar vantagens sob tamanho amostral adequado. Isso será objeto de teste, não condição assumida.

A **transferência de aprendizado** aproveita padrões estimados na carteira de origem para gerar PDs no destino. A **adaptação de domínio** ajusta o uso desse conhecimento à população de destino. A heterogeneidade será separada em: (i) diferença de taxa-base de inadimplência; (ii) diferença na distribuição de atributos (*covariate shift*); e (iii) diferença na relação entre atributos e risco (*concept/conditional shift*). Uma correção de intercepto pode lidar com determinadas mudanças de taxa-base; reponderação por composição depende de hipóteses de estabilidade da relação condicional e de suporte comum entre as distribuições. Diferenças estruturais mais profundas podem provocar transferência negativa.

A calibração é a concordância entre probabilidades previstas e riscos efetivos. Em amostras reais, costuma ser avaliada com eventos observados e incerteza amostral; em simulações, também pode ser comparada diretamente com as probabilidades verdadeiras produzidas pelo DGP. Serão preservadas as distinções entre calibração média, inclinação de calibração, discriminação e pontuação probabilística (Van Calster et al., 2019).

### 3.3 Estudos de simulação e avaliação de métodos

O estudo seguirá o esquema **ADEMP** de Morris, White e Crowther (2019): *Aims* (objetivos), *Data-generating mechanisms* (mecanismos geradores), *Estimands* (quantidades-alvo), *Methods* (métodos comparados) e *Performance measures* (medidas de desempenho). Seu principal benefício é obrigar o pesquisador a definir, antes dos resultados, quais propriedades do gerador são conhecidas, quais métodos serão comparados e quais estimandos justificam cada inferência.

Será feita distinção entre **microdados sintéticos gerados por um DGP explícito** e **dados sintéticos derivados de microdados reais**. A pesquisa propõe a primeira abordagem: os registros serão artificialmente gerados sob parâmetros documentados. O uso de estatísticas agregadas reais para calibração não significa que a distribuição conjunta dos contratos fictícios reproduza a distribuição verdadeira dos contratos brasileiros.

### 3.4 Lacuna candidata e revisão da literatura

Os trabalhos de Kiefer (2009), Blümke (2020) e Suryanto et al. (2022) constituem antecedentes necessários. A lacuna candidata será investigada em três eixos combinados: (a) fronteira de utilidade da transferência segundo disponibilidade de eventos e diferença entre populações; (b) estabilidade dessa fronteira entre diferentes mecanismos geradores e sob avaliação de **calibração**, além de discriminação; e (c) repercussão monetária do erro de PD em uma medida sintética de perda esperada sob condições conhecidas.

A revisão sistematizada deve procurar **estudos de simulação** sobre transferência de aprendizado, *low-default portfolios*, *domain shift*, *credit scoring*, calibração, modelos hierárquicos e mensuração de ECL. A lacuna não será declarada demonstrada antes da execução e documentação da busca. Caso existam estudos que já realizem essa combinação, a contribuição será reclassificada como replicação, extensão metodológica ou aplicação em condições calibradas com dados brasileiros, conforme a evidência encontrada.

## 4. Hipóteses e estimandos

O **estimando central** é a diferença esperada de desempenho preditivo entre métodos sobre uma população de teste do destino, **sob um mecanismo gerador fixado**. O desempenho será calculado com a mesma amostra de teste para os métodos comparados. Sinais de efeitos poderão variar entre DGPs; resultados discrepantes deverão ser interpretados como dependência das condições de geração, e não como inconsistência a ocultar.

**H1 — Disponibilidade local.** Em mecanismos nos quais existe compartilhamento informacional útil, a vantagem média do modelo transferido e adaptado sobre o modelo local tende a diminuir com o aumento do número de eventos de inadimplência disponíveis no destino. A hipótese será testada pelo contraste pareado de *log-loss* em função da disponibilidade; a relação não será imposta como monotônica e poderá não se verificar em todos os DGPs.

**H2 — Heterogeneidade e transferência negativa.** Em cenários com aumento de diferença condicional entre carteiras, a frequência e/ou a magnitude da transferência negativa tendem a aumentar, especialmente quando a estratégia de adaptação não consegue recuperar as relações específicas do destino. Serão comparados contrastes pareados sob níveis controlados de heterogeneidade de composição e de relação condicional.

**H3 — Recalibração.** Quando as carteiras diferirem predominantemente em taxa-base, o modelo transferido com recalibração local tenderá a apresentar melhor calibração média do que o modelo transferido sem adaptação, desde que haja informação local suficiente; a hipótese não presume correção adequada de diferenças condicionais.

**H4 — Especificação do algoritmo.** A vantagem relativa entre *gradient boosting* e regressão logística regularizada dependerá conjuntamente do tamanho amostral e do mecanismo gerador. Prevê-se ausência de superioridade sistemática do algoritmo mais complexo em DGPs logísticos, com vantagem potencial em DGPs não lineares quando houver informação suficiente. Será avaliada por interação entre algoritmo, volume local e tipo de DGP; trata-se de hipótese dependente de cenário, não de uma afirmação de superioridade universal.

**Desdobramento contábil pré-especificado (C1).** Diferenças de PD entre métodos produzirão diferenças no erro da ECL sintética; sua magnitude dependerá da distribuição das exposições, das recuperações e do desconto. A análise será predominantemente quantitativa e descritiva, com intervalos de Monte Carlo e sensibilidade às hipóteses do simulador.

**Resultado derivado.** A fronteira de utilidade será definida como o ponto ou faixa de disponibilidade em que o contraste esperado entre estratégia adaptada e local cruza zero ou uma margem pré-especificada de irrelevância prática. Se não existir cruzamento na região testada, registrar-se-á “não identificado no domínio experimental”, sem extrapolação automática. Não se presumirá que toda condição tenha um único ponto de cruzamento. No cenário sem modelo externo, será descrita, de modo análogo, a faixa de histórico ou de eventos locais a partir da qual o contraste pareado entre o modelo local (R1) e a referência simples (R0) cruza zero ou a mesma margem. Essa análise é pré-especificada e descritiva, sem hipótese direcional, e fica restrita às replicações em que ambos os regimes forem estimáveis.

### Matriz de amarração

| Objetivo | Hipótese / análise | Fatores manipulados | Desfechos | Unidade de inferência |
|---|---|---|---|---|
| 1 | Verificação do DGP | Família de DGP, parâmetros, sementes | Taxas agregadas, eventos, distribuições | Replicação independente do cenário |
| 2, 3 e 6 | Cenário sem modelo externo | Histórico e eventos locais | Viabilidade de R0 e R1 e diferença pareada de *log-loss* quando ambos forem estimáveis | Replicação de Monte Carlo × cenário |
| 2 e 3 | H1 | Volume local e nº de eventos | Diferença de *log-loss*, calibração | Replicação de Monte Carlo × cenário |
| 4 e 6 | H2 | Composição e diferença condicional | Transferência negativa, desempenho | Replicação de Monte Carlo × cenário |
| 2 e 4 | H3 | Diferença de taxa-base e tamanho local | Calibração média; *log-loss* | Replicação de Monte Carlo × cenário |
| 5 | H4 | Complexidade × DGP × volume | Diferença de desempenho | Replicação de Monte Carlo × cenário |
| 7 | C1 | Exposição, LGD, recuperação, desconto | Desvio da ECL estimada frente à ECL verdadeira simulada | Replicação de Monte Carlo × cenário |
| 6 | Regra de seleção | Condições conhecidas de treino | Arrependimento e frequência de acerto | Novas replicações independentes |

## 5. Enquadramento contábil, regulatório e fontes de dados

### 5.1 Normas de perdas esperadas

A Resolução CMN nº 4.966/2021 disciplina critérios contábeis aplicáveis a instrumentos financeiros e perdas esperadas para instituições em seu âmbito; a Resolução BCB nº 352/2023 estabelece disposições e procedimentos complementares, conforme o âmbito de aplicação pertinente. A metodologia simplificada, associada em especial a instituições dos segmentos S4 e S5 nos termos normativos, não elimina a responsabilidade de apurar provisões segundo critérios consistentes, verificáveis e fundamentados em informações internas e externas (art. 51 da Resolução CMN nº 4.966). O enquadramento deve sempre ser examinado segundo o tipo institucional e a data-base.

**A avaliação de suficiência de provisão não exige automaticamente a adoção de um modelo interno formal de PD–LGD–EAD equivalente ao utilizado por instituições sob metodologia completa.** A dissertação não conclui que uma divergência entre sua ECL simulada e um piso regulatório gera obrigação real de complemento. A simulação utilizará conceitos de perda esperada para fundamentar sua relevância, e não reproduzirá integralmente os critérios de constituição da provisão por categoria regulatória.

### 5.2 Documento 3040 — modelo de estrutura, não fonte obrigatória de dados individuais

O Documento 3040 do SCR, com leiaute e instruções públicas mantidos pelo BCB, será utilizado como **referência semântica e estrutural** para representar contratos, exposições, vencimentos, modalidades, garantias e evolução mensal do risco. O 3040 é objeto de atualizações periódicas de leiaute; a Instrução Normativa BCB nº 733/2026, por exemplo, alterou seus campos e instruções em datas-bases de 2026. A versão aplicável ao desenho será congelada e identificada na documentação do estudo, observadas as alterações vigentes para a data-base escolhida.

**Não será necessário acessar ou copiar um arquivo 3040 de instituição real.** Os identificadores de instituições, tomadores e contratos serão inteiramente fictícios. O banco de dados principal será analítico e longitudinal, não necessariamente um XML de remessa. A eventual exportação para XML compatível com o 3040 será tratada como funcionalidade de teste, separada da evidência científica.

O leiaute não fornece necessariamente todas as variáveis requeridas para modelar o processo gerador, como históricos completos de originação, renda, fluxos de recuperação ou relações condicionais de risco. Cada atributo sintético será classificado como: (a) diretamente inspirado na estrutura do 3040; (b) variável analítica adicional; (c) variável latente do DGP, não observável pelo algoritmo; ou (d) parâmetro de cenário. A correspondência exata com os nomes, códigos e tipos de dados vigentes do 3040 será documentada em dicionário próprio antes da implementação.

### 5.3 SCR.data — calibração agregada e limites

O SCR.data disponibiliza estatísticas mensais **agregadas**, derivadas do SCR, por dimensões como segmento da instituição, tipo de cliente, modalidade e outras categorias. Sua utilização poderá ajudar a estabelecer faixas de distribuição de exposições, participação por modalidade e indicadores agregados de inadimplência e ativo problemático. Serão documentados versão, filtros, período, unidade de medida e eventual supressão/agrupamento de observações. A aderência dos resultados será verificada com margens de tolerância previamente definidas.

**A inadimplência agregada em estoque não equivale à incidência de primeiro atraso superior a 90 dias ao longo dos 12 meses seguintes.** Por isso, a taxa de inadimplência do SCR.data não será tomada diretamente como a PD verdadeira nem como rótulo individual do experimento. Os parâmetros do DGP serão ajustados para que estatísticas observáveis simuladas sejam compatíveis com os agregados públicos selecionados, mediante hipóteses adicionais explícitas. As correlações microeconômicas, os coeficientes de risco e os fluxos de recuperação não serão apresentados como empiricamente identificados apenas com o SCR.data.

### 5.4 Informações macroeconômicas

Quando incluídas, variáveis e cenários macroeconômicos serão obtidos de fontes públicas apropriadas, como séries do BCB/SGS e previsões históricas datadas, quando disponíveis. Cada simulação distinguirá a trajetória econômica geradora dos eventos das informações efetivamente observáveis na data-base. Variáveis revisadas ou resultados futuros não poderão entrar indevidamente no treinamento ou na previsão. A análise com e sem variáveis macroeconômicas será de sensibilidade, sem transformar a seleção macroeconômica em outro problema central.

## 6. Metodologia

### 6.1 Delineamento e lógica geral

A pesquisa é **quantitativa, preditiva e metodológica**, por meio de **experimento computacional de Monte Carlo** sobre microdados sintéticos gerados por mecanismos probabilísticos especificados. A comparação de algoritmos será feita em condições controladas, com replicações independentes. Não se trata de pesquisa de campo em instituições reais nem de inferência causal sobre comportamento econômico efetivamente observado. O experimento permitirá conclusões internas às famílias de DGPs estudadas e hipóteses limitadas de extrapolação aos perfis estilizados.

O protocolo seguirá ADEMP: (i) problema e contrastes; (ii) mecanismos de geração; (iii) estimandos; (iv) métodos; (v) medidas de desempenho. Serão separados **piloto para configurar o experimento** e **simulações confirmatórias independentes**, evitando selecionar cenários retrospectivamente em função dos resultados desejados.

### 6.2 Perfis de instituições virtuais

As instituições serão arquétipos experimentais, não reproduções de empresas reais nem representantes estatísticos de segmentos prudenciais. Sugere-se inicialmente:

| Perfil fictício | Carteira predominante | Condição informacional | Variação controlada principal |
|---|---|---|---|
| IF-A — iniciante | Crédito pessoal PF | Histórico curto, poucos eventos | Disponibilidade e ausência de inadimplências observadas |
| IF-B — especializada | Consignado PF | Histórico maior, público específico | Diferença de composição e taxa-base |
| IF-C — especializada | Capital de giro PJ | Histórico médio, exposição heterogênea | Diferença de relação condicional e sensibilidade econômica |
| IF-D — referência | Conjunto de carteiras sintéticas | Histórico longo e maior volume | Uso como possível origem de aprendizado |

Os nomes indicam **cenários estilizados**. Não se presumirá que instituições de modalidades distintas disponham das mesmas variáveis explicativas. Os testes confirmatórios de transferência utilizarão somente um **núcleo comum de atributos** que possa ser representado de modo consistente entre origem e destino. Testes de variáveis específicas de uma modalidade serão complementares. O perfil de capacidade operacional será tratado separadamente da estrutura estatística do risco e não será usado como justificativa automática para reduzir qualidade de dados.

Neste estudo, carteira é o conjunto de operações delimitado por instituição, modalidade e perfil dos tomadores. A PD é estimada por contrato e data-base. A carteira de destino reúne as operações avaliadas. Quando há transferência, a carteira de origem fornece a experiência utilizada para treinar o modelo. Para representar a especialização setorial, poderá ser simulado um contraste dentro da mesma modalidade, como capital de giro PJ para empresas do varejo e da cadeia do agronegócio. O DGP poderá variar tanto a frequência de receitas sazonais como a relação da sazonalidade com o risco. Essas diferenças são hipóteses experimentais.

### 6.3 Estrutura da base sintética

A base conterá pelo menos as seguintes entidades relacionais, ligadas por chaves **inteiramente fictícias**:

| Entidade | Granularidade | Conteúdo mínimo | Origem conceitual |
|---|---|---|---|
| Instituição | Instituição–mês | Perfil, data de início, política, disponibilidade histórica | Cenário simulado |
| Tomador | Tomador–mês | Características observáveis e, em tabela protegida, fator latente | Campos públicos compatíveis + DGP |
| Contrato | Contrato | Modalidade, valor, prazo, taxa, garantias, calendário contratual | Estrutura inspirada no 3040 + DGP |
| Evolução da operação | Contrato–mês | Saldo, vencimentos, pagamentos, dias em atraso, liquidação e renegociação | Estrutura inspirada no SCR + regras simuladas |
| Ambiente econômico | Mês | Variáveis correntes, projeções disponíveis, choques simulados | Séries públicas + DGP |
| Eventos e recuperação | Contrato–mês | Início do evento, fluxos de recuperação e baixa | DGP; não inferível integralmente do 3040 |
| Verdade do simulador | Contrato–data-base | PD verdadeira, horizonte e perda esperada verdadeira | Variáveis do DGP indisponíveis aos modelos |

A evolução temporal respeitará restrições contábeis e contratuais básicas: saldos não negativos, amortizações coerentes, vencimentos e estados de atraso compatíveis com pagamentos, e ausência de fluxos posteriores à extinção efetiva do contrato, ressalvados recebimentos de recuperação. O histórico de um tomador que contrata múltiplas operações terá dependência identificável. Os modelos não terão acesso à tabela de verdade do simulador durante seu treinamento ou ajuste.

### 6.4 Mecanismos geradores de dados (DGPs)

O DGP deve produzir simultaneamente: (a) contratos e características individuais; (b) trajetórias mensais de pagamento e atraso; (c) eventos de inadimplência; (d) dados observáveis e informação latente; (e) exposição e eventual recuperação. Em cenário introdutório, a probabilidade condicional de evento poderá ser produzida por uma função logística:

\[
\Pr(Y_{i,t}=1\mid X_{i,t},M_t,j)=\operatorname{logit}^{-1}
\left(\alpha_j+\boldsymbol{\beta}_j^{\top} X_{i,t}+\boldsymbol{\gamma}_j^{\top} M_t\right),
\]

em que \(i\) indica o tomador ou contrato, \(j\) a carteira e \(t\) o período. **Essa função será apenas uma das famílias**, pois um experimento inteiramente logístico favoreceria por construção o modelo logístico. Nos cenários temporais, poderão ser simuladas intensidades mensais de transição para atraso e inadimplência, liquidação antecipada e outros estados, das quais se obterá a PD acumulada de primeiro evento em 12 meses. Quando houver risco competitivo de liquidação, o cálculo da PD verdadeira respeitará a ordem dos eventos.

**Famílias pré-especificadas:**

1. **DGP-L — relações aproximadamente logísticas:** efeitos aditivos e ausência de interações fortes; cenário de referência em que a regressão logística está próxima da especificação verdadeira.
2. **DGP-N — relações não lineares:** interações e limiares de risco em funções contínuas ou por partes, evitando que um único algoritmo corresponda exatamente a todos os mecanismos.
3. **DGP-C — heterogeneidade de composição:** distribuições de atributos diferentes entre origem e destino, com relação condicional de risco compartilhada e suporte comum documentado.
4. **DGP-R — heterogeneidade condicional:** mesma característica observada podendo exercer efeito diferente sobre o risco no destino; inclui regiões sem suporte comum e avaliação de transferência negativa.
5. **DGP-T — mudança temporal:** alterações de taxa-base, condições macroeconômicas e/ou sensibilidade ao ciclo, além de defasagens de maturação e saída da carteira.

As famílias não precisam ser cruzadas em todas as combinações. O **núcleo obrigatório** compreenderá L, N, C e R; T será um módulo de sensibilidade se o piloto demonstrar viabilidade. Os níveis de parâmetros serão escolhidos **antes** do experimento final. Também serão incluídos cenários com baixa taxa-base, zero eventos locais observados, valores ausentes e erro de mensuração em atributos, conforme capacidade computacional.

### 6.5 Calibração e validação do próprio simulador

A calibração será feita em dois níveis que não devem ser confundidos:

**Nível de coerência estrutural.** Verificação de integridade dos contratos, transições entre estados, saldos, cronogramas, ausência de eventos impossíveis e consistência do primeiro evento em 12 meses. Testes unitários e testes de propriedades verificarão esses elementos.

**Nível de plausibilidade agregada.** Confronto entre métricas calculadas na base sintética e indicadores públicos selecionados do SCR.data: composição por modalidade, distribuição agregada de carteira, evolução temporal e taxas de inadimplência em definições comparáveis. Serão registradas divergências, intervalos de tolerância, dimensões sem informação e hipóteses necessárias à aproximação.

Parâmetros identificados apenas por suposição serão variados em **análises de sensibilidade**; não serão classificados como “estimados pelo SCR”. Um conjunto de indicadores agregados será usado para ajuste do simulador e, quando possível, outro período/recorte público será reservado para verificar sua estabilidade. Aproximação das estatísticas agregadas não será denominada validação microeconômica ou externa.

### 6.6 Disponibilidade, heterogeneidade e condições experimentais

**Disponibilidade de informação local.** Serão variados, separadamente quando possível, o número de tomadores, o número efetivo de eventos e a extensão temporal do histórico. Uma malha **candidata** para o piloto é de 0, 5, 20, 50 e 200 eventos locais maturados, complementada por níveis maiores. Para replicações em que o número aleatório observado de eventos não coincida com o alvo, registrar-se-á o valor realizado, sem selecionar observações futuras para forçar um número exato de casos. Poderão ser controlados também números de contratos e meses de histórico. O tratamento de **zero eventos** deverá ser explícito; métodos não estimáveis serão contabilizados, e métodos de transferência sem adaptação supervisionada continuarão elegíveis.

O piloto distinguirá ausência de contratos com acompanhamento completo de 12 meses e ausência de eventos entre contratos já acompanhados por esse período. No primeiro caso, faltam desfechos completos para o treino supervisionado em horizonte fixo. No segundo, o número de contratos acompanhados fornece informação sobre a frequência de eventos, mas limita a estimação de diferenças de risco entre perfis.

**Heterogeneidade.** A distância de composição será variada alterando parâmetros de distribuição dos atributos e, quando apropriado, o suporte entre populações. A diferença de taxa-base será variada por interceptos ou mecanismos equivalentes. A diferença condicional será variada por coeficientes, interações ou funções diferentes entre origem e destino. As diferenças conhecidas nos parâmetros do DGP serão registradas como verdade experimental; índices empíricos de separabilidade de domínios serão calculados apenas com dados de desenvolvimento.

**Complexidade do algoritmo.** A regressão logística regularizada e o *gradient boosting* serão treinados sob protocolo comparável de seleção de hiperparâmetros, sem exigir igualdade artificial de tempo de computação. O custo observado será reportado separadamente.

**Desenho econômico-computacional.** Um experimento piloto determinará o número mínimo de condições necessário para identificar os contrastes e o tempo de execução. Como desenho inicial viável, recomenda-se selecionar dois níveis por fator principal em um experimento fracionário e ampliar apenas as regiões em que aparecerem mudanças relevantes de desempenho; o protocolo final identificará quais cenários são confirmatórios e quais são exploratórios. A expansão não será decidida a partir do resultado final mantido em reserva.

### 6.7 Estratégias de estimação

O experimento cruzará a disponibilidade de histórico local com três condições de acesso. Sem modelo externo nem microdados da origem, serão avaliados R0 e R1 quando viáveis. Com acesso às previsões de um modelo externo, também serão elegíveis R3 e R4, conforme haja informação local para recalibrar. R2 exigirá acesso aos microdados de desenvolvimento da origem. Em todos os casos, a avaliação usará os mesmos contratos futuros do destino em cada replicação. O simulador manterá a PD de referência reservada à avaliação.

| Regime | Definição | Situação com zero evento local |
|---|---|---|
| **R0 — Referência simples** | Taxa agregada comparável ao evento e horizonte ou estimativa suavizada fundamentada nas informações disponíveis na data-base | Aplicável se houver base documentada. Sem ela, registrar indisponibilidade |
| **R1 — Local** | Modelo ajustado apenas com desenvolvimento do destino | Pode ser não estimável sem regularização/prior apropriado |
| **R2 — Agrupado** | Modelo único com dados de origem e destino elegíveis | Executável quando houver eventos na origem |
| **R3 — Transferido** | Treinado na origem e aplicado no destino sem atualização | Executável; calibração local não pode ser comprovada sem rótulos |
| **R4 — Transferido + recalibração** | Modelo da origem atualizado com intercepto e, quando suportado, inclinação estimados no destino com estabilização/regularização | Adaptação supervisionada pode ser não estimável; retornar a R3 ou atualização por prior documentado |

Os regimes R1–R4 serão avaliados com regressão logística regularizada e *gradient boosting* quando a arquitetura do regime comportar o algoritmo. A referência simples (R0) não será artificialmente duplicada. Os algoritmos terão o mesmo conjunto básico de atributos observáveis, e os hiperparâmetros serão ajustados somente no desenvolvimento.

**Extensões condicionadas:** reponderação por importância sob *covariate shift* com suporte adequado, atualização bayesiana para poucos/nenhum evento, modelo hierárquico parcial e horizontes adicionais. A reponderação não será tomada como solução geral para diferenças condicionais; estimativas de razão de densidades serão estabilizadas e verificadas quanto à variância dos pesos.

### 6.8 Treinamento e validação temporal

Cada replicação simulará uma história completa, porém os modelos terão acesso apenas ao passado elegível em sua data-base. Serão separados: (i) desenvolvimento; (ii) validação cronológica interna; e (iii) teste em datas futuras, sem reutilização para seleção. A construção de rótulos de primeiro evento em 12 meses exigirá **maturação completa** do horizonte ou métodos explícitos de tratamento de censura. Datas-base de treino cujas janelas de resultado invadam o início da validação ou do teste serão excluídas ou separadas por intervalo de embargo justificado; valores futuros de macroeconomia e recuperações não entrarão nos preditores.

O identificador de tomador controlará a dependência entre contratos. A estrutura de origem e destino não permitirá que o mesmo tomador seja duplicado em ambos de modo a criar vazamento. Transformações, imputação, seleção de variáveis, reponderação e recalibração ocorrerão **dentro** das janelas permitidas, sem acesso à probabilidade verdadeira do simulador. Essa verdade estará disponível apenas à avaliação externa dos métodos.

A regra de escolha de regime será ajustada em **replicações de simulação de desenvolvimento** e testada em **novas replicações**, geradas com sementes independentes, evitando escolher o vencedor por conhecimento do próprio conjunto de avaliação final.

### 6.9 Medidas de desempenho e quantidades-alvo

**Métrica primária de previsão:** *log-loss* médio no destino, em que valores menores representam previsões probabilísticas melhores. O escore de Brier será complementar. Ambos são *proper scoring rules* e devem ser calculados com as mesmas observações de teste por contraste.

**Calibração observada:** intercepto, inclinação, curvas de calibração e seus intervalos; discriminação pela AUC-ROC como medida complementar. A interpretação dos intervalos deverá reconhecer a quantidade de eventos de teste e a correlação entre contratos, tomadores e datas-base.

**Avaliação contra a verdade conhecida:** erro médio de probabilidade \(N^{-1}\sum_i(\widehat{p}_i-p_i^*)\), erro absoluto médio e erro quadrático médio frente à PD verdadeira \(p_i^*\) definida pelo DGP. O desvio sistemático de probabilidades será calculado **ao longo das replicações independentes**, não identificado a partir de uma única realização binária do evento.

**Transferência negativa:** proporção de replicações/cenários em que o regime transferido ou adaptado apresenta *log-loss* superior ao local por margem superior ao limiar de irrelevância pré-especificado. Se o local for não estimável, a comparação será marcada como indisponível; não se imputará vantagem ao transferido por ausência de concorrente.

**Desfecho monetário:** ECL sintética estimada e sua diferença para o valor esperado verdadeiro do simulador, em moeda simulada e pontos-base da exposição. Resultados realizados de perda serão relatados separadamente da ECL verdadeira, pois ruído de realização não equivale a viés do estimador.

**Critério de adequação:** será definido no protocolo prévio com margens de relevância prática justificadas, precisão estatística e medidas de incerteza por replicação. Evitar-se-á a inconsistência da v4 entre exigir intervalos inteiramente contidos em uma faixa ±0,2 e planejar intervalos com meia-largura 0,2. Os limiares só serão fixados após piloto independente, sem acesso aos resultados confirmatórios. Se o intervalo ou o número de eventos não permitir conclusão, a célula será classificada como **inconclusiva** — não como adequada por ausência de rejeição.

**Custo operacional descritivo:** tempo de treino, memória, tempo de inferência, número de parâmetros/decisões de ajuste e dependência de dados da origem. Não se afirmarão custos comerciais ou organizacionais com base apenas no tempo de computador.

### 6.10 Número de replicações, precisão e análise inferencial

O número de replicações independentes de Monte Carlo não será confundido com o número de contratos ou com repetições de reamostragem da mesma carteira. Será escolhido para alcançar **erro de Monte Carlo** suficientemente pequeno nos contrastes principais. No piloto, poderá ser utilizado número inicial de 100 replicações por condição candidata, com posterior cálculo do erro-padrão dos contrastes; o tamanho definitivo será aumentado conforme a precisão requerida e os recursos disponíveis. **Esse valor é ilustrativo e não constitui dimensionamento definitivo.**

Para cada DGP e condição experimental serão calculados: média do contraste pareado entre modelos, erro-padrão de Monte Carlo, intervalo de confiança, distribuição dos contrastes e frequência de transferência negativa. Como a comparação é pareada dentro da replicação, os modelos utilizarão exatamente as mesmas operações de teste. As replicações independentes constituem a principal unidade de incerteza do experimento; múltiplos contratos do mesmo tomador ou múltiplas datas-base dentro de uma replicação não serão tratados como replicações independentes. A multiplicidade dos testes confirmatórios será controlada por procedimento pré-especificado (por exemplo, Holm) quando apropriado.

A precisão da **calibração em uma carteira simulada** será tratada separadamente da precisão da **média de Monte Carlo**. Mesmo milhares de replicações não tornam precisa a calibração de uma carteira real individual com poucos eventos; apenas permitem conhecer melhor o comportamento esperado do método sob o DGP. A frequência de falha, não estimação ou classificação inconclusiva será resultado substantivo, sobretudo nos cenários de baixa disponibilidade.

### 6.11 Fronteira de utilidade e regra experimental de seleção

A fronteira de utilidade será estimada em cada família de DGP e tipo de heterogeneidade. A regra de seleção utilizará características disponíveis **antes** da estimação do destino (por exemplo, volume local, número de eventos maturados, duração histórica, indicadores de distância de composição e atributos dos regimes), sem utilizar diferenças condicionais verdadeiras que só o simulador conhece. A regra será comparada, em replicações independentes, ao regime local, ao transferido e a um **oráculo retrospectivo** que escolhe o melhor método com conhecimento do desempenho de teste. A distância em desempenho entre a regra factível e esse oráculo será denominada *arrependimento* (*regret*), sem sugerir que o oráculo seja aplicável por uma instituição real. A seleção será restrita aos regimes elegíveis segundo o acesso efetivo da instituição. Indicadores que exijam microdados da origem só poderão ser usados no cenário que os disponibiliza. Se nenhum regime for estimável, será registrada a insuficiência de informação.

Caso as condições observáveis não permitam prever qual regime é melhor, esse resultado deverá ser relatado. A dissertação não se compromete a produzir um seletor universal ou eficaz em todo cenário.

### 6.12 Validade, robustez e ameaças

**Validade interna:** deriva do controle experimental, da geração transparente dos dados, dos contrastes pareados, da avaliação independente e do conhecimento da verdade do DGP. Falhas de código, vazamento temporal e escolha retrospectiva de cenários permanecem ameaças, mitigadas por testes, protocolo e registro de decisões.

**Validade de construto:** instituições virtuais não reproduzem automaticamente políticas de crédito, seleção de tomadores, qualidade cadastral, renegociações, governança, práticas de cobrança e interações macroeconômicas reais. A diminuição sintética de amostra não é equivalente ao início de operação; serão testados também históricos truncados e dados incompletos.

**Validade externa:** calibração com agregados do SCR não valida as relações de risco individuais nem o desempenho em instituições reais. A inferência terá alcance **condicional às famílias de DGPs estudadas e seus parâmetros**. Se surgirem dados reais acessíveis e autorizados, sua aplicação será uma etapa complementar de validação externa, com protocolo próprio e sem revisão retrospectiva das hipóteses confirmatórias.

**Robustez:** repetir conclusões sob DGP linear e não linear; heterogeneidade de composição e condicional; diferentes frequências do evento; cenários com ausência de eventos; múltiplos níveis de ruído, concentração de exposições e qualidade de atributos; análises com e sem macroeconomia, quando viável.

## 7. Da PD à perda esperada sintética

### 7.1 Grandezas distintas

A pesquisa separará três grandezas: (i) probabilidade verdadeira de primeiro evento em 12 meses \(PD_{12,i}^*\), produzida pelo DGP; (ii) probabilidade estimada pelo modelo \(\widehat{PD}_{12,i}\); e (iii) indicador observado de evento \(Y_{12,i}\), sujeito à variabilidade aleatória. A diferença \(\widehat{PD}_{12,i}-Y_{12,i}\) é **erro de previsão realizado**, e não uma medida direta e isolada de viés estatístico.

### 7.2 Perda esperada de referência e estimada

Para a etapa contábil, o simulador atribuirá parâmetros de exposição, fluxos de recuperação e taxas de desconto. Em uma aproximação estática transparente, será possível calcular:

\[
LP_{12}^{\mathrm{sim}}(m)=\sum_i \widehat{PD}_{12,i}^{(m)}\, LGD_i\, EAD_i,
\]

mantendo \(LGD_i\) e \(EAD_i\) comuns aos métodos \(m\), e a referência verdadeira:

\[
LP_{12}^{*}=\sum_i PD_{12,i}^{*}\,LGD_i\,EAD_i.
\]

O desvio \(LP_{12}^{\mathrm{sim}}(m)-LP_{12}^{*}\) isola, **sob essas premissas**, o componente monetário relacionado às diferenças de PD. Quando houver simulação de datas de evento e de fluxos de recuperação, uma versão mais consistente descontará a perda de fluxos de caixa em cada possível período de inadimplência, incluindo recuperações posteriores ao horizonte de ocorrência do evento. Essa versão dependerá da capacidade do piloto e deverá ser identificada separadamente da aproximação estática.

### 7.3 Limites da interpretação contábil

A multiplicação \(PD\times LGD\times EAD\) é uma representação simplificada do cálculo de perdas esperadas, não uma fórmula universal da IFRS 9. A *ECL de 12 meses* está associada às perdas decorrentes de eventos que possam ocorrer nos próximos 12 meses, e não somente aos vencimentos financeiros dentro desses 12 meses. Uma estimativa sintética baseada em PD de atraso superior a 90 dias, em LGD presumida e em EAD simulada **não será apresentada como provisão contábil válida para instituição real**.

A comparação de cenários de provisionamento regulatório não é objeto confirmatório desta versão. A contribuição contábil consiste em demonstrar, em condições controladas, **quando o erro da PD pode tornar materialmente diferente a medida monetária de perdas esperadas**, especialmente em carteiras com exposições concentradas.

## 8. Execução, bases de referência e cenários de contingência

### 8.1 Estratégia principal independente de microdados sigilosos

A pesquisa **não dependerá** de receber o 3040 de instituição real. Os três insumos primários serão: (a) documentação pública do leiaute 3040; (b) agregados do SCR.data; (c) parâmetros e mecanismos probabilísticos justificados pela literatura, com sensibilidade explícita. Será mantida uma tabela de **proveniência de parâmetros** com a origem de cada suposição e seu grau de identificabilidade.

A ausência de microdados reais não impedirá o experimento metodológico, mas impedirá afirmar validação externa de modelos em carteiras reais brasileiras. Também impedirá inferir que a estratégia se aplica universalmente a S4, S5 ou a modalidades específicas.

### 8.2 Plano de contingência

- **Plano principal:** dados inteiramente sintéticos com plausibilidade agregada verificada perante indicadores públicos do Brasil, mediante definições compatíveis; conclusões condicionais aos DGPs.
- **Extensão opcional:** comparação, em base pública de microdados de crédito adequada e legalmente utilizável, de parte dos regimes; essa extensão não comprovará aderência ao mercado brasileiro se a base for de outra jurisdição.
- **Extensão externa posterior:** acesso autorizado a carteiras reais de uma ou mais instituições; avaliação totalmente separada, com sigilo e governança apropriados.

A dissertação seguirá executável no plano principal mesmo sem concretização das extensões. Não será criado compromisso de obter dados confidenciais em prazo incompatível com o mestrado.

## 9. Reprodutibilidade, ética e governança

O protótipo será desenvolvido em Python e deverá gerar instituições, contratos, eventos, PDs verdadeiras, perdas esperadas sintéticas e relatórios de avaliação a partir de parâmetros e sementes versionados. Serão registrados: fonte e versão do leiaute 3040, extração e tratamento de agregados públicos, dicionário de dados, parâmetros do DGP, versões de bibliotecas, configurações dos modelos, critérios de avaliação e histórico de decisões.

O código e conjuntos **inteiramente sintéticos** poderão ser compartilhados, desde que não incorporem informações derivadas de microdados confidenciais. O leiaute público não confere autorização para reproduzir arquivos individuais de instituições. Se forem empregados dados reais posteriormente, serão necessárias análise de sigilo, base legal, controle de acesso, eventual autorização institucional e verificação das condições éticas aplicáveis. Dados sintéticos produzidos **a partir de registros reais** demandariam avaliação específica de risco de reidentificação; essa não é a estratégia principal.

Serão utilizados testes automáticos de integridade, casos-limite (zero eventos, pré-pagamento, múltiplos contratos por tomador) e ensaios independentes de reprodutibilidade. O protocolo ADEMP e a lista final de hipóteses deverão ser congelados **antes da execução confirmatória**, admitindo emendas datadas.

## 10. Entregas, cronograma e aplicação posterior

### 10.1 Entregas científicas

1. Revisão sistematizada dos antecedentes e da lacuna; protocolo ADEMP documentado.
2. Dicionário de dados sintéticos inspirado no 3040, com rastreabilidade da origem conceitual dos atributos.
3. Gerador longitudinal reproduzível de carteiras e instituições virtuais.
4. Relatório de calibração e limitações perante agregados do SCR.data.
5. Comparação estatística de regimes e algoritmos sob diferentes DGPs, com erros de Monte Carlo.
6. Mapas de transferência negativa, fronteiras de utilidade quando identificáveis e regra de escolha avaliada fora das replicações usadas em seu desenvolvimento.
7. Análise da repercussão monetária do erro da PD em perdas esperadas simuladas.
8. Relatório explícito de validade interna, validade de construto e ausência de validação externa automática.

### 10.2 Cronograma indicativo

| Meses | Atividade e critério de passagem |
|---|---|
| 1–2 | Revisão de literatura; congelamento do recorte de eventos e atributos; escolha de indicadores públicos SCR.data |
| 2–3 | Dicionário inspirado no 3040; DGP piloto; testes de coerência estrutural |
| 3–4 | Calibração agregada, verificação de plausibilidade e seleção de cenários confirmatórios |
| 4–5 | Implementação de modelos locais, agrupados, transferidos e recalibrados; validação temporal |
| 5–7 | Simulações confirmatórias e estimativa de precisão de Monte Carlo |
| 7–8 | Sensibilidades, zero eventos, diferentes DGPs e custos operacionais |
| 8–9 | ECL sintética; fronteira de utilidade; regra de seleção em replicações independentes |
| 9–10 | Consolidação de inferência e relatório de limites de validade |
| 10–12 | Redação, discussão com orientação e revisão final |

Os prazos pressupõem aprovação do piloto dentro dos quatro primeiros meses. Caso a simulação longitudinal completa ultrapasse recursos ou tempo disponíveis, o núcleo mínimo será um DGP com risco de evento em horizonte fixo, desde que as conclusões não afirmem ter simulado trajetórias mensais de operações ou fluxos completos de recuperação. A redução de escopo deverá ser relatada como tal.

### 10.3 Finalidade comercial posterior da plataforma de perdas esperadas de crédito

O produto pretendido é uma plataforma que permita às equipes de risco e contabilidade de instituições financeiras estimar, monitorar e documentar a perda esperada de crédito (ECL) por operação e consolidar os valores por carteira e data-base. A plataforma deverá mostrar como se chegou ao valor em reais, quais dados e premissas sustentam a estimativa e quanto ela varia sob diferentes hipóteses de risco e recuperação. O público de interesse inclui instituições recém-operantes, com pouco histórico próprio, e instituições especializadas que já dispõem de dados, mas atendem a públicos com características distintas.

A dissertação fornecerá a base metodológica do módulo de probabilidade de inadimplência (PD) em 12 meses. Para cada carteira, esse módulo deverá identificar o histórico disponível, os desfechos já observados e o acesso a informações externas, comparar as estratégias viáveis e registrar a evidência que sustenta a escolha. Em uma instituição recém-operante sem modelo externo e sem desfechos locais suficientes, a plataforma poderá apresentar cenários com premissas explícitas e acompanhar as safras de concessão. À medida que os contratos completarem o período de observação, será possível confrontar as previsões anteriores com os resultados e avaliar o uso de modelos locais ou, quando disponíveis, de modelos externos recalibrados.

Para estimar a ECL em produção, o desenvolvimento posterior deverá integrar a PD à exposição esperada no momento da inadimplência (EAD) e à perda em caso de inadimplência (LGD), considerando valores e prazos de recuperação. O cálculo deverá respeitar o horizonte aplicável a cada operação, os cenários prospectivos e o desconto dos fluxos, com tratamento consistente do desconto já incorporado à LGD. Quando a mensuração abranger a vida da operação, será necessário desenvolver e validar estimativas de risco ao longo desse horizonte. A plataforma deverá preservar as versões dos dados, modelos e premissas usados em cada data-base para permitir a reprodução dos resultados e apoiar a análise da provisão pela instituição.

O laboratório de instituições virtuais servirá para experimentar métodos e demonstrar funcionalidades. A implantação comercial exigirá acesso legítimo aos dados, segregação entre clientes, governança, auditoria e avaliação de aderência às normas aplicáveis. A validação do módulo de PD confrontará previsões com os eventos observados nos mesmos contratos reais nos 12 meses seguintes, reservando um período posterior a qualquer recalibração para o teste. Os demais componentes da ECL também exigirão validação própria e monitoramento de desempenho na carteira de cada instituição. O desenvolvimento da plataforma e essas validações estão **fora do objeto da dissertação**.

## 11. Limitações e decisões pendentes

A proposta está metodologicamente delimitada, mas as decisões abaixo precisam ser tomadas com a orientação **antes** dos experimentos confirmatórios:

1. **Revisão da lacuna:** verificar se existem estudos prévios com desenho equivalente de simulação, transferência, calibração e implicação monetária de PD.
2. **Escolha de agregados SCR.data:** selecionar séries, intervalos e segmentos comparáveis e verificar mudanças metodológicas das versões publicadas; não tratar agregados de inadimplência como PD individual.
3. **Versão do 3040:** definir a data-base regulatória de referência, identificar os campos exatos e congelar o dicionário; não atribuir códigos ou campos sem confirmação do leiaute oficial.
4. **DGPs e parâmetros:** documentar hipóteses identificáveis, parcialmente identificáveis e arbitradas, com amplitudes de sensibilidade justificadas; impedir que um DGP favoreça todos os métodos testados por construção.
5. **Escopo temporal:** confirmar se o DGP principal gerará eventos em horizonte fixo ou trajetórias mensais completas; distinguir o nível alcançado no texto e nos resultados.
6. **Precisão:** dimensionar replicações, eventos e faixas de adequação por piloto, separando erro de Monte Carlo de incerteza de calibração em carteira individual.
7. **Contribuição contábil:** decidir se será usada apenas a aproximação estática \(PD\times LGD\times EAD\) ou também simulação descontada de fluxos de recuperação, sem afirmar conformidade normativa indevida.
8. **Limite de generalização:** resultados favoráveis em instituições virtuais não serão apresentados como evidência de desempenho em instituições reais ou de suficiência de provisões regulatórias.

**Parecer propositivo sobre a viabilidade:** a simulação reduz a dependência de microdados sob sigilo e fortalece a identificação experimental dos efeitos estudados, mas transfere parte relevante do esforço científico à construção, calibração e validação do próprio mecanismo gerador. A viabilidade deve ser comprovada por um piloto anterior à execução confirmatória.

---

## Referências

Banco Central do Brasil. (2023). *Resolução BCB nº 352, de 23 de novembro de 2023* (versão vigente). https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?numero=352&tipo=Resolu%C3%A7%C3%A3o+BCB

Banco Central do Brasil. (2026a). *SCR.data* [Conjunto de dados agregados, atualizado mensalmente]. https://dadosabertos.bcb.gov.br/dataset/scr_data

Banco Central do Brasil. (2026b). *Instrução Normativa BCB nº 733, de 4 de maio de 2026*. https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?numero=733&tipo=Instru%C3%A7%C3%A3o+Normativa+BCB

Banco Central do Brasil. (s.d.). *Documento 3040 — Dados de Risco de Crédito: leiaute e instruções de preenchimento*. https://www.bcb.gov.br/estabilidadefinanceira/scrdoc3040

Basel Committee on Banking Supervision. (2015). *Guidance on credit risk and accounting for expected credit losses*. Bank for International Settlements. https://www.bis.org/bcbs/publ/d350.htm

Beatty, A., & Liao, S. (2014). Financial accounting in the banking industry: A review of the empirical literature. *Journal of Accounting and Economics, 58*(2–3), 339–383. https://doi.org/10.1016/j.jacceco.2014.08.009

Blümke, O. (2020). Estimating the probability of default for no-default and low-default portfolios. *Journal of the Royal Statistical Society: Series C (Applied Statistics), 69*(1), 89–107. https://doi.org/10.1111/rssc.12381

Comitê de Pronunciamentos Contábeis. (2019). *Pronunciamento Técnico CPC 00 (R2): Estrutura conceitual para relatório financeiro*. http://static.cpc.aatb.com.br/Documentos/573_CPC00(R2).pdf

Conselho Monetário Nacional. (2021). *Resolução CMN nº 4.966, de 25 de novembro de 2021* (versão vigente). https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?numero=4966&tipo=RESOLU%C3%87%C3%83O+CMN

International Accounting Standards Board. (2014). *IFRS 9 Financial Instruments*. IFRS Foundation. https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/

Kiefer, N. M. (2009). Default estimation for low-default portfolios. *Journal of Empirical Finance, 16*(1), 164–173. https://doi.org/10.1016/j.jempfin.2008.03.004

Morris, T. P., White, I. R., & Crowther, M. J. (2019). Using simulation studies to evaluate statistical methods. *Statistics in Medicine, 38*(11), 2074–2102. https://doi.org/10.1002/sim.8086

Riley, R. D., Debray, T. P. A., Collins, G. S., Archer, L., Ensor, J., van Smeden, M., & Snell, K. I. E. (2021). Minimum sample size for external validation of a clinical prediction model with a binary outcome. *Statistics in Medicine, 40*(19), 4230–4251. https://doi.org/10.1002/sim.9025

Shmueli, G. (2010). To explain or to predict? *Statistical Science, 25*(3), 289–310. https://doi.org/10.1214/10-STS330

Suryanto, H., Mahidadia, A., Bain, M., Guan, C., & Guan, A. (2022). Credit risk modeling using transfer learning and domain adaptation. *Frontiers in Artificial Intelligence, 5*, Article 868232. https://doi.org/10.3389/frai.2022.868232

Van Calster, B., McLernon, D. J., van Smeden, M., Wynants, L., & Steyerberg, E. W. (2019). Calibration: The Achilles heel of predictive analytics. *BMC Medicine, 17*, Article 230. https://doi.org/10.1186/s12916-019-1466-7

---

### Registro de alterações em relação à v4

- Mantidos problema científico único, uso de ML, transferência de aprendizado, foco em calibração, análise contábil subordinada e finalidade comercial posterior.
- Substituída a dependência de microdados reais por simulação de Monte Carlo com DGP explícito e replicações independentes.
- Adotados o Documento 3040 como **referência estrutural** e o SCR.data como **referência de calibração agregada**, sem pressupor acesso a arquivos 3040 individuais.
- Incluídas instituições virtuais, base longitudinal, variáveis latentes e diferentes tipos de heterogeneidade e mecanismos geradores.
- Incorporados ADEMP, validação interna do simulador, distinção entre PD verdadeira e evento observado e limites explícitos de validade externa.
- Tratados cenários com zero eventos; revisadas hipóteses que pressupunham superioridade ou fronteira necessariamente existente.
- Corrigida a interpretação da ECL e do erro monetário, além do conflito entre margens de adequação e precisão do intervalo de calibração.
- Reduzido o núcleo obrigatório de regimes; reponderação e outras extensões permanecem condicionadas ao piloto.
- Delimitada a capacidade operacional como dimensão descritiva e preservado o produto comercial como etapa posterior.
