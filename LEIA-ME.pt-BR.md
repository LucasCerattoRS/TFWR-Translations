# TFWR-Translations (fork do Lukas)

Fork de [Timiodon/TFWR-Translations](https://github.com/Timiodon/TFWR-Translations), o
repositório oficial com **todos os textos do jogo The Farmer Was Replaced** (interface, dicas e
a documentação in-game) em 15 idiomas. A comunidade corrige traduções por pull request.

Este arquivo é a única diferença do fork em relação ao original — o `README.md` (inglês) é do
upstream e fica intocado para não gerar conflito na sincronização.

## Para que serve este fork

Mandar correções da tradução pt-BR para o upstream. O histórico até aqui:

- **PR #32** (jul/2026, mergeado): nome do desbloqueio `"Variables"` deixado em inglês em
  `PT/docs/scripting/operators.md` e crase fora do lugar em `tuples.md`. A auditoria completa
  que originou o PR está em `the-farmer-was-replaced-lab/tools/translation-audit.md`.
- **Regressão (out/2026):** uma atualização de textos do próprio jogo (`a068079`, "Update
  Translations") sobrescreveu a correção — a linha voltou a dizer `"Variáveis"`. O conserto
  está pronto na branch `fix/pt-variables-unlock-regressao`, **ainda sem PR aberto** no upstream.
  O README do upstream avisa que isso acontece: texto do jogo atualizado apaga tradução da
  comunidade.

## Estado

- `main` sincronizado com `upstream/main` em 08/10/2026.
- Checagem mecânica PT × EN (08/10): nenhuma chave `@...` faltando, nenhum placeholder `{0}` /
  `{{ ... }}` quebrado, nenhuma crase desbalanceada em `PT/Strings/`.
  (`languages.txt` só existe em EN, de propósito.)

## Como usar

Não há código para rodar. Para ver uma correção dentro do jogo, substitua a pasta `Languages`
da instalação do jogo por este repositório (instrução do upstream).

Sincronizar com o original:

```bash
git remote add upstream https://github.com/Timiodon/TFWR-Translations.git   # uma vez
git fetch upstream && git checkout main && git merge --ff-only upstream/main && git push
```

Para propor correção: branch nova a partir de `upstream/main`, editar só o arquivo do idioma,
PR no repositório do Timiodon com o nome para crédito.

## Estrutura

| Caminho | O que é |
|---|---|
| `XX/Strings/*.txt` | Textos curtos da interface; cada entrada começa com `@chave = ...` |
| `XX/docs/**.md` | Páginas da janela de informação do jogo (Markdown com extensões próprias) |
| `XX/docs/unlocks/` | Páginas de desbloqueios — o upstream avisa que vão mudar, não vale traduzir |
| `builtins.py` | Stub de tipos da API do jogo para autocomplete em editores Python |

`XX` = código do idioma (`EN`, `PT`, `ES`, ...). O português é `PT`.

## Regras de tradução que pegam mais gente

- Código não se traduz — nem `while`, `dictionary` etc. fora do bloco de código.
- Nomes de itens, entidades, solos, desbloqueios e leaderboards ficam em inglês quando se referem
  ao objeto do jogo (`Items.Carrot`, desbloqueio `"Variables"`).
- Placeholders `{0}` e `{{ algo }}` nunca mudam: quebram o jogo.

## Tecnologias

Só texto: Markdown com extensões do jogo (`{{codeexample ...}}`, `<right>`) e arquivos `.txt`
chave-valor. `builtins.py` é Python 3.12+ (usa `type X = ...`).

## Pendências

- Abrir o PR da branch `fix/pt-variables-unlock-regressao` no upstream (decisão do Lukas).

## Para estudar

1. **Stub de tipos para uma linguagem que não é Python** — `builtins.py:22-49`: importa tipos do
   próprio `builtins` com apelidos (`str as string`, `range as range_class`) para poder
   redefinir nomes sem perder o original.
2. **`@overload`** — `builtins.py:606` em diante: três assinaturas de `range` para o editor
   saber os tipos de cada forma de chamada, sem implementação real (`...`).
3. **Enums como namespace de constantes** — `builtins.py:956` (`class Entities(_Enum)`): é assim
   que `Entities.Carrot` aparece no autocomplete.
4. **Exemplo executável embutido em Markdown** — `PT/docs/scripting/tuples.md:10`: o bloco
   `{{codeexample {json} #SETUP #CODE ...}}` é configuração + código que o jogo roda dentro da
   página de ajuda.
