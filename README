# Flowkit Docker Setup

Este repositório contém uma configuração Docker Compose para criar um ambiente completo de ferramentas voltadas para IA Generativa e gerenciamento de dados. Abaixo estão os serviços incluídos e suas funcionalidades principais.

---

## Serviços Disponíveis

### 1. **Flowise**
- **Imagem**: `flowiseai/flowise`
- **Funcionalidade**:
  - Ferramenta para criar fluxos de trabalho baseados em modelos de linguagem.
  - Ideal para configuração e integração de fluxos complexos para tarefas baseadas em IA Generativa.
- **Configurações Principais**:
  - Porta configurável via variável de ambiente.
  - Suporte para personalização com variáveis adicionais como `APIKEY_PATH` e `SECRETKEY_PATH`.
  - Persistência de dados em `~/.flowise`.

---

### 2. **Ollama**
- **Imagem**: `ollama/ollama:latest`
- **Funcionalidade**:
  - Hospeda modelos de linguagem baseados em IA localmente com suporte a GPUs.
  - Permite experimentação e execução de prompts diretamente no ambiente local.
- **Configurações Principais**:
  - Usa porta `11444`.
  - Suporte à aceleração por GPU com drivers NVIDIA.
  - Dados persistidos em `./ollama/ollama`.

---

### 3. **Flowkit WebUI**
- **Imagem**: `ghcr.io/open-webui/open-webui:main`
- **Funcionalidade**:
  - Interface web para interagir com o Ollama.
  - Permite criar e testar fluxos de trabalho visualmente.
- **Configurações Principais**:
  - Porta `8080`.
  - Integração direta com o Ollama via `OLLAMA_BASE_URLS`.
  - Nome personalizável da interface web via `WEBUI_NAME`.

---

### 4. **LangFlow**
- **Imagem**: `langflowai/langflow:latest`
- **Funcionalidade**:
  - Interface para criar, ajustar e testar fluxos baseados em modelos de linguagem.
  - Facilita o design de pipelines para projetos de IA Generativa.
- **Configurações Principais**:
  - Porta `7860`.
  - Dados armazenados em `langflow_data`.

---

### 5. **Flowkit Postgres**
- **Imagem**: `postgres:16-alpine`
- **Funcionalidade**:
  - Banco de dados relacional para armazenamento persistente.
  - Utilizado para salvar dados estruturados relacionados à execução de modelos e fluxos.
- **Configurações Principais**:
  - Porta configurável via `DATABASE_PORT`.
  - Variáveis de ambiente: `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`.
  - Persistência de dados em `./flowkit-db`.

---

### 6. **Flowkit MongoDB**
- **Imagem**: `mongo`
- **Funcionalidade**:
  - Banco de dados NoSQL para armazenamento flexível.
  - Ideal para projetos que exigem dados não estruturados ou semi-estruturados.
- **Configurações Principais**:
  - Porta: `27017`.
  - Dados persistidos em `mongodb_data`.

---

## Redes e Volumes

- **Rede**: `flowkit-docker` (bridge).
- **Volumes Persistentes**:
  - `postgres_data`: Para dados do PostgreSQL.
  - `flowkit_data`: Para dados do LangFlow.
  - `mongodb_data`: Para dados do MongoDB.

---

## Instruções para Uso

1. Clone este repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_REPOSITORIO>
   ```

2. Configure o arquivo `.env` com as variáveis de ambiente necessárias:
   - Exemplo de `.env`:
     ```env
     PORT=3000
     POSTGRES_DB=flowkit
     POSTGRES_USER=admin
     POSTGRES_PASSWORD=admin
     DATABASE_PORT=5432
     ```

3. Suba os containers:
   ```bash
   docker-compose up -d
   ```

4. Acesse as ferramentas nos endereços correspondentes:
   - **Flowise**: [http://localhost:<PORT>](http://localhost:<PORT>)
   - **Ollama WebUI**: [http://localhost:8080](http://localhost:8080)
   - **LangFlow**: [http://localhost:7860](http://localhost:7860)

---

## Contribuições

Fique à vontade para abrir issues ou enviar pull requests para melhorias e novas funcionalidades.

---

**Licença**: Este projeto está sob a licença [MIT](LICENSE).

