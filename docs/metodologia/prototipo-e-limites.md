# Protótipo: capacidades existentes e implementação prevista

Referência: [proposta v3](../proposta/proposta-dissertacao-v3-2026-11-13.md). O nome `ecl_suficiencia` foi mantido para não romper importações. A versão 0.3.0 identifica a revisão da proposta e das interfaces documentadas, não a entrega de modelos treinados.

## O que funciona hoje

- `ecl_engine.ecl_12m`: produto elemento a elemento de PD, LGD e EAD, com verificação de limites de PD/LGD. Não trata cenários, desconto ou trajetórias; pode servir à aproximação LP12 sob premissas explícitas.
- `local_recalibration.shrinkage_weight`: peso heurístico `n/(n+k)`. Não estima recalibração e não implementa inferência hierárquica/bayesiana.
- `regulatory_floors.dias_para_faixa`: classifica algumas faixas de atraso, agrupando todas as superiores a 90 dias. É insuficiente para reproduzir os anexos e exceções normativas; entradas também exigem validação adicional.
- `sufficiency.complement` e `sufficiency_ratio`: calculam diferença positiva e razão. Seus nomes legados não significam determinação de suficiência contábil. A convenção usada para denominador não positivo não é conclusão normativa.
- `reporting.relative_loss_error`: erro relativo quando a perda observada é não nula. Não cria uma base observada de perdas nem valida ECL sozinho.

## Interfaces ainda não implementadas

Ingestão, construção de atributos, treinamento, recalibração, ajuste macro, LGD/EAD, ECL multiperíodo, aplicação integral de níveis normativos, calibração e divisões temporais lançam `NotImplementedError`. A configuração YAML não é consumida por um executor existente. Imports de bibliotecas não representam implementação.

## Mapeamento do desenho v3

`ingestion` e `features` devem garantir linhagem e disponibilidade histórica. `validation` deve separar desenvolvimento, adaptação e teste maturado. `pd_models` atenderá aos quatro regimes definidos na proposta; `fit_global` pode ajustar origem ou conjunto agrupado conforme a população de treino explicitamente fornecida. `local_recalibration` acomodará adaptação regularizada, sem tratar a heurística atual como solução validada.

`macro_selection` é uma interface histórica para extensões: o núcleo da v3 prevê conjunto parcimonioso comum. `lgd_ead` e `ecl_engine` suportarão o desdobramento contábil condicionado aos dados. `regulatory_floors`, `sufficiency` e `reporting` devem distinguir parâmetros normativos, estimativas experimentais e provisões registradas.

## Trabalho futuro condicionado

Implementar o protocolo apenas após decisão de dados e definições congeladas. Exigir testes próprios de vazamento, censura, maturação, transferência, calibração e recuperação conforme cada módulo for implementado. Os testes aritméticos atuais não demonstram validade empírica, governança ou aptidão comercial. Não há promessa de compatibilidade regulatória completa nesta versão.
