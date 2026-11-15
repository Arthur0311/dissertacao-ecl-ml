# Registro de atualização — 15/11/2026

## Escopo

Alinhamento dos documentos dependentes e da apresentação à [proposta v5](proposta/proposta-dissertacao-v5-2026-11-14.md). A proposta não foi alterada. Versão documental 0.5.0. A incorporação da estrutura da mini revisão, feita no mesmo dia, está em [registro próprio](revisao/registro-incorporacao-2026-11-15.md).

## Documentos alterados

| Documento | O que mudou |
|---|---|
| [README](../README.md) | Título da v5, documentos correntes, pendências da seção 11 da proposta |
| [CHANGELOG](../CHANGELOG.md), [CITATION.cff](../CITATION.cff), `pyproject.toml` | Versão 0.5.0, título e palavras-chave da v5 |
| [Configuração ilustrativa](../configs/experimento-exemplo.yaml) | Reescrita: instituições virtuais, DGPs, R0–R4, H1–H4 e C1, Monte Carlo |
| [Dicionário de dados](../data_dictionary/README.md) | Reescrito para a base sintética; sem atribuir campos do 3040 |
| [Protocolo experimental v5](metodologia/protocolo-experimental-v5.md) | Novo, no esquema ADEMP, preliminar |
| [Protocolo experimental v4](metodologia/protocolo-experimental-v4.md) | Aviso de superação |
| [Mapa do protótipo](metodologia/prototipo-e-limites.md) | O que a v5 exige; registra que não existe simulador |
| [Notas normativas](normativo/notas-verificacao-normativa.md) | Adendo da seção 7 |
| [Acervo histórico](historico/README.md) | v5 como corrente; síntese v4 → v5 |
| [Apresentação](index.html), [fonte](apresentacao/apresentacao-fragmento-artefato.html) e [instruções](apresentacao/README.md) | Refeita |
| Docstrings em `src/ecl_suficiencia/` | Referências à v5; nenhuma mudança de comportamento |

## Decisões

1. **Protocolo v5 preliminar.** Reproduz o que a proposta já fixa e marca como "a definir" o que ela deixa ao piloto. O congelamento fica no gate G4 do roadmap.
2. **Dicionário sem campos do 3040.** A proposta proíbe atribuir códigos sem confirmação do leiaute oficial. O dicionário descreve entidades, classes de atributo e regras; o mapeamento fica pendente.
3. **Código.** Só docstrings e número de versão. Módulos de versões anteriores (níveis regulatórios, suficiência) foram mantidos e identificados como legado. Nenhum módulo de simulação foi criado.
4. **Notas normativas.** Nenhum dispositivo foi relido. O adendo registra o que a v5 afirma e lista o que falta conferir: art. 51 da Resolução CMN nº 4.966/2021, Instrução Normativa BCB nº 733/2026, versão do leiaute 3040 e parágrafos da IFRS 9.

## Apresentação

Nova estrutura: página inicial com cartões de seção, leitura por seção e modo apresentação com revelação progressiva. Visual baseado no Arphia Docs (Fraunces e Inter, fundo creme, acento vermelho, tema escuro). Doze seções, 51 blocos.

**Regra de conteúdo adotada.** Toda afirmação traz citação ou seção da proposta; toda escolha metodológica tem justificativa com fonte.

**Referências acrescentadas.** Para justificar escolhas que a proposta adota sem citar fonte, a apresentação usa 17 obras que não constam na lista da v5:

Brier (1950); Burton et al. (2006); Friedman (2001); Gneiting e Raftery (2007); Hand (2006); Holm (1979); Kaufman et al. (2012); Lessmann et al. (2015); Moreno-Torres et al. (2012); Niculescu-Mizil e Caruana (2005); Pan e Yang (2010); Pavlou et al. (2015); Savage (1951); Shimodaira (2000); Steyerberg et al. (2004); Sugiyama et al. (2007); van Smeden et al. (2019).

Estão identificadas na apresentação como apoio adicional, com borda tracejada e cor própria no grafo. **Pendência:** confirmar cada uma por leitura na mini revisão e decidir se entram na proposta. A atribuição de cada afirmação a essas obras foi feita de memória do conteúdo e não por releitura dos textos.

**Componentes interativos.** Curva de calibração, erro-padrão de Monte Carlo e sorteio de eventos são ilustrações matemáticas. A carteira de oito contratos é fictícia. O laboratório de brinquedo roda um Monte Carlo logístico no navegador com parâmetros arbitrários e não antecipa resultados.

## Verificações

- Metadados de 23 referências com DOI conferidos na API do Crossref em 15/11/2026 (autores, ano, título, periódico, volume e páginas). Sugiyama et al. (2007) e Holm (1979) não têm DOI e não foram conferidos por essa via. Normas e fontes oficiais repetem a lista da proposta.
- Apresentação percorrida em navegador automatizado, nos temas claro e escuro, a 1280 × 760: 51 blocos, nenhum erro de script, nenhum conteúdo fora do quadro. Leitura em 390 px sem rolagem horizontal. Popover de citação e salto para o grafo testados.
- Testes do pacote: 6 aprovados, com `PYTHONPATH=src`. O pacote não está instalado no ambiente virtual local.
- Configuração YAML carregada sem erro.
- Links locais dos documentos correntes conferidos.

## Não realizado

Nenhum simulador, piloto ou experimento. Nenhuma busca bibliográfica. Nenhuma releitura normativa. O roadmap e os documentos da mini revisão, já alinhados à v5, não foram alterados.
