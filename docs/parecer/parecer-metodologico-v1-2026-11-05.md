# Parecer metodológico — Proposta de dissertação "Personalização e robustez de modelos de ML para estimação de ECL em instituições com dados limitados" (versão de 28/10/2026)

**Finalidade:** avaliação da relevância, da lacuna e da correção técnica do projeto preliminar, com recomendações de reescrita, para discussão com a orientação (PPGCONT/UFRGS).
**Data do parecer:** 05/11/2026.

---

## 1. Diagnóstico metodológico ponto a ponto

### 1.1 Problema de pesquisa

A questão central (seção 1.3) é interrogativa, não binária, não carrega juízo de valor e coloca a variável explicada ("calibração e estimação das perdas esperadas") ao final, com as variáveis explicativas (personalização; seleção macroeconômica) no início. Nesses aspectos formais, atende.

Há, contudo, três falhas de delimitação, duas delas graves.

- **Erro grave — "condições" não nomeadas.** A pergunta abre com "em que condições", mas não diz quais dimensões constituem essas condições. O restante do texto deixa claro que são o volume de observações, o número de eventos de inadimplência e a heterogeneidade entre carteiras (seções 3, 7.4 e 8). Se a pergunta não as nomeia, o desenho experimental não tem ancoragem e qualquer resultado pode ser apresentado como "uma condição encontrada". A pergunta precisa fixar as condições que serão manipuladas ou observadas.
- **Erro grave — população indefinida com consequência sobre a relevância.** "Instituições financeiras de menor porte" não é recorte operacional. No arcabouço brasileiro, o porte prudencial (S1 a S5, Resolução CMN nº 4.553/2017) decide qual metodologia de provisão a instituição aplica. Para instituições submetidas à metodologia simplificada, um modelo de PD não altera a provisão contábil; para as que aplicam (ou pleiteiam) a metodologia completa, altera. A pergunta precisa dizer de qual segmento trata, porque disso depende para quem o resultado é útil (ver 1.4).
- **Erro menor — direcionalidade na pergunta.** O verbo "melhora" já embute a direção esperada. A direção pertence às hipóteses; a pergunta deve ser neutra ("altera", "afeta").

### 1.2 Objetivos

- **Erro grave — desalinhamento vertical entre problema e objetivo geral.** O problema pergunta *em que condições a personalização e a seleção macroeconômica melhoram a calibração e a estimação de ECL*. O objetivo geral responde outra coisa: "desenvolver e avaliar uma arquitetura modular e adaptativa de ML". Além de empilhar dois verbos, o objetivo está formulado como problema de engenharia (construir um artefato) e não retoma as palavras-centrais da pergunta (condições, personalização, seleção macroeconômica, calibração). Da forma como está, a banca pode ler o trabalho como projeto de desenvolvimento de software, e não como pesquisa empírica.
- **Erro grave — objetivos específicos que abrem portas não anunciadas.** O objetivo 7 (integrar LGD/EAD e construir módulo de conciliação regulatória) e parte do objetivo 8 (custo operacional, reprodutibilidade) introduzem objetos que não constam da pergunta. Ou a pergunta passa a contemplá-los (e há bons motivos para que a conciliação regulatória passe a constar, ver 1.4), ou eles saem da lista de objetivos e vão para a descrição do protótipo.
- **Erro menor — procedimentos listados como objetivos.** Os objetivos 1 (sistematizar a literatura) e 2 (definir base de dados) são etapas do método, não objetivos de pesquisa. Oito objetivos específicos para uma dissertação de mestrado também sinalizam risco de inexequibilidade; quatro ou cinco bem encadeados bastam.

### 1.3 Hipóteses

- **Erro grave — H1 é infalsificável como redigida.** "Em pelo menos determinados perfis de carteira" é uma cláusula existencial: com número suficiente de carteiras e métricas, sempre haverá algum perfil em que o híbrido vence. A hipótese precisa pré-especificar o perfil (por exemplo, carteiras com menos de *k* eventos de inadimplência no treino) e a métrica primária.
- **Erro grave — H4 é hipótese de equivalência e o plano de análise não a trata como tal.** "Calibração e erro de ECL estatisticamente comparáveis" não se demonstra pela ausência de diferença significativa; exige teste de equivalência (procedimento TOST ou intervalo de confiança dentro de margem de equivalência pré-definida). A margem precisa ser fixada *a priori* e justificada em termos de relevância contábil (por exemplo, diferença de ECL agregada inferior a *x*% da provisão).
- **Erro menor — H2 e H3 sem operacionalização.** "Após controle de complexidade" (H2) e "deteriora-se menos" (H3) precisam de definição operacional: número de parâmetros efetivos ou validação aninhada para H2; inclinação da curva desempenho × fração de treino para H3.
- **Erro grave — hipóteses sem derivação teórica.** As quatro hipóteses são plausíveis, mas o texto não mostra de qual teoria decorrem. Há fundamentação disponível: H1 e H3 decorrem diretamente da teoria de encolhimento (*shrinkage*) e de modelos hierárquicos, segundo a qual a estimação com agrupamento parcial domina a estimação local quando os grupos são pequenos (Efron & Morris, 1975; Gelman & Hill, 2007); H2 decorre da não estacionariedade da relação macro-inadimplência entre modalidades; H4 decorre da evidência de benchmarks em *credit scoring* de que ganhos de algoritmos complexos sobre a regressão logística são modestos e concentrados em discriminação, não em calibração (Lessmann et al., 2015). A ausência dessa derivação torna as hipóteses conjecturas de engenharia, e isso é o que mais fragiliza a proposta perante uma banca de Contabilidade.

### 1.4 Lacuna, relevância e Pentágono da Qualidade

**Lacuna — erro grave, e o ponto central deste parecer.** O texto é honesto ao dizer que a lacuna é "provisória" e "sujeita à RSL". Mas um projeto de qualificação não pode prometer uma lacuna; precisa demonstrá-la, ainda que a revisão sistemática a refine depois. E a lacuna tal como formulada na seção 4.6 — "escassez de evidência empírica integrada sobre (i), (ii), (iii) e (iv)" — é uma lacuna de combinação: afirma que ninguém juntou quatro ingredientes. Esse tipo de lacuna é frágil por construção, porque sempre é possível adicionar um ingrediente até que a combinação seja inédita, e não aponta ponto cego teórico algum.

Há, no entanto, um ponto cego real que o próprio texto tangencia sem nomear, e que pode ser formulado como lacuna legítima em três proposições:

1. **A literatura de ML em crédito é dominada pela discriminação em bases grandes.** Os benchmarks de referência (Lessmann et al., 2015; Gunnarsson et al., 2021) comparam algoritmos por AUC em bases com dezenas de milhares de observações. Para ECL, o que importa é o nível da PD (calibração), não o ordenamento; e a calibração é o aspecto menos estudado da análise preditiva (Van Calster et al., 2019). O regime de poucos eventos, tratado na literatura prudencial como *low default portfolios* (Pluto & Tasche, 2005), é exatamente aquele em que a calibração se degrada primeiro.
2. **Há tensão teórica não resolvida entre seleção macroeconômica específica e sobreajuste.** A relação macro-inadimplência é estimada no nível carteira-período, com poucas dezenas de observações temporais (trimestres). Selecionar indicadores e defasagens por carteira multiplica os graus de liberdade do pesquisador sobre uma série curta. A teoria prevê, portanto, que a seleção específica pode piorar o desempenho fora da amostra — o oposto do que a prática de *overlays* assume. Breed et al. (2023) e Moodley et al. (2025) propõem ajustes macro uniformes ou pragmáticos; não testam se a especificidade por carteira sobrevive à validação temporal. Isso é um ponto cego com previsão teórica em aberto, e é o que torna H2 interessante.
3. **A teoria de agrupamento parcial prevê o sinal, não a magnitude.** Que o híbrido supere o local em grupos pequenos é previsão teórica estabelecida; o que não se sabe é a magnitude do ganho em PD de crédito, em qual número de defaults o ganho se anula e se ele sobrevive a heterogeneidade entre carteiras com dinâmica de risco distinta (consignado versus agro, por exemplo). A contribuição empírica está em medir isso, não em mostrar que existe.

Formulada assim, a lacuna deixa de ser "ninguém combinou A+B+C+D" e passa a ser "a teoria prevê X, a prática assume Y, e a evidência que decidiria entre elas no regime de poucos dados não existe". Esse é o padrão que uma banca reconhece como lacuna.

**Relevância — erro grave, por dependência da população indefinida.** A verificação normativa feita para este parecer altera o argumento de relevância:

- A Resolução BCB nº 352/2023, citada na proposta como parte do arcabouço de bancos e cooperativas, aplica-se a corretoras, distribuidoras, corretoras de câmbio, administradoras de consórcio e instituições de pagamento, e consolida (revogando) as Resoluções BCB nº 219/2022 e nº 309/2023, conforme o Voto BCB 170/2023 que a fundamenta. A provisão de instituições financeiras permanece disciplinada pela Resolução CMN nº 4.966/2021, com suas alterações (entre elas a Resolução CMN nº 5.100/2023), e por atos complementares do BCB. Citar a 352 como norma das instituições financeiras é erro técnico que uma banca com experiência regulatória identificará de imediato.
- O pedido de autorização para uso da metodologia completa está regulado pela Instrução Normativa BCB nº 487/2024, que o faculta a instituições do **S4** (art. 1º) e exige, entre outros requisitos, comprovação de uso das perdas esperadas na gestão de crédito há pelo menos dois anos (art. 6º), validação independente e documentação de PD, LGD e cenários prospectivos. Não há previsão análoga para o S5.

Duas consequências para a proposta. Primeira: a hipótese de "S5 optar pela metodologia completa", já tratada com cautela no texto, deve ser retirada; o recorte relevante é **S3 (metodologia completa obrigatória) e S4 (completa mediante autorização)**. Segunda, e mais favorável ao projeto: a exigência de dois anos de uso gerencial de ECL antes do pedido de autorização significa que uma instituição S4 precisa operar modelos internos de PD/LGD *antes* de poder usá-los contabilmente. É exatamente o problema que a proposta ataca — modelos viáveis com dados limitados — e isso deve ser dito na justificativa com a norma citada.

Há ainda uma frente de relevância subaproveitada: a conciliação entre ECL modelada e provisão regulatória (seção 5.7), hoje um módulo periférico, é o que conecta o trabalho a usuários externos da informação contábil. Se a metodologia simplificada produz provisões sistematicamente diferentes da perda esperada modelada, ou as reconhece com atraso, isso afeta a comparabilidade e a tempestividade da informação para depositantes, cooperados, auditores e supervisor — a literatura de tempestividade do reconhecimento de perdas (Beatty & Liao, 2011; Bushman & Williams, 2012) oferece a lente. Recomenda-se elevar esse módulo a objetivo específico e definir uma métrica de tempestividade (defasagem, em períodos, entre a elevação da ECL modelada e a elevação da provisão regulatória antes dos defaults observados).

**Inovação, contribuição e impacto.** O texto diz corretamente que não inventa algoritmo, mas então precisa nomear a inovação: ela é **metodológica** — o desenho experimental de escassez controlada (subamostragem por número de defaults, não por percentual) combinado com calibração hierárquica por grupo — e **empírica** — as magnitudes e os limiares. A contribuição teórica (se a tensão macro-seleção versus sobreajuste se confirma) e a prática (instituições S4 em trajetória para autorização) devem aparecer segregadas na introdução. O impacto não é discutido em lugar algum; o parágrafo final da justificativa deve dizer o que muda para o supervisor, para a instituição e para a literatura caso cada hipótese se confirme ou seja refutada.

### 1.5 Teoria de base

**Erro grave — ausência de lente teórica.** A seção 4.1 lista temas (tempestividade, discricionariedade, pró-ciclicidade), mas não adota teoria alguma, e a seção 4.3 trata a modelagem como técnica. Para uma dissertação em Controladoria e Contabilidade, dois níveis de ancoragem são necessários e compatíveis entre si: no nível contábil, a qualidade da informação (relevância e representação fidedigna, CPC 00 R2/Estrutura Conceitual) e a tempestividade do reconhecimento de perdas (Beatty & Liao, 2011, 2014); no nível estatístico, a teoria de estimação com agrupamento parcial e o dilema viés-variância (Gelman & Hill, 2007; Hastie, Tibshirani & Friedman, 2009 — já disponível na pasta de leituras). O estudo de Lu e Nikolaev sobre um modelo empírico de provisão esperada, também já disponível, é a ponte natural entre os dois níveis.

### 1.6 Delineamento e método

- **Erro grave — classificação "explicativa/preditiva" sem sustentação.** Um estudo de avaliação comparativa de modelos preditivos não é explicativo: não testa relações causais nem controla endogeneidade. A classificação correta é pesquisa quantitativa, de finalidade preditiva/avaliativa, com delineamento quase-experimental computacional (configurações manipuladas pelo pesquisador sobre dados observacionais). Quanto ao *Design Science Research*, o texto hesita; precisa decidir. Se o produto central é o artefato, adota-se DSR (Hevner et al., 2004; Peffers et al., 2007) com seus ciclos de relevância e rigor. Se o produto central é a evidência, como o próprio texto afirma, o artefato é instrumento e o enquadramento é de estudo de *benchmark* comparativo (Lessmann et al., 2015), devendo-se abandonar o vocabulário de "artefato" e "arquitetura" como objeto.
- **Erro grave — amostragem não probabilística sem discussão de viés de seleção.** As instituições que cederem dados serão uma amostra de conveniência; as carteiras disponíveis, idem. Não há uma linha sobre o que isso implica para a generalização, e no Cenário A o número de instituições será pequeno demais para inferência estatística sobre "condições" entre instituições — nesse cenário a análise entre instituições é descritiva/comparativa, e isso precisa ser dito.
- **Erro grave — variável dependente sem definição operacional primária.** O texto lista oito famílias de métricas (7.7) e dezenas de configurações (7.5). Sem métrica primária pré-especificada por hipótese, o estudo fica exposto a multiplicidade: entre tantas combinações, algo sempre "funciona". Recomenda-se um plano de análise pré-registrado (ainda que internamente, no repositório), com uma métrica primária por hipótese (por exemplo, inclinação e intercepto de calibração para H1; log-loss fora do tempo para H2; razão de degradação para H3; erro relativo de ECL agregada para H4) e as demais como secundárias.
- **Erro grave — horizonte de PD incompatível com ECL vitalícia.** A ECL do segundo estágio é vitalícia (IFRS 9, § 5.5.3; Res. CMN 4.966). Com PD de 12 meses apenas, o protótipo calcula ECL do primeiro estágio e não responde pela maior parte da provisão em carteiras deterioradas. Ou se delimita explicitamente o estudo ao primeiro estágio (aceitável, mas tem de estar na pergunta e no título), ou se adota sobrevivência em tempo discreto desde o início (Saavedra et al., 2024, já disponível na pasta, faz exatamente isso com riscos competitivos).
- **Erro grave — identificação do componente macroeconômico.** A especificação da seção 5.3 soma f_θ(X), α_j, γ_c e s_{j,c,t}. Se f_θ for treinado com identificadores de instituição e carteira, α_j e γ_c duplicam efeitos; se s_{j,c,t} for livre por período, equivale a efeito fixo de tempo e absorve toda a macroeconomia, tornando a seleção de variáveis inidentificável. A formulação precisa ser em dois estágios: (1) modelo-base sem identificadores de grupo e sem variáveis macro; (2) recalibração logística por grupo (intercepto e inclinação) com encolhimento para o modelo global; (3) componente macro estimado no nível carteira-período sobre as taxas de default agregadas, com poucas variáveis e regularização — o que, de resto, é o que a tensão teórica da lacuna exige.
- **Erro grave — vintages macroeconômicos.** O SGS/BCB e o SIDRA/IBGE não fornecem, em regra, séries em tempo real (*vintages*). Reconstruí-las é trabalhoso e, para várias séries, impossível. Uma solução consistente com o requisito de "informação razoável e sustentável disponível na data" é usar as expectativas do Focus (BCB), que são por construção a informação disponível em cada data e representam previsões, não realizações. Isso resolve o problema de vazamento e fortalece o caráter prospectivo.
- **Erro menor — testes estatísticos.** Com poucas janelas fora do tempo, comparações pareadas têm baixo poder; o texto deve prever testes de acurácia preditiva do tipo Diebold–Mariano sobre perdas por período e bootstrap agrupado por contrato e período. Para a regressão logística com poucos eventos, prever separação quase completa e estimação penalizada (Firth).
- **Erro menor — cenário de escassez por percentual.** O próprio texto reconhece que o número de defaults importa mais que o percentual; então o desenho deve ser definido por número de eventos (por exemplo, 25, 50, 100, 200 defaults no treino), não por 10/25/50/100%.
- **Erro menor — ética e dados.** Há menção a anonimização e acordos, mas não a base legal (LGPD) nem ao termo de cessão de dados; para dados secundários anonimizados de instituições, a submissão a CEP costuma ser dispensável, mas isso deve ser afirmado e justificado.
- **Risco de exequibilidade.** O produto cartesiano da seção 7.5 ultrapassa cem configurações antes das repetições. O cronograma de doze meses depende de dados ainda não obtidos. Recomenda-se um critério de decisão explícito ("se não houver microdados até o mês 3, o estudo migra para o Cenário B com pergunta ajustada") e um plano fatorial reduzido pré-especificado: algoritmo (logística, GBM) × regime (global, local, híbrido) × macro (M0, M1, M2) = 18 células, por quatro níveis de defaults.

### 1.7 Encadeamento e vocabulário

O texto está em formato de projeto esquemático, o que é aceitável nesta fase; a introdução, porém, precisará ser reescrita em prosa com lógica de funil (do reconhecimento de perdas esperadas à calibração de PD em instituições S3/S4) e com parágrafo de síntese metodológica. Vícios a eliminar: "Além disso" (seção 1.1), "portanto" (seções 4.2 e 9.4). A primeira sentença da contextualização ("A mensuração de perdas de crédito constitui componente relevante...") é truísmo; a abertura deve partir do fato que motiva o estudo — por exemplo, a entrada em vigor da metodologia de perdas esperadas em 2025 e a assimetria de capacidade de modelagem entre segmentos. Afirmações como "A literatura tem discutido..." (seção 1.1) e "Estudos sobre ECL desenvolveram..." estão sem citação e devem recebê-la na versão em prosa.

---

## 2. Auditoria de formatação APA (7ª edição)

| Item | Desvio | Regra |
|---|---|---|
| Referências de periódico (Bikker & Metzemakers; Bushman & Williams; Laeven & Majnoni; Pool et al.) | Sem DOI | APA 7 exige DOI quando existente, no formato https://doi.org/... |
| Normas (CMN, BCB) | Sem URL e sem indicação de versão consolidada | Para documentos legais/normativos, indicar URL da fonte oficial e, quando pertinente, a data da consolidação consultada |
| Resolução BCB nº 352/2023 | Escopo incorreto (não se aplica a instituições financeiras) | Substituir pelas normas aplicáveis: Res. CMN 4.966/2021 e alterações; IN BCB 487/2024 para autorização de S4 |
| Diagrama da seção 5 | Sem rótulo "Figura 1" nem título | Figuras recebem número em negrito e título em itálico, acima do elemento |
| Tabelas das seções 6, 7.5, 12 e 13 | Sem rótulo "Tabela n" nem título | Tabelas recebem número em negrito e título descritivo em itálico, acima; sem bordas verticais |
| Seções 1.1 e 4 | Afirmações de literatura sem citação autor-data | Toda afirmação atribuída à literatura exige citação |
| GPPC (2016), IFRS Foundation (2014) | Sem URL/editor | Documentos institucionais exigem editora/URL |
| Equações | Não numeradas | Numerar (1), (2), (3) à direita, para referência no texto |

O uso de "et al." para três ou mais autores desde a primeira citação está correto; a grafia "Article 59" para artigos numerados também.

---

## 3. Recomendações de reescrita

**Questão de pesquisa — original:**
> Em que condições a personalização de modelos de Machine Learning por instituição e carteira, combinada com a seleção de variáveis macroeconômicas prospectivas, melhora a calibração e a estimação das perdas esperadas de crédito em instituições financeiras de menor porte com históricos limitados?

**Sugestão:**
> *Em que condições — definidas pelo número de eventos de inadimplência disponíveis e pela heterogeneidade entre carteiras — a personalização de modelos de probabilidade de inadimplência por instituição e carteira e a seleção de indicadores macroeconômicos específicos por carteira alteram a calibração das probabilidades de inadimplência e o erro de estimação das perdas esperadas de crédito em instituições financeiras brasileiras dos segmentos S3 e S4?*

**Objetivo geral — original:** "Desenvolver e avaliar uma arquitetura modular e adaptativa de Machine Learning para estimação de perdas esperadas de crédito..."

**Sugestão:** "Analisar em que condições, definidas pelo número de eventos de inadimplência e pela heterogeneidade entre carteiras, a personalização de modelos de probabilidade de inadimplência por instituição e carteira e a seleção de indicadores macroeconômicos específicos por carteira alteram a calibração das probabilidades de inadimplência e o erro de estimação das perdas esperadas de crédito em instituições financeiras dos segmentos S3 e S4."

**Objetivos específicos — sugestão (substituindo os oito atuais):**
1. Estimar modelos de probabilidade de inadimplência de referência (regressão logística regularizada) e de *gradient boosting* sob os regimes global, local e híbrido, com validação temporal fora do tempo.
2. Comparar a calibração e o erro de perdas agregadas entre os regimes em função do número de eventos de inadimplência no treinamento, mediante subamostragem controlada.
3. Verificar a contribuição incremental, fora da amostra, da seleção de indicadores macroeconômicos por carteira em relação a um conjunto uniforme de indicadores.
4. Mensurar a diferença e a defasagem temporal entre a perda esperada modelada e a provisão apurada pela metodologia regulatória aplicável à instituição, por carteira e período.

(A revisão sistemática, a construção da base e a documentação do protótipo passam a constar do capítulo de método como procedimentos.)

**H1 — original:** "...em pelo menos determinados perfis de carteira."
**Sugestão:** "Em carteiras com menos de *k* eventos de inadimplência no conjunto de treinamento, modelos híbridos com recalibração por grupo apresentam intercepto e inclinação de calibração mais próximos de (0, 1) e menor erro relativo de perdas agregadas do que modelos globais e locais; a diferença se anula a partir de um número de eventos a ser estimado." (*k* fixado antes da análise, por exemplo em 50.)

**H4 — original:** "...podem apresentar calibração e erro de ECL estatisticamente comparáveis..."
**Sugestão:** "A diferença de erro relativo de perdas agregadas entre a regressão logística regularizada e o *gradient boosting* situa-se dentro de uma margem de equivalência de ±δ pontos percentuais da provisão, verificada por teste de equivalência (TOST)." (δ justificado em termos de materialidade contábil.)

**Lacuna — original:** "A contribuição a verificar na RSL é a escassez de evidência empírica integrada sobre (i)... (ii)... (iii)... (iv)..."
**Sugestão de parágrafo:** "A literatura de aprendizado de máquina em risco de crédito concentra-se na discriminação em bases amplas (Lessmann et al., 2015; Gunnarsson et al., 2021), ao passo que a mensuração de perdas esperadas depende do nível das probabilidades, isto é, da calibração — dimensão reconhecidamente menos estudada (Van Calster et al., 2019) e a primeira a se degradar em carteiras com poucos eventos (Pluto & Tasche, 2005). A teoria de estimação com agrupamento parcial prevê que modelos híbridos superem modelos locais quando os grupos são pequenos (Gelman & Hill, 2007), mas não informa a magnitude do ganho nem o número de eventos a partir do qual ele se anula em carteiras de crédito. Em paralelo, os ajustes macroeconômicos prospectivos propostos para a IFRS 9 (Breed et al., 2023; Moodley et al., 2025) assumem conjuntos uniformes de indicadores; a seleção específica por carteira, estimada sobre séries temporais curtas, pode tanto capturar heterogeneidade real quanto sobreajustar. A evidência que permitiria decidir entre essas previsões, no regime de dados limitados em que operam as instituições dos segmentos S3 e S4, não foi localizada na revisão preliminar; a revisão sistemática descrita na seção 10 verificará esse ponto."

**Delineamento — original:** "Pesquisa quantitativa, aplicada e explicativa/preditiva, com desenvolvimento de artefato analítico..."
**Sugestão:** "Pesquisa quantitativa, de finalidade preditiva e avaliativa, com delineamento quase-experimental computacional: as configurações de modelagem (regime de personalização, conjunto macroeconômico, número de eventos de treinamento) são manipuladas pelo pesquisador sobre dados observacionais de crédito, e o desempenho é mensurado fora do tempo. O estudo segue o protocolo de benchmarks comparativos em risco de crédito (Lessmann et al., 2015); o protótipo computacional é instrumento de pesquisa, não objeto."

**Enquadramento regulatório — original (seções 1.1 e 9.3):** "...a Resolução CMN nº 4.966/2021 e a Resolução BCB nº 352/2023 integram o arcabouço regulatório..." / "Não pressupõe que S5 possa optar indistintamente pela metodologia completa..."
**Sugestão:** "No Brasil, a Resolução CMN nº 4.966/2021, em vigor desde 1º de janeiro de 2025, disciplina a mensuração de perdas esperadas das instituições financeiras e prevê metodologia completa para os segmentos S1 a S3 e simplificada para os segmentos S4 e S5. A Instrução Normativa BCB nº 487/2024 faculta às instituições do S4 o pedido de autorização para uso da metodologia completa, condicionado, entre outros requisitos, à comprovação de uso das perdas esperadas na gestão de crédito há pelo menos dois anos (art. 6º). O estudo delimita-se, por isso, às instituições dos segmentos S3 e S4, para as quais a estimação de probabilidades de inadimplência tem consequência contábil direta ou prospectiva." (Conferir o artigo da Res. CMN 4.966 que fixa a regra por segmento no texto consolidado antes da redação final.)

---

## 4. Parecer síntese

**Pontos fortes.** O projeto parte de um problema real e bem percebido — a assimetria de capacidade de modelagem entre segmentos prudenciais após a entrada em vigor do regime de perdas esperadas —, demonstra domínio técnico de validação temporal, vazamento, calibração e governança de modelos, e tem a maturidade de não reivindicar superioridade do ML nem ineditismo de arquitetura. A separação entre motor econômico e camada regulatória é decisão correta. A pergunta é formalmente adequada e as hipóteses são, em essência, boas conjecturas.

**O que precisa ser reestruturado, em ordem de prioridade.**
1. **Lacuna:** abandonar a formulação de combinação e adotar a formulação de ponto cego teórico (calibração em regime de poucos eventos; tensão entre seleção macro específica e sobreajuste; magnitude não conhecida do ganho de agrupamento parcial). A lacuna deve ser demonstrada no projeto, não prometida à RSL.
2. **Teoria de base:** explicitar as duas lentes — qualidade/tempestividade da informação contábil e estimação com agrupamento parcial — e derivar as hipóteses delas.
3. **Alinhamento problema–objetivo:** reescrever o objetivo geral como resposta à pergunta, reduzir os específicos a quatro, retirar o vocabulário de engenharia.
4. **População e relevância:** delimitar aos segmentos S3 e S4, corrigir a citação da Res. BCB 352/2023 e usar a IN BCB 487/2024 como argumento de relevância prática; elevar a conciliação regulatória a objetivo, com métrica de tempestividade, para conectar o trabalho aos usuários externos da informação.
5. **Correções técnicas:** H1 falsificável; H4 como equivalência; horizonte de PD coerente com ECL vitalícia ou delimitação explícita ao primeiro estágio; especificação em dois estágios para evitar duplicação de efeitos; expectativas Focus como variáveis prospectivas; escassez definida por número de eventos; métrica primária por hipótese; discussão de viés de seleção.
6. **Exequibilidade:** plano fatorial reduzido e critério de decisão sobre dados até o terceiro mês.

Com essas alterações, a proposta tem condições de ser apresentada como pesquisa empírica em Contabilidade com contribuição metodológica identificável, e não como projeto de desenvolvimento de sistema.

---

## 5. Referências sugeridas para ancorar a lacuna (a conferir nas fontes primárias)

Os títulos abaixo são conhecidos da literatura; metadados, volumes, páginas e DOIs devem ser confirmados antes da inclusão. Os marcados com (*) já estão na pasta de leituras do mestrado.

- Beatty, A., & Liao, S. (2011). Do delays in expected loss recognition affect banks' willingness to lend? *Journal of Accounting and Economics*.
- Beatty, A., & Liao, S. (2014). Financial accounting in the banking industry: A review of the empirical literature. *Journal of Accounting and Economics*.
- Efron, B., & Morris, C. (1975). Data analysis using Stein's estimator and its generalizations. *Journal of the American Statistical Association*.
- Gelman, A., & Hill, J. (2007). *Data analysis using regression and multilevel/hierarchical models*. Cambridge University Press.
- Gunnarsson, B. R., vanden Broucke, S., Baesens, B., Óskarsdóttir, M., & Lemahieu, W. (2021). Deep learning for credit scoring: Do or don't? *European Journal of Operational Research*.
- Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The elements of statistical learning* (2nd ed.). Springer. (*)
- Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. *MIS Quarterly*. (apenas se DSR for adotado)
- Lessmann, S., Baesens, B., Seow, H.-V., & Thomas, L. C. (2015). Benchmarking state-of-the-art classification algorithms for credit scoring: An update of research. *European Journal of Operational Research*.
- Lu, Y., & Nikolaev, V. V. Expected loan loss provisioning: An empirical model. *The Accounting Review*. (*)
- Moodley et al. (2025). A pragmatic macroeconomic default risk adjustment in developing countries. (*)
- Nori, H., Jenkins, S., Koch, P., & Caruana, R. (2019). InterpretML: A unified framework for machine learning interpretability. arXiv. (para o EBM)
- Pluto, K., & Tasche, D. (2005). Thinking positively. *Risk*. (estimação de PD em carteiras com poucos defaults)
- Saavedra et al. (2024). Probability of default for lifetime credit loss for IFRS 9 using machine learning competing risks survival analysis. (*)
- Van Calster, B., McLernon, D. J., van Smeden, M., Wynants, L., & Steyerberg, E. W. (2019). Calibration: The Achilles heel of predictive analytics. *BMC Medicine*.
- Vasicek, O. (2002). The distribution of loan portfolio value. *Risk*. (fundamento do ajuste macro sobre log-odds)

**Cadeias de busca complementares (Web of Science / Scopus), para fechar a lacuna reformulada:**
- `TS=(("probability of default" OR "credit scoring") AND (calibration OR "calibrat*") AND ("small sample*" OR "low default" OR "limited data" OR "few events"))`
- `TS=(("hierarchical" OR "multilevel" OR "partial pooling" OR "transfer learning" OR "federated") AND ("credit risk" OR "probability of default" OR "credit scoring"))`
- `TS=(("IFRS 9" OR "expected credit loss*" OR CECL) AND ("macroeconomic" OR "forward-looking") AND (overfit* OR "out-of-sample" OR "out-of-time" OR "variable selection"))`
- `TS=(("loan loss provision*" OR "expected credit loss*") AND (timeliness OR "timely recognition") AND (bank* OR "credit union*" OR cooperativ*))`
- SPELL / bases nacionais: `("perda esperada" OR "PCLD" OR "provisão para créditos") AND ("Resolução 4.966" OR "IFRS 9") AND (cooperativ* OR "segmento S4" OR "instituições de menor porte")`

**Fontes normativas consultadas para este parecer:** Voto BCB 170/2023 (fundamenta a Res. BCB 352/2023; delimita seu escopo e revogações) — https://normativos.bcb.gov.br/Votos/BCB/2023170/Voto_do_BC_170_2023.pdf; Res. BCB 352/2023 (texto) — https://www.leasingabel.com.br/wp-content/uploads/2024/03/Resolucao-BCB-352-23nov23.pdf; IN BCB 487/2024 — https://www.normasbrasil.com.br/norma/instrucao-normativa-487-2024_461679.html.
