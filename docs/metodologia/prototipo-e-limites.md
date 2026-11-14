# Protótipo: capacidades existentes e implementação prevista

Referência: [proposta v4](../proposta/proposta-dissertacao-v4-2026-11-14.md) e [protocolo v4](protocolo-experimental-v4.md). O nome `ecl_suficiencia` foi mantido para não romper importações. A versão 0.4.1 identifica a revisão da proposta e das interfaces documentadas, não a entrega de modelos treinados.

## O que funciona hoje

- `ecl_engine.ecl_12m`: produto elemento a elemento de PD, LGD e EAD, com verificação de limites. Serve à aproximação LP12 e ao numerador do viés monetário; não trata cenários, desconto ou trajetórias.
- `local_recalibration.shrinkage_weight`: peso heurístico `n/(n+k)`. Não é a recalibração penalizada do regime adaptado.
- `regulatory_floors.dias_para_faixa`: classifica faixas básicas de atraso. Insuficiente para reproduzir anexos e exceções normativas.
- `sufficiency.complement` e `sufficiency_ratio`: diferença positiva e razão. Os nomes legados não significam determinação de suficiência contábil.
- `reporting.relative_loss_error`: erro relativo quando a perda observada é não nula.

## Interfaces ainda não implementadas

Ingestão, construção de atributos, treinamento, recalibração, LGD/EAD, perda esperada multiperíodo, níveis normativos, calibração e divisões temporais lançam `NotImplementedError`. A configuração YAML não é consumida por um executor.

## O que a proposta v4 exige e ainda não tem interface

| Elemento do desenho | Módulo previsto |
|---|---|
| Regimes taxa base e local reduzido | `pd_models` |
| Recalibração de intercepto e inclinação penalizada em direção a (0, 1) | `local_recalibration` |
| Adaptação por reponderação: pesos de importância limitados e reestimação da origem | `local_recalibration` e `pd_models` |
| Logística regularizada e gradient boosting com orçamento de ajuste equivalente | `pd_models` |
| Sorteio de tomadores por nível de disponibilidade | `validation` |
| Classificador de domínio e subamostragem da origem por nível de distância | novo módulo de fatores experimentais |
| Medidas de distância observada (taxa base, separabilidade, composição, desajuste condicional) | novo módulo de fatores experimentais |
| Intercepto e inclinação de calibração com intervalos | `reporting` |
| Viés monetário em pontos-base | `reporting` |
| Critério de adequação com três classes | `reporting` |
| Contrastes H1–H5, C1 e C2, fronteira de utilidade e reamostragem | `reporting` |
| Custo operacional por regime e algoritmo | `reporting` |
| Regra de seleção de regime, derivada e avaliada em janelas distintas | `reporting` |

## Mapeamento dos módulos existentes

`ingestion` e `features` devem garantir linhagem e disponibilidade histórica. `validation` deve separar desenvolvimento, recalibração e teste maturado. `pd_models.fit_global` pode ajustar a origem ou o conjunto agrupado, conforme a população fornecida. `macro_selection` é interface histórica: o núcleo prevê conjunto parcimonioso comum. `lgd_ead` e `ecl_engine` fornecem as premissas comuns do desdobramento contábil. `regulatory_floors` e `sufficiency` só são usados se a comparação regulatória for habilitada.

## Ordem de implementação

1. Estudo-piloto em base pública: ingestão mínima, regimes, recalibração, medidas e critério.
2. Fatores experimentais e reamostragem.
3. Ingestão dos dados autorizados e dicionário fixado.

O protótipo reprodutível é entrega da dissertação e base da aplicação posterior; integração, segregação de dados entre clientes e governança não fazem parte dele.

Cada módulo implementado terá testes próprios de vazamento, censura, maturação e calibração. Os testes aritméticos atuais não demonstram validade empírica.
