📂 Estrutura do Projeto
Core da Aplicação (Ingestão)
app.py: O ponto de entrada da aplicação. Contém a lógica da interface de linha de comando (CLI) e as funções CRUD para interagir com o banco de dados. É aqui que o dado nasce.

users_songs.db: Banco de dados relacional (SQLite) que armazena de forma persistente as informações de usuários, bandas e álbuns.

Camada de Processamento (ETL)
export_data.py: Script de integração que utiliza a biblioteca Pandas para extrair dados do SQLite e convertê-los para o formato CSV. Funciona como a ponte entre o operacional e o analítico.

meu pipeline.hpl: Arquivo de configuração do Apache Hop. Contém a orquestração visual do pipeline, realizando transformações, ordenação e limpeza dos dados exportados.

Saídas de Dados (Outputs)
users_songs_export.csv: Arquivo intermediário gerado pelo Python, utilizado como fonte de dados (Source) para o pipeline de ETL.

data_songs.txt / data_year.txt: Resultados finais do processamento. São arquivos formatados e limpos, prontos para serem utilizados em relatórios ou visualizações.
