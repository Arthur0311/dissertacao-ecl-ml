# Apresentação da proposta v3

A apresentação corrente é [../index.html](../index.html). Resume a [proposta v3](../proposta/proposta-dissertacao-v3-2026-11-13.md), sem resultados empíricos. O exemplo interativo mostra apenas a propagação aritmética de PD para LP12 sob parâmetros comuns; não avalia suficiência regulatória.

## Fonte e construção

`apresentacao-fragmento-artefato.html` contém metadados, estilo, conteúdo e comportamento. O script adiciona o documento HTML completo. O script Bash preexistente foi preservado integralmente; o construtor Python oferece alternativa no Windows.

Na raiz do repositório:

```powershell
python docs/apresentacao/build.py
```

Ou, em Git Bash, com `python3` disponível no PATH:

```bash
bash docs/apresentacao/build.sh
```

Neste Windows, o alias `python3` não estava configurado. Prefira o comando Python acima; não é necessário alterar o construtor histórico.

Não editar apenas o HTML gerado. Atualizar a fonte e reconstruir. A estrutura usa o primeiro fechamento de `style` como fronteira entre cabeçalho e corpo, conforme o construtor original.

## Consulta

Setas ou botões anterior/próximo navegam; o seletor permite escolher uma seção. O botão Modo contínuo ou a tecla M empilha os slides. O palco mantém proporção 16:9 em telas pequenas. Há suporte à impressão e à preferência de movimento reduzido. As fontes Google são opcionais, com substitutas locais; CSS e JavaScript estão no próprio arquivo.

A [apresentação v2](../historico/2026-11-06-v2/docs/index.html) foi preservada byte a byte, incluindo simulador e grafo antigos. Seu conteúdo é histórico e contém interpretações corrigidas na v3; não deve ser apresentado como proposta corrente.
