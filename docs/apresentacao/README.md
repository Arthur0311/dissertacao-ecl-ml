# Apresentação da proposta v5

A apresentação corrente é [../index.html](../index.html). Expõe a [proposta v5](../proposta/proposta-dissertacao-v5-2026-11-14.md), sem resultados. Tem 12 seções e 51 blocos, contando a capa e as aberturas de seção.

## Como usar

- **Modo documento.** A página inicial lista as seções em cartões. Cada seção abre como página de leitura, com navegação para a anterior e a próxima.
- **Modo apresentação.** Botão Apresentar ou tecla `P`. Setas, espaço ou toque lateral avançam; os itens de cada slide entram um a um. `F` alterna tela cheia, `T` alterna o tema, `Esc` sai.
- **Citações.** Cada chave de citação abre a referência completa e leva ao grafo. As marcas `§` indicam a seção da proposta v5 que sustenta a afirmação.
- **Grafo de referências.** Último bloco. Nós arrastáveis, busca, detalhe com a lista de blocos em que cada obra é citada e alternância para a lista em APA.

## Regras de conteúdo

1. Toda afirmação traz uma citação ou a seção da proposta v5 de onde vem.
2. Toda escolha metodológica tem um quadro "Por que", com a justificativa e a fonte. O quadro-resumo está na seção 12.
3. As referências com borda tracejada são **apoio metodológico acrescentado na apresentação**. Não constam na lista da proposta v5 e devem ser confirmadas na mini revisão antes de entrarem no texto da dissertação. Os metadados das que têm DOI foram conferidos no Crossref em 15/11/2026.
4. Os componentes interativos são ilustrações matemáticas ou aritméticas, identificadas como tais. O "laboratório de brinquedo" executa um Monte Carlo no navegador com DGP logístico e parâmetros arbitrários; não é o simulador da dissertação e não antecipa resultados.

## Fonte e construção

`apresentacao-fragmento-artefato.html` contém metadados, estilo, conteúdo e comportamento, sem bibliotecas externas além das fontes tipográficas. O construtor adiciona o esqueleto do documento HTML.

Na raiz do repositório:

```powershell
python docs/apresentacao/build.py
```

Ou, em Git Bash, com `python3` disponível no PATH:

```bash
bash docs/apresentacao/build.sh
```

Não editar o HTML gerado: atualizar a fonte e reconstruir. A estrutura usa o primeiro fechamento de `style` como fronteira entre cabeçalho e corpo.

## Versões anteriores

As apresentações da v3 e da v4 estão no histórico do Git (ver [acervo histórico](../historico/README.md)). A [apresentação da v2](../historico/2026-11-06-v2/docs/index.html) foi preservada em cópia integral. Todas contêm formulações superadas.
