# Template LaTeX do PPGCONT/UFRGS

`ppgcont.sty` reproduz a formatação do `MODELO_PROJETO_PPGCONT-UFRGS_2024.doc` e é
usado pelo [projeto](../projeto/) e pela [dissertação](../dissertacao/). Mudou uma
regra de formatação? Altere só este arquivo.

## O que o template aplica

| Elemento | Regra |
|---|---|
| Página | A4; margens superior e esquerda 3 cm, inferior e direita 2 cm |
| Texto | Times 12, justificado, entrelinhas 1,5, recuo de 1,25 cm |
| Seção primária | `\section{}` → **1 MAIÚSCULAS EM NEGRITO** |
| Seção secundária | `\subsection{}` → 1.1 MAIÚSCULAS SEM NEGRITO |
| Seção terciária | `\subsubsection{}` → **1.1.1 Negrito** |
| Seção quaternária | `\paragraph{}` → 1.1.1.1 Sem destaque |
| Numeração | Canto superior direito, a partir da Introdução; a capa não conta |
| Capa, folha de rosto, sumário | `\capa`, `\folhaderosto`, `\sumario` |
| Listas | `enumerate` → a), b), c) no recuo do parágrafo |
| Tabela | "Tabela 1", título em negrito na linha seguinte, corpo em 10 pt |
| Figura | "**Figura 1.** Título" abaixo da figura |
| Fonte e nota | `\fonte{...}` e `\nota{...}` depois da tabela ou figura |
| Hipótese | `\hipotese{1}{texto}` |
| Citações | APA 7: `\parencite{chave}` → (Autor, 2020); `\textcite{chave}` → Autor (2020) |
| Referências | `\printbibliography`: APA, à esquerda, uma linha em branco entre elas |
| Trecho pendente | `\aescrever` ou `\aescrever[o que falta]` (vermelho no PDF) |

As maiúsculas dos títulos são automáticas: escreva `\section{Introdução}`.

## Ver tudo funcionando

`guia-do-template.tex` mostra cada elemento com o código correspondente:

```bash
latexmk -pdf -outdir=build guia-do-template.tex
```

## Decisões que valem conferir com a orientação

- **Fonte:** o template usa a Times do pacote `newtx`, equivalente ao Times New
  Roman, porque compila com `pdflatex` sem depender de fonte instalada no sistema.
- **Referências:** ficam logo após a última seção, sem quebra de página, como o
  modelo instrui.
- **Dissertação:** o modelo do programa é o do projeto. A dissertação reutiliza a
  mesma formatação; a redação da folha de rosto e os elementos pré-textuais
  próprios da dissertação precisam ser conferidos nas normas do programa.
