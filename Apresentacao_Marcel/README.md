# Apresenta-o_Marcel

# Dataset retirado do paper "The State of the ML-universe: 10 Years of Artificial Intelligence & Machine Learning Software Development on GitHub".


# O Dataset foi extraido através do link fornecido no paper, link utilizado para download dos arquivos em .csv https://zenodo.org/records/3722450

# Após realizar o download dos arquivos .csv foram extraidos os seguintes arquivos para a analise dos dados: 
#   repo-metadata.csv
#   collaboration-issues.csv
#   pull-requests.csv
#   pull-request-history.csv

# Instruções para os relacionamentos entre tabelas disponiveis no arquivo "Relacionamentos entre tabelas.jpg".

# Para a limpeza dos dados nas tabelas foram realizadas da seguinte forma:
#   na tabela "repo-metadata.csv":
#           * Na coluna "Languagem" foi aplicado o filtro que exclui todas as linhas com valores que contem ('CSS','HTML','Jupyter Notebook','Python').
#           * Na coluna "Category" foi substituido os valores que contiam ('Applied'), passaram a se chamar ('Application'), como forma de se adequar ao conteudo que será analisado.
#           * Na coluna "Category" foi aplicado o filtro de valores que contem apenas ('Tool','Application'). 
#
#   na tabela "pull-requests.csv":
#           * Foram removidas todas as linhas que contem valores duplicados.

#       || PARA REPLICAR OS DADOS DOS GRÁFICOS SERÁ NECESSÁRIO APLICAR OS SEGUINTES PASSOS ||

#           Foi criado uma Medida para verificar quais são as 5 linguagens que mais possuem Commits,  Ranking criado com Linguagem DAX: "RANKX(ALL('repo-metadata'[Language]),[Total Commit])" 

#           Foi criado uma Medida para verificar quais são os 5 maoires repositórios de acordo com as linguagens selecionadas acima, Ranking criado com Linguagem DAX: RANKX(ALL('repo-metadata'[name]),[Total Commit]) 

#           GRÁFICO 1.0 -> Utilizar a tabela repo-metadata.csv, Eixo Y: Soma da coluna "Commits", Eixo X: "Date Created", Legenda: "Languagem".

#           GRÁFICO 2.0 -> Utilizar a tabela repo-metadata.csv, Fitrar a coluna "Category" buscando apenas dados que contem valeores ('Tool'), Eixo Y: Porcentagem da soma da coluna "Commits", Eixo X: "Languagem".

#           GRÁFICO 2.1 -> Utilizar a tabela repo-metadata.csv, Fitrar a coluna "Category" buscando apenas dados que contem valeores ('Tool'), Soma da coluna "Commits", Eixo X: "Date Created", Legenda: "Languagem".

#           GRÁFICO 2.2 -> Utilizar a tabela repo-metadata.csv, Fitrar a coluna "Category" buscando apenas dados que contem valeores ('Application') Eixo Y: Porcentagem da soma da coluna "Commits", Eixo X: "Languagem"

#           GRÁFICO 2.3 -> Utilizar a tabela repo-metadata.csv, Fitrar a coluna "Category" buscando apenas dados que contem valeores ('Application'), Soma da coluna "Commits", Eixo X: "Date Created", Legenda: "Languagem".

#           GRÁFICO 3.0 -> Utilizar a tabela repo-metadata.csv, Eixo Y: Contagem da coluna "ght_id", Eixo X: "Languagem", Legenda: "Category".

#           GRÁFICO 4.0 -> Utilizar a tabela repo-metadata.csv, Eixo Y: Contagem da coluna "ght_id", Eixo X: "Date Created", Legenda: "Category".

#           GRÁFICO 5.0 -> Utilizar a tabela collaboration-issues.csv para  (Eixo Y:Contagem de "artifact_id", e para Legenda: "interaction"), utilizar a tabela repo-metadata.csv para o Eixo X: "Language".

#           GRÁFICO 6.0 -> Utilizar a tabela pull-requests.csv para o Eixo Y: "id", utilizar tabela pull-request-history.csv para Eixo X: "created_at", utilizar a tabela repo-metadata.csv para a Legenda: "name"