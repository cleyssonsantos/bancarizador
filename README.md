# Bancarizador - MVP

## Visão Geral

O **Bancarizador** é uma solução para integrar múltiplos sistemas bancários (bancarizadores) a um sistema central. Com este projeto, é possível simular ofertas de produtos financeiros, emitir CCB (Cédula de Crédito Bancário), assinar e endossar documentos, e realizar outras operações financeiras. A estrutura foi pensada para ser modular, permitindo facilmente adicionar novos bancarizadores, sem impactar a lógica de negócios central.

Este projeto segue a arquitetura **Clean Architecture**, com o uso do **Adapter Pattern** para garantir que a aplicação seja fácil de manter, expandir e testar. A solução também permite que novos bancarizadores sejam adicionados de forma simples e isolada.

---

## Funcionalidades

- **Simulação de Ofertas**: Permite simular ofertas de produtos financeiros com diferentes condições. Atualmente o que temos é uma amostra de como funcionaria uma simulação de ofertas nessa arquitetura.
- **Não Desenvolvido:Emissão de CCB**: Criação e emissão de Cédulas de Crédito Bancário para formalizar a contratação do produto.
- **Não Desenvolvido:Assinatura e Endosse de CCB**: Processa as assinaturas e o endosse de CCBs para validação de acordos.
- **Integração com Bancarizadores**: Suporte para integrar múltiplos bancarizadores, adaptando suas diferentes APIs de forma transparente.

---

## Arquitetura

A aplicação segue os princípios da **Clean Architecture** e utiliza o **Adapter Pattern** para integrar os bancarizadores de maneira desacoplada. A principal responsabilidade de cada camada é clara:

1. **Camada de Apresentação (Controller)**: Recebe as requisições HTTP e orquestra a execução das operações.
2. **Camada de Domínio**: Contém as regras de negócios e casos de uso (como a simulação de ofertas).
3. **Camada de Infraestrutura**: Faz a comunicação com sistemas externos (como APIs de bancarizadores) e a persistência de dados, além dos serviços utilizados.
4. **Configuração**: Arquivos de configuração e variáveis de ambiente para a aplicação.

---

## Tecnologias Utilizadas

- **FastAPI**: Framework web.
- **Pydantic**: Validação de dados e criação de modelos.

---

## ⚙️ Como Rodar o Projeto

- **Em desenvolvimento**: uvicorn main:app --reload
