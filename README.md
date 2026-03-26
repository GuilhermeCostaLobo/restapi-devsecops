Alunos: Nicolas Tosin, Guilherme Lobo, Lucas Aiolf

## 1. Tampering (Adulteração de dados)

A ameaça de Tampering acontece quando um usuário ou atacante altera dados da aplicação de forma indevida.

No código atual, existem as mitigações:
- as alterações de tarefas só podem ser feitas pelos endpoints específicos da API ('POST', 'PUT' e 'DELETE');
- o parâmetro 'id' das rotas é definido como 'int', o que impede valores de tipo incorreto na URL.

## 2. Information Disclosure (Divulgação de informação)

A ameaça de Information Disclosure acontece quando a aplicação expõe informações internas desnecessárias para o usuário.

No código atual, existem as mitigações:
- a aplicação não expõe credenciais, tokens, caminhos internos do sistema ou configurações sensíveis;
- os dados ficam apenas em memória, em uma lista simples, sem integração com banco de dados ou arquivos internos do servidor;
- a resposta do endpoint de exclusão retorna apenas uma mensagem simples: "Tarefa removida".

Futuramente, podem ser implementadas mitigações para que usuário não visualizem todas as tarefas cadastradas ao acessar GET /tarefas. Além da adição de um sistema de autenticação e controle de acesso para restringir quem pode realizar as atividades com os dados.
