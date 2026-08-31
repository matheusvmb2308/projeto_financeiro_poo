# Projeto Financeiro POO

Projeto de estudo desenvolvido para a disciplina **Programação Orientada a Objetos II**, no Módulo 2 — *Evoluindo o Domínio*. O objetivo é modelar, em Python, o controle financeiro de lançamentos (débitos e créditos), sua consolidação em fechamentos periódicos, a conciliação entre débitos e créditos e a geração de extratos mensais.

O projeto segue, no domínio financeiro, a mesma evolução aplicada ao domínio de e-commerce no material do curso: assim como um **Carrinho** vira **Pedido**, aqui um conjunto de **Lançamentos** vira um **Fechamento**, que por sua vez alimenta um **Extrato**.

## 📁 Estrutura do projeto

```
projeto_financeiro_poo/
├── financeiro/
│   ├── __init__.py
│   ├── categoria.py      # Categoria de um lançamento (ex.: Alimentação)
│   ├── conta.py           # Conta com nome e saldo
│   ├── lancamento.py      # Lançamento financeiro (débito ou crédito)
│   ├── fechamento.py      # Consolida os lançamentos de um período
│   ├── conciliacao.py     # Verifica se débitos e créditos conferem
│   └── extrato.py         # Gera o extrato de um mês/ano
├── tests/
│   ├── __init__.py
│   ├── test_categoria.py
│   ├── test_conta.py
│   ├── test_lancamento.py
│   ├── test_fechamento.py
│   ├── test_conciliacao.py
│   └── test_extrato.py
├── requirements.txt
└── .gitignore
```

## 🧩 Classes principais

| Classe | Responsabilidade |
| --- | --- |
| `Categoria` | Representa a categoria de um lançamento (ex.: Alimentação, Transporte). |
| `Conta` | Guarda nome e saldo de uma conta, com validação ao alterar saldo/nome. |
| `Lancamento` | Representa um lançamento financeiro (descrição, valor, data, categoria e tipo `debito`/`credito`). |
| `Fechamento` | Recebe e consolida uma lista de `Lancamento`, permitindo adicionar/remover itens e calcular totais. |
| `Conciliacao` | Recebe listas de débitos e créditos e verifica se os totais batem (`verifica_conciliacao`). |
| `Extrato` | Agrega os `Fechamento` de um mês/ano e calcula total de lançamentos, débitos, créditos, saldo final e se há conciliação pendente no período. |

## ▶️ Como executar

**Requisitos:** Python 3.10+ (o projeto usa anotações de tipo como `list[Lancamento]`).

```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar os testes
pytest tests/
```

## 🧪 Testes

Cada classe do módulo `financeiro/` possui um arquivo de teste correspondente em `tests/`, utilizando `pytest`.

## 📚 Contexto acadêmico

Este repositório é o "Projeto Financeiro" aplicado ao longo do curso de POO II, como contraponto prático ao domínio de e-commerce apresentado no material da disciplina:

- **Módulo 2, Cap. 5** → criação da classe `Fechamento`
- **Módulo 2, Cap. 6** → criação da classe `Conciliacao`
- **Módulo 2, Cap. 7** → criação da classe `Extrato`

## ❓ Aplicando ao Projeto Financeiro — Módulo 2

Respostas às perguntas propostas nos capítulos 5, 6 e 7 do material do curso, com base na implementação real deste repositório.

### Capítulo 5 — `Fechamento`

**Que informações o `Fechamento` deve guardar?**
No código, `Fechamento` guarda apenas uma lista de `Lancamento` (`self.lancamentos`). Isso é suficiente para consolidar: a partir dela dá pra calcular o total (`calculaTotal`) e a quantidade (`quantidade_lancamentos`). 

**Os lançamentos devem ser copiados ou referenciados?**
Eles são **referenciados** (a mesma instância de `Lancamento` é guardada), mas `getFechamentos()` retorna uma **cópia da lista** (`list(self.lancamentos)`), não uma cópia dos objetos. É o mesmo padrão usado no material do curso para `Pedido.itens` e `Cliente.pedidos`: protege a lista interna de ser alterada por fora, mas os objetos dentro continuam sendo os mesmos — o que faz sentido, já que um lançamento não deveria ser duplicado, só referenciado a partir de diferentes agrupamentos.

**O que acontece se não houver lançamentos no período?**
`calculaTotal()` retorna `0.0` (soma de lista vazia) e `quantidade_lancamentos()` retorna `0` — não há erro, o que é um comportamento razoável (fechamento vazio é um estado válido, diferente do `Carrinho.finalizar()` do material, que levanta `ValueError` se estiver vazio).

### Capítulo 6 — `Conciliacao`

**Classe própria ou método de `Fechamento`?**
`Conciliacao` é uma **classe própria**, separada de `Fechamento` — seguindo o mesmo raciocínio do material para `Pagamento` não virar atributo do `Pedido`: cada classe fica com uma responsabilidade única (`Fechamento` consolida, `Conciliacao` valida).

**Como ela garante a invariante (débitos == créditos)?**
`Conciliacao` recebe duas listas (`debito`, `credito`), soma cada uma (`total_debitos`, `total_creditos`) e `verifica_conciliacao()` retorna um booleano comparando os dois totais. Diferença em relação à sugestão do capítulo: lá a ideia era falhar com uma mensagem clara (ex.: levantar exceção); no código atual a verificação apenas retorna `True`/`False`, sem lançar erro — quem decide o que fazer com esse resultado é o código que chama (no caso, `Extrato.possui_conciliacao_pendente`).

### Capítulo 7 — `Extrato`

**Classe separada ou método de `Fechamento`?**
Também **separada** — igual à decisão do `Cliente.finalizar_compra()` no material, que orquestra várias peças (carrinho, pedido, pagamento) sem colocar tudo numa única classe.

**O extrato detecta conciliação pendente?**
Sim — é exatamente o "desafio extra" do capítulo 7, e já está resolvido: `possui_conciliacao_pendente()` filtra os lançamentos do período por tipo, monta uma `Conciliacao` com eles e retorna `not conciliacao.verifica_conciliacao()`.

**Estrutura do resumo:**
`resumo()` devolve um dicionário com `periodo`, `total_lancamentos`, `total_debitos`, `total_creditos`, `saldo_final` e `conciliacao_pendente` — cobrindo exatamente os itens pedidos no capítulo (total de lançamentos, débitos, créditos e saldo final).

## 📝 Licença

Projeto acadêmico, sem licença específica definida.
