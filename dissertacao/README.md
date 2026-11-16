# Dissertação em LaTeX

Texto da dissertação, versionado junto com o código que gera os resultados. Usa a
mesma formatação do [projeto](../projeto/), definida em
[`../latex/ppgcont.sty`](../latex/README.md). Os capítulos 1 a 3 partem do texto do
projeto depois da qualificação.

## Estrutura

| Pasta/arquivo | Conteúdo |
|---|---|
| `main.tex` | Título, autor, orientador e a ordem das partes |
| `preambulo.tex` | Carrega o template e define as macros de notação |
| `pre-textuais/` | Resumo |
| `capitulos/` | Um arquivo por capítulo, com as seções da proposta v5 |
| `apendices/` | Apêndices |
| `referencias/referencias.bib` | Exportação do Zotero (Better BibTeX) |
| `tabelas/`, `figuras/` | Arquivos **gerados** pelo Python; não editar à mão |
| `build/` | Saída da compilação (ignorada pelo Git) |

## Compilar

No Cursor, com a extensão LaTeX Workshop: abrir `main.tex` e salvar. No terminal:

```bash
latexmk -pdf -outdir=build main.tex
```

O PDF fica em `dissertacao/build/main.pdf`.

## Tabelas e figuras geradas pelo código

```python
from ecl_suficiencia.reporting.latex import salvar_tabela, salvar_figura

salvar_tabela(df, "contraste-h1", "Contraste H1: R3 frente a R1")  # tabelas/contraste-h1.tex
salvar_figura(fig, "fig-calibracao")                                # figuras/fig-calibracao.pdf
```

No texto: `\tabelagerada{contraste-h1}` e `\includegraphics{fig-calibracao.pdf}`.
Reexecutar o pipeline atualiza os números no documento.

## A conferir nas normas do programa

O modelo disponível é o do projeto. Para a dissertação, falta conferir a redação da
folha de rosto e os elementos pré-textuais exigidos (abstract, listas, ficha
catalográfica, folha de aprovação).
