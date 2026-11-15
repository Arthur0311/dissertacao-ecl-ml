# Fluxo de seleção da mini RSL

**Situação:** nenhuma busca executada; todas as contagens pendentes. [Protocolo](protocolo-busca-wos-q0-q6.md) e [registro](registro-buscas.md).

Modelo de relato inspirado no PRISMA, a adaptar ao processo efetivamente executado. Registros bibliográficos, relatórios/publicações e estudos não são unidades intercambiáveis.

```mermaid
flowchart TD
    A["WoS Q0 a Q6: registros N pendente"] --> C["Consolidação: N pendente"]
    B["Outras vias: registros N pendente"] --> C
    C --> D["Duplicatas removidas: N pendente"]
    C --> E["Registros únicos triados: N pendente"]
    E --> F["Excluídos em título e resumo: N pendente"]
    E --> G["Relatórios procurados: N pendente"]
    G --> H["Não recuperados: N pendente"]
    G --> I["Relatórios avaliados: N pendente"]
    I --> J["Excluídos por motivo: N pendente"]
    I --> K["Relatórios incluídos: N pendente"]
    K --> L["Evidência principal: estudos N pendente"]
    K --> M["Suporte: estudos ou fontes N pendente"]
```

## Contagens a preencher

- Identificação WoS por Q e execução: **pendente**.
- Identificação por outras vias, separada por origem: **pendente**.
- Duplicatas removidas entre consultas, execuções e vias: **pendente**.
- Registros únicos triados: **pendente**.
- Excluídos em títulos/resumos: **pendente**.
- Relatórios procurados: **pendente**.
- Relatórios não recuperados: **pendente**.
- Relatórios avaliados integralmente: **pendente**.
- Relatórios excluídos por motivo principal (listar cada motivo e N): **pendente**.
- Relatórios incluídos, principais e de suporte: **pendente**.
- Estudos únicos principais (`id_estudo`): **pendente**.
- Estudos/fontes únicos de suporte: **pendente**.

## Reconciliação

Registros identificados = WoS + outras vias. Registros únicos = identificados − duplicatas (registrar separadamente qualquer remoção adicional antes da triagem). Registros únicos = excluídos em título/resumo + relatórios procurados, quando cada registro representar um relatório. Relatórios procurados = não recuperados + avaliados. Avaliados = excluídos com motivo + incluídos. A soma dos motivos principais deve igualar o total excluído integralmente.

Contar XLSX e BibTeX da mesma exportação uma única vez. Relatórios incluídos não equivalem necessariamente a estudos únicos: ligar publicações por `id_estudo`, sem apagar referências. Atribuir categoria principal exclusiva para os totais, conservando múltiplos temas na triagem. Normativos recuperados para contextualização ficam identificados como suporte, fora do total de estudos empíricos. Se fontes adicionais forem rastreadas somente após a triagem, adaptar o fluxo com ramificação própria e manter reconciliação auditável.
