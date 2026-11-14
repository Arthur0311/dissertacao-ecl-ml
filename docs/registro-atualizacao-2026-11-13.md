# Registro de atualização — 13/11/2026

## Escopo e estado inicial

Atualização local solicitada para refletir modelagem adaptativa de ECL com Machine Learning, transferência entre carteiras com disponibilidade de dados e heterogeneidade distintas, validação de PD e repercussões contábeis, sem presumir escassez em S4/S5. A conversa de referência “Validar avaliação da dissertação” foi recuperada para contexto; não substitui evidência bibliográfica ou normativa.

Foram inspecionados README, propostas v1/v2, parecer, notas normativas, apresentação e construtor, configuração, dicionário, metadados, módulos Python e testes. Não havia documentos Word/PDF/PPTX no repositório a atualizar. A árvore de trabalho inicialmente indicava apenas alteração de modo do arquivo `docs/apresentacao/build.sh` (100755 → 100644), sem mudança de conteúdo. Essa condição preexistente foi preservada.

## Decisões de reformulação

1. **Problema único:** confiabilidade da transferência/adaptação de conhecimento estatístico entre carteiras. Disponibilidade e heterogeneidade são condicionantes; ECL é o desdobramento contábil.
2. **População:** contexto brasileiro e interesse aplicado em S4/S5, com dados e capacidade operacional observados separadamente. Não se presume que novas instituições sejam necessariamente S5 nem que S4/S5 tenham poucos eventos.
3. **Objetivos e hipóteses:** quatro objetivos específicos; H1–H3 sobre adaptação, distância entre domínios e informação local. Removidas do desenho corrente as hipóteses autônomas de seleção macro, equivalência de algoritmos e insuficiência dos mínimos da v2.
4. **Comparadores:** local, agrupado, transferência pura e adaptação regularizada, sob logística e gradient boosting. Técnicas adicionais permanecem extensões condicionadas.
5. **Validação:** rótulos maturados, separação temporal, calibração e discriminação, incerteza, transferência negativa e falhas de estimação. Redução aleatória por tomador evita tratar amostragem apenas de defaults como prevalência natural.
6. **PD → ECL:** LP12 é aproximação; recuperação, EAD, cenários, horizonte e desconto são explicitados. Validação monetária depende de perdas comparáveis. Diferença experimental não é determinação de provisão obrigatória.
7. **Normas:** corrigida a exclusão da BCB 352/2023 e o uso corrente da revogada 309/2023. Ressalvas institucionais e vigência por data registradas na [nota normativa](normativo/notas-verificacao-normativa.md), com fontes oficiais e limites da consulta.
8. **Contribuição:** lacuna ainda sujeita à revisão sistemática; protótipo científico separado de futuro produto comercial. Não há promessa de desempenho, conformidade ou viabilidade econômica comprovados.

## Arquivos correntes e rastreabilidade

- [Proposta v3](proposta/proposta-dissertacao-v3-2026-11-13.md): formulação integral e decisões pendentes.
- [README](../README.md), `CITATION.cff`, `pyproject.toml` e versão do pacote: identificação 0.3.0 e escopo coerente; nome técnico do pacote preservado.
- [Protocolo](metodologia/protocolo-experimental-v3.md) e [configuração](../configs/experimento-exemplo.yaml): mesmos regimes, H1–H3, contrastes e limites; planejamento, não pré-registro concluído.
- [Dicionário](../data_dictionary/README.md): disponibilidade histórica, domínios, evento, censura, recuperação, EAD e regras por vigência.
- [Mapa do protótipo](metodologia/prototipo-e-limites.md) e docstrings: distinguem auxiliares existentes das interfaces não implementadas. Lógica de cálculo e assinaturas preservadas.
- [Apresentação](index.html) e sua fonte: 17 slides, mesmos conceitos e exemplo de sensibilidade explicitamente fictício; recursos antigos preservados no histórico.
- Construtor Python adicionado para Windows; construtor Bash anterior preservado.
- [CHANGELOG](../CHANGELOG.md): nova entrada, mantendo as anteriores.

## Preservação

Propostas v1/v2 e parecer mantidos byte a byte nos caminhos originais. O [acervo histórico](historico/README.md) inclui oito cópias integrais de documentos substituídos e [manifesto SHA-256](historico/2026-11-06-v2/manifesto-sha256.json). O manifesto também registra os três documentos históricos originais e o script Bash. Arquivos sincronizados em `sources/` do projeto ChatGPT não foram alterados.

## Verificações

- Seis testes existentes de auxiliares: aprovados. Não são validação empírica dos modelos ou certificação regulatória.
- Integridade das oito cópias e dos quatro arquivos preservados: conferida pelo manifesto.
- Configuração YAML e metadados YAML/TOML: leitura válida; versões 0.3.0 e H1–H3 consistentes.
- Comparação estrutural do código Python com a revisão inicial: somente docstrings e metadado de versão alterados; nenhum algoritmo de estimação implementado nesta revisão.
- 56 links locais dos documentos correntes e da apresentação: nenhum destino ausente. Links internos de cópias históricas não foram reescritos.
- Apresentação no Microsoft Edge: 17 slides verificados em 1280×720 e conferência de proporção/controles em 390×844. Capturas inspecionadas; nenhum transbordamento de conteúdo detectado, sem erros JavaScript. Navegação, seletor, modo contínuo e cálculo ilustrativo exercitados.
- HTML reconstruído pelo Python: resultado determinístico. Construtores Python e Bash produziram o mesmo conteúdo. O Bash precisou de associação temporária de `python3` ao Python instalado; o construtor Python é a opção direta neste Windows.
- `git diff --check`: sem erros de espaços. As ferramentas de verificação foram instaladas em `.venv/`, ignorada pelo Git; isso não constitui instalação/validação de todo o futuro pipeline científico.

## Limitações e próximos passos científicos

Acesso a dados, instituições, evento definitivo, precisão desejada, cortes, orçamento de ajuste e plano estatístico precisam ser fechados antes dos experimentos. Recuperações e horizontes podem limitar o estudo a sensibilidades de LP12. A literatura não foi objeto de revisão sistemática completa. A verificação normativa foi direcionada; anexos, alterações e aplicação por data/ativo exigem conferência para a fase empírica. No cenário de dados estrangeiros/sintéticos, revisar o recorte empírico e suspender inferências sobre provisões brasileiras.

As alterações são locais, documentadas para revisão. Nenhum dado privado foi obtido, nenhum resultado científico foi inventado e nenhuma publicação remota foi realizada.
