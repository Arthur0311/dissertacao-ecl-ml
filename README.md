# Modelagem adaptativa de perdas esperadas de crédito com Machine Learning

**Transferência de modelos de probabilidade de inadimplência, disponibilidade de dados e heterogeneidade entre carteiras de instituições financeiras brasileiras.**

Projeto de dissertação em Controladoria e Contabilidade, PPGCONT/UFRGS, linha Usuários Externos. Base científica: **proposta v5 — 14/11/2026**. Estrutura bibliográfica atualizada em **15/11/2026**.

> Proposta para discussão com a orientação. Não há resultados empíricos nem acesso a microdados confirmado, e a mini revisão sistemática da literatura não foi executada. O código é um esqueleto experimental.

## Questão de pesquisa

Em que condições a disponibilidade de dados locais, a heterogeneidade entre carteiras de origem e destino e a complexidade dos algoritmos influenciam a qualidade das estimativas de PD produzidas por estratégias de Machine Learning com transferência e adaptação?

O desenho corrente usa simulação de Monte Carlo e instituições virtuais, com PD verdadeira conhecida sob múltiplos mecanismos geradores. O Documento 3040 orienta a estrutura; SCR.data e, quando útil, IF.data apoiam a calibração agregada. Compara R0 referência ingênua, R1 local, R2 agrupado, R3 transferido e R4 transferido com recalibração, usando logística regularizada e gradient boosting quando aplicáveis. A repercussão em ECL é sintética e condicional às premissas de LGD, EAD e desconto. Validação com dados reais é complementar, não pré-requisito do desenho principal. A ferramenta comercial permanece fora do escopo.

## Documentos correntes

- [Proposta v5](docs/proposta/proposta-dissertacao-v5-2026-11-14.md): desenho científico corrente, ainda sujeito à orientação.
- [Roadmap v5](docs/roadmap-dissertacao-ecl-ml-v5.md): etapas E01–E12 e critérios de passagem.
- [Parecer sobre a v3](docs/parecer/parecer-metodologico-v3-2026-11-14.md): avaliação que motivou a v4, com quadro de atendimento.
- [Protocolo experimental v4](docs/metodologia/protocolo-experimental-v4.md): antecedente a reconciliar com a v5 antes dos experimentos; não é o protocolo confirmatório do desenho sintético.
- [Protocolo operacional da mini RSL Q0–Q6](docs/revisao/protocolo-busca-wos-q0-q6.md): buscas, seleção e rastreabilidade sob a v5.
- [Notas normativas](docs/normativo/notas-verificacao-normativa.md), [dicionário de dados](data_dictionary/README.md) e [configuração ilustrativa](configs/experimento-exemplo.yaml).
- [Apresentação](docs/index.html): síntese da proposta em slides.
- [Registro da revisão de 14/11](docs/registro-atualizacao-2026-11-14.md): mudanças, decisões e verificações.

## Pendências que condicionam a qualificação

1. Aprovação do desenho sintético, DGPs e fontes públicas para calibração agregada.
2. Execução da mini revisão sistemática; a lacuna é candidata.
3. Faixas do critério de adequação, margem de irrelevância e limiar de materialidade.
4. Conferência normativa por instituição e data-base.

## Mini RSL

Q0 faz o mapeamento; Q1–Q2 constituem o núcleo científico; Q3–Q4 sustentam simulação e calibração; Q5 sustenta a discussão contábil; Q6 reúne métodos gerais. Uma única revisão delimitada, ainda não executada.

- [Registro de buscas](docs/revisao/registro-buscas.md) e [fluxo PRISMA](docs/revisao/fluxo-prisma.md).
- [Organização bibliográfica e planilhas](literature/README.md), separadas de `data/`.
- [Relatório da incorporação](docs/revisao/registro-incorporacao-2026-11-15.md).

## Histórico

As propostas [v1](docs/proposta/proposta-dissertacao-v1-2026-10-28.md), [v2](docs/proposta/proposta-dissertacao-v2-2026-11-06.md) e [v3](docs/proposta/proposta-dissertacao-v3-2026-11-13.md), o [parecer de 05/11](docs/parecer/parecer-metodologico-v1-2026-11-05.md), o [protocolo v3](docs/metodologia/protocolo-experimental-v3.md) e o [registro de 13/11](docs/registro-atualizacao-2026-11-13.md) permanecem nos caminhos originais e contêm formulações superadas. O [acervo histórico](docs/historico/README.md) indica como recuperar cada estado anterior. O [CHANGELOG](CHANGELOG.md) resume a evolução.

A [proposta v4](docs/proposta/proposta-dissertacao-v4-2026-11-14.md), os [protocolos v3/v4](docs/metodologia/mini-revisao-protocolo-wos-2026-11-14.md), o [adendo v4](docs/revisao/protocolo-revisao-literatura.md) e o [protocolo inicial v5](docs/mini-rsl-wos-ecl-ml-v5.md) foram preservados como antecedentes. A apresentação, a configuração ilustrativa e o protocolo experimental ainda precisam de revisão integral frente à v5.

## Desenho analítico

```mermaid
flowchart LR
    F["3040 e estatísticas públicas"] --> D["Múltiplos DGPs e instituições virtuais"]
    D --> M["Replicações de Monte Carlo"]
    M --> R["Regimes R0 a R4"]
    R --> T["Avaliação independente da PD"]
    T --> C["Calibração, erro e transferência negativa"]
    T --> E["Implicações condicionais para ECL sintética"]
```

## Organização e estado de implementação

`src/ecl_suficiencia/` conserva o nome técnico por compatibilidade. Estão implementados apenas auxiliares aritméticos (produto PD × LGD × EAD, peso heurístico, faixas de atraso e diferenças); estimadores, recalibração, fatores experimentais, medidas e validação são interfaces com `NotImplementedError`. Veja o [mapa do protótipo](docs/metodologia/prototipo-e-limites.md).

`configs/` descreve o desenho; não existe executor para o YAML. `experiments/` e `notebooks/` estão reservados. Dados privados em `data/` não são versionados.

## Ambiente e apresentação

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -e ".[dev]"
.\.venv\Scripts\python -m pytest
```

Em Linux/macOS, usar `.venv/bin/python`. Os testes verificam apenas os auxiliares existentes.

Abra `docs/index.html` no navegador. Para reconstruir: `python docs/apresentacao/build.py`. A fonte e as instruções estão em [docs/apresentacao](docs/apresentacao/README.md).

## Licenças e citação

Código sob [MIT](LICENSE). Textos e apresentação sob [CC BY 4.0](docs/LICENSE-CC-BY-4.0.md). As licenças não concedem direitos sobre dados de terceiros. Metadados em [CITATION.cff](CITATION.cff).
