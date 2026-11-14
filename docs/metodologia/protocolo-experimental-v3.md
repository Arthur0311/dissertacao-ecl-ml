# Protocolo experimental — proposta v3

**Estado:** planejamento em 13/11/2026; sem pré-registro concluído, sem microdados confirmados e sem experimentos executados. Este protocolo operacionaliza a [proposta corrente](../proposta/proposta-dissertacao-v3-2026-11-13.md), especialmente seções 3, 6–9. Valores da [configuração](../../configs/experimento-exemplo.yaml) são candidatos.

## 1. Registro anterior ao teste final

Criar um registro datado por experimento com versão da proposta, revisão do código, identificação da base autorizada, período, instituições e carteiras, critérios de inclusão, evento, horizonte, censura, atributos e disponibilidade histórica. Registrar os cortes de treino/validação/teste, maturação dos rótulos, exclusões e contagens por classe. Nenhum teste final pode ser aberto enquanto o registro estiver incompleto.

Fixar algoritmo, espaço de ajuste, orçamento, fontes elegíveis, regra de distância, cortes de compatibilidade e informação, frações e sementes. Registrar comparadores, métricas, unidade de inferência, método de reamostragem, tratamento de falhas, ajuste de multiplicidade e critérios de relevância. Mudança posterior é emenda datada com justificativa e identificação do que já foi observado; não se chama pré-registro retroativamente.

## 2. Disponibilidade e heterogeneidade são eixos distintos

O desenho principal reduz unidades de tomador do desenvolvimento local em frações candidatas de 10%, 40% e 100%, por 20 sementes. Manter o mesmo teste futuro, população elegível e distribuição observada; registrar eventos e não eventos efetivamente sorteados. Não selecionar apenas defaults nem descartar silenciosamente sorteios sem ambas as classes. Simular histórico curto em análise separada. Segmento prudencial não define o regime de informação.

Construir pares de origem–destino compatíveis quanto a evento, horizonte, campos e uso autorizado. Calcular distância usando só desenvolvimento: Wasserstein normalizada para numéricas e variação total para categorias; definir escalas, pesos e tratamento de constantes antes do teste. As diferenças de política e modalidade complementam essa medida. Um indicador de covariáveis não identifica completamente concept shift. A heterogeneidade observada não é aleatorizada; sua associação com desempenho não será interpretada causalmente.

## 3. Regimes comparáveis

- **Local:** desenvolvimento disponível do destino.
- **Agrupado:** origem e esse mesmo desenvolvimento local.
- **Transferido sem adaptação:** somente origem.
- **Adaptado:** modelo da origem mais recalibração local regularizada de intercepto/inclinação.

Usar logística regularizada e gradient boosting com orçamento de busca documentado. O teste do destino não pode ser usado para escolher origem ou ajuste. O algoritmo e a penalização são escolhidos na validação interna cronológica. Fonte e destino não devem compartilhar tomadores que tornem a transferência uma duplicação inadvertida. A avaliação de novos tomadores exige separação adicional entre períodos; a de clientes recorrentes deve ser identificada.

Ausência de informação para ajuste local gera resultado não estimável. A adaptação pode recuar para a identidade/origem conforme regra prévia; contar e publicar esses casos. Ausência de rótulos locais permite transferência pura, não validação de recalibração supervisionada. Modelos hierárquicos ou reponderação são extensões sujeitas a orçamento, não métodos já presentes no código.

## 4. Hipóteses, contrastes e análise

**H1 / objetivo 1:** log-loss(adaptado) − log-loss(local), nos estratos prévios de menor informação e maior compatibilidade; sinal esperado negativo. Comparação pareada somente onde ambos são estimáveis; relatar a fração da população excluída por inviabilidade.

**H2 / objetivo 2:** coeficiente da distância na diferença log-loss(transferido) − log-loss(local), controlando informação local; sinal esperado positivo. Reportar efeitos por par, transferência negativa e intervalos. O número de pares independentes limita os ajustes possíveis; não ajustar regressão complexa a poucas instituições.

**H3 / objetivo 3:** coeficiente de log2(1 + n local), com n local definido como tomadores distintos utilizáveis, na diferença log-loss(adaptado) − log-loss(transferido); sinal esperado negativo na faixa prévia. Contar também contratos, eventos e meses; distinguir aumento de quantidade de aumento de horizonte histórico. Curvas não monotônicas, saturação e efeitos nulos devem ser reportados.

O plano final escolherá a especificação de efeitos por par/janela e covariáveis de controle usando desenvolvimento e simulações de precisão. Com unidades insuficientes, a hipótese correspondente ficará não testável e a análise será descritiva, sem fabricar poder por sementes. Intervalos de 95% e Holm para a família H1–H3. Não se herda o TOST nem a hipótese H5 da v2.

Obrigatoriamente acompanhar log-loss por Brier, intercepto/inclinação, curvas de calibração e intervalos, discriminação, estabilidade e cobertura de execução. Brier/log-loss não medem exclusivamente calibração. Não reportar AUC ou regressão de calibração como definidas quando faltar uma classe ou identificabilidade. Registrar clipping numérico usado em log-loss.

## 5. Cronologia e incerteza

Reservar datas-base futuras com os 12 meses seguintes integralmente observados; treinamento usa apenas rótulos já maturados na data simulada. Aplicar purga/embargo de acordo com sobreposição dos horizontes. Transformações e recalibração ficam dentro da validação aninhada, sem vazamento de prevalência, macro ou seleção.

A reamostragem deve refletir dependência por tomador e blocos de tempo; especificar o algoritmo e tamanho dos blocos antes do teste. Reportar intervalos das diferenças, não apenas intervalos individuais de cada modelo. Repetições de redução de dados medem sensibilidade à amostra, não replicações independentes do sistema financeiro.

## 6. Desdobramento contábil / objetivo 4

Calcular LP12 = PD12 × LGD × EAD com parâmetros comuns para isolar PD. Reportar diferenças em BRL e pontos-base da exposição; separar efeito aritmético de evidência de acurácia. Só tratar como aproximação de ECL de 12 meses quando as perdas/recuperações ao longo da vida decorrentes desses defaults e o desconto estiverem sustentados. Na ausência disso, usar a designação ilustrativa LP12.

Extensão ECL usa cenários ponderados, PD marginal, exposição e recuperação compatíveis, desconto e horizonte apropriados. Não extrapolar PD12 linearmente. Sem recuperações maturadas, não calcular erro monetário como se fosse validado. Comparação regulatória só é habilitada após validação do perímetro, regras por ativo/data e horizonte; diferenças não constituem comandos de lançamento.

## 7. Portões de viabilidade e entregas

Até o mês 3, documentar decisão A (multi-instituição), B (carteiras internas) ou C (prova de conceito), com o ajuste de inferência correspondente. Sem dados brasileiros, suspender conclusões de provisão brasileira e revisar o recorte empírico. Sem identificação estatística, restringir a descrição.

Entregas: manifesto de dados sem conteúdo privado, configuração congelada, métricas por par/janela/semente, registro de falhas, contrastes com incerteza, análise contábil condicionada, consumo de recursos e limitações. Resultados serão escritos em `experiments/` apenas após execução real; as pastas atualmente vazias não demonstram realização dos testes.
