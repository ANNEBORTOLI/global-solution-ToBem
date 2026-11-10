<div align="center">

# 💚 TôBem

### Um toque por dia para dizer: tô bem.

_Check-in diário para idosos que moram sozinhos em Copacabana. Se o aviso não chega, o condomínio vai conferir._

![FIAP](https://img.shields.io/badge/FIAP-Global%20Solution%202026.2-ED145B?style=for-the-badge)
![CitizenTech](https://img.shields.io/badge/Desafio-CitizenTech-0B5C7A?style=for-the-badge)
![Rio de Janeiro](https://img.shields.io/badge/Rio%20de%20Janeiro-Copacabana-F2B705?style=for-the-badge)

**Engenharia de Software · 1º ano · Rio de Janeiro**

</div>

---

## 👥 Equipe

| Nome completo   | RM     |
| --------------- | ------ |
| Anne Bortoli    | 574750 |
| Gabriel Almeida | 575525 |

---

## 📋 Ficha da CitizenTech

|     | Campo                      | Resposta                                                                                                                                                                                            |
| :-: | -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 💚  | **Nome da CitizenTech**    | **TôBem**                                                                                                                                                                                           |
| 📍  | **Cidade e bairro**        | Rio de Janeiro (RJ), Copacabana                                                                                                                                                                     |
| 👵  | **Cidadão beneficiado**    | Pessoas idosas (60+) que moram sozinhas em prédios de Copacabana, um dos bairros com maior proporção de idosos da cidade. Indiretamente, também os familiares, o síndico, o porteiro e os vizinhos. |
| ⚠️  | **Problema, em uma frase** | Idosos que moram sozinhos podem sofrer quedas ou mal-estar dentro de casa e ficar horas, ou até um dia inteiro, sem socorro, porque ninguém percebe a tempo que algo está errado.                   |
| 📈  | **Indicador de impacto**   | Tempo entre a falta do check-in e a verificação presencial do idoso: de cerca de **24 h** (caso real) para **até 1 h** (meta do protótipo).                                                         |
| 🌍  | **ODS conectados**         | 3 · Saúde e bem-estar, 10 · Redução das desigualdades e 11 · Cidades e comunidades sustentáveis                                                                                                     |

> 💡 **Por que o TôBem existe:** uma vizinha do nosso prédio caiu dentro de casa. Estava consciente, mas não conseguia se levantar. Só foi encontrada no dia seguinte, quando as amigas estranharam que ela não atendia o telefone. O TôBem nasceu para que ninguém precise esperar 24 horas por ajuda.

---

## 🔄 Como funciona

O TôBem **não tenta detectar a queda**. Ele percebe a **falta do sinal**: um idoso caído, que não consegue chegar ao telefone, também não confirma que está bem, e isso já dispara o aviso.

| Passo |     | O que acontece                                                                                                                                          |
| :---: | :-: | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1** | ⏰  | **Lembrete:** às 8h e às 20h, o aparelho no apartamento acende uma luz e toca um bipe curto.                                                            |
| **2** | 💚  | **Um toque:** o idoso aperta o botão do aparelho ou o botão verde "Tô bem!". Sem digitar nada, sem senha.                                               |
| **3** | 🔔  | **Aviso:** sem check-in 1 h depois do horário, a portaria é avisada de qual apartamento conferir. Sem resposta, o aviso segue para vizinhos e familiar. |
| **4** | 🤝  | **Verificação:** quem atendeu registra o resultado: "está tudo bem" ou "precisou de ajuda".                                                             |
| **+** | 🌡️  | **Calor:** o sensor mede a temperatura e a umidade da casa e avisa o idoso quando o ambiente fica perigoso.                                             |

### 🚦 Os três estados

|     Estado     | Quando                                                                              | O que o aparelho faz                     |
| :------------: | ----------------------------------------------------------------------------------- | ---------------------------------------- |
|   🟢 **OK**    | Check-in em dia e casa agradável                                                    | LED verde                                |
| 🟡 **ATENÇÃO** | 12 h sem check-in, calor a partir de 28 °C, ar seco ou muito úmido                  | LED amarelo e lembrete ao idoso          |
| 🔴 **PERIGO**  | 13 h sem check-in, calor a partir de 32 °C, ar muito seco ou calor com umidade alta | LED vermelho, buzzer e alerta à portaria |

As regras, os limites e as mensagens são **os mesmos** no aparelho, no programa em Python e na página web.

---

## 🧩 O que cada parte faz

|     | Disciplina                                      | O que entregamos                                                                                                      | Pasta                                                                    |
| :-: | ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| 📟  | **Edge Computing**                              | Aparelho com Arduino Uno, sensor DHT22, botão, LEDs, buzzer e LCD, simulado no Wokwi. Funciona sozinho, sem internet. | [`edge-computing/`](edge-computing/)                                     |
| 🐍  | **Computational Thinking with Python**          | O "cérebro": classifica as leituras de um dia com `if/elif/else` e calcula o resumo dos alertas.                      | [`computational-thinking-python/`](computational-thinking-python/)       |
| 📐  | **Differentiated Problem Solving (Matemática)** | Parábola do calor ao longo do dia e cálculo do indicador de impacto.                                                  | [`differentiated-problem-solving/`](differentiated-problem-solving/)     |
| 🎨  | **Front-end Design**                            | Landing page que explica o problema, a jornada, o impacto e os ODS.                                                   | [`front-end-design/`](front-end-design/)                                 |
| ⚙️  | **Web Development**                             | Modo claro/escuro, botão "Tô bem!" funcionando e simulador do aparelho com a regra de decisão em JavaScript.          | [`web-development/`](web-development/)                                   |
| 🧭  | **Software & Total Experience Design**          | Escopo, requisitos, backlog e priorização pensados para idosos.                                                       | [`software-total-experience-design/`](software-total-experience-design/) |
| 🎬  | **Storytelling & Inspiração Empreendedora**     | Videopitch de até 3 minutos e slide deck.                                                                             | [`storytelling/`](storytelling/)                                         |

---

## 🔗 Links

|     | Onde                                                | Link                                                               |
| :-: | --------------------------------------------------- | ------------------------------------------------------------------ |
| 📟  | Simulação do aparelho no Wokwi                      | [Abrir no Wokwi](https://wokwi.com/projects/479775938984317953)    |
| 🎬  | Videopitch no YouTube                               | [Assistir no YouTube](https://www.youtube.com/watch?v=9rOr9LILAIQ) |
| 🐍  | Repositório original do Python                      | _(adicionar link)_                                                 |
| 🌐  | Repositório original do Front-end e Web Development | _(adicionar link)_                                                 |
| 🎬  | Apresentação de Edge no YouTube                     | [Assistir no YouTube](https://youtu.be/VURCeW4LhFE)                |

---

## 📈 Indicador de impacto

<div align="center">

|      Hoje       | ➡️  | Meta do protótipo |
| :-------------: | :-: | :---------------: |
| 🔴 **24 horas** |     | 🟢 **até 1 hora** |

**Redução de 95,8% no tempo até alguém conferir se o idoso está bem.**

</div>

**Indicadores complementares:**

- 📅 Percentual de check-ins feitos no horário, por semana.
- 🚪 Percentual de alertas atendidos dentro do prazo.

---

## 🌍 ODS conectados

| ODS                                                                                                        | Como o TôBem contribui                                                                                                           |
| ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| ![ODS 3](https://img.shields.io/badge/ODS_3-Saúde_e_bem--estar-4C9F38?style=flat-square)                   | Reduz o tempo até o socorro depois de quedas e mal-estar, e diminui o isolamento do idoso.                                       |
| ![ODS 10](https://img.shields.io/badge/ODS_10-Redução_das_desigualdades-DD1367?style=flat-square)          | Meta 10.2: promove a inclusão de todos, independentemente da idade. O idoso continua morando sozinho, com autonomia e segurança. |
| ![ODS 11](https://img.shields.io/badge/ODS_11-Cidades_e_comunidades_sustentáveis-FD9D24?style=flat-square) | Torna o lugar onde se mora mais seguro e inclusivo, usando a estrutura que o prédio já tem: portaria, síndico e vizinhos.        |

---

## 🗂️ Estrutura do repositório

```
global-solution/
├── README.md                              ← você está aqui
├── computational-thinking-python/
├── differentiated-problem-solving/
├── edge-computing/
├── front-end-design/
├── software-total-experience-design/
├── storytelling/
└── web-development/
```

---

## ⚠️ Observações

- 📊 **Dados simulados:** nenhuma informação real de moradores foi usada.
- 🚑 **Não substitui emergência:** o TôBem não substitui o SAMU (192) nem atendimento médico.
- 🤖 **Uso de IA:** cada pasta tem o registro de como usamos inteligência artificial (`prompts.md` ou `AI.md`).

<div align="center">

---

Feito com 💚 em Copacabana · **FIAP Global Solution 2026.2**

</div>
