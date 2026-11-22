# Roadmap de desenvolvimento da dissertação — ECL e Machine Learning

**Projeto:** Modelagem adaptativa de probabilidades de inadimplência com Machine Learning: experimentos de transferência entre carteiras sintéticas e implicações para a mensuração de perdas esperadas de crédito.  
**Documento-base:** `proposta-dissertacao-v5-2026-11-14.md` (versão 5, 14/11/2026).  
**Estado:** planejamento proposto; submetido à revisão do(a) orientador(a).  
**Horizonte indicativo:** 12 meses contados da aprovação do escopo. **Não** equivale à data regulamentar de defesa.  
**Documentos complementares:** [protocolo operacional Q0–Q6](revisao/protocolo-busca-wos-q0-q6.md) e [antecedente v5](mini-rsl-wos-ecl-ml-v5.md).

> **Premissa científica.** O problema central não é construir um simulador de bancos, nem uma solução comercial: é identificar **em que condições** disponibilidade de dados locais, heterogeneidade origem–destino e complexidade do algoritmo favorecem ou prejudicam a estimação de PD por modelos locais, agrupados, transferidos e adaptados. O simulador é o ambiente experimental; a repercussão na ECL é a aplicação contábil subordinada. Resultados condicionais a DGPs sintéticos **não** validam automaticamente modelos para provisionamento de instituições reais.

---

## 1. Objetivo, escopo e critérios de êxito

### 1.1 Objetivo do projeto

Planejar, implementar, documentar e avaliar um estudo quantitativo de simulação de Monte Carlo, com carteiras de crédito sintéticas inspiradas na estrutura pública do Documento 3040 e com calibração de características agregadas por dados do SCR.data (e, quando útil, IF.data). O estudo comparará estratégias de aprendizado e adaptação de modelos de PD, quantificará condições de transferência negativa e investigará a propagação de erros de PD para medidas **sintéticas** de ECL.

### 1.2 Objetos distintos que não devem ser confundidos

| Objeto | Papel no estudo | O que não autoriza concluir |
|---|---|---|
| Leiaute público 3040 | Referência estrutural/semântica de operações e exposições | Que o XML de um 3040 real esteja disponível ou seja livre para pesquisa |
| SCR.data | Calibração e verificação de agregados | Que inadimplência de estoque >90 dias seja PD de primeiro evento em 12 meses |
| Instituições virtuais | Perfis estilizados sob DGPs documentados | Que reproduzam instituições brasileiras individuais |
| PD verdadeira do DGP | Referência conhecida para avaliar erro do estimador | Que corresponda à PD individual observável em instituições reais |
| ECL sintética | Medir consequência contábil condicional a LGD/EAD/desconto simulados | Que demonstre conformidade regulatória ou necessidade real de provisão complementar |
| Protótipo Python | Reprodutibilidade do experimento | Que seja um produto comercial validado |

### 1.3 Definição de conclusão satisfatória

- [ ] Mini revisão sistematizada executada, documentada e com lacuna delimitada sem alegar ineditismo não comprovado.
- [ ] Protocolo ADEMP aprovado e congelado antes da fase confirmatória.
- [ ] Dicionário sintético e mapeamento de atributos ao 3040 com versão/data-base registradas.
- [ ] SCR.data extraído de forma reproduzível; calibrado e verificado por métricas comparáveis.
- [ ] DGPs independentes, com hipóteses e parâmetros explícitos, incluindo relações lineares, não lineares e heterogeneidade.
- [ ] Testes automatizados validam a coerência dos saldos, dos eventos e do tempo.
- [ ] Modelos e regras de adaptação avaliados sem acesso a rótulos futuros ou às PDs verdadeiras do simulador.
- [ ] Contrastes pareados e seus erros de Monte Carlo reportados; casos com zero eventos tratados explicitamente.
- [ ] Resultados de ECL apresentados como simulação com premissas de LGD, EAD e desconto documentadas.
- [ ] Discussão explicita validade interna, validade de construto e limitação de validade externa.
- [ ] Dissertação final, código e materiais reproduzíveis entregues conforme regras do programa.

---

## 2. Cronograma executivo (12 meses indicativos)

**Legenda:** `●` execução principal, `○` consolidação/revisão, `◆` marco de decisão. As fases podem se sobrepor.

| Etapa | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10 | M11 | M12 |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| E01 Escopo e governança | ● | ○ | | | | | | | | | | |
| E02 Mini RSL / lacuna | ● | ● | ○ | | | | | | | ○ | | |
| E03 Base conceitual e normativa | ● | ● | ○ | | | | | | | | | |
| E04 3040 e dicionário sintético | | ● | ● | ○ | | | | | | | | |
| E05 SCR.data / IF.data e calibração | | ● | ● | ● | | | | | | | | |
| E06 DGPs e piloto do simulador | | | ● | ● | ◆ | | | | | | | |
| E07 ADEMP final e congelamento | | | | ● | ◆ | | | | | | | |
| E08 Algoritmos e validação temporal | | | | ● | ● | ● | | | | | | |
| E09 Monte Carlo confirmatório | | | | | | ● | ● | ● | | | | |
| E10 ECL, robustez e seletor | | | | | | | ● | ● | ● | ● | | |
| E11 Inferência e interpretação | | | | | | | | ● | ● | ● | ○ | |
| E12 Redação, revisão e defesa* | ● | ○ | | ● | ○ | ● | ○ | ○ | ● | ● | ● | ◆ |

* **Atenção ao calendário institucional:** prazos de projeto, qualificação, depósito, banca e defesa serão inseridos após conferência das exigências e da situação individual no PPGCONT/UFRGS. O roteiro de 12 meses é um plano técnico e **não** afirma que defesa ocorrerá necessariamente no M12.

### Marcos de decisão (gates)

| Gate | Quando | Decisão | Evidência mínima |
|---|---|---|---|
| G1 — Lacuna e escopo | Fim do M2 | Prosseguir/reformular contribuição | Matriz da mini RSL, questão e hipóteses coerentes |
| G2 — Integridade da base | Fim do M3 | Autorizar desenvolvimento do DGP | Dicionário versionado e fonte pública documentada |
| G3 — Simulador plausível | Fim do M4 / início M5 | Autorizar estudo confirmatório | Testes de integridade e relatório de calibração sem confundir estoque e fluxo |
| G4 — Protocolo congelado | M5 | Congelar DGPs, métricas, contrastes e sementes | ADEMP e plano estatístico aprovados, resultados confirmatórios ainda não examinados |
| G5 — Precisão alcançável | M6 | Definir nº de replicações | Piloto com erro-padrão Monte Carlo e orçamento de execução |
| G6 — Resultados interpretáveis | M9–M10 | Ampliar ou reduzir análises secundárias | Contrastes, falhas, incerteza e sensibilidade relatados |
| G7 — Entrega acadêmica | M12, sujeito ao programa | Submeter/discutir versão final | Texto, anexos, reprodutibilidade e checklist de limitações |

---

## 3. Etapas operacionais detalhadas

### E01 — Formalização do escopo e organização do projeto (M1)

**Dependências:** proposta v5 lida integralmente; alinhamento inicial com orientação.

**Atividades**
- [ ] Confirmar título provisório, linha de pesquisa e diferença entre objeto principal (PD) e desdobramento contábil (ECL).
- [ ] Registrar questão de pesquisa, objetivos, H1–H4 e C1 com métricas e comparadores definidos.
- [ ] Fixar unidade de previsão (contrato–data-base), destino/origem, evento de primeiro atraso >90 dias e horizonte principal de 12 meses; manter horizontes de 3/6 meses como extensão opcional.
- [ ] Distinguir limitação de dados da instituição de restrição de orçamento/equipe (esta última é dimensão descritiva).
- [ ] Definir política de versionamento Git, revisão por pares/orientação, registro de decisões e organização de dados/código.
- [ ] Consultar datas e requisitos oficiais do programa para qualificação e defesa; adaptar calendário.

**Entregáveis:** `docs/governanca/termo-de-escopo.md`, `docs/governanca/registro-decisoes.md`, `docs/governanca/cronograma-academico.md`.

**Critério de saída:** uma pergunta científica principal, sem compromisso de demonstrar suficiência de provisões reais ou concluir desenvolvimento comercial.

### E02 — Mini revisão sistematizada e teste da lacuna (M1–M2)

**Dependências:** E01; [protocolo de busca Q0–Q6](revisao/protocolo-busca-wos-q0-q6.md).

**Estrutura preparada em 15/11/2026:** protocolo, registros e modelos vazios disponíveis. A execução da revisão e o gate G1 permanecem pendentes.

**Atividades**
- [ ] Formular perguntas secundárias da revisão: transferência/heterogeneidade; poucas inadimplências; calibração; simulação; ECL.
- [ ] Executar Q0 exploratória, Q1–Q2 como núcleo e Q3–Q6 como suporte no WoS Core Collection; registrar data, índices, intervalo, filtros e totais retornados.
- [ ] Testar sensibilidade das consultas usando estudos-semente conhecidos e ajustar vocabulário de forma documentada.
- [ ] Exportar registros completos, referências e identificadores; deduplicar DOI/título.
- [ ] Selecionar por título/resumo e por texto completo com justificativa de exclusão; registrar fluxo inspirado em PRISMA 2020.
- [ ] Extrair: domínio, dados, população, transferência, DGP, calibração, métricas monetárias, validação, riscos de viés e achados.
- [ ] Executar busca reversa (referências) e prospectiva (citações) de estudos centrais; diferenciar descobertas fora da consulta inicial.
- [ ] Redigir síntese argumentativa: conhecimento estabelecido, contradições, lacuna candidata e desfechos possíveis caso a lacuna seja refutada.

**Entregáveis disponíveis:** [protocolo](revisao/protocolo-busca-wos-q0-q6.md), [registro](revisao/registro-buscas.md), [fluxo PRISMA](revisao/fluxo-prisma.md), [triagem](../literature/processed/triagem_estudos.xlsx) e [matriz](../literature/analysis/matriz-extracao.xlsx), ainda sem dados. **Após execução:** `literature/analysis/sintese-mini-rsl.md` e `literature/analysis/tabela-lacunas.md`.

**Critério de saída G1:** a contribuição potencial é escrita de modo verificável; não atribuir originalidade sem contraste com estudos de transferência e simulação em crédito.

### E03 — Fundamentação contábil, metodológica e regulatória (M1–M3)

**Dependências:** E01 e revisão em andamento.

**Atividades**
- [ ] Consolidar conceitos de PD, risco competitivo, ECL de 12 meses, LGD, EAD e desconto de fluxos.
- [ ] Revisar CPC 00 (R2): neutralidade, representação fidedigna e incerteza; tratar calibração como indicador estatístico parcial, não equivalência contábil automática.
- [ ] Conferir Resolução CMN 4.966/2021 e Resolução BCB 352/2023 **nas versões vigentes e datas-base pertinentes**; distinguir metodologia simplificada de necessidade de modelo formal PD–LGD–EAD.
- [ ] Conferir fontes e versões do Documento 3040, histórico de alterações e restrições de inferência a partir do leiaute.
- [ ] Documentar claramente a diferença entre inadimplência agregada de estoque do SCR.data e incidência de primeiro evento em 12 meses.
- [ ] Definir critérios de validação temporal, *data leakage*, inferência em Monte Carlo e limitações de validade externa.

**Entregáveis:** `docs/referencial/matriz-conceitual.md`, `docs/normativo/notas-verificacao.md`, `docs/metodologia/glossario-operacional.md`.

**Critério de saída:** conceitos, grandezas e público de aplicação são consistentes no texto inteiro.

### E04 — Arquitetura dos dados sintéticos e mapeamento ao 3040 (M2–M3)

**Dependências:** E03 e confirmação de versão do leiaute.

**Atividades**
- [ ] Documentar versão/data-base do 3040 e mapear **somente** campos/códigos efetivamente confirmados em documentação oficial.
- [ ] Definir tabelas: instituição–mês, tomador–mês, contrato, contrato–mês, cenário econômico, eventos/recuperação, verdade do DGP.
- [ ] Criar chave fictícia por instituição, tomador e contrato; permitir tomador com múltiplos contratos.
- [ ] Definir núcleo comum de preditores para transferência (sem presumir variáveis idênticas entre PF e PJ).
- [ ] Classificar atributos como: inspirados no 3040; adicionais de originação/comportamento; latentes; cenários; e resultados futuros.
- [ ] Estabelecer regras de integridade: fluxo de originação, cronograma, amortização, saldo, atraso, liquidação, renegociação e recuperação.
- [ ] Isolar fisicamente os campos de **verdade** (PD verdadeira, estados latentes) do conjunto permitido para treinamento.

**Entregáveis:** `data_dictionary/README.md`, `data_dictionary/3040-mapeamento.md`, `docs/arquitetura/esquema-relacional.md`, testes de integridade.

**Critério de saída G2:** gerador pode produzir registros coerentes sem dados pessoais reais; XML 3040 completo é opcional e não será tratado como pré-requisito científico.

### E05 — Coleta de fontes públicas e calibração agregada (M2–M4)

**Dependências:** E04; definições comparáveis com fontes públicas.

**Atividades**
- [ ] Selecionar indicadores públicos pertinentes do SCR.data; documentar cobertura, segmentação, séries, datas de extração, unidades e definições.
- [ ] Usar IF.data e BCB/SGS somente quando as métricas disponíveis forem úteis e comparáveis.
- [ ] Construir pipeline reproduzível de aquisição, dicionário, limpeza e agregação.
- [ ] Separar períodos/recortes utilizados para ajuste daqueles reservados para **verificação agregada** quando disponível.
- [ ] Calibrar participação por modalidade, exposição e trajetória agregada de inadimplência; não equiparar automaticamente estoque de atraso >90 dias à PD de 12 meses.
- [ ] Registrar parâmetros não identificáveis (correlações micro, relação condicional, severidade, recuperação) e intervalos plausíveis, com fonte ou justificativa.
- [ ] Comparar distribuição e evolução de indicadores sintéticos com dados públicos mediante tolerâncias pré-especificadas.

**Entregáveis:** `data/public/reference/manifest.yml`, `docs/dados/catalogo-fontes.md`, `docs/dados/hipoteses-calibracao.md`, `reports/calibracao-agregada.md`.

**Critério de saída:** plausibilidade agregada documentada **sem** alegar validação de microdados sintéticos com base apenas em marginais.

### E06 — DGPs, simulador longitudinal e piloto (M3–M5)

**Dependências:** E04/E05.

**Atividades**
- [ ] Implementar um DGP inicial simples com resultado de inadimplência e PD verdadeira conhecida.
- [ ] Expandir, se factível, para transições mensais: originação → adimplência → atraso → evento >90 dias, com liquidação, renegociação e saídas definidas.
- [ ] Implementar **DGP-L** (aditivo/logístico), **DGP-N** (não linear), **DGP-C** (mudança de composição) e **DGP-R** (mudança condicional); tratar **DGP-T** (mudança temporal/macroeconômica) como extensão condicionada.
- [ ] Parametrizar mecanismos com diferenças de taxa-base, suportes distintos, relações condicionais distintas, zero/poucos eventos e variáveis ausentes.
- [ ] Gerar PD verdadeira de primeiro evento em 12 meses **respeitando eventos competitivos**, se modelados.
- [ ] Implementar gerador de LGD/EAD e recuperação, quando previsto, com verdade sintética conhecida e testes de desconto.
- [ ] Executar testes unitários, de propriedade, invariantes e cenários extremos (nenhum evento; todos liquidados; duplicidade de tomador; censura).
- [ ] Usar estudo-piloto para estimar tempo/memória e escolher número viável de condições, sem explorar resultado confirmatório.

**Entregáveis:** `src/simulator/`, `configs/dgp/`, `tests/simulator/`, `reports/piloto-simulador.md`.

**Critério de saída G3:** o mecanismo gerador produz dados estruturalmente válidos e resultados agregados plausíveis; pressupostos ficam explícitos; diferenças microeconômicas não identificáveis variam entre DGPs.

### E07 — Pré-registro ADEMP e plano de análise (M4–M5)

**Dependências:** piloto E06; mini RSL suficientemente madura.

**Atividades**
- [ ] **Aims:** fixar pergunta, H1–H4 e C1; contrastes principais e secundários.
- [ ] **Data-generating mechanisms:** fixar famílias, parâmetros, níveis de volume e de distância, horizontes e mecanismos de saída.
- [ ] **Estimands:** definir diferenças esperadas de *log-loss*, erro frente à PD verdadeira, frequência de transferência negativa e diferença de ECL sintética.
- [ ] **Methods:** fixar R0 referência simples; R1 local; R2 agrupado; R3 transferido; R4 transferido + recalibração; regressão logística regularizada e *gradient boosting*.
- [ ] **Performance:** fixar *log-loss* primário, Brier, calibração, erro frente à verdade, AUC descritiva, ECL sintética e custo operacional.
- [ ] Definir limiares de relevância e critérios de adequação, com precisão estatística e custos; não confundir IC de calibração individual com erro de Monte Carlo.
- [ ] Planejar número de replicações pelo erro-padrão observado em piloto e orçamento; `100` é apenas valor inicial exploratório da v5, não meta fixada.
- [ ] Fixar partições treino/validação/teste e **replicações independentes** para testar a regra de seleção de regime.
- [ ] Congelar configurações e registrar hashes/versões antes da execução confirmatória.

**Entregáveis:** `docs/metodologia/ademp-protocolo.md`, `docs/metodologia/plano-analise.md`, `configs/experiment/confirmatorio.yml`, registro de aprovação.

**Critério de saída G4:** não se alteram cenários confirmatórios, métricas e contraste principal após observar resultados finais; emendas posteriores são datadas e rotuladas exploratórias.

### E08 — Implementação das estratégias e validação (M4–M6)

**Dependências:** E06, E07.

**Atividades**
- [ ] Construir pipelines comuns de imputação, codificação de categorias e seleção de variáveis **somente no treino**.
- [ ] Implementar R0–R4 com interfaces comparáveis; registrar quando um regime é não estimável.
- [ ] Ajustar hiperparâmetros sem vazamento de dados; separar origem e destino, evitando tomadores repetidos entre domínios.
- [ ] Implementar validação temporal com maturação de 12 meses e embargo adequado; nunca usar variáveis futuras, PD verdadeira ou recuperações futuras como atributos.
- [ ] Separar experimentos de zero eventos: R3 pode prever, mas a calibração local não poderá ser comprovada sem rótulos.
- [ ] Implementar métricas e seus testes, comparando saídas com casos conhecidos.
- [ ] Rodar testes de paridade em mesma amostra de avaliação e com as mesmas janelas para todos os regimes.

**Entregáveis:** `src/models/`, `src/evaluation/`, `tests/models/`, `reports/piloto-modelos.md`.

**Critério de saída:** pipeline reproduzível, sem vazamento, com documentação de regimes não estimáveis e comportamento em zero eventos.

### E09 — Experimento confirmatório Monte Carlo (M6–M8)

**Dependências:** Gates G3, G4 e G5.

**Atividades**
- [ ] Executar replicações independentes nos DGPs e níveis pré-especificados.
- [ ] Comparar modelos de forma **pareada** no mesmo conjunto de teste dentro de cada replicação.
- [ ] Salvar configurações, sementes, resumo por cenário/replicação, falhas e ambiente de execução.
- [ ] Monitorar erro de Monte Carlo dos estimandos principais, intervalo dos contrastes e distribuição de transferência negativa.
- [ ] Não tratar contratos nem datas-base correlacionadas dentro de uma replicação como replicações independentes.
- [ ] Reportar cenários em que a comparação é impossível porque o modelo local não pode ser ajustado.
- [ ] Não alterar desenho em função de resultados finais; análises acrescentadas serão identificadas como exploratórias.

**Entregáveis:** `results/confirmatorio/` (tabelas derivadas e metadados), `reports/resultados-pd.md`, `reports/precisao-monte-carlo.md`.

**Critério de saída:** todos os contrastes pré-especificados têm valor, incerteza ou justificativa clara para impossibilidade de estimação.

### E10 — Repercussão contábil, robustez e seletor de regime (M7–M10)

**Dependências:** E09; E03 para delimitação contábil.

**Atividades**
- [ ] Propagar PD estimada para perdas esperadas **sintéticas**, mantendo tratamento coerente de LGD, EAD e desconto.
- [ ] Quando possível, simular recuperações ao longo do tempo e registrar separadamente ECL verdadeira do DGP e perda efetivamente realizada.
- [ ] Estimar erros monetários normalizados pela exposição e diferenças entre estratégias, sem concluir insuficiência real de provisão.
- [ ] Analisar resultados por família DGP, tamanho, composição, mudança condicional e zero eventos; avaliar consistência/sensibilidade.
- [ ] Procurar fronteiras de utilidade; se não houver cruzamento, reportar “não identificado no domínio simulado”.
- [ ] Treinar regra factível de escolha de regime apenas com variáveis **observáveis antes da decisão**, sem parâmetros latentes do DGP.
- [ ] Avaliar regra em **novas replicações**; comparar contra baselines e oráculo retrospectivo, explicitando que oráculo não é implementável.
- [ ] Registrar custos descritivos (tempo, memória, ajustes), não custos comerciais presumidos.

**Entregáveis:** `reports/ecl-sintetica.md`, `reports/robustez.md`, `reports/mapa-transferencia-negativa.md`, `reports/seletor-regime.md`.

**Critério de saída:** aplicação contábil subordinada à PD, limites da regra de seleção e hipóteses de LGD/EAD totalmente transparentes.

### E11 — Inferência, interpretação e limites (M8–M11)

**Dependências:** resultados E09 e E10.

**Atividades**
- [ ] Organizar resultados por hipótese e diferenciar magnitude, precisão e significância estatística.
- [ ] Avaliar dependência dos resultados ao DGP, não linearidade e interação entre disponibilidade, heterogeneidade e algoritmo.
- [ ] Discutir viés, calibração, falha de estimação e transferência negativa, inclusive ausência de efeito ou resultados contraditórios.
- [ ] Distinguir validade interna, estrutural/agregada, de construto e externa; não apresentar SCR.data como validação de microdados.
- [ ] Revisitar literatura e CPC 00 (R2) sem converter métricas estatísticas em prova de representação fidedigna.
- [ ] Formular recomendações **condicionais**, acompanhadas de cenários nos quais não se aplicam.
- [ ] Comparar com um conjunto independente de dados reais, **somente se** houver acesso legítimo; registrar como validação adicional e não requisito do desenho principal.

**Entregáveis:** `docs/resultados/discussao.md`, `docs/resultados/limitacoes.md`, tabelas e figuras finais versionadas.

**Critério de saída:** todas as afirmações inferenciais limitadas ao domínio simulado ou adequadamente sustentadas por evidência externa.

### E12 — Redação contínua, qualificação e entrega (M1–M12)

**Dependências:** todas as anteriores, em graus diferentes.

**Atividades**
- [ ] Redigir introdução, problema, questão, hipóteses e justificativa em paralelo à RSL.
- [ ] Consolidar referencial e metodologia (incluindo ADEMP) **antes** de executar confirmatório.
- [ ] Encaminhar versão de projeto à orientação, programar qualificação e incorporar alterações formalmente aprovadas.
- [ ] Redigir resultados, discussão e conclusão após a análise; separar achados observados de expectativas.
- [ ] Verificar citações, DOI, normativos, referências, anexos, glossário e padronização APA 7 ou regra do programa.
- [ ] Executar auditoria final de reprodutibilidade: nova máquina/ambiente, mesma configuração, saídas consistentes.
- [ ] Preparar apresentação, limites, respostas a objeções e repositório de materiais depositáveis.
- [ ] Conferir calendário real da secretaria/orientação para depósito e defesa.

**Entregáveis:** `dissertacao/` (capítulos), `apendices/`, `slides/` (se requeridos), `reproducibility/README.md`.

**Critério de saída G7:** documento coerente, resultados rastreáveis, afirmações proporcionais à evidência, orientador ciente das limitações.

---

## 4. Escopo mínimo viável versus ampliações

| Componente | Núcleo obrigatório | Extensão somente se houver tempo e justificativa |
|---|---|---|
| Estrutura | Dados sintéticos longitudinalmente coerentes ou horizonte fixo explicitado | XML 3040 validado para integração |
| DGPs | L, N, C, R com parâmetros documentados | T macroeconômico, faltantes avançados e drift |
| Modos de estimação | R0–R4 | Reponderação por importância, bayesiano, hierárquico |
| Algoritmos | Logística regularizada e boosting de árvores | Modelos adicionais, redes neurais |
| Risco observado | Primeiro evento >90 dias, 12 meses (conforme desenho possível) | Horizontes de 3/6 meses, modelos de duração |
| Verificação | Invariantes internos e calibração agregada SCR.data | Dados reais de instituições com autorização |
| ECL | Propagação controlada da PD com LGD/EAD documentados | Recuperações estocásticas e desconto de fluxos completos |
| Seleção de regime | Derivar e testar condicionalmente em novas replicações | Implementação como módulo comercial |

**Plano de contingência:** se o simulador longitudinal completo não for operacional até G3, usar DGP em horizonte fixo para estimar PD e erro monetário simplificado, reescrevendo claramente os objetivos/resultados; **não** afirmar simulação de histórico 3040, estoque de inadimplência ou fluxos recuperatórios inexistentes.

---

## 5. Riscos prioritários, controles e gatilhos

| Risco | Consequência | Mitigação | Gatilho |
|---|---|---|---|
| Lacuna já explorada na literatura | Contribuição original enfraquecida | Mini RSL + buscas de citações + redefinição para replicação metodológica | G1 |
| 3040 não contém variáveis essenciais | DGP pouco informativo | Núcleo comum e atributos analíticos adicionais explicitados | G2 |
| Calibração agregada usada como se fosse PD individual | Erro conceitual grave | Duas métricas diferentes: estoque SCR e incidência 12m | G3 |
| Simulação favorecer um algoritmo | Comparação enviesada | DGPs lineares, não lineares e com shifts variados | G3–G4 |
| DGP temporal gera vazamento | Desempenho inflado | Maturação, embargo, auditoria de features e teste com dados futuros | G3–G4 |
| Poucos eventos geram métricas não estimáveis | Células inconclusivas | Zero eventos explícito e relatório de taxas de falha | G4–G5 |
| Explosão combinatória de fatores | Cronograma inexequível | Desenho fracionário pré-definido, piloto e extensões condicionadas | G5 |
| Replicações não independentes | IC indevidamente estreito | Unidade de Monte Carlo = replicação independente | G5–G6 |
| Regra de seleção usa a verdade simulada | Regra impraticável | Apenas preditores observáveis e novas sementes para avaliação | G6 |
| ECL sintética tomada por provisão regulatória | Conclusões contábeis indevidas | Linguagem condicional, LGD/EAD/desconto explicitados | G6 |
| Dados reais não disponíveis | Validade externa limitada | Definir pesquisa como simulação; validação externa opcional | Permanente |
| Retrabalho de escrita | Entrega em risco | Redação contínua e revisão por marcos | Permanente |

---

## 6. Organização sugerida e estrutura bibliográfica incorporada

**Atualização de 15/11/2026:** a estrutura bibliográfica efetiva está em [literature](../literature/README.md), com documentação em `docs/revisao/`. Este roadmap permanece em `docs/`, sem movimentação. Na árvore de planejamento abaixo, a matriz CSV e a localização do protocolo são sugestões históricas substituídas pelos caminhos da E02. Os demais diretórios continuam planejados.

```text
dissertacao-ecl-ml/
├── README.md
├── docs/
│   ├── proposta/
│   │   └── proposta-dissertacao-v5-2026-11-14.md
│   ├── planejamento/
│   │   └── roadmap-dissertacao-ecl-ml-v5.md
│   ├── revisao/
│   │   ├── mini-rsl-wos-ecl-ml-v5.md
│   │   ├── registro-buscas.md
│   │   ├── matriz-extracao.csv
│   │   └── sintese-mini-rsl.md
│   ├── governanca/
│   ├── referencial/
│   ├── normativo/
│   ├── metodologia/
│   └── resultados/
├── data_dictionary/
├── data/
│   ├── public/          # dados públicos, versões e metadados
│   └── synthetic/       # apenas dados sintéticos
├── configs/
│   ├── dgp/
│   └── experiment/
├── src/
│   ├── simulator/
│   ├── models/
│   └── evaluation/
├── tests/
├── results/
├── reports/
├── dissertacao/
└── reproducibility/
```

**Proteção de dados:** se no futuro forem recebidos microdados reais, guardá-los fora do repositório público e do controle de versão, sob autorização e regras de segurança. A árvore acima é uma recomendação e **não significa que as pastas já foram criadas no repositório do usuário**.

---

## 7. Rotina de gestão e checkpoints

- **Semanal:** registrar entregas concluídas, bloqueios, decisões e alterações em `registro-decisoes.md`.
- **Quinzenal:** revisar andamento das tarefas críticas; estimar tempo/recursos do próximo ciclo.
- **Mensal:** conferir gates, atualizar riscos e submeter síntese de progresso à orientação conforme acordo.
- **A cada alteração no DGP:** executar bateria de testes e comparar métricas sintéticas com referências agregadas.
- **Antes de cada execução confirmatória:** checar commit, seed, versão do protocolo, índices do treino/teste e integridade das fontes.
- **Depois de cada experimento:** arquivar apenas saídas e metadados necessários para reprodução; anotar falhas e decisões sem editar resultados retrospectivamente.

### Checklist de pronta execução — primeiros 30 dias

- [ ] Discussão com a orientação sobre o problema central, 12 meses de PD e desenho experimental.
- [ ] Fixar perguntas e string principal da mini RSL; abrir planilha de registro de buscas.
- [ ] Executar Q0–Q6 com prioridade para Q1–Q2 no WoS, conferir recuperação de estudos-semente e exportar resultados.
- [ ] Definir recortes preliminares do SCR.data e a versão do 3040 a consultar.
- [ ] Criar dicionário inicial de 15–25 atributos **candidatos**, sem inventar equivalência normativa.
- [ ] Especificar DGP mínimo e a distinção entre variáveis observadas e latentes.
- [ ] Criar cronograma real da qualificação/defesa com base na situação do aluno.
- [ ] Registrar critérios G1/G2 e pendências com risco de atraso.

---

## 8. Referências técnicas e fontes de consulta

1. **Documento-base do projeto:** `proposta-dissertacao-v5-2026-11-14.md`.
2. Morris, T. P., White, I. R., & Crowther, M. J. (2019). Using simulation studies to evaluate statistical methods. *Statistics in Medicine, 38*(11), 2074–2102. https://doi.org/10.1002/sim.8086
3. Page, M. J., et al. (2021). The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. *BMJ, 372*, n71. https://doi.org/10.1136/bmj.n71
4. Clarivate. Web of Science — Search Rules: https://webofscience.zendesk.com/hc/en-us/articles/25350084904721-Search-Rules
5. Banco Central do Brasil. SCR.data: https://dadosabertos.bcb.gov.br/dataset/scr_data
6. Banco Central do Brasil. Documento 3040 — documentação: https://www.bcb.gov.br/estabilidadefinanceira/scrdoc3040
7. Banco Central do Brasil. IF.data: https://www3.bcb.gov.br/ifdata/

*Este plano é uma projeção metodológica, não um registro de fases já executadas. Nenhum resultado de pesquisa, dado regulatório individual ou número de registros bibliográficos foi presumido.*
