# Dicionário de dados — proposta v4

Modelo a preencher após confirmação de acesso. Referências: [proposta](../docs/proposta/proposta-dissertacao-v4-2026-11-14.md) e [protocolo](../docs/metodologia/protocolo-experimental-v4.md). Nenhuma base foi validada por este documento.

## Registro obrigatório de cada campo

Registrar nome, definição, tipo, unidade, granularidade, fonte autorizada, data de referência, data de disponibilidade, versão, domínio válido, tratamento de ausentes, responsável e uso (atributo, rótulo, auditoria, ECL ou regulação). Um campo calculado posteriormente pode ser rótulo, mas não atributo disponível na data-base.

## 1. Identificação, tempo e domínio

- `id_contrato_pseudonimo` e `id_tomador_pseudonimo`: strings estáveis para agrupamento e prevenção de sobreposição. Hash não prova anonimização; proteger chaves e avaliar reidentificação.
- `instituicao`, `carteira_analitica`, `dominio`: identificam origem/destino; registrar critério de agrupamento, modalidade, política e suas mudanças.
- `segmento_prudencial`, `metodologia_contabil`, `vigencia_enquadramento`: contexto regulatório por instituição/data; segmento não determina volume informacional.
- `data_base`, `data_disponibilidade`, `fim_acompanhamento`: datas essenciais para o corte histórico, maturação e censura.
- `papel_amostral`: treino de origem, desenvolvimento local, validação interna ou teste final; acompanhado de identificador da janela e semente.

## 2. Operações e tomadores: camada de PD

- `modalidade`, `tipo_garantia`, `data_origem`, `vencimento`, `saldo_devedor`, `dias_atraso`: atributos contratuais e de desempenho observados na data-base; documentar moeda e unidade.
- `natureza_tomador`, perfil, renda/faturamento e tempo de relacionamento: somente se necessários, permitidos e historicamente disponíveis; registrar qualidade, atualização e seleção de dados.
- `evento_default_12m`: 0/1 apenas quando o horizonte estiver observado e o evento definido; ausência de seguimento não vira zero.
- `data_primeiro_atraso_90`, `indicador_ativo_problematico`, `data_caracterizacao_problematico`: campos separados; não substituir um pelo outro silenciosamente.
- `data_liquidacao`, `data_cessao`, `data_baixa`, `data_renegociacao`, `cura`: registros para desfechos concorrentes e observação de eventos.

## 3. Informação local e heterogeneidade

Por carteira, janela e amostra, derivar `n_contratos`, `n_tomadores`, `n_eventos`, `n_nao_eventos`, `meses_historico`, `fracao_rotulos_maturados` e completude dos atributos. Identificar redução aleatória versus histórico efetivamente curto. Reportar essas medidas também para instituições com dados abundantes.

Definir campos comuns entre origem e destino antes do experimento. Registrar diferenças de política, modalidade, composição e distância de covariáveis estimada no desenvolvimento; guardar escala, pesos e tratamento de categorias novas. Taxas de default e respectivos intervalos entram separadamente. C1–C5 não definem automaticamente o domínio estatístico.

Campos dos fatores experimentais da proposta v4, gravados por sorteio:

- `nivel_disponibilidade`, `fracao_tomadores`, `semente`, `n_local` (tomadores distintos no desenvolvimento) e indicador de regime não estimável.
- `nivel_distancia`, `lambda_subamostragem`, `prob_destino` (saída do classificador de domínio, estimada só no desenvolvimento) e `separabilidade_nivel` (verificação da manipulação). O tamanho da origem é constante entre níveis.
- Distância observada por par: `dif_taxa_base_logito`, `auc_dominio`, `dist_composicao` e `desajuste_condicional` (excesso de log-loss do modelo da origem no desenvolvimento do destino após correção do intercepto).
- `variaveis_local_reduzido`: lista fixada antes do teste.
- `algoritmo` (logística regularizada ou gradient boosting), `regime` e, para a adaptação por reponderação, `peso_importancia` e o limite aplicado.
- Custo operacional por regime e algoritmo: `tempo_treino`, `tempo_inferencia`, `memoria`, `decisoes_de_ajuste`, `acesso_origem_reestimacao`, com identificação do equipamento.
- `regime_selecionado` por célula, com a janela em que a regra foi derivada e a janela em que foi avaliada.

## 4. Recuperação, exposição e ECL

- `data_evento`, `data_fluxo_recuperacao`, `valor_recuperado`, `custo_recuperacao`, `garantia_realizada`, `fim_observacao_recuperacao`: necessários à LGD estimada e ao tratamento de censura.
- `ead_evento`, saldo e fluxos contratuais, limites e desembolsos: avaliar exposição no default, amortização e comportamento de produtos rotativos; saldo atual pode ser apenas aproximação.
- `taxa_efetiva`, fatores de desconto e prazo esperado: documentar origem e compatibilidade com o instrumento.
- `cenario`, `peso_cenario`, `pd_marginal`, `lgd_cenario`, `ead_cenario`: necessários à extensão multiperíodo; pesos somam um, PD marginal não é PD acumulada repetida.
- `origem_parametro`, intervalo e justificativa: distinguir estimado com dados, externo e arbitrado para sensibilidade. Premissa comum aos modelos isola PD, mas não valida a ECL integral.

Sem recuperações comparáveis e maturadas, reportar LP12/sensibilidade; não usar defaults como perda monetária realizada. Não fixar 24 meses como maturação universal sem avaliar o perfil de recuperação.

Para o viés monetário (proposta v4, seção 6.6), registrar por contrato do teste `lgd_comum`, `ead_comum` e `origem_parametro`; os valores são idênticos entre regimes. O resultado por regime e célula é gravado em `vies_monetario_pb`, com o limiar de materialidade vigente. O viés monetário usa a ocorrência do evento, não a perda realizada.

## 5. Informações prospectivas

Para cada indicador: `data_referencia`, `data_publicacao`, `vintage`, horizonte da previsão, unidade e valor disponível no corte. Para Focus, identificar a expectativa histórica e sua disponibilidade efetiva; a base atual não é automaticamente a versão conhecida no passado. SGS/IBGE e séries revisadas exigem tratamento de revisão e calendário. Valores futuros realizados não são previsões históricas.

## 6. Camada regulatória, separada da PD

Campos condicionados à comparação: `carteira_regulatoria` C1–C5, garantia elegível, atraso, ativo problemático, tipo de operação, base de cálculo, componente de provisão, percentual, regra especial, início/fim da vigência e fonte oficial. Referência: Resolução BCB 352/2023 e alterações aplicáveis, conforme a [nota normativa](../docs/normativo/notas-verificacao-normativa.md).

Separar `provisao_regras`, `provisao_registrada` e `ecl_experimental`. O cálculo de regras deve ser por ativo antes da agregação e necessita de mais informação que carteira × atraso. Sem os campos, a comparação fica desabilitada; não imputar enquadramento jurídico por similaridade estatística.

## 7. Dicionário de eventos a congelar

1. **Evento principal:** primeiro atraso superior a 90 dias dentro de 12 meses, sem evento presente na data-base. É aproximação da definição regulatória de ativo problemático e é denominado evento de inadimplência.
2. **Ativo problemático:** definição alternativa com critérios, datas e qualidade documentados; avaliar separadamente. Sua equivalência ao proxy precisa de evidência.
3. **Cura e recorrência:** definir janela e requisitos; não apagar evento ocorrido nem tratar reentrada como nova observação independente sem regra prévia.
4. **Renegociação:** manter trilha do contrato e evento anterior; verificar se há reestruturação e alteração do risco, em vez de reiniciar automaticamente atraso/histórico.
5. **Baixa:** não equivale a fim de recuperação nem deve eliminar default conhecido; acompanhar fluxos posteriores quando disponíveis.
6. **Cessão:** registrar motivo e data; desfecho posterior desconhecido pode gerar censura informativa, não ausência de default.
7. **Liquidação/prepagamento:** documentar tratamento como término da exposição ou evento competitivo; manter horizonte e população consistentes entre modelos.
8. **Fim de acompanhamento:** horizonte incompleto exige censura/exclusão documentada ou método adequado; nunca rótulo negativo automático.

## 8. Critérios de qualidade

Verificar unicidade de contrato–data-base, sequência temporal, rastreabilidade entre contratos renegociados, coerência de moeda/saldo/atraso, eventos repetidos, duplicação de tomador entre domínios e campos conhecidos apenas depois do corte. Reportar perdas de amostra e mudança de perfil provocadas pelas exclusões. Não excluir carteiras com poucos eventos só para melhorar métricas; registrar inviabilidade de ajuste e limitações de inferência.
