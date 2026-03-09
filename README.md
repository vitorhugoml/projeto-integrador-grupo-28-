## Projeto Integrador - Grupo 28: Análise de Sobrevivência do Titanic

## 1. Tema do Projeto
*Análise de sobrevivência dos passageiros do RMS Titanic para identificação de padrões demográficos e socioeconômicos.*

## 2. Integrantes do Grupo
* **Vitor** - [(https://github.com/vitorhugoml)]
* **Karla** - [(https://github.com/karlam-lgtm)]
* **Natalia** - [(https://github.com/natrod141-coder)]
* **Matheus** - [(https://github.com/MatheusEduardo10)]
* **Isabella** - [https://github.com/Bellasguarden]
* **Emerson** - [(https://github.com/emerson-maker)]
* **Pedro** - [(https://github.com/pedrovilaca97)]

## 3. Objetivo da Análise. 
*Identificar quais fatores (como classe, idade e sexo) foram determinantes para a sobrevivência no naufrágio. A base utilizada é a "Titanic - Machine Learning from Disaster" do Kaggle.*

## 4. Planejamento das Tarefas (Cronograma)
| Integrante | Atividade | Prazo | 
| :--- | :--- | :--- |
| **Integrante A** | Limpeza e tratamento dos dados (ETL) | 00/03 |
| **Integrante B** | Criação das visualizações no Power BI/Tableau | 00/03 |
| **Integrante C** | Documentação e revisão final | 00/03 |
| **qualquer int** | Prazo final p/entrega | 23/03 |

## 5. Base de Dados
* **Fonte:** https://www.kaggle.com/datasets/dimplebathija/titanic-machine-learning-from-disaster
* **Contexto:** Titanic: Machine Learning from Disaster

O dataset Titanic – Machine Learning from Disaster, disponível na plataforma Kaggle, é um dos conjuntos de dados mais famosos utilizados para aprendizado de Ciência de Dados e Machine Learning. Ele contém informações sobre os passageiros que estavam a bordo do navio Titanic durante sua viagem inaugural em 1912, quando a embarcação colidiu com um iceberg e afundou no Oceano Atlântico. Esse desastre resultou em grande perda de vidas e se tornou um dos naufrágios mais conhecidos da história.

O objetivo principal desse dataset é permitir que pesquisadores e estudantes desenvolvam modelos de aprendizado de máquina capazes de prever quais passageiros sobreviveram ao desastre, com base em diferentes características presentes nos dados. Entre essas características estão fatores como idade, sexo, classe do passageiro, valor da passagem, número de familiares a bordo e porto de embarque.

O conjunto de dados é dividido em dois arquivos principais:

train.csv: contém os dados dos passageiros juntamente com a informação de sobrevivência, sendo utilizado para treinar modelos de machine learning.

test.csv: possui os mesmos atributos, porém sem o resultado de sobrevivência, sendo utilizado para testar a capacidade de previsão do modelo desenvolvido.

A análise desses dados permite identificar padrões importantes relacionados à sobrevivência no Titanic. Estudos realizados com esse dataset indicam que fatores como gênero, idade e classe social tiveram forte influência nas chances de sobrevivência. Por exemplo, mulheres, crianças e passageiros de classes mais altas tiveram maior probabilidade de sobreviver em comparação com homens adultos e passageiros de classes mais baixas.

Dessa forma, o dataset Titanic é amplamente utilizado em projetos educacionais e competições de ciência de dados, pois permite aplicar diversas técnicas como análise exploratória de dados, limpeza de dados, engenharia de atributos e construção de modelos preditivos. Além de servir como introdução prática ao aprendizado de máquina, ele também ajuda a compreender como os dados podem revelar padrões e apoiar a tomada de decisões baseada em evidências.

## 6. Transformações Planejadas
* Remoção de valores nulos e duplicados.
* Criação de colunas calculadas (ex: Margem de Lucro = Preço - Custo).
* Conversão de formatos de data para análise temporal.

## 7. Ideia Inicial do Dashboard (Métricas e Visualizações)
**Métricas:** Taxa de sobrevivência geral e média de idade dos sobreviventes.
**Visualizações:** Gráfico de barras de sobrevivência por classe social e gráfico de pizza por gênero.
