
<p align="center">
  <img src="BannerGit/bannerPrinciapal.png" alt="Banner do projeto Garimpo" />
</p>


Sistema de divulgação e monitoramento de ofertas com link de afiliado, reunindo automação de coleta/publicação e uma interface web moderna para acompanhamento em tempo real.

## Visão geral

O **Garimpo** é dividido em duas partes principais:

- **`deal-bot/`** — motor em Python responsável por **coletar**, **afiliar**, **deduplicar** e **publicar** ofertas no Telegram. Também expõe uma API HTTP (`web_api.py`) e aplica um **portão de afiliação** (`gate.py`) para impedir a publicação de ofertas sem rastreio.
- **`garimpo-web/`** — painel web em **React + Vite** com um **proxy Node** para o agente de IA.

Essa arquitetura permite centralizar a operação de ofertas em um único projeto: o backend automatiza o fluxo de promoção, enquanto o frontend oferece uma experiência amigável para login, monitoramento e gestão.

## Preview da interface

### Tela principal / login

<p align="center">
  <img src="BannerGit/telaLogin.png" alt="Tela de login do projeto Garimpo" />
</p>

> Sugestão: salve a imagem da interface em `docs/login-preview.png` para que ela apareça corretamente no README.

## Como funciona

O fluxo do Garimpo segue esta lógica:

1. **Coleta de ofertas** em fontes configuradas.
2. **Processamento e validação** dos dados.
3. **Aplicação de link de afiliado** para garantir rastreamento e monetização.
4. **Deduplicação** para evitar publicar a mesma oferta repetidas vezes.
5. **Publicação automatizada** em canais como Telegram.
6. **Visualização e acompanhamento** pelo painel web.

## Funcionalidades

- Monitoramento e divulgação de ofertas.
- Integração com links de afiliado.
- Proteção contra publicação sem rastreamento.
- API HTTP para consumo interno/externo.
- Painel web para acompanhamento.
- Proxy do agente de IA com proteção de chave no servidor.
- Rate limit e autenticação por token no endpoint do agente.

## Arquitetura dos serviços

Ao subir o ambiente completo, você terá os seguintes serviços:

| Serviço | Função |
|---|---|
| `web` | Nginx servindo o frontend e fazendo proxy de `/api` e `/data` |
| `agent-proxy` | Proxy Node do agente, responsável por proteger a `ANTHROPIC_API_KEY` |
| `deal-bot-api` | API HTTP de ofertas, bot e links |
| `deal-bot-worker` | Worker responsável pelo ciclo de publicação |

## Instalação

### Pré-requisitos

Antes de começar, garanta que você tenha instalado:

- **Docker** e **Docker Compose** para rodar tudo com um único comando.
- **Python 3** para desenvolvimento do backend.
- **Node.js** para desenvolvimento do frontend.
- **Git** para clonar o repositório.

## Executando com Docker

A forma mais simples de iniciar o projeto é via Docker:

```bash
cp .env.example .env
# preencha as variáveis necessárias no arquivo .env

docker compose up --build
```

Depois, abra:

```text
http://localhost:8080
```

## Desenvolvimento sem Docker

### Backend Python

Consulte também `deal-bot/README.md` para detalhes específicos.

Exemplo de setup local:

```bash
cd deal-bot
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

Para executar os testes:

```bash
pytest
```

### Frontend + agente

Consulte `garimpo-web/README.md` para instruções detalhadas do frontend e do proxy do agente.

Fluxo comum de desenvolvimento:

```bash
cd garimpo-web
npm install
cp .env.example .env
npm run server
npm run dev
```

## Como fazer login

Com base na interface atual do projeto:

1. Acesse a aplicação no navegador.
2. Na tela inicial, informe seu **e-mail**.
3. Informe sua **senha**.
4. Clique em **Entrar**.

### Login em modo demonstração

Atualmente, o frontend indica suporte a acesso de demonstração:

- **Use qualquer e-mail e senha** para entrar no ambiente demo.

Isso é útil para apresentação do projeto, testes visuais e validação do fluxo inicial da interface.

## Estrutura do projeto

```text
.
├── deal-bot/
├── garimpo-web/
├── docs/
│   ├── banner-placeholder.png
│   └── login-preview.png
└── README.md
```

## Testes

```bash
cd deal-bot
python -m venv .venv && .venv/bin/pip install -e ".[dev]"
.venv/bin/pytest
```

## Segurança e regras de negócio

- O endpoint do agente (`/api/agent`) exige **token** (`AGENT_API_TOKEN`).
- O endpoint também possui **rate limit**, reduzindo risco de abuso e custo excessivo.
- O **portão de afiliação** (`REQUIRE_AFFILIATE_TRACKING=1`) garante que apenas ofertas com rastreamento sejam publicadas.
- A `ANTHROPIC_API_KEY` permanece **somente no servidor**, nunca no bundle do frontend.

## Próximos passos recomendados para o README

Para deixá-lo ainda mais profissional, você pode adicionar:

- Logo oficial do projeto no topo.
- Banner principal real em vez do placeholder.
- GIF ou vídeo curto de navegação no sistema.
- Seção de variáveis de ambiente.
- Instruções de deploy.
- Licença do projeto.
- Créditos e contribuição.

## Status

Projeto em evolução, focado em centralizar ofertas, automação de publicação e experiência web para acompanhamento.
