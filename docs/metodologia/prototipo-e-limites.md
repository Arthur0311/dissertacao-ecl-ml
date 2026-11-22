# Protótipo: capacidades existentes e implementação prevista

Referência: [proposta v5](../proposta/proposta-dissertacao-v5-2026-11-14.md) e [protocolo v5](protocolo-experimental-v5.md). O nome `ecl_suficiencia` foi mantido para não romper importações. A versão 0.5.0 identifica o alinhamento documental à v5, não a entrega de simulador ou de modelos treinados.

## O que funciona hoje

- `ecl_engine.ecl_12m`: produto elemento a elemento de PD, LGD e EAD, com verificação de limites. Serve à aproximação estática da ECL sintética; não trata desconto, recuperações ou trajetórias.
- `local_recalibration.shrinkage_weight`: peso heurístico `n/(n+k)`. Não é a recalibração regularizada do regime R4.
- `regulatory_floors.dias_para_faixa`: classifica faixas básicas de atraso. Fora do experimento confirmatório da v5.
- `sufficiency.complement` e `sufficiency_ratio`: diferença positiva e razão. Nomes legados; fora do experimento confirmatório da v5.
- `reporting.relative_loss_error`: erro relativo quando o valor de referência é não nulo.

## Interfaces ainda não implementadas

Ingestão, construção de atributos, treinamento, recalibração, LGD/EAD, perda multiperíodo, calibração e divisões temporais lançam `NotImplementedError`. A configuração YAML não é consumida por um executor. **Não existe simulador.**

## O que a proposta v5 exige e ainda não tem interface

| Elemento do desenho | Módulo previsto |
|---|---|
| Gerador de instituições, tomadores, contratos e trajetórias mensais | novo módulo de simulação |
| Famílias DGP-L, N, C, R e T, com PD verdadeira e risco competitivo | novo módulo de simulação |
| Tabela de verdade isolada do treino | novo módulo de simulação |
| Testes de coerência estrutural e de propriedades | `tests/` |
| Extração e tratamento reproduzível do SCR.data; relatório de plausibilidade | `ingestion` e `reporting` |
| Regime R0 (referência simples) | `pd_models` |
| Regimes R1–R3 com logística regularizada e gradient boosting | `pd_models` |
| R4: intercepto e inclinação no destino, com regularização e retorno a R3 | `local_recalibration` |
| Partições cronológicas, maturação e embargo | `validation` |
| Log-loss, Brier, calibração e erro frente à PD verdadeira | `reporting` |
| Transferência negativa, contrastes pareados e erro de Monte Carlo | `reporting` |
| ECL sintética estimada e verdadeira | `ecl_engine` |
| Regra de seleção, oráculo retrospectivo e arrependimento | `reporting` |
| Custo operacional por regime e algoritmo | `reporting` |
| Executor de replicações com sementes versionadas | novo módulo de experimento |

## Mapeamento dos módulos existentes

`ingestion` passa a tratar agregados públicos e séries macroeconômicas, não microdados de instituições. `features` constrói atributos observáveis na data-base a partir da base sintética. `validation` separa desenvolvimento, validação interna e teste. `lgd_ead` e `ecl_engine` fornecem as premissas comuns do desdobramento contábil. `macro_selection` é interface histórica: macroeconomia é análise de sensibilidade. `regulatory_floors` e `sufficiency` são legados de versões anteriores.

## Ordem de implementação

1. Dicionário e gerador mínimo, com testes de integridade (E04, E06).
2. Calibração agregada e relatório de plausibilidade (E05).
3. Regimes, validação temporal e medidas (E08).
4. Executor de Monte Carlo, contrastes e ECL sintética (E09, E10).

O protótipo reprodutível é entrega da dissertação. Integração, segregação de clientes e governança de produção não fazem parte dele.

Os testes aritméticos atuais não demonstram validade do simulador nem dos modelos.
