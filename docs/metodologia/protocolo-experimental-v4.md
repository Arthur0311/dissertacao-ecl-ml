# Protocolo experimental — proposta v4

**Estado:** planejamento em 14/11/2026. Sem pré-registro concluído, sem microdados confirmados e sem experimentos executados. Operacionaliza as seções 4 e 6 a 9 da [proposta v4](../proposta/proposta-dissertacao-v4-2026-11-14.md). Os valores da [configuração](../../configs/experimento-exemplo.yaml) são candidatos. O [protocolo v3](protocolo-experimental-v3.md) permanece como referência histórica.

## 1. Registro anterior ao teste

Cada experimento terá um registro datado com: versão da proposta e do código; base autorizada, período, instituições e carteiras; critérios de inclusão; definição de evento, horizonte e censura; atributos e sua disponibilidade histórica; cortes de desenvolvimento, validação e teste; contagens por classe. O teste não será aberto com o registro incompleto.

Serão fixados antes do teste:

| Decisão | Valor candidato |
|---|---|
| Malha de disponibilidade (fração de tomadores) | 5%, 10%, 20%, 40%, 70%, 100% |
| Repetições por nível | 20 |
| Níveis de distância induzida | 5 |
| Faixa do intercepto de calibração (δa, escala logito) | 0,2 |
| Faixa da inclinação de calibração (δb) | 0,2 |
| Precisão-alvo (meia-largura do IC 95% da inclinação) | 0,2 |
| Margem de irrelevância para diferença de log-loss | a definir no desenvolvimento |
| Limiar de materialidade do viés monetário (pb da exposição) | a definir com a orientação |
| Mínimo de destinos independentes para testar heterogeneidade observada | a definir por simulação |
| Variáveis do regime local reduzido | a definir no desenvolvimento |

Alteração posterior é emenda datada, com justificativa e indicação do que já havia sido observado.

## 2. Fatores experimentais

**Disponibilidade.** Sortear tomadores do desenvolvimento do destino, sem seleção por classe, em cada nível da malha. Manter o mesmo teste em todos os níveis. Registrar, por sorteio, tomadores, contratos, eventos, não eventos e meses de histórico. Sorteios sem as duas classes são registrados como não estimáveis para os regimes que dependem de rótulos locais; não são descartados. A condição de início de operação é aproximada, em análise separada, por janelas históricas curtas.

**Distância induzida.** Estimar, no desenvolvimento, um classificador de domínio (origem versus destino) e obter e(x), a probabilidade de pertencer ao destino. Reamostrar a origem com probabilidade de inclusão proporcional a exp(λ × logit e(x)), com λ em cinco níveis simétricos em torno de zero; λ positivo aproxima a origem do destino, λ negativo a afasta. Manter o tamanho da origem constante entre níveis. Registrar, para cada nível, a separabilidade resultante. O nível ordinal de distância é o regressor das hipóteses H2 e H3; a separabilidade medida é reportada como verificação da manipulação.

**Distância observada.** Para cada par, no desenvolvimento e com rótulos maturados: diferença de taxa base em logito; área sob a curva ROC do classificador de domínio em validação cruzada; média das distâncias de Wasserstein normalizadas (numéricas) e de variação total (categóricas); excesso de log-loss do modelo da origem no desenvolvimento do destino após correção do intercepto. Lista de variáveis, escalas e tratamento de categorias novas são fixados antes do teste.

## 3. Regimes

| Regime | Dados de ajuste | Observação |
|---|---|---|
| Taxa base | Desenvolvimento do destino | PD constante |
| Local | Desenvolvimento do destino | — |
| Local reduzido | Desenvolvimento do destino | Variáveis pré-especificadas |
| Agrupado | Origem e desenvolvimento do destino | Ajuste único |
| Transferido | Origem | Sem ajuste local |
| Adaptado | Origem; recalibração no desenvolvimento do destino | Intercepto e inclinação penalizados em direção a (0, 1) |

Algoritmo principal: regressão logística regularizada. Gradient boosting em árvores nos regimes local, agrupado, transferido e adaptado, como robustez, com orçamento de busca equivalente e documentado. Penalização e hiperparâmetros escolhidos em validação cronológica aninhada. Tomadores presentes em origem e destino são atribuídos a um único domínio.

## 4. Medidas

- **Log-loss** (primária), com limite numérico das probabilidades registrado. **Brier** como complemento.
- **Intercepto de calibração** (inclinação fixada em 1) e **inclinação de calibração**, com intervalos de 95%. Curvas de calibração com intervalos.
- **Viés monetário:** VM = Σ (PD − y) × LGD × EAD / Σ EAD, em pontos-base, com LGD e EAD comuns aos regimes e de origem documentada.
- **Área sob a curva ROC**, descritiva, quando as duas classes existirem no teste.
- **Cobertura de execução:** proporção de sorteios estimáveis por regime e célula.

**Critério de adequação por célula e regime:** adequada se (i) IC 95% do intercepto contido em ±δa, (ii) IC 95% da inclinação contido em [1 − δb, 1 + δb] e (iii) limite superior do IC 95% da diferença de log-loss em relação à taxa base negativo; inadequada se algum intervalo estiver inteiramente fora da faixa; inconclusiva nos demais casos.

## 5. Hipóteses, contrastes e análise

Família confirmatória, algoritmo principal, ajuste de Holm sobre cinco testes, intervalos de 95%.

| Identificação | Contraste | Estimando | Sinal esperado |
|---|---|---|---|
| H1 | log-loss(adaptado) − log-loss(local) | Coeficiente de log2(n local) | Positivo |
| H2 | log-loss(adaptado) − log-loss(local) | Coeficiente do nível de distância | Positivo |
| H3 | log-loss(transferido) − log-loss(adaptado) | Coeficiente do nível de distância | Positivo |
| H4 | \|VM(adaptado)\| − \|VM(local)\|, dois níveis inferiores da malha | Diferença média | Negativo |
| C1 | log-loss(adaptado) − log-loss(agrupado), dois níveis inferiores | Diferença média | Bilateral |

H1 e H2 são estimadas no mesmo modelo linear da diferença por célula, com efeitos fixos por par origem–destino e janela. Fronteira de utilidade derivada: n\*(d), volume local em que a diferença ajustada se anula no nível de distância d; reportar com intervalo e indicar quando estiver fora da malha. Examinar resíduos quanto a não linearidade em log2(n) e reportar a especificação por níveis categóricos.

Incerteza: reamostragem que combina os sorteios de desenvolvimento com bootstrap de tomadores do teste em blocos temporais; algoritmo e tamanho dos blocos fixados antes do teste. Comparações pareadas apenas onde os dois regimes são estimáveis, com a fração excluída reportada.

A inferência é condicional às carteiras estudadas. A associação entre distância observada e desempenho é descritiva; torna-se teste, com reamostragem por destino, somente se o número de destinos independentes atingir o mínimo registrado. Efeito nulo só é afirmado com intervalo contido na margem de irrelevância.

Análises fora da família (gradient boosting, definição alternativa de evento, ausência de variáveis macroeconômicas, janelas curtas, subgrupos) são identificadas como exploratórias ou de robustez.

## 6. Cronologia

Datas-base de teste posteriores ao desenvolvimento, com 12 meses seguintes observados. Treino usa apenas rótulos maturados na data simulada. Intervalo de exclusão de 12 meses entre treino e validação interna. Imputação, seleção e recalibração ajustadas dentro de cada janela de treino. Variáveis macroeconômicas na versão disponível em cada data-base.

## 7. Precisão

Calcular, com dados de desenvolvimento, o número de eventos de teste necessário para a precisão-alvo da inclinação de calibração, pelo procedimento de Riley et al. (2021) e por simulação. Células abaixo da precisão-alvo permanecem na análise e tendem à classificação inconclusiva. Ajustar a malha antes do teste para que os níveis inferiores permitam estimar o regime local em parcela relevante dos sorteios; registrar a parcela esperada.

## 8. Desdobramento contábil

Viés monetário por regime e célula, com a origem de LGD e EAD identificada (estimada, externa ou arbitrada). LP12 = PD12 × LGD × EAD reportada como aproximação; diferenças de LP12 entre regimes são análise de sensibilidade. Comparação com níveis regulatórios somente com classificação por ativo, garantias e regras vigentes por data-base.

## 9. Portões e entregas

- **Mês 3:** decisão de cenário (A, B ou C); estudo-piloto em base pública concluído; mini revisão sistemática executada.
- **Mês 4:** registro da seção 1 completo.
- **Entregas:** manifesto de dados sem conteúdo privado; configuração fixada; métricas por célula e sorteio; registro de falhas de estimação; contrastes com intervalos; fronteira de utilidade; mapa de adequação; viés monetário; limitações. Resultados são gravados em `experiments/` apenas após execução real.
