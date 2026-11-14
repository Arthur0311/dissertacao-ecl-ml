# Apresentação da proposta v4

A apresentação corrente é [../index.html](../index.html). Resume a [proposta v4](../proposta/proposta-dissertacao-v4-2026-11-14.md), sem resultados empíricos. O exemplo interativo calcula o viés monetário de uma carteira fictícia sob LGD e EAD comuns; não avalia provisão.

## Fonte e construção

`apresentacao-fragmento-artefato.html` contém metadados, estilo, conteúdo e comportamento. O construtor adiciona o esqueleto do documento HTML.

Na raiz do repositório:

```powershell
python docs/apresentacao/build.py
```

Ou, em Git Bash, com `python3` disponível no PATH:

```bash
bash docs/apresentacao/build.sh
```

Não editar o HTML gerado: atualizar a fonte e reconstruir. A estrutura usa o primeiro fechamento de `style` como fronteira entre cabeçalho e corpo.

## Consulta

Setas ou botões navegam; o seletor escolhe uma seção; o botão Modo contínuo ou a tecla M empilha os slides. O palco mantém proporção 16:9. Há suporte à impressão e à preferência de movimento reduzido.

## Versões anteriores

A apresentação da v3 está no histórico do Git (ver [acervo histórico](../historico/README.md)). A [apresentação da v2](../historico/2026-11-06-v2/docs/index.html) foi preservada em cópia integral. Ambas contêm formulações superadas.
