# Casos de teste

- **CT01 – Leitura dos arquivos CSV**

Objetivo: Verificar se o sistema consegue carregar producao.csv e operadores.csv.
Entrada: Arquivos válidos.
Resultado esperado: DataFrames carregados sem erro.

- **CT02 – Cálculo de produtividade**

Objetivo: Validar o cálculo da porcentagem de meta atingida.
Entrada: Produção = 800, Meta = 1000.
Resultado esperado: 80%.

- **CT03 – Geração de relatório**

Objetivo: Verificar se o relatório é impresso no console.
Resultado esperado: Linha com data, operador, produção e meta.

- **CT04 – Geração de gráfico**

Objetivo: Verificar se o gráfico matplotlib é exibido.
Resultado esperado: Janela com gráfico.

- **CT05 – Dados inconsistentes**

Objetivo: Identificar valores inválidos.
Entrada: horas_trabalhadas = 0.
Resultado esperado: Mensagem de erro indicando dado inválido.