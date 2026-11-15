# Incorporação da estrutura da mini RSL — 15/11/2026

## Resultado

Estrutura incorporada diretamente ao repositório local e alinhada à proposta v5. Nenhuma busca WoS, importação de registros reais, experimento, commit ou publicação foi realizada. O gate G1 permanece pendente.

## Origem e inspeção

Pacote encontrado em `Downloads/pacote-rsl-dissertacao-ecl-ml.zip`, inspecionado antes da cópia. Somente os caminhos bibliográficos foram incorporados; `INSTALACAO.md` não foi copiado porque descreve instalação futura. SHA-256 do pacote: `d42770eedb46949119a52423ae43c257601ee2cfb131f7e250a7997c06dc67a3`.

Inventário completo dos arquivos do projeto realizado, excluindo apenas metadados Git, ambiente Python e caches. A proposta mais recente encontrada foi a v5 de 14/11/2026. Já existiam um protocolo inicial v5, protocolos v3/v4, um adendo v4 e um roadmap v5 em `docs/`. Não havia `literature/` nem colisão com os caminhos do pacote. `data/` foi preservada.

Antes desta tarefa, `docs/apresentacao/build.sh` já aparecia alterado; proposta v5, protocolo inicial v5 e roadmap v5 já existiam sem rastreamento no Git. O conteúdo de build.sh e da proposta v5 não foi alterado. As mudanças nos dois outros arquivos limitam-se à integração documental solicitada.

## Arquivos criados

- `docs/revisao/fluxo-prisma.md`
- `docs/revisao/protocolo-busca-wos-q0-q6.md`
- `docs/revisao/registro-buscas.md`
- `docs/revisao/registro-incorporacao-2026-11-15.md`
- `literature/README.md`
- `literature/analysis/README.md`
- `literature/analysis/matriz-extracao.xlsx`
- `literature/processed/README.md`
- `literature/processed/triagem_estudos.xlsx`
- `literature/raw/.gitkeep`
- `literature/raw/README.md`
- `literature/references/.gitkeep`
- `literature/references/README.md`

## Arquivos modificados

- `.gitignore`
- `README.md`
- `docs/metodologia/mini-revisao-protocolo-wos-2026-11-14.md`
- `docs/mini-rsl-wos-ecl-ml-v5.md`
- `docs/revisao/protocolo-revisao-literatura.md`
- `docs/roadmap-dissertacao-ecl-ml-v5.md`

## Conflitos e decisões

- README ainda apresentava a v4, sete regimes e acesso a microdados como condicionante. Atualizado para v5, R0–R4 e simulação; materiais anteriores continuam referenciados.
- Protocolo inicial v5 sobrepunha-se ao pacote. Mantido como antecedente com link para o protocolo operacional corrente, que conserva as sete strings do pacote.
- Queries v3/v4 reutilizavam IDs com sentidos diferentes. Notas de vigência e registro de versão evitam misturar execuções.
- Roadmap previa matriz CSV em docs/revisao e movimentação de documentos. Os caminhos operacionais foram atualizados; o roadmap permaneceu em docs/, sem criar cópia em planejamento. A árvore prospectiva foi identificada como planejamento histórico.
- `.gitignore` ignorava qualquer XLSX. Exceções somente para planilhas em literature/raw, processed e analysis; nenhuma regra de data foi removida.
- Modelos do pacote não continham todos os campos solicitados e não possuíam filtros nativos. Foram ampliados preservando as colunas originais; acrescentada aba Origens para múltiplas recuperações. Nenhum estudo foi preenchido.
- Fluxo distingue registros, relatórios e estudos; textos não recuperados e suporte são separados. XLSX e BibTeX da mesma consulta não contam duas vezes.

## Validações

- Preservação por SHA-256: nenhum arquivo anterior excluído; somente os seis arquivos listados sofreram alteração. Proposta v5, código, dados e apresentação preservados.
- As sete queries são idênticas às do pacote, com aspas e parênteses balanceados. Regras TS/booleanos/truncamentos conferidas na documentação oficial da Clarivate; aceitação e sensibilidade na conta institucional continuam pendentes.
- Cinco diagramas (README, três no protocolo e um no fluxo) analisados e renderizados com Mermaid 11.12.2.
- literature/processed/triagem_estudos.xlsx: 22 campos, tabela com filtros, cabeçalho e identificador congelados, 4 validações na aba principal, conteúdo de estudos vazio e XML/ZIP íntegros.
- literature/analysis/matriz-extracao.xlsx: 47 campos, tabela com filtros, cabeçalho e identificador congelados, 3 validações na aba principal, conteúdo de estudos vazio e XML/ZIP íntegros.

- Abas das planilhas renderizadas e inspecionadas visualmente; campos adicionais conferidos. Nenhuma fórmula de resultado foi necessária. Não houve teste de interação no Excel instalado.
- Links relativos dos documentos criados/modificados e regras de inclusão no Git conferidos ao final.
- Diretórios raw, processed, analysis e references disponíveis. `.gitkeep` do pacote mantidos em raw e references, ainda sem dados bibliográficos.

## Pendências e próximos passos

1. Confirmar com a orientação os critérios, período candidato 2009–2026 até a execução, tipos documentais, idioma e índices da assinatura institucional.
2. Abrir Core Collection / Advanced Search; pilotar Q0 e priorizar Q1–Q2. Testar estudos-semente e registrar qualquer ajuste antes da seleção definitiva.
3. Executar Q3–Q6 para fundamentação complementar, mantendo proveniência e classificação. Complementar por citações/títulos quando necessário.
4. Registrar string exata, horário/fuso, filtros, contagens reais, arquivos, lotes e hashes. Exportar XLSX/BibTeX quando disponíveis e preservar originais.
5. Consolidar e deduplicar em processed; triar, ler integralmente, extrair evidências e reconciliar o fluxo PRISMA.
6. Produzir síntese e decisão fundamentada sobre a lacuna. Estrutura preparada não significa revisão concluída.
7. A revisão integral da apresentação, configuração experimental, dicionário e protocolo experimental v4 frente à v5 fica para trabalho posterior. Foram preservados e sinalizados no README.

## Estrutura final

Árvore dos arquivos do projeto, sem `.git`, ambiente virtual ou caches. Os diretórios experimentais anteriores permanecem intactos.

```text
dissertacao-ecl-ml/
├── configs/
│   └── experimento-exemplo.yaml
├── data/
│   ├── processed/
│   │   └── .gitkeep
│   └── raw/
│       └── .gitkeep
├── data_dictionary/
│   └── README.md
├── docs/
│   ├── apresentacao/
│   │   ├── README.md
│   │   ├── apresentacao-fragmento-artefato.html
│   │   ├── build.py
│   │   └── build.sh
│   ├── historico/
│   │   ├── 2026-11-06-v2/
│   │   │   ├── configs/
│   │   │   │   └── experimento-exemplo.yaml
│   │   │   ├── data_dictionary/
│   │   │   │   └── README.md
│   │   │   ├── docs/
│   │   │   │   ├── apresentacao/
│   │   │   │   │   ├── README.md
│   │   │   │   │   └── apresentacao-fragmento-artefato.html
│   │   │   │   ├── normativo/
│   │   │   │   │   └── notas-verificacao-normativa.md
│   │   │   │   └── index.html
│   │   │   ├── CITATION.cff
│   │   │   ├── README.md
│   │   │   └── manifesto-sha256.json
│   │   └── README.md
│   ├── metodologia/
│   │   ├── mini-revisao-protocolo-wos-2026-11-14.md
│   │   ├── mini-revisao-queries-wos-2026-11-14.txt
│   │   ├── protocolo-experimental-v3.md
│   │   ├── protocolo-experimental-v4.md
│   │   └── prototipo-e-limites.md
│   ├── normativo/
│   │   └── notas-verificacao-normativa.md
│   ├── parecer/
│   │   ├── parecer-metodologico-v1-2026-11-05.md
│   │   └── parecer-metodologico-v3-2026-11-14.md
│   ├── proposta/
│   │   ├── proposta-dissertacao-v1-2026-10-28.md
│   │   ├── proposta-dissertacao-v2-2026-11-06.md
│   │   ├── proposta-dissertacao-v3-2026-11-13.md
│   │   ├── proposta-dissertacao-v4-2026-11-14.md
│   │   └── proposta-dissertacao-v5-2026-11-14.md
│   ├── revisao/
│   │   ├── fluxo-prisma.md
│   │   ├── protocolo-busca-wos-q0-q6.md
│   │   ├── protocolo-revisao-literatura.md
│   │   ├── registro-buscas.md
│   │   └── registro-incorporacao-2026-11-15.md
│   ├── LICENSE-CC-BY-4.0.md
│   ├── index.html
│   ├── mini-rsl-wos-ecl-ml-v5.md
│   ├── registro-atualizacao-2026-11-13.md
│   ├── registro-atualizacao-2026-11-14.md
│   └── roadmap-dissertacao-ecl-ml-v5.md
├── experiments/
│   └── .gitkeep
├── literature/
│   ├── analysis/
│   │   ├── README.md
│   │   └── matriz-extracao.xlsx
│   ├── processed/
│   │   ├── README.md
│   │   └── triagem_estudos.xlsx
│   ├── raw/
│   │   ├── .gitkeep
│   │   └── README.md
│   ├── references/
│   │   ├── .gitkeep
│   │   └── README.md
│   └── README.md
├── notebooks/
│   └── .gitkeep
├── src/
│   └── ecl_suficiencia/
│       ├── ecl_engine/
│       │   └── __init__.py
│       ├── features/
│       │   └── __init__.py
│       ├── ingestion/
│       │   └── __init__.py
│       ├── lgd_ead/
│       │   └── __init__.py
│       ├── local_recalibration/
│       │   └── __init__.py
│       ├── macro_selection/
│       │   └── __init__.py
│       ├── pd_models/
│       │   └── __init__.py
│       ├── regulatory_floors/
│       │   └── __init__.py
│       ├── reporting/
│       │   └── __init__.py
│       ├── sufficiency/
│       │   └── __init__.py
│       ├── validation/
│       │   └── __init__.py
│       └── __init__.py
├── tests/
│   └── test_basics.py
├── .gitignore
├── CHANGELOG.md
├── CITATION.cff
├── LICENSE
├── README.md
└── pyproject.toml
```
