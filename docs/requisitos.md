**Requisitos do Sistema – SmartView Lite**

**1. Introdução**

- **1.1. Objetivo:**  **Desenvolver um sistema simples que possa ler dados de produção, calcular indicadores, gerar gráficos para visualização de dados, simular monitoramento de fábrica por meio de relatório.**
- **1.4. Referências:** Citar quaisquer documentos, sites ou materiais que serviram de base para os requisitos.

**2. Descrição Geral**

- **2.1. Requisitos Funcionais (RFs):**
    - *Carregar dados de produção:* `[RF001]`O sistema deve ler automaticamente o arquivo `producao.csv`.
    - *Carregar lista de operadores:* `[RF002]` O sistema deve ler o arquivo `operadores.csv`.
    - *Calcular produtividade:* `[RF003]`O sistema deve calcular total produzido no dia, diferença entre planejado e realizado e porcentagem do atingido.
    - *Gerar relatório:* `[RF004]` O sistema deve imprimir no console um relatório com a data, a produção, meta e o operador responsável.
    - *Exibir gráfico:* `[RF005]`Deve gerar um gráfico usando matplotlib, exibindo a performance diária de produção.
    - *Detectar inconsistências:* `[RF006]` O sistema deve identificar valores negativos, falta de metas, horas trabalhadas zeradas e dados duplicados.
- **2.2. Requisitos Não Funcionais (RNFs) / Atributos de Qualidade:**
    - *Linguagem:* `[RNF001]` O sistema deve ser implementado em Python.
    - *Usabilidade:* `[RNF002]` O dashboard deve ser simples e com facilidade de uso.
    - *Arquitetura:* `[RNF003]` O projeto deve ser organizado em pastas separadas.
    - *Documentação:* `[RNF004]` Todo o código deve estar documentado.