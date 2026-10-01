# Engenharia da Qualidade e Confiabilidade de Software (ESW451)

![UniRV](https://img.shields.io/badge/Institui%C3%A7%C3%A3o-UniRV%20--%20Universidade%20de%20Rio%20Verde-blue)
![Disciplina](https://img.shields.io/badge/Disciplina-ESW451%20--%20Engenharia%20da%20Qualidade%20e%20Confiabilidade-green)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange)

Este repositório reúne o material didático, programas de aula, cronogramas, listas de exercícios em LaTeX, cadernos de análise de dados em Python e capítulos do livro da disciplina **Engenharia da Qualidade e Confiabilidade (ESW451)** ministrada pelo **Prof. Me. Sérgio Guimarães de Oliveira** na **Universidade de Rio Verde (UniRV)**.

---

## 📋 Visão Geral da Disciplina

A disciplina abrange desde os fundamentos clássicos da Qualidade e Confiabilidade de Software (baseados na literatura de Ian Sommerville) até as práticas mais modernas da indústria de tecnologia, como a **Engenharia de Confiabilidade de Sites (Google SRE)**, resiliência em **Microsserviços**, **Engenharia de Segurança da Informação**, **GitFlow** e **Análise de Dados aplicadas à Qualidade**.

---

## 🗂️ Estrutura do Repositório

```text
.
├── ESW451_programa.doc            # Ementa e programa detalhado da disciplina
├── ESW451_cronograma.doc          # Cronograma acadêmico de aulas e avaliações
├── .gitignore                     # Configuração de arquivos ignorados pelo Git
├── README.md                      # Documentação geral do repositório
├── notas/                         # [IGNORADO] Planilhas com notas de alunos (n1.xlsx, n2.xlsx, n3.xlsx)
└── aulas/                         # Conteúdo programático das aulas e materiais práticos
    ├── 1.Introducao/                                       # Conceitos fundamentais de qualidade e atributos de software
    ├── 2.Engenharia da Confiabilidade Sommerville/         # Métricas de confiabilidade (MTBF, MTTF, MTTR) e disponibilidade
    ├── 3.Arquiteturas tolerantes a defeitos.../            # Automonitoramento, Programação N-versões e 8 Diretrizes de Sommerville
    ├── 4. Métricas Google SRE/                             # Indicadores Google SRE (SLO, SLA, SLI, Error Budgets)
    ├── 4.1 Google SRE/                                     # Práticas e métricas complementares de SRE
    ├── 5- Monitoração agregada Princípios do Google SRE/   # Telemetria, observabilidade e monitoramento agregado
    ├── 6.AtividadeAnaliseDados/                            # Práticas de Análise de Dados com Python e Jupyter Notebook
    ├── 7. Métodologias ágeis (Cópia)/                      # Qualidade em métodos ágeis, User Stories e Planning Poker
    ├── 8.Resposta a Emergências/                           # Gestão de incidentes, planos de contingência e post-mortems
    ├── 9.Engenharia de Segurança/                          # Princípios de segurança e mitigação de vulnerabilidades
    ├── 10.parte 1 - Engenharia de Segurança da informação/ # Segurança da Informação (Parte 1)
    ├── 11.parte 2 - Engenharia de Segurança da informação/ # Segurança da Informação (Parte 2)
    ├── 12. Introdução a microsserviços/                    # Qualidade e resiliência em arquiteturas distribuídas
    ├── 13. Introdução ao GitFlow /                         # Fluxo de trabalho de versionamento profissional com GitFlow
    ├── 14. Avaliando a qualidade sobre o ponto de vista do usuário/ # UX, usabilidade e percepção do usuário
    ├── livro/                                              # Compilação em LaTeX dos capítulos do livro da disciplina
    └── provas/                                             # Avaliações e materiais de exame
```

---

## 📚 Módulos do Curso

1. **Introdução à Qualidade de Software**  
   Conceitos de qualidade, modelos de processo, requisitos não funcionais e importância da confiabilidade no ciclo de vida do software.

2. **Engenharia da Confiabilidade (Sommerville)**  
   Métricas estatísticas de confiabilidade (MTBF - *Mean Time Between Failures*, MTTF - *Mean Time To Failure*, MTTR - *Mean Time To Repair*), cálculo de disponibilidade e fault-tolerance.

3. **Arquiteturas Tolerantes a Defeitos**  
   Técnicas de tolerância a falhas, automonitoramento, sistemas de proteção, programação N-versões e aplicação das 8 diretrizes de confiabilidade de Ian Sommerville.

4. **Google SRE (*Site Reliability Engineering*)**  
   Conceitos e aplicação prática dos pilares de SRE: *Service Level Indicators* (SLI), *Service Level Objectives* (SLO), *Service Level Agreements* (SLA) e gestão de *Error Budgets*.

5. **Observabilidade e Monitoramento Agregado**  
   Estratégias de telemetria, agregação de logs, métricas em tempo real e monitoramento contínuo em sistemas em produção.

6. **Análise de Dados aplicada à Qualidade**  
   Exercícios práticos utilizando **Python** e **Jupyter Notebooks** para análise de dados operacionais, estatística de falhas e tomada de decisão baseada em métricas.

7. **Qualidade em Metodologias Ágeis**  
   Critérios de aceitação, escrita de *User Stories*, estimativa com *Planning Poker* e integração de testes contínuos no fluxo ágil.

8. **Resposta a Emergências e Incidentes**  
   Planos de ação para indisponibilidade, gerenciamento de crises, análise de causa raiz (*Root Cause Analysis*) e elaboração de *Post-Mortems* sem culpa (*Blameless Post-Mortems*).

9. **Engenharia de Segurança da Informação**  
   Fundamentos de segurança de sistemas, criptografia, autenticação, controle de acesso e modelagem de ameaças.

10. **Arquiteturas de Microsserviços**  
    Padrões de resiliência (*Circuit Breaker*, *Retry*, *Bulkhead*) e desafios de garantia da qualidade em ambientes distribuídos.

11. **Estratégia de Versionamento com GitFlow**  
    Gerenciamento profissional de repositórios usando branches (`main`, `develop`, `feature`, `release`, `hotfix`).

12. **Qualidade sob a Perspectiva do Usuário**  
    Engajamento do usuário, usabilidade, acessibilidade, testes de experiência de usuário (UX) e satisfação do cliente.

---

## 🛠️ Tecnologias e Ferramentas

- **LaTeX**: Edição de documentos acadêmicos, apresentações Beamer e compilação do livro da disciplina.
- **Python / Jupyter Notebooks**: Manipulação e análise de conjuntos de dados de qualidade.
- **Git & GitFlow**: Controle de versão e gestão de branches.
- **Microsoft Office / Excel**: Planilhas e documentos suplementares de acompanhamento.

---

## 🔒 Segurança e Dados Sensíveis

A pasta `notas/` contém planilhas de acompanhamento acadêmico e avaliações de alunos. Para assegurar a privacidade dos estudantes e o cumprimento da Lei Geral de Proteção de Dados (LGPD), essa pasta está incluída no arquivo `.gitignore` e **nunca deve ser enviada ao controle de versão (Git)**.

---

## ✍️ Autor e Licença

- **Docente:** Prof. Me. Sergio Souza Novak
- **Instituição:** Universidade de Rio Verde (UniRV)
- **Ano Letivo:** 2026-01
