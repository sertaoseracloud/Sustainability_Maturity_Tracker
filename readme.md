# 🌱 Sustainability Maturity Tracker

Este projeto automatiza o versionamento e o envio de critérios de maturidade relacionados a práticas sustentáveis como **GreenOps** e **Green Software**, utilizando **GitHub Actions** e **Azure Data Lake Storage Gen2 (ADLS Gen2)**.

## 📦 Objetivo

Permitir o rastreamento contínuo da evolução de práticas sustentáveis em TI por meio de um arquivo `maturity.json`, versionado automaticamente com base na data do envio e armazenado com segurança na nuvem.

---

## 📘 Estrutura do `maturity.json`

O arquivo contém duas categorias principais:

- `GreenOps`: práticas sustentáveis aplicadas à infraestrutura, automação e observabilidade em cloud.
- `GreenSoftware`: boas práticas de desenvolvimento sustentável e eficiente em software.

### Exemplo:

```json
{
    "GreenOps": [
        {
            "id": "GO001",
            "título": "Monitoramento centralizado de consumo energético",
            "descrição": "Coleta e visualização contínua de métricas de consumo de energia dos recursos de TI.",
            "pilar": "Observabilidade",
            "categoria": "infra",
            "relevante_para": ["cloud", "monitoramento"],
            "criterio": 2
        },
        {
            "id": "GO002",
            "título": "Medição da pegada de carbono dos workloads",
            "descrição": "Ferramentas ou processos para calcular a emissão de carbono dos serviços em nuvem ou sistemas.",
            "pilar": "Observabilidade",
            "categoria": "devops",
            "relevante_para": ["cloud", "sustentabilidade"],
            "criterio": 1
        },
        {
            "id": "GO003",
            "título": "Alertas para uso anômalo de recursos",
            "descrição": "Configuração de alertas que disparam quando o consumo de recursos se desvia de padrões sustentáveis.",
            "pilar": "Observabilidade",
            "categoria": "devops",
            "relevante_para": ["monitoramento", "infraestrutura"],
            "criterio": 2
        },
        {
            "id": "GO004",
            "título": "Logs detalhados de uso de recursos",
            "descrição": "Registro granular do consumo de CPU, memória e rede por aplicação para análise energética.",
            "pilar": "Observabilidade",
            "categoria": "devops",
            "relevante_para": ["monitoramento", "infraestrutura"],
            "criterio": 1
        },
        {
            "id": "GO005",
            "título": "Dimensionamento adequado de instâncias",
            "descrição": "Redimensionar instâncias e clusters de acordo com a demanda para evitar recursos ociosos.",
            "pilar": "Otimização de Recursos",
            "categoria": "infra",
            "relevante_para": ["cloud", "containers"],
            "criterio": 1
        },
        {
            "id": "GO006",
            "título": "Escalonamento automático baseado em demanda",
            "descrição": "Configurar auto-scaling para ajustar automaticamente recursos computacionais conforme variação de carga.",
            "pilar": "Otimização de Recursos",
            "categoria": "devops",
            "relevante_para": ["cloud", "kubernetes"],
            "criterio": 2
        },
        {
            "id": "GO007",
            "título": "Desligamento de recursos inativos",
            "descrição": "Políticas e scripts para encerrar máquinas virtuais, contêineres ou serviços sem uso por longos períodos.",
            "pilar": "Otimização de Recursos",
            "categoria": "devops",
            "relevante_para": ["cloud", "automação"],
            "criterio": 0
        },
        {
            "id": "GO008",
            "título": "Uso de serviços gerenciados otimizados",
            "descrição": "Preferência por serviços nativos de nuvem que fazem otimização automática de recursos e escala eficiente.",
            "pilar": "Otimização de Recursos",
            "categoria": "devops",
            "relevante_para": ["cloud", "infraestrutura"],
            "criterio": 1
        },
        {
            "id": "GO009",
            "título": "Desligamento programado de ambientes de teste",
            "descrição": "Programar desligamento de ambientes de desenvolvimento/teste fora do horário comercial para economizar energia.",
            "pilar": "Automação",
            "categoria": "devops",
            "relevante_para": ["CI/CD", "infraestrutura"],
            "criterio": 2
        },
        {
            "id": "GO010",
            "título": "Pipelines CI/CD eficientes",
            "descrição": "Builds e deploys otimizados que evitam etapas desnecessárias e reutilizam caches para reduzir uso de recursos.",
            "pilar": "Automação",
            "categoria": "devops",
            "relevante_para": ["CI/CD", "cloud"],
            "criterio": 1
        },
        {
            "id": "GO011",
            "título": "Scripts para desligamento de servidores ociosos",
            "descrição": "Uso de scripts ou ferramentas que automaticamente desligam servidores inativos após período definido.",
            "pilar": "Automação",
            "categoria": "infra",
            "relevante_para": ["infraestrutura", "scripts"],
            "criterio": 2
        },
        {
            "id": "GO012",
            "título": "Provisionamento via Infrastructure-as-Code",
            "descrição": "Uso de IaC para criar e replicar infraestrutura verde de forma versionada e auditável.",
            "pilar": "Automação",
            "categoria": "devops",
            "relevante_para": ["automação", "infraestrutura"],
            "criterio": 0
        },
        {
            "id": "GO013",
            "título": "Testes automatizados de desempenho energético",
            "descrição": "Executar testes automatizados que avaliem o consumo energético ou emissões de carbono do sistema.",
            "pilar": "Automação",
            "categoria": "desenvolvimento",
            "relevante_para": ["CI/CD", "medição"],
            "criterio": 1
        },
        {
            "id": "GO014",
            "título": "Metas de sustentabilidade alinhadas ao FinOps",
            "descrição": "Definição de objetivos claros de redução de carbono integrados às práticas de gestão de custos em nuvem.",
            "pilar": "Governança e FinOps",
            "categoria": "devops",
            "relevante_para": ["governança", "FinOps"],
            "criterio": 1
        },
        {
            "id": "GO015",
            "título": "Política de tags para consumo energético",
            "descrição": "Obrigatoriedade de tags em recursos (ex.: nível de criticidade ou impacto ambiental) para facilitar análise.",
            "pilar": "Governança e FinOps",
            "categoria": "infra",
            "relevante_para": ["governança", "cloud"],
            "criterio": 0
        },
        {
            "id": "GO016",
            "título": "Relatórios periódicos de pegada de carbono",
            "descrição": "Geração de relatórios frequentes sobre emissões de TI e consumo energético consolidado.",
            "pilar": "Governança e FinOps",
            "categoria": "infra",
            "relevante_para": ["relatórios", "sustentabilidade"],
            "criterio": 1
        },
        {
            "id": "GO017",
            "título": "Revisão regular de recursos vs demanda",
            "descrição": "Auditorias periódicas para verificar se os recursos provisionados atendem adequadamente à demanda atual.",
            "pilar": "Governança e FinOps",
            "categoria": "devops",
            "relevante_para": ["auditoria", "processos"],
            "criterio": 2
        },
        {
            "id": "GO018",
            "título": "Uso de regiões com energia renovável",
            "descrição": "Hospedar aplicações em regiões ou datacenters que utilizam majoritariamente fontes renováveis de energia.",
            "pilar": "Eficiência Energética",
            "categoria": "infra",
            "relevante_para": ["cloud", "sustentabilidade"],
            "criterio": 0
        },
        {
            "id": "GO019",
            "título": "Seleção de hardware energeticamente eficiente",
            "descrição": "Escolher máquinas, instâncias ou CPUs com certificações ou designs que priorizem baixo consumo.",
            "pilar": "Eficiência Energética",
            "categoria": "infra",
            "relevante_para": ["infraestrutura", "hardware"],
            "criterio": 2
        },
        {
            "id": "GO020",
            "título": "Balanceamento de carga verde",
            "descrição": "Distribuir cargas considerando a eficiência energética dos datacenters disponíveis.",
            "pilar": "Eficiência Energética",
            "categoria": "infra",
            "relevante_para": ["cloud", "balanceamento"],
            "criterio": 1
        },
        {
            "id": "GO021",
            "título": "Otimização de refrigeração",
            "descrição": "Monitorar e ajustar sistemas de refrigeração no datacenter para reduzir consumo de energia.",
            "pilar": "Eficiência Energética",
            "categoria": "infra",
            "relevante_para": ["datacenter", "energia"],
            "criterio": 2
        },
        {
            "id": "GO022",
            "título": "Políticas de retenção de dados",
            "descrição": "Definição de prazos para arquivar ou excluir dados obsoletos, reduzindo armazenamento inativo.",
            "pilar": "Sustentabilidade de Dados",
            "categoria": "desenvolvimento",
            "relevante_para": ["dados", "governança"],
            "criterio": 2
        },
        {
            "id": "GO023",
            "título": "Armazenamento de dados eficiente",
            "descrição": "Uso de formatos e compressão adequados para minimizar o espaço ocupado e o consumo energético.",
            "pilar": "Sustentabilidade de Dados",
            "categoria": "infra",
            "relevante_para": ["banco de dados", "armazenamento"],
            "criterio": 0
        },
        {
            "id": "GO024",
            "título": "Desduplicação de dados",
            "descrição": "Processos para identificar e eliminar duplicatas em bases de dados.",
            "pilar": "Sustentabilidade de Dados",
            "categoria": "infra",
            "relevante_para": ["dados", "armazenamento"],
            "criterio": 1
        },
        {
            "id": "GO025",
            "título": "Uso de cache para reduzir consultas",
            "descrição": "Implementação de cache efetivo para evitar acesso repetido desnecessário a dados armazenados.",
            "pilar": "Sustentabilidade de Dados",
            "categoria": "desenvolvimento",
            "relevante_para": ["desempenho", "cache"],
            "criterio": 1
        }
    ],
    "GreenSoftware": [
        {
            "id": "GS001",
            "título": "Medição de consumo energético no desenvolvimento",
            "descrição": "Ferramentas que medem o uso de CPU/memória durante a execução de funcionalidades de software.",
            "pilar": "Observabilidade",
            "categoria": "desenvolvimento",
            "relevante_para": ["linguagem", "ferramentas"],
            "criterio": 1
        },
        {
            "id": "GS002",
            "título": "Monitoramento de emissões de código",
            "descrição": "Avaliação das emissões de carbono associadas à execução de componentes de software.",
            "pilar": "Observabilidade",
            "categoria": "devops",
            "relevante_para": ["sustentabilidade", "CI/CD"],
            "criterio": 2
        },
        {
            "id": "GS003",
            "título": "Perfis de desempenho focados em energia",
            "descrição": "Execução de testes de carga para medir consumo de energia sob diferentes cenários de uso.",
            "pilar": "Observabilidade",
            "categoria": "devops",
            "relevante_para": ["testes", "CI/CD"],
            "criterio": 0
        },
        {
            "id": "GS004",
            "título": "Logs de consumo por serviço",
            "descrição": "Captura de métricas de uso de CPU/memória para cada serviço ou microserviço.",
            "pilar": "Observabilidade",
            "categoria": "desenvolvimento",
            "relevante_para": ["microserviços", "monitoramento"],
            "criterio": 1
        },
        {
            "id": "GS005",
            "título": "Código otimizado em algoritmos",
            "descrição": "Uso de algoritmos com menor complexidade para reduzir processamento e consumo energético.",
            "pilar": "Otimização de Recursos",
            "categoria": "desenvolvimento",
            "relevante_para": ["linguagem", "performance"],
            "criterio": 2
        },
        {
            "id": "GS006",
            "título": "Uso eficiente de memória",
            "descrição": "Gerenciamento e liberação de memória para evitar desperdício durante a execução do software.",
            "pilar": "Otimização de Recursos",
            "categoria": "desenvolvimento",
            "relevante_para": ["linguagem", "performance"],
            "criterio": 1
        },
        {
            "id": "GS007",
            "título": "Minificação e otimização de assets",
            "descrição": "Minificar e compactar arquivos CSS/JS/imagens em aplicações web para reduzir consumo em clients e servidores.",
            "pilar": "Otimização de Recursos",
            "categoria": "desenvolvimento",
            "relevante_para": ["web", "desempenho"],
            "criterio": 1
        },
        {
            "id": "GS008",
            "título": "Eliminação de dependências desnecessárias",
            "descrição": "Remover bibliotecas ou módulos não utilizados que aumentam o consumo de processamento.",
            "pilar": "Otimização de Recursos",
            "categoria": "desenvolvimento",
            "relevante_para": ["linguagem", "bibliotecas"],
            "criterio": 0
        },
        {
            "id": "GS009",
            "título": "Linters e análises estáticas para eficiência",
            "descrição": "Ferramentas automatizadas que verificam padrões de código otimizados e alertam para práticas de alto consumo.",
            "pilar": "Automação",
            "categoria": "desenvolvimento",
            "relevante_para": ["ferramentas", "linguagem"],
            "criterio": 0
        },
        {
            "id": "GS010",
            "título": "Testes de regressão de consumo",
            "descrição": "Execução automática de testes que garantem que mudanças não aumentam o consumo de energia.",
            "pilar": "Automação",
            "categoria": "devops",
            "relevante_para": ["CI/CD", "testes"],
            "criterio": 1
        },
        {
            "id": "GS011",
            "título": "Scripts de desligamento em ambientes CI/CD",
            "descrição": "Encerrar recursos temporários (como bancos de dados locais) após execução de pipelines de CI.",
            "pilar": "Automação",
            "categoria": "devops",
            "relevante_para": ["CI/CD", "infraestrutura"],
            "criterio": 2
        },
        {
            "id": "GS012",
            "título": "Automação de otimização de código",
            "descrição": "Ferramentas que aplicam refatorações automáticas para melhorar eficiência energética do código.",
            "pilar": "Automação",
            "categoria": "desenvolvimento",
            "relevante_para": ["ferramentas", "linguagem"],
            "criterio": 1
        },
        {
            "id": "GS013",
            "título": "Diretrizes de codificação sustentável",
            "descrição": "Padrões arquiteturais e de código que incentivam práticas de desenvolvimento de software de baixo impacto ambiental.",
            "pilar": "Governança e FinOps",
            "categoria": "arquitetura",
            "relevante_para": ["governança", "padrões"],
            "criterio": 1
        },
        {
            "id": "GS014",
            "título": "Revisões de código com foco em sustentabilidade",
            "descrição": "Incluir verificação do impacto energético nas revisões de pull requests.",
            "pilar": "Governança e FinOps",
            "categoria": "desenvolvimento",
            "relevante_para": ["CI/CD", "processos"],
            "criterio": 0
        },
        {
            "id": "GS015",
            "título": "Acordos de nível de serviço verdes",
            "descrição": "SLA de sistemas que incluem métricas de eficiência energética ou uso de energia renovável.",
            "pilar": "Governança e FinOps",
            "categoria": "devops",
            "relevante_para": ["governança", "SLA"],
            "criterio": 1
        },
        {
            "id": "GS016",
            "título": "Metas de melhoria contínua",
            "descrição": "Definir metas (OKRs/KPIs) para redução progressiva do consumo energético por versão do software.",
            "pilar": "Governança e FinOps",
            "categoria": "desenvolvimento",
            "relevante_para": ["processo", "OKR"],
            "criterio": 2
        },
        {
            "id": "GS017",
            "título": "Escolha de frameworks leves",
            "descrição": "Preferir frameworks e bibliotecas que sejam eficientes em termos de uso de recursos computacionais.",
            "pilar": "Eficiência Energética",
            "categoria": "desenvolvimento",
            "relevante_para": ["linguagem", "framework"],
            "criterio": 2
        },
        {
            "id": "GS018",
            "título": "Modos de economia em aplicações",
            "descrição": "Implementar modos (ex: power saving) que reduzem a atividade computacional quando possível.",
            "pilar": "Eficiência Energética",
            "categoria": "desenvolvimento",
            "relevante_para": ["mobile", "aplicação"],
            "criterio": 1
        },
        {
            "id": "GS019",
            "título": "Teste de eficiência energética em clientes",
            "descrição": "Avaliar e otimizar o consumo de energia em dispositivos finais (móveis, IoT, desktop).",
            "pilar": "Eficiência Energética",
            "categoria": "desenvolvimento",
            "relevante_para": ["mobile", "IoT"],
            "criterio": 0
        },
        {
            "id": "GS020",
            "título": "Gerenciamento de threads/processos",
            "descrição": "Limitar o número de threads/processos simultâneos para reduzir overhead de CPU.",
            "pilar": "Eficiência Energética",
            "categoria": "desenvolvimento",
            "relevante_para": ["linguagem", "sistema operacional"],
            "criterio": 2
        },
        {
            "id": "GS021",
            "título": "Compilação otimizada",
            "descrição": "Configurar compiladores para otimizar código visando baixo consumo de energia.",
            "pilar": "Eficiência Energética",
            "categoria": "desenvolvimento",
            "relevante_para": ["linguagem", "compilador"],
            "criterio": 1
        },
        {
            "id": "GS022",
            "título": "Purga de dados não utilizados",
            "descrição": "Remover bases de testes ou dados obsoletos em ambientes de desenvolvimento e produção.",
            "pilar": "Sustentabilidade de Dados",
            "categoria": "desenvolvimento",
            "relevante_para": ["dados", "teste"],
            "criterio": 0
        },
        {
            "id": "GS023",
            "título": "Compactação de dados",
            "descrição": "Armazenar informações em formatos comprimidos ou índices otimizados para economizar espaço.",
            "pilar": "Sustentabilidade de Dados",
            "categoria": "infra",
            "relevante_para": ["banco de dados", "armazenamento"],
            "criterio": 2
        },
        {
            "id": "GS024",
            "título": "Cache eficiente de resultados",
            "descrição": "Guardar resultados de consultas frequentes para evitar processamento repetido de dados.",
            "pilar": "Sustentabilidade de Dados",
            "categoria": "desenvolvimento",
            "relevante_para": ["desempenho", "cache"],
            "criterio": 1
        },
        {
            "id": "GS025",
            "título": "Minimização de jobs em batch",
            "descrição": "Agendar tarefas em lote para horários de menor custo energético ou agrupar jobs sempre que possível.",
            "pilar": "Sustentabilidade de Dados",
            "categoria": "devops",
            "relevante_para": ["CI/CD", "banco de dados"],
            "criterio": 1
        }
    ]
}
```

---

## ⚙️ Automação com GitHub Actions

Sempre que o arquivo `maturity.json` for alterado no repositório, a pipeline:

1. Faz login seguro no Azure com OIDC (sem client secrets)
2. Cria o container `sustainability-data` no ADLS Gen2 (se não existir)
3. Envia o arquivo para a pasta `raw/`, com a data incluída no nome do blob

### Caminho no ADLS Gen2:

```
sustainability-data/
└── raw/
    └── maturity-2025/05/06.json
```

---

## 🚀 Como usar

1. Edite o arquivo `maturity.json` conforme os critérios sustentáveis aplicáveis ao seu contexto.
2. Faça um `git push` com as alterações.
3. O GitHub Actions cuidará do resto: autenticação, envio e versionamento por data.

---

## 🔐 Pré-requisitos

* Armazenar os seguintes **secrets** no repositório:

  * `AZURE_CLIENT_ID`
  * `AZURE_TENANT_ID`
  * `AZURE_SUBSCRIPTION_ID`

* Definir o nome da conta de armazenamento no `env.STORAGE_ACCOUNT` do workflow (`.github/workflows/send-maturity.yml`).

---

## 📊 Próximos passos sugeridos

* Criar uma visualização em Power BI conectada ao ADLS
* Adicionar testes automatizados para validar o formato do JSON
* Gerar relatórios semanais de evolução da maturidade

---

## 📄 Licença

Este projeto está sob a licença [MIT](LICENSE).

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests com sugestões, correções ou novos critérios sustentáveis.
