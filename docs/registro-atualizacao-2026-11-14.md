# Registro de atualização — 14/11/2026

## Escopo

Reformulação da proposta de dissertação a partir do [parecer metodológico de 14/11](parecer/parecer-metodologico-v3-2026-11-14.md) sobre a [proposta v3](proposta/proposta-dissertacao-v3-2026-11-13.md), e alinhamento dos documentos dependentes. Resultado: [proposta v4](proposta/proposta-dissertacao-v4-2026-11-14.md), versão documental 0.4.0.

## Estado inicial do repositório

A atualização de 13/11 (v3) estava na árvore de trabalho, sem commit. Foi registrada em commit próprio, sem alteração de conteúdo, antes de qualquer mudança da v4. O protocolo de mini revisão sistemática e o arquivo de consultas Web of Science, criados em 14/11 durante esta revisão, foram registrados em commit separado, também sem alteração.

## Decisões de reformulação

1. **Título e questão (primeira redação; alterado na revisão 2).** Título alinhado ao método (transferência e recalibração de PD). Questão única, com a variável dependente ao final.
2. **Variável dependente.** "Qualidade" da PD com três atributos mensuráveis: pontuação probabilística (log-loss), calibração (intercepto e inclinação) e viés monetário.
3. **Critério de adequação.** Três classes — adequada, inadequada, inconclusiva —, com intervalos contidos em faixas de tolerância fixadas antes do teste. Substitui o construto "confiável".
4. **Teoria de base.** Representação fidedigna e usuário externo (CPC 00 R2), com tabela de correspondência entre atributos contábeis e medidas da estimativa; literatura de contabilidade bancária como contexto.
5. **Hipóteses (primeira redação; ver revisão 2).** H1 (disponibilidade), H2 (heterogeneidade), H3 (atenuação pela recalibração), H4 (viés monetário) e contraste bilateral C1 (adaptado versus agrupado), em família fechada com ajuste de Holm. Resultado derivado: fronteira de utilidade n\*(d). As hipóteses H1–H3 da v3 não conservam numeração nem significado.
6. **Regimes (primeira redação; alterado na revisão 2).** Acrescentados taxa base e local reduzido. Regressão logística regularizada como algoritmo principal; gradient boosting como robustez.
7. **Fatores experimentais.** Disponibilidade em malha de seis níveis; distância induzida por subamostragem da origem com classificador de domínio, em cinco níveis. Distância observada descrita em três componentes.
8. **Inferência.** Condicional às carteiras estudadas, com efeitos fixos por par e janela. Associação com distância observada é descritiva, salvo número mínimo de destinos independentes. Efeito nulo só com margem de irrelevância.
9. **Desdobramento contábil.** Viés monetário como medida principal; diferença de LP12 entre regimes rebaixada a análise de sensibilidade.
10. **Precisão e validade.** Precisão-alvo declarada; seção de validade interna, de construto e externa.
11. **Dados.** Desenho executável com uma única instituição (cenário B); estudo-piloto em base pública nos meses 1 a 3.
12. **Redação.** Texto afirmativo, sem remissões a versões anteriores; pendências reunidas em uma seção; lista de referências em APA, com as normas incluídas.

## Revisão 2 (mesmo dia): Machine Learning e aplicação

A primeira redação da v4 reduziu o Machine Learning a análise de robustez e retirou o termo do título. Por decisão do autor, o Machine Learning permanece no núcleo e o objetivo de aplicação volta a orientar o desenho. A crítica do parecer (título além do método; algoritmo sem hipótese) foi atendida elevando o método, e não reduzindo a promessa:

- Título restituído; a complexidade do algoritmo passa a ser variável independente da questão.
- Logística regularizada e gradient boosting em paridade; regime de adaptação por reponderação de importância.
- Família B de hipóteses: H5 (complexidade do algoritmo) e C2 (reponderação versus recalibração, bilateral). A reponderação não é avaliada sob distância induzida, por circularidade.
- Custo operacional como medida descritiva da capacidade operacional exigida.
- Regra de seleção de regime, derivada e avaliada em janelas distintas, como contribuição metodológica e núcleo da aplicação posterior.
- Seção de aplicação posterior na proposta: a dissertação entrega método validado e protótipo; a ferramenta é desenvolvimento posterior.

A formulação "como desenvolver estimativas confiáveis" foi mantida como motivação aplicada, e não como questão de pesquisa, por descrever um problema de engenharia; a questão científica é a das condições em que cada estratégia produz estimativas adequadas. Versão documental 0.4.1.

## Correções ao próprio parecer

- A fronteira n\* diminui com a distância entre origem e destino; o parecer havia indicado a direção oposta.
- O critério de adequação exige intervalo contido na faixa; o parecer havia sugerido apenas que o intervalo contivesse o valor ideal.

## Decisões que cabem ao autor e à orientação

Adotadas na v4 como proposta, e não como definição:

- Viés monetário e H4 como conteúdo contábil do desdobramento, em vez de rebaixar todo o objetivo a análise de sensibilidade.
- Inferência condicional às carteiras, em vez de inferência sobre uma população de carteiras.
- Valores candidatos das faixas (0,2), da malha e do número de níveis de distância.
- Na revisão 2: adaptação por reponderação como único regime de adaptação próprio de ML no núcleo (ajuste fino e modelos hierárquicos como extensões); duas famílias de hipóteses; regra de seleção como análise secundária.

## Arquivos

**Criados:** proposta v4; parecer sobre a v3; [protocolo experimental v4](metodologia/protocolo-experimental-v4.md); [adendo de revisão da literatura](revisao/protocolo-revisao-literatura.md); este registro.

**Atualizados no local:** README, CHANGELOG, `CITATION.cff`, `pyproject.toml`, [configuração](../configs/experimento-exemplo.yaml), [dicionário de dados](../data_dictionary/README.md), [notas normativas](normativo/notas-verificacao-normativa.md) (adendo), [mapa do protótipo](metodologia/prototipo-e-limites.md), [índice do histórico](historico/README.md), [apresentação](index.html) com sua fonte e README, e docstrings de `ecl_suficiencia`, `reporting`, `local_recalibration`, `pd_models` e `macro_selection`. Nenhuma lógica de cálculo ou assinatura foi alterada.

**Preservados sem alteração:** propostas v1, v2 e v3; parecer de 05/11; protocolo v3; registro de 13/11; acervo `historico/2026-11-06-v2/`; protocolo de mini revisão e consultas Web of Science. O estado dos documentos da v3 atualizados no local está no commit da v3.

## Relação com o protocolo de mini revisão

O [protocolo de mini revisão sistemática](metodologia/mini-revisao-protocolo-wos-2026-11-14.md) refere-se à v3 e permanece como protocolo operativo. O adendo registra a correspondência com a v4, uma rota adicional de busca para a literatura contábil e os critérios de refutação da lacuna. A atualização do próprio protocolo para a v4 fica a critério do autor.

## Verificações

- Referências novas (Beatty e Liao, 2014; Riley et al., 2021; Shmueli, 2010; CPC 00 R2) e lista completa de autores de Van Calster et al. (2019): metadados conferidos por busca em 14/11/2026. Não houve leitura integral; a situação está no adendo de revisão.
- Datas das normas conferidas por busca em fontes secundárias; dispositivos não relidos.
- Seis testes existentes dos auxiliares: aprovados. Não validam a proposta.
- Configuração YAML, `CITATION.cff` e `pyproject.toml`: leitura válida; versão 0.4.1 consistente com o pacote.
- 96 links locais dos documentos correntes, históricos mantidos no local e da apresentação: nenhum destino ausente.
- Apresentação: 21 slides (revisão 2) reconstruídos pelo construtor Python, com resultado idêntico ao arquivo versionado; verificação automática de transbordamento em 1280×782 sem ocorrências; exemplo interativo exercitado, sem erros de JavaScript.
- Código Python: compilação sem erros.

## O que esta revisão não resolve

Acesso a microdados; execução da mini revisão sistemática; justificação dos parâmetros do critério; conferência normativa por instituição e data-base, incluindo a exigência de estimativa própria sob a metodologia simplificada. Nenhum experimento foi executado e nenhum resultado foi produzido.
