# Protocolo experimental — proposta v5 (ADEMP preliminar)

**Estado:** planejamento em 15/11/2026. Não congelado, sem piloto e sem experimentos executados. Operacionaliza as seções 4 e 6 a 8 da [proposta v5](../proposta/proposta-dissertacao-v5-2026-11-14.md), no esquema ADEMP de Morris, White e Crowther (2019). Os valores da [configuração](../../configs/experimento-exemplo.yaml) são candidatos. O congelamento ocorre no gate G4 do [roadmap](../roadmap-dissertacao-ecl-ml-v5.md), antes de qualquer simulação confirmatória. Os protocolos [v4](protocolo-experimental-v4.md) e [v3](protocolo-experimental-v3.md) permanecem como registro do desenho com microdados reais, superado.

Em caso de divergência, prevalece a proposta v5.

## 1. Registro anterior à execução confirmatória

Fixar e datar, antes do gate G4:

| Decisão | Situação em 15/11/2026 |
|---|---|
| Versão do leiaute 3040 e dicionário sintético | a congelar |
| Séries, período e filtros do SCR.data; tolerâncias de plausibilidade | a definir |
| Famílias de DGP, níveis de parâmetros e proveniência de cada parâmetro | a definir no piloto |
| Malha de eventos locais maturados | candidata: 0, 5, 20, 50, 200 e níveis maiores |
| Cenários confirmatórios e exploratórios | a identificar após o piloto |
| Margem de irrelevância prática para a diferença de *log-loss* | a fixar após piloto independente |
| Faixas do critério de adequação | a fixar após piloto independente |
| Número de replicações confirmatórias | a dimensionar pelo erro de Monte Carlo; 100 por condição é valor ilustrativo de piloto |
| Procedimento de multiplicidade | Holm, quando apropriado |
| Sementes e versões de bibliotecas | a versionar |
| Aproximação estática ou versão descontada da ECL | a decidir com a orientação |

Alteração posterior é emenda datada, com justificativa e indicação do que já havia sido observado.

## 2. A — Objetivos (*Aims*)

Estimar, sob mecanismos geradores fixados, a diferença esperada de desempenho preditivo entre regimes de estimação de PD de 12 meses no destino, em função de disponibilidade local, heterogeneidade origem–destino e algoritmo (H1–H4), com e sem transferência de aprendizado. Os regimes elegíveis dependem do acesso: sem modelo externo nem microdados da origem, R0 e R1; com previsões de um modelo externo, também R3 e R4; R2 exige os microdados da origem. Mensurar a propagação do erro de PD à ECL sintética (C1). Derivar, quando identificável, a fronteira de utilidade e avaliar uma regra de seleção de regime.

## 3. D — Mecanismos geradores (*Data-generating mechanisms*)

**Instituições virtuais.** IF-A (crédito pessoal PF, histórico curto), IF-B (consignado PF), IF-C (capital de giro PJ) e IF-D (referência, possível origem). São arquétipos, não empresas reais nem segmentos prudenciais. Os testes confirmatórios usam o núcleo comum de atributos.

**Base.** Entidades instituição–mês, tomador–mês, contrato, contrato–mês, ambiente econômico, eventos e recuperação, e verdade do simulador (ver [dicionário](../../data_dictionary/README.md)). A tabela de verdade é inacessível ao treino e ao ajuste.

**Famílias.** Núcleo obrigatório: DGP-L (logístico), DGP-N (não linear), DGP-C (composição), DGP-R (condicional). DGP-T (temporal) é sensibilidade condicionada ao piloto. Cenários adicionais: baixa taxa-base, zero eventos locais, valores ausentes e erro de mensuração. As famílias não são cruzadas integralmente. Nenhum DGP deve favorecer por construção todos os métodos testados.

**Fatores.**

- *Disponibilidade:* número de tomadores, número de eventos maturados e meses de histórico, variados separadamente quando possível. O número realizado de eventos é registrado; não se selecionam observações futuras para forçar o alvo.
- *Heterogeneidade:* taxa-base (interceptos), composição (distribuição dos atributos e suporte) e relação condicional (coeficientes, interações ou funções). As diferenças de parâmetros do DGP são a verdade experimental; índices empíricos de separabilidade usam apenas dados de desenvolvimento.
- *Algoritmo:* regressão logística regularizada e *gradient boosting*, com protocolo comparável de seleção de hiperparâmetros; o custo é reportado à parte.

**Desenho.** Fracionário com dois níveis por fator principal, ampliado apenas nas regiões de mudança relevante, por decisão tomada sem acesso ao resultado final reservado.

**Calibração do simulador.** Dois níveis: coerência estrutural (testes unitários e de propriedades) e plausibilidade agregada frente ao SCR.data, com tolerâncias prévias. Inadimplência de estoque não é incidência de primeiro evento em 12 meses. Parâmetros arbitrados são variados em sensibilidade e não são descritos como estimados pelo SCR.

## 4. E — Estimandos (*Estimands*)

- **Central:** diferença esperada de *log-loss* entre dois regimes na população de teste do destino, sob DGP fixado, calculada na mesma amostra de teste.
- **Contra a verdade:** erro médio, absoluto médio e quadrático médio da PD estimada frente à PD verdadeira do DGP, ao longo das replicações.
- **Transferência negativa:** probabilidade de o regime transferido ou adaptado ter *log-loss* superior ao local por mais que a margem de irrelevância.
- **Monetário:** diferença entre a ECL sintética estimada e a ECL verdadeira do simulador, em moeda simulada e em pontos-base da exposição.
- **Derivado:** ponto ou faixa de disponibilidade em que o contraste adaptado–local cruza zero ou a margem. Sem cruzamento na região testada: "não identificado no domínio experimental". No cenário sem modelo externo, descreve-se de modo análogo o contraste R1–R0, sem hipótese direcional.

## 5. M — Métodos (*Methods*)

| Regime | Definição | Zero evento local |
|---|---|---|
| R0 — Referência simples | Taxa agregada comparável ao evento e ao horizonte ou estimativa suavizada, com as informações disponíveis na data-base | Aplicável se houver base documentada; sem ela, registrar indisponibilidade |
| R1 — Local | Apenas desenvolvimento do destino | Pode ser não estimável |
| R2 — Agrupado | Modelo único com origem e destino | Executável com eventos na origem |
| R3 — Transferido | Treinado na origem, sem atualização | Executável |
| R4 — Transferido + recalibração | Intercepto e, quando suportado, inclinação estimados no destino com regularização | Retornar a R3 ou a atualização por prior documentado |

R1–R4 com os dois algoritmos, quando a arquitetura comportar. Hiperparâmetros ajustados só no desenvolvimento. Extensões condicionadas ao piloto: reponderação por importância, atualização bayesiana, modelo hierárquico parcial e horizontes adicionais.

**Validação temporal.** Desenvolvimento, validação cronológica interna e teste em datas futuras, sem reuso. Rótulos com maturação completa ou censura tratada. Embargo entre janelas. Tomador em um único domínio. Transformações, imputação, seleção, reponderação e recalibração dentro das janelas permitidas.

**Regra de seleção.** Ajustada em replicações de desenvolvimento e testada em novas replicações com sementes independentes, contra o local, o transferido e um oráculo retrospectivo; a distância ao oráculo é o arrependimento.

## 6. P — Medidas de desempenho (*Performance measures*)

- ***Log-loss*** (primária) e **Brier** (complementar), nas mesmas observações de teste por contraste.
- **Calibração observada:** intercepto, inclinação e curvas, com intervalos; **AUC-ROC** como complemento.
- **Erro frente à PD verdadeira**, por replicação e agregado.
- **Frequência de transferência negativa** e de casos indisponíveis (local não estimável).
- **Desvio da ECL sintética**; perda realizada relatada à parte.
- **Cobertura de execução:** falhas, não estimação e células inconclusivas são resultado.
- **Custo operacional descritivo:** tempo de treino e de inferência, memória, decisões de ajuste e dependência de dados da origem.

Para cada DGP e condição: média do contraste pareado, erro-padrão de Monte Carlo, intervalo de confiança, distribuição dos contrastes e frequência de transferência negativa. A replicação independente é a unidade de incerteza; contratos, tomadores e datas-base dentro de uma replicação não são replicações. A precisão da calibração em uma carteira simulada é tratada à parte da precisão da média de Monte Carlo.

**Critério de adequação.** Três classes: adequada, inadequada e inconclusiva. Margens fixadas após piloto independente. A ausência de rejeição não classifica uma célula como adequada.

## 7. Piloto e execução confirmatória

O piloto configura o experimento: tempo de execução, estimabilidade, erro de Monte Carlo e níveis dos fatores. As simulações confirmatórias são independentes do piloto. Cenários não são escolhidos retrospectivamente. Se a simulação longitudinal completa exceder os recursos, o núcleo mínimo é um DGP de evento em horizonte fixo, relatado como redução de escopo.

## 8. Limites de inferência

Conclusões condicionais às famílias de DGP e aos parâmetros estudados. A plausibilidade agregada frente ao SCR.data não valida relações individuais de risco nem o desempenho em instituições reais. A ECL sintética não é provisão contábil nem referência regulatória.

## Referência

Morris, T. P., White, I. R., & Crowther, M. J. (2019). Using simulation studies to evaluate statistical methods. *Statistics in Medicine, 38*(11), 2074–2102. https://doi.org/10.1002/sim.8086
