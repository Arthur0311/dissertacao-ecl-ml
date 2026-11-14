# Estimação de perdas esperadas com dados limitados

Modelos de aprendizado de máquina para a avaliação de suficiência da provisão para perdas esperadas em instituições financeiras brasileiras dos segmentos S4 e S5 (Resolução CMN nº 4.966/2021).

Projeto de dissertação de mestrado em Controladoria e Contabilidade, PPGCONT/UFRGS, linha de pesquisa Usuários Externos.

> **Status:** proposta em discussão com a orientação. Nenhum resultado empírico foi produzido ainda. Os dispositivos normativos citados devem ser conferidos no texto consolidado vigente e as referências bibliográficas nas fontes primárias.

## O problema em uma frase

As instituições dos segmentos S4 e S5 apuram a provisão pela metodologia simplificada, cujos percentuais por carteira e faixa de atraso são níveis mínimos; a norma exige, ainda assim, montantes suficientes para a totalidade da perda esperada e o registro segregado do excedente. Para cumprir essa avaliação de suficiência, a instituição precisa estimar a perda esperada com histórico curto, poucos eventos de inadimplência e equipe reduzida. A pesquisa investiga em que condições modelos de probabilidade de inadimplência, com personalização por carteira e informação macroeconômica prospectiva, produzem estimativas calibradas para esse fim, e, como desdobramento aplicado, em que carteiras e fases do ciclo essas estimativas excedem os níveis mínimos.

## Conteúdo do repositório

| Caminho | Conteúdo |
|---|---|
| `docs/index.html` | Apresentação interativa da proposta (abre no navegador; publicável via GitHub Pages) |
| `docs/proposta/` | Proposta de dissertação, versão 1 (28/10/2026) e versão 2 reformulada (06/11/2026) |
| `docs/parecer/` | Parecer metodológico sobre a versão 1, que motivou a reformulação |
| `docs/normativo/` | Notas de verificação do enquadramento normativo |
| `docs/apresentacao/` | Fonte da apresentação (fragmento publicado como artefato) e script de construção |
| `src/ecl_suficiencia/` | Esqueleto do protótipo computacional, organizado conforme a seção 8 da proposta |
| `configs/` | Configuração declarativa dos experimentos (exemplo) |
| `data_dictionary/` | Modelo de dicionário de dados e critérios de qualidade |
| `experiments/`, `notebooks/`, `tests/` | Reservados para os experimentos, as análises exploratórias e os testes |
| `data/` | Ignorado pelo Git. Dados de instituições nunca são versionados |

## Como abrir a apresentação

Abra `docs/index.html` em qualquer navegador. Navegação pelas setas do teclado ou pelos pontos no rodapé; o botão "Modo contínuo" empilha todos os slides. Com o GitHub Pages apontado para a pasta `docs/`, a apresentação fica disponível em `https://<usuário>.github.io/<repositório>/`.

## Arquitetura do protótipo (prevista)

```
microdados de contratos ─┐
instituição e carteira ──┼─▶ modelo global ─▶ recalibração híbrida por carteira ─┐
macro e expectativas ────┼─▶ modelo local ──────────────────────────────────────┼─▶ comparação sob escassez controlada ─▶ PD calibrada
                         └─▶ ajuste macro prospectivo (M0 · M1 · M2) ────────────┘                                          │
recuperações ──▶ LGD segmentada ─┐                                                                                         ▼
EAD contratual ──────────────────┼─▶ perda esperada estimada ─▶ avaliação de suficiência ◀── níveis mínimos (C1–C5 × atraso)
                                 └──────────────────────────────────────────────────▶ provisão complementar por carteira e período
```

Os módulos em `src/ecl_suficiencia/` contêm apenas a interface prevista (docstrings e assinaturas). A implementação começa após a confirmação do acesso aos dados, conforme a regra de decisão do item 7.4 da proposta.

## Ambiente

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

## Licenças

Código sob licença MIT (`LICENSE`). Textos, figuras e apresentação sob CC BY 4.0 (`docs/LICENSE-CC-BY-4.0.md`). Os textos normativos citados pertencem aos seus emissores.

## Citação

Veja `CITATION.cff`.
