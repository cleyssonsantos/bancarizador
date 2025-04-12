# Arquitetura do Projeto - Bancarizador

## Visão Geral

O projeto foi desenvolvido seguindo os princípios da **Clean Architecture** e utilizando o **Adapter Pattern** para permitir a integração de múltiplos bancarizadores. O objetivo principal é garantir que a lógica de negócios (core) do sistema permaneça independente das implementações específicas de cada bancarizador.

## Decisão de Arquitetura: Clean Architecture + Adapter

### 🔹 Por que utilizar a **Arquitetura Limpa**?

A Arquitetura Limpa (Clean Architecture), proposta por Robert C. Martin (Uncle Bob), é um modelo que visa **separar responsabilidades** de forma clara, mantendo o **código desacoplado, testável e de fácil evolução**.

No contexto do projeto **Bancarizador**, ela foi escolhida porque:

- Precisamos integrar com **vários provedores externos (bancarizadores)** que possuem formatos diferentes de autenticação, endpoints e regras.
- Queremos isolar o **core da aplicação (regras de negócio)** para que ele **não dependa de nenhuma implementação externa**.
- Buscamos manter o projeto **escalável**, preparado para crescer com segurança e sem "quebrar" o sistema quando novos bancarizadores forem adicionados.
- Facilita a **testabilidade de cada camada** de forma isolada (unit, integration, e2e).

---

### 🔹 Por que utilizar o **Design Pattern Adapter**?

O padrão **Adapter** foi adotado para tratar da **variação de implementações dos bancarizadores** de forma elegante e flexível.
Mais informações sobre o padrão Adapter: https://refactoring.guru/design-patterns/adapter

No projeto:

- Cada bancarizador possui APIs e autenticações próprias.
- O Adapter permite **padronizar a comunicação** entre o sistema e qualquer provedor externo, implementando uma **interface comum** (`BancarizadorPort`).
- Isso mantém o **use case isolado e agnóstico** sobre qual bancarizador está sendo usado, respeitando o **princípio da inversão de dependência (DIP)**.
- Facilita a **troca ou adição de novos provedores**, bastando apenas criar um novo adapter que implemente a interface.

---

### Benefícios dessa combinação

| Vantagem                            | Descrição                                                                 |

| Desacoplamento                      | As camadas não conhecem os detalhes umas das outras                       |
| Testabilidade                       | Cada camada pode ser testada isoladamente                                 |
| Flexibilidade para novos provedores | Basta adicionar um novo Adapter sem mexer no core                         |
| Manutenção facilitada               | Alterações em APIs externas não afetam regras de negócio                  |
| Reutilização de lógica              | Use cases e entidades podem ser reaproveitadas em outros contextos        |

---

### Possíveis desvantagens

| Desvantagem                        | Mitigação                                                                 |

| Estrutura mais complexa            | Justificada pela escalabilidade e múltiplas integrações                   |
| Mais arquivos/pastas               | Organização clara e padronizada evita confusão                            |
| Overhead inicial de implementação  | Compensado pela redução de retrabalho no futuro                           |

---

### Conclusão

A junção da **Arquitetura Limpa com o padrão Adapter** foi essencial para garantir que o projeto do **Bancarizador** seja:

- **Sustentável** a longo prazo,
- **Escalável** para novos parceiros,
- E **confiável** mesmo em contextos complexos de negócio.

Essa escolha arquitetural garante que o sistema continue **ágil, testável e desacoplado**, mesmo com integrações com múltiplos serviços externos distintos.


---

## Estrutura de Pastas

### 1. `src/controllers/` → **Camada de Apresentação (Entrada)**
- **Responsabilidade**: Recebe as requisições HTTP, valida dados de entrada e aciona o caso de uso correspondente. Nunca contém lógica de negócio.
- **Exemplo**: O arquivo `bancarizador_controller.py` define endpoints como `POST /oferta/simular`, criando DTOs e chamando o caso de uso de simulação.
- **Comunicação**: 
  - Recebe dados da camada de apresentação (ex: FastAPI).
  - Chama `src/domain/use_cases/`.

---

### 2. `src/domain/` → **Núcleo da Regra de Negócio**
- **Responsabilidade**: Contém as regras de negócio principais, como a definição de modelos de dados e a implementação dos casos de uso.
- **Subpastas**:
  - **`models/`**: Define os modelos principais do domínio, como a estrutura de `Oferta`. Usado nos use_cases.
  - **`dto/`**: Contém os DTOs usados para a comunicação entre as camadas, como `SimularOfertaInputDTO`. Usado na "viewer", comunicação entre camadas.
  - **`use_cases/`**: Define os casos de uso (ex: simular oferta, emitir CCB).
  - **`ports/`**: Define as interfaces de comunicação com a infraestrutura (ex: `BancarizadorPort`).
- **Comunicação**: 
  - **Com controllers**: Recebe dados da entrada e chama os casos de uso.
  - **Com infraestrutura**: Usa interfaces (ports) para se comunicar com a infraestrutura, mantendo o código desacoplado.

---

### 3. `src/infrastructure/` → **Mundo Externo (Infraestrutura)**
- **Responsabilidade**: Contém as integrações com sistemas externos, como APIs de bancarizadores e autenticações.
- **Subpastas**:
  - **`adapters/`**: Implementações específicas de cada bancarizador. Aqui ocorre o **Adapter Pattern**, transformando as interfaces externas em algo que o sistema entende.
    - Exemplo: `qitech_adapter.py` implementa a interface `BancarizadorPort` para a integração com a Qitech.
  - **`resolver/`**: Resolvem qual adapter utilizar com base na configuração do produto.
  - **`repositories/`**: Caso seja necessário acessar o banco de dados para persistência de dados (como configuração de produtos).
- **Comunicação**: 
  - **Com o domínio**: Adaptadores implementam as interfaces de portas definidas no domínio e comunicam-se com a camada de casos de uso.
  - **Com os controllers**: Adaptadores são resolvidos dinamicamente com base nas configurações de produto.

---

### 4. `src/config/` → **Configuração**
- **Responsabilidade**: Contém configurações do sistema, como variáveis de ambiente ou arquivos de configuração.
- **Exemplo**: Arquivo `settings.py` usando `pydantic.BaseSettings` para carregar variáveis de configuração.

---

### 5. `main.py` → **Ponto de Entrada**
- **Responsabilidade**: Inicia a aplicação e sobe o servidor (ex: FastAPI). É o ponto de entrada do sistema.
- **Comunicação**: 
  - Registra as rotas definidas no controller e disponibiliza a API para comunicação com o cliente.

---

## Testes

A arquitetura de testes está organizada em três tipos de testes:

- **`unit/`**: Testes unitários para testar a lógica isolada, como a execução de um caso de uso.
- **`integration/`**: Testes de integração para verificar a comunicação com um adaptador específico (ex: integração com a Qitech).
- **`e2e/`**: Testes ponta a ponta para validar o fluxo completo de simulação de oferta, desde a requisição do usuário até a resposta final.

---

## Fluxo de Execução

1. O **controller** recebe uma requisição (`POST /simular`), valida os dados e os converte para um DTO.
2. O **use case** `SimularOferta` é chamado e resolve qual **adapter** usar com base na configuração do produto.
3. O **adapter** correspondente faz a comunicação com a API do bancarizador, adaptando a resposta para o formato esperado pelo sistema.
4. A resposta final é retornada ao usuário com os dados simulados.

---

## Como Adicionar um Novo Bancarizador?

1. Crie a pasta `src/infrastructure/adapters/nome/` para o novo bancarizador.
2. Adicione os arquivos:
   - `nome_client.py`: Cliente para a API do bancarizador.
   - `autenticacao.py`: Lógica de autenticação, se necessário.
   - `nome_adapter.py`: Adaptador que implementa a interface `BancarizadorPort`.
3. No arquivo `resolver/bancarizador_resolver.py`, adicione a lógica para resolver o novo adaptador conforme a configuração do produto.

---

## Regras de Ouro

- **Domínio não sabe nada sobre a infraestrutura.**
- **Use cases não sabem com quem estão falando, só que eles implementam a interface.**
- **Cada bancarizador é "adaptado" à realidade do seu domínio.**
- **Nada quebra se uma API externa mudar.**
