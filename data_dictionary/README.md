# Dicionário de dados sintéticos — proposta v5

Modelo a preencher nas etapas E04 e E06 do [roadmap](../docs/roadmap-dissertacao-ecl-ml-v5.md). Referências: [proposta v5](../docs/proposta/proposta-dissertacao-v5-2026-11-14.md), seções 5.2 e 6.3, e [protocolo v5](../docs/metodologia/protocolo-experimental-v5.md). Nenhuma base foi gerada. Não se usam arquivos 3040 de instituições reais.

**Pendência central:** a versão do leiaute do Documento 3040 ainda não foi congelada. Este dicionário não atribui nomes, códigos ou tipos do 3040. A correspondência exata será registrada em `data_dictionary/3040-mapeamento.md` somente com campos confirmados na documentação oficial.

## Registro obrigatório de cada atributo

Nome, definição, tipo, unidade, granularidade, domínio válido, regra de geração, semente, versão e classe:

| Classe | Significado | Visível aos modelos |
|---|---|---|
| (a) Inspirado no 3040 | Segue a estrutura e os conceitos do leiaute público | Sim |
| (b) Analítico adicional | Necessário ao experimento, sem correspondência no leiaute | Sim, se observável na data-base |
| (c) Latente do DGP | Fator ou estado que gera o risco | Não |
| (d) Parâmetro de cenário | Define a condição experimental | Não |

Cada parâmetro tem também **proveniência**: identificado por dado público, parcialmente identificado ou arbitrado para sensibilidade.

## Entidades

| Entidade | Granularidade | Conteúdo mínimo | Origem conceitual |
|---|---|---|---|
| Instituição | Instituição–mês | Perfil, data de início, política, disponibilidade histórica | Cenário simulado |
| Tomador | Tomador–mês | Características observáveis; fator latente em tabela protegida | Campos públicos compatíveis e DGP |
| Contrato | Contrato | Modalidade, valor, prazo, taxa, garantias, calendário contratual | Estrutura inspirada no 3040 e DGP |
| Evolução da operação | Contrato–mês | Saldo, vencimentos, pagamentos, dias em atraso, liquidação e renegociação | Estrutura inspirada no SCR e regras simuladas |
| Ambiente econômico | Mês | Variáveis correntes, projeções disponíveis, choques simulados | Séries públicas e DGP |
| Eventos e recuperação | Contrato–mês | Início do evento, fluxos de recuperação e baixa | DGP; não inferível integralmente do 3040 |
| Verdade do simulador | Contrato–data-base | PD verdadeira, horizonte e perda esperada verdadeira | DGP; indisponível aos modelos |

## Chaves e domínios

- `id_instituicao`, `id_tomador`, `id_contrato`: inteiramente fictícios. Um tomador pode ter vários contratos; a dependência é identificável.
- `dominio`: origem ou destino. Um tomador pertence a um único domínio.
- `data_base`, `inicio_historico`, `fim_acompanhamento`: sustentam corte temporal, maturação e censura.
- `papel_amostral`: desenvolvimento, validação cronológica interna ou teste; com identificador da replicação e da semente.

## Evento e rótulos

- **Evento principal:** primeiro atraso superior a 90 dias em até 12 meses após a data-base, para contratos elegíveis sem o evento na data-base. É *proxy* operacional, não equivalência à classificação regulatória de ativo com problema de recuperação de crédito.
- `evento_12m`: 0/1 apenas com horizonte maturado; seguimento incompleto não vira zero.
- Liquidação antecipada é risco competitivo: a PD verdadeira respeita a ordem dos eventos.
- Renegociação, cura e baixa têm regras fixadas antes da geração; o evento ocorrido não é apagado.

## Verdade do simulador (tabela isolada)

`pd_verdadeira_12m`, estados latentes, `lgd`, `ead`, fluxos de recuperação esperados e `perda_esperada_verdadeira`. A tabela é fisicamente separada do conjunto permitido ao treino e usada só na avaliação externa dos métodos.

## Fatores experimentais gravados por replicação

- `familia_dgp` (L, N, C, R, T), parâmetros e semente.
- `eventos_locais_alvo`, `eventos_locais_realizados`, `n_tomadores`, `n_contratos`, `meses_historico`.
- `dif_taxa_base`, `dif_composicao`, `dif_condicional`: diferenças de parâmetros entre origem e destino, conhecidas pelo simulador.
- Índices empíricos de separabilidade de domínios, calculados só no desenvolvimento.
- `regime` (R0–R4), `algoritmo`, indicador de não estimável e motivo.
- Custo operacional: `tempo_treino`, `tempo_inferencia`, `memoria`, `decisoes_de_ajuste`, `dependencia_origem`, com identificação do equipamento.
- `regime_selecionado` pela regra, com as replicações em que foi ajustada e testada.

## Exposição, recuperação e ECL sintética

`ead`, `lgd`, cronograma de recuperação e taxa de desconto são gerados por mecanismos explícitos e comuns aos métodos. `ecl_estimada` usa a PD de cada regime; `ecl_verdadeira` usa a PD do DGP. A perda realizada é gravada à parte. A aproximação estática PD × LGD × EAD e a versão descontada com recuperações são identificadas separadamente.

## Calibração agregada

Para cada indicador do SCR.data usado: série, versão, filtros, período, unidade, supressões, tolerância e papel (ajuste ou verificação reservada). Inadimplência de estoque não é rótulo individual nem PD verdadeira.

## Informações macroeconômicas

Para cada variável: data de referência, data de publicação, versão e horizonte. Distinguir a trajetória que gera os eventos da informação observável na data-base. Valores revisados ou futuros não entram nos preditores.

## Critérios de integridade

Saldos não negativos; amortização coerente; atraso compatível com pagamentos; nenhum fluxo após a extinção do contrato, salvo recuperação; unicidade de contrato–data-base; tomador sem duplicação entre domínios; consistência do primeiro evento em 12 meses. Casos-limite testados: zero eventos, pré-pagamento e múltiplos contratos por tomador.

## Fora deste dicionário

Campos de carteira regulatória C1–C5, níveis de provisão e provisão registrada pertencem ao desenho anterior e não integram o experimento confirmatório da v5. O dicionário da v4, voltado a microdados reais, está no histórico do Git.
