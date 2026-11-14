# Parecer metodológico sobre a proposta v3 — 14/11/2026

Parecer emitido em 14/11/2026 sobre a [proposta v3 de 13/11/2026](../proposta/proposta-dissertacao-v3-2026-11-13.md), na perspectiva de avaliação metodológica em Controladoria e Contabilidade. Motivou a [proposta v4](../proposta/proposta-dissertacao-v4-2026-11-14.md). As citações normativas da v3 não foram conferidas neste parecer. Uma errata ao final corrige dois pontos do próprio parecer.

**Veredito.** A v3 é um bom protocolo experimental e ainda não é uma proposta de dissertação defensável em um programa de Contabilidade. A higiene preditiva é superior à média; faltam lacuna demonstrada, teoria contábil de base, definição operacional do construto central e dados.

## 1. Diagnóstico metodológico

### Erros graves

**G1. O construto "confiável" não tem definição operacional (§1.3, §2.1, §3).** A questão pergunta quando as PDs são confiáveis, um atributo absoluto. As três hipóteses testam apenas diferenças de log-loss entre modelos, um atributo relativo. O log-loss é uma regra de pontuação: penaliza probabilidades distantes do resultado observado, mas não diz se a PD está correta em nível. Um modelo adaptado pode vencer o local e ambos estarem mal calibrados. O §3 reconhece o risco e não fixa critério. Trata-se de falha de validade de construto: a medida não captura o conceito anunciado.

**G2. A lacuna não está demonstrada (§4.4).** O texto a chama de "hipótese de lacuna". A formulação "pode produzir evidência útil no contexto brasileiro" é lacuna de contexto, e ausência de estudos sobre um recorte não é ponto cego teórico. O referencial tem quatro parágrafos e duas citações; das sete referências, duas tiveram apenas resumo conferido e uma aguarda leitura crítica. A proposta não nomeia o tipo de contribuição.

**G3. Não há teoria contábil de base nem vínculo com a linha Usuários Externos.** O §4.1 menciona representação fidedigna e incerteza de mensuração sem citar a Estrutura Conceitual nem a literatura sobre qualidade e discricionariedade de provisões. O usuário externo não aparece. Falta também responder para quem a PD modelada é relevante se S4/S5 podem aplicar a metodologia simplificada.

**G4. O objetivo 4 é mecânico (§7.1).** ΔLP12 = Σ(PD_A − PD_B) × LGD × EAD é consequência aritmética dos objetivos 1 a 3. O texto admite que é "propagação aritmética, não evidência". O único elo contábil da dissertação não tem hipótese nem teoria.

**G5. A unidade de inferência não sustenta H2 (§6.1, §6.6).** H2 estima o coeficiente da distância sobre pares origem–destino. Com uma instituição, haverá poucos pares, e eles não são independentes. A reamostragem por tomadores mede a incerteza dentro de cada par, não entre pares. A distância proposta é marginal e de covariáveis, e o próprio §3 reconhece que ela não identifica mudança na relação entre covariáveis e inadimplência.

**G6. O objeto empírico não existe (§8, §12).** Não há microdados confirmados. Evento, coortes, distância, malha e plano de análise estão em aberto. O cenário C invalida o título e a parte contábil.

### Erros de gravidade intermediária

- **Questão dupla (§1.3):** duas perguntas unidas por "e"; o objetivo geral replica o defeito com dois verbos.
- **Título promete mais que o método:** "modelagem adaptativa de perdas esperadas com Machine Learning" descreve uma recalibração logística de dois parâmetros aplicada à PD.
- **H1 e H3 têm baixo conteúdo empírico:** decorrem de propriedades conhecidas de estimadores com encolhimento. O que interessa é o ponto de cruzamento entre modelo local e adaptado.
- **Desalinhamento objetivos–hipóteses:** o objetivo 1 compara quatro regimes e H1 contrasta dois; o modelo agrupado não tem hipótese; o gradient boosting não aparece em hipótese alguma; a família do ajuste de Holm é indefinida; o objetivo 3 reúne utilidade, estabilidade e incerteza, e H3 cobre só a primeira.
- **Faltam referências ingênuas:** PD constante igual à taxa histórica e modelo local parcimonioso.
- **Escassez simulada não é escassez real:** sortear 10% de uma carteira grande preserva política, sistemas e qualidade de dados de instituição madura.
- **Precisão não especificada:** promete-se planejar a amostra "pela precisão desejada" sem declará-la.

### Erros menores

- Registro defensivo: dezenas de frases dizem o que o trabalho não fará.
- Remissões internas ininteligíveis para a banca ("H1–H5 da v2", "k=50 do auxiliar histórico", nome do pacote).
- Infinitivo de comando nos §§6.6, 7, 9 e 10.
- Oscilação terminológica (default, inadimplência, proxy, ativo problemático) e anglicismos sem glosa.
- Conectivo automático "portanto" no §1.1.
- Tipologia de pesquisa sem apoio na literatura metodológica.

## 2. Auditoria de formatação APA (7ª edição)

| Desvio | Regra |
|---|---|
| "Van Calster, B., et al. (2019)" na lista | A lista traz até 20 autores; "et al." só no texto |
| Lista fora de ordem alfabética | Ordenação pelo sobrenome do primeiro autor |
| IFRS Foundation sem data | Ano obrigatório |
| Resoluções citadas e ausentes da lista | Toda fonte citada deve constar |
| Anotações de status dentro das entradas | A entrada contém apenas elementos bibliográficos |
| Link no corpo do texto (§7.1) | Sistema autor-data |
| "BCBS (2015)" sem introdução da sigla | Nome por extenso na primeira citação |

## 3. Recomendações e seu atendimento na v4

| Recomendação | Atendimento na v4 |
|---|---|
| Questão única, variável dependente ao final, sem "confiável" | §1.2 |
| Critério operacional de adequação | §6.6, com três classes |
| Teoria contábil de base e usuário externo | §1.1, §1.3, §3.1 e Tabela 1 |
| Conteúdo contábil para o desdobramento monetário | Viés monetário (§6.6, §7) e H4 |
| Hipóteses em torno do cruzamento; modelo agrupado; família fechada | §4: H1–H4, C1, fronteira n\*(d) |
| Unidade de inferência | §6.4 (distância induzida) e §6.9 (inferência condicional) |
| Referências ingênuas | §6.5, regimes 1 e 3 |
| Escassez simulada e validade | §6.11 |
| Precisão declarada | §6.10 |
| Lacuna | §3.4: candidata, com critérios de refutação; revisão por executar |
| Dados | §8: desenho executável no cenário B; piloto público; pendência mantida |
| Redação e APA | Texto afirmativo; lista de referências refeita |

G2 e G6 não se resolvem por redação. A v4 as estrutura e as mantém como pendências (seção 11).

## 4. Parecer síntese

**Pontos fortes da v3.** Controle de vazamento de informação; distinção entre discriminação e calibração; definição prévia de transferência negativa; separação entre LP12 ilustrativa e perda esperada; sinais esperados algebricamente corretos; franqueza sobre limites.

**Prioridades.** (1) Confirmar os dados. (2) Executar a revisão e demonstrar a lacuna. (3) Definir a adequação da PD e reescrever questão e objetivo. (4) Construir a base contábil. (5) Reformular hipóteses e unidade de inferência. (6) Reescrever em registro afirmativo e corrigir a APA.

## Errata do parecer

1. **Direção da fronteira.** A versão do parecer entregue em conversa sugeriu a hipótese de que o volume local de cruzamento "aumenta com a distância origem–destino". A direção correta é a oposta: quanto maior a distância, menos útil é a informação da origem e mais cedo o modelo local alcança o adaptado. A v4 adota a direção correta (n\* diminui com a distância).
2. **Critério de adequação.** O parecer sugeriu exigir que o intervalo do intercepto "contenha zero". Esse critério aprova estimativas imprecisas. A v4 exige que o intervalo esteja contido em uma faixa de tolerância e cria a classe inconclusiva.
