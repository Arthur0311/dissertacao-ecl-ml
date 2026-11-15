# Projeto de dissertação (qualificação)

Projeto de dissertação no modelo do PPGCONT/UFRGS, em LaTeX. Entrega: março de 2027.

## Estrutura

| Pasta/arquivo | Conteúdo |
|---|---|
| `main.tex` | Título, autor, orientador e a ordem das seções |
| `secoes/1-introducao.tex` | 1 Introdução: problema, objetivos, justificativa, delimitação |
| `secoes/2-referencial-teorico.tex` | 2 Referencial teórico e hipóteses |
| `secoes/3-procedimentos-metodologicos.tex` | 3 Procedimentos metodológicos e quadro-síntese |
| `secoes/4-cronograma.tex` | 4 Cronograma |
| `secoes/5-resultados-esperados.tex` | 5 Resultados esperados |
| `referencias/referencias.bib` | Exportação do Zotero (Better BibTeX) |
| `tabelas/`, `figuras/` | Arquivos **gerados** pelo Python; não editar à mão |
| `build/` | Saída da compilação (ignorada pelo Git) |

As seções e subseções seguem o modelo do programa. Cada arquivo traz, em comentário,
a orientação do modelo para aquela seção e a parte da proposta v5 de onde vem o
conteúdo. O marcador `\aescrever` aparece em vermelho no PDF; apague-o ao escrever.

## Compilar

No Cursor, com a extensão LaTeX Workshop: abrir `main.tex` e salvar. No terminal:

```bash
latexmk -pdf -outdir=build main.tex
```

O PDF fica em `projeto/build/main.pdf`.

## Formatação

Vem de [`../latex/ppgcont.sty`](../latex/README.md). Exemplos de tabela, figura,
lista, citação e hipótese: `../latex/guia-do-template.tex`.

## Tabelas e figuras geradas pelo código

```python
from ecl_suficiencia.reporting.latex import salvar_tabela, salvar_figura

salvar_tabela(df, "parametros-dgp", "Parâmetros dos DGPs", documento="projeto")
salvar_figura(fig, "desenho-pesquisa", documento="projeto")
```

No texto: `\tabelagerada{parametros-dgp}` e `\includegraphics{desenho-pesquisa.pdf}`.
