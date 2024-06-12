
# Desafio de Machine Learning Engineering

## Objetivo
Desenvolver um sistema de previsão de churn de clientes usando dados de uma empresa fictícia de telecomunicações. O candidato deve demonstrar habilidades em processamento de dados, engenharia de características, construção e avaliação de modelos de machine learning, bem como na criação de um pipeline de machine learning para produção.

## Datasets
Fornecemos dois datasets:
1. `customers.csv`: Informações demográficas e comportamentais dos clientes.
2. `transactions.csv`: Histórico de transações e interações dos clientes com a empresa.

### Estrutura do `customers.csv`:
- `customer_id`: Identificação única do cliente.
- `age`: Idade do cliente.
- `gender`: Gênero do cliente.
- `signup_date`: Data de cadastro do cliente.
- `region`: Região onde o cliente reside.
- `churn`: Indicador se o cliente cancelou o serviço (0 para não, 1 para sim).

### Estrutura do `transactions.csv`:
- `customer_id`: Identificação única do cliente.
- `transaction_date`: Data da transação.
- `amount`: Valor da transação.
- `service`: Tipo de serviço utilizado na transação.

## Desafios Técnicos

### Parte 1: Processamento de Dados
1. **Limpeza de Dados**:
   - Verificar e tratar valores ausentes.
   - Corrigir ou remover dados inconsistentes.

2. **Engenharia de Características**:
   - Criar novas características a partir dos dados existentes (ex.: tempo de assinatura, frequência de transações, valor total gasto).
   - Normalizar ou padronizar os dados conforme necessário.

### Parte 2: Modelagem
1. **Divisão do Conjunto de Dados**:
   - Dividir os dados em conjuntos de treino e teste.

2. **Seleção e Treinamento de Modelos**:
   - Experimentar com diferentes algoritmos de machine learning (ex.: regressão logística, árvores de decisão, random forest, gradient boosting).
   - Ajustar hiperparâmetros dos modelos.

3. **Avaliação de Modelos**:
   - Usar métricas apropriadas (ex.: acurácia, precisão, recall, F1-score, AUC-ROC) para avaliar os modelos.
   - Comparar e selecionar o melhor modelo com base nas métricas de avaliação.

### Parte 3: Pipeline de Machine Learning
1. **Criação do Pipeline**:
   - Implementar um pipeline completo que inclua todas as etapas desde o carregamento dos dados até a previsão.
   - Automatizar o pré-processamento, treinamento, e validação do modelo.

2. **MLOps**:
   - Configurar o pipeline para ser executado regularmente (ex.: diariamente, semanalmente) usando ferramentas como Apache Airflow ou Kubeflow.
   - Implementar monitoramento para detectar degradação de desempenho do modelo ao longo do tempo.

### Parte 4: Deploy em Produção
1. **Implementação do Modelo em Produção**:
   - Criar uma API (usando Flask, FastAPI ou similar) para disponibilizar o modelo para previsões em tempo real.
   - Implementar testes unitários e de integração para a API.

2. **Monitoramento e Manutenção**:
   - Implementar logs e alertas para monitorar o desempenho da API e do modelo.
   - Estabelecer um processo para atualização periódica do modelo com novos dados.

## Entrega Esperada
O candidato deve fornecer:
1. **Código Fonte**:
   - Scripts de processamento de dados, modelagem, e criação do pipeline.
   - Código da API para deploy do modelo.

2. **Documentação**:
   - Descrição das etapas do processamento de dados e da engenharia de características.
   - Justificativa da escolha dos modelos e hiperparâmetros.
   - Instruções para executar o pipeline e a API.

3. **Relatório de Resultados**:
   - Análise dos resultados dos modelos, incluindo gráficos e métricas.
   - Discussão sobre possíveis melhorias e futuras iterações.

4. **Arquivo README**:
   - Instruções detalhadas para configurar o ambiente e executar o código.
   - Dependências e bibliotecas necessárias.

## Critérios de Avaliação
- **Qualidade do Código**: Clareza, organização, e boas práticas.
- **Precisão do Modelo**: Desempenho do modelo com base nas métricas de avaliação.
- **Completeness**: Cobertura de todos os aspectos do desafio, incluindo MLOps e deploy.
- **Documentação**: Clareza e detalhamento das explicações e instruções fornecidas.
