# Histórico

## 0.4.0 — 2026-11-14
- Nova proposta v4, motivada pelo parecer metodológico de 14/11 sobre a v3. Título, questão única e objetivo geral reescritos; a variável dependente passa a ser a qualidade da PD (pontuação probabilística, calibração e viés monetário).
- Teoria de base explicitada: representação fidedigna e usuário externo (CPC 00 R2), com correspondência entre atributos contábeis e medidas da estimativa.
- Critério de adequação com três classes (adequada, inadequada, inconclusiva), fixado antes do teste, em substituição ao construto "confiável".
- Hipóteses H1–H4 e contraste bilateral C1 em família fechada; fronteira de utilidade n*(d) como resultado derivado. A numeração H1–H3 da v3 não se conserva.
- Regimes de referência acrescentados (taxa base e local reduzido); distância entre origem e destino induzida por subamostragem; inferência condicional às carteiras estudadas; precisão-alvo declarada.
- Viés monetário (erro da PD ponderado por exposição e severidade) substitui a propagação aritmética como desdobramento contábil principal.
- Criados protocolo experimental v4, adendo de revisão da literatura para a v4 e registro da revisão. Atualizados README, metadados, configuração, dicionário, notas normativas, apresentação, mapa do protótipo e docstrings. Lista de referências refeita em APA.
- Proposta v3, protocolo v3 e registro de 13/11 preservados nos caminhos originais; demais documentos da v3 preservados no histórico do Git.
- Permanecem pendentes: acesso a microdados, execução da mini revisão sistemática, parâmetros do critério e conferência normativa. Nenhum experimento executado.

## 0.3.0 — 2026-11-13
- Nova proposta v3: modelagem adaptativa de ECL com Machine Learning; transferência/adaptação entre carteiras, disponibilidade observada de dados e heterogeneidade como condicionantes.
- Problema, questão, objetivos e H1–H3 alinhados; validação de PD como resultado primário e repercussões em ECL como desdobramento contábil.
- Removida dos documentos correntes a presunção de poucos dados em S4/S5; capacidade operacional e produto comercial delimitados como viabilidade secundária e aplicação futura.
- Corrigida a base normativa: Resolução BCB 352/2023, inclusive art. 1º, II, e arts. 76–81; 309/2023 preservada apenas como referência histórica revogada. Ressalvas ao enquadramento S4/S5 e às conclusões de suficiência.
- Atualizados apresentação, README, metadados, configuração, dicionário e documentação das interfaces. Criados protocolo experimental e mapa de limitações do protótipo.
- V1, v2 e parecer preservados integralmente; cópias dos documentos substituídos e manifesto SHA-256 em `docs/historico/`. Script Bash anterior preservado; construtor Python equivalente adicionado.
- Nenhum experimento científico executado, dado privado obtido ou modelo declarado validado. Detalhes e verificações em `docs/registro-atualizacao-2026-11-13.md`.

## 0.2.0 — 2026-11-06
- Proposta reformulada: problema único centrado na avaliação de suficiência (S4 e S5); lacuna em três pontos cegos; duas lentes teóricas; cinco hipóteses; seção de dados necessários; enquadramento normativo corrigido (Res. CMN 4.966, Res. BCB 309, IN BCB 487).
- Apresentação interativa com desenho de pesquisa, desenho metodológico, simulador de suficiência e grafo de referências.
- Esqueleto do protótipo em `src/ecl_suficiencia/`.

## 0.1.0 — 2026-10-28
- Proposta preliminar: arquitetura modular e adaptativa de ML para ECL em instituições com dados limitados.
