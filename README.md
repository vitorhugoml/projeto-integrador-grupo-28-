## Projeto Integrador - Grupo 28: Análise de Sobrevivência do Titanic

## 1. Tema do Projeto
*Análise de sobrevivência dos passageiros do RMS Titanic para identificação de padrões demográficos e socioeconômicos.*

## 2. Integrantes do Grupo
* **Vitor** - [(https://github.com/vitorhugoml)]
* **Karla** - [(https://github.com/karlam-lgtm)]
* **Natalia** - [(https://github.com/natrod141-coder)]
* **Matheus** - [(https://github.com/MatheusEduardo10)]
* **Isabella** - [(https://github.com/Bellasguarden)]
* **Emerson** - [(https://github.com/emerson-maker)]
* **Pedro** - [(https://github.com/pedrovilaca97)]

## 3. Objetivo da Análise. 
*Identificar quais fatores (como classe, idade e sexo) foram determinantes para a sobrevivência no naufrágio. A base utilizada é a "Titanic - Machine Learning from Disaster" do Kaggle.

## 4. Planejamento das Tarefas (Cronograma)
| Integrante | Atividade | Prazo | 
| :--- | :--- | :--- |
| **Karla e Vitor** | Criação e estruturação do repositório no GitHub | 01-03/03/2026 |
| **Natália e Vitor** | Escolha do dataset no Kaggle | 05-08/03/2026 |
| **Vitor, Pedro e Isabella** | Redação da seção 'Tema, contexto e objetivo' no README | 10-13/03/2026 |
| **Matheus e Natália** | Planejamento das transformações de ETL | 13-16/03/2026 |
| **isabella e Pedro** | Definição das métricas, KPIs e visualisações do dashboard | 13-16/03/2026 |
| **Pedro, Karla e Emerson** | Revisão cruzada do conteúdo técnico e textual | 17-18/03/2026 |
| **Matheus, Emerson e Natália** | Ajustes finais, conferência de links, padronização do README | 18-20/03/2026 |
| **Vitor** | Entrega Oficial: envio do link do repositório | 20-23/03/2026 |

## 5. Base de Dados
* **Fonte:** https://www.kaggle.com/datasets/dimplebathija/titanic-machine-learning-from-disaster
* **Contexto:** Titanic: Machine Learning from Disaster

O dataset Titanic – Machine Learning from Disaster, disponível na plataforma Kaggle, é um dos conjuntos de dados mais famosos utilizados para aprendizado de Ciência de Dados e Machine Learning. Ele contém informações sobre os passageiros que estavam a bordo do navio Titanic durante sua viagem inaugural em 1912, quando a embarcação colidiu com um iceberg e afundou no Oceano Atlântico. Esse desastre resultou em grande perda de vidas e se tornou um dos naufrágios mais conhecidos da história.

O objetivo principal desse dataset é permitir que pesquisadores e estudantes desenvolvam modelos de aprendizado de máquina capazes de prever quais passageiros sobreviveram ao desastre, com base em diferentes características presentes nos dados. Entre essas características estão fatores como idade, sexo, classe do passageiro, valor da passagem, número de familiares a bordo e porto de embarque.

O conjunto de dados é dividido em três arquivos principais:

train.csv: contém os dados dos passageiros juntamente com a informação de sobrevivência, sendo utilizado para treinar modelos de machine learning.

test.csv: possui os mesmos atributos, porém sem o resultado de sobrevivência, sendo utilizado para testar a capacidade de previsão do modelo desenvolvido.

gender_submission.csv: funciona como um gabarito de formato, servindo exclusivamente para orientar a criação do arquivo de submissão final do projeto, e não como fonte de dados para aprendizado de máquina.

A análise desses dados permite identificar padrões importantes relacionados à sobrevivência no Titanic. Estudos realizados com esse dataset indicam que fatores como gênero, idade e classe social tiveram forte influência nas chances de sobrevivência. Por exemplo, mulheres, crianças e passageiros de classes mais altas tiveram maior probabilidade de sobreviver em comparação com homens adultos e passageiros de classes mais baixas.

Dessa forma, o dataset Titanic é amplamente utilizado em projetos educacionais e competições de ciência de dados, pois permite aplicar diversas técnicas como análise exploratória de dados, limpeza de dados, engenharia de atributos e construção de modelos preditivos. Além de servir como introdução prática ao aprendizado de máquina, ele também ajuda a compreender como os dados podem revelar padrões e apoiar a tomada de decisões baseada em evidências.

## 6. Transformações Planejadas (processamente com Pandas)
6.1. Padronização e Limpeza de Dados
 * Renomeação de Colunas: Tradução e padronização para o formato snake_case (ex: de PassengerId para id_passageiro, Pclass para classe_pax) para facilitar a codificação.
 * Ajuste de Tipagem: Conversão de variáveis categóricas (como porto de embarque) para o tipo category, reduzindo o uso de memória.
6.2. Tratamento de Dados Ausentes (Data Imputation)
 * Coluna Age (Idade): Preenchimento de valores nulos utilizando a mediana agrupada por Classe e Sexo. Isso evita que a média geral ignore as diferenças de perfil entre as cabines.
 * Coluna Embarked: Preenchimento dos valores faltantes com a moda (Porto "S" - Southampton), por ser o ponto de partida da maioria dos passageiros.
 * Coluna Cabin: Criação de uma categoria sinalizadora "Nao_Informado", transformando a ausência de dado em uma variável de análise (pode indicar passageiros sem cabine fixa).
6.3. Engenharia de Variáveis (Feature Engineering)
Criaremos novas métricas que não existem no dado original, mas que são cruciais para o Dashboard:
 * Tamanho_Familia: Junção das colunas SibSp (irmãos/cônjuge) e Parch (pais/filhos) + 1.
 * Viajava_Sozinho: Variável binária (Sim/Não) derivada do tamanho da família.
 * Titulo_Social: Extração de prefixos dos nomes (Ex: Mr, Miss, Master, Dr) para analisar se o status social influenciou na prioridade de salvamento.
6.4. Normalização e Agregações
 * Faixas Etárias: Criação de colunas de agrupamento: Criança (0-12), Adolescente (13-17), Adulto (18-59) e Idoso (60+).
 * Métricas de Sobrevivência: Geração de tabelas agregadas com a Taxa de Sobrevivência (%) segmentada por classe, gênero e faixa etária para alimentação direta dos gráficos.
6.5. Geração da Base Final
 * Exportação: O resultado final será salvo na pasta /data/processed/titanic_cleaned.csv, servindo como fonte de dados única e otimizada.

## 7. Ideia Inicial do Dashboard (Métricas e Visualizações)
**Métricas:** Taxa de sobrevivência geral e média de idade dos sobreviventes.
**Visualizações:** Gráfico de barras de sobrevivência por classe social e gráfico de pizza por gênero.
