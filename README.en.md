# UN AI Agent Teams

An open starter kit for **product development** and **YouTube production** agent teams.

[Русская инструкция](README.md)

## Scope

Version 0.1 provides role prompts, task templates, example configuration, a 14–21 day YouTube pilot, and a dependency-free local task generator. It does not include an autonomous AI runner, hosted service, account integrations, or video uploading. The JSON configuration documents intended limits; enforcement requires a runtime.

## Get started

1. Choose a team in `teams/` and copy `config.example.json` to `config.local.json`.
2. Create a task with Python 3.9 or later:

```bash
python3 tools/new_task.py --team development --project my-product --goal 'Add an expense form' --output tasks/expense-form.json
```

3. Give your AI assistant `prompts/coordinator.md`, the task card, and relevant input files.
4. Delegate only independent work when your environment supports subagents. Otherwise execute roles sequentially.
5. Validate the user journey or video deliverable and record actual resource usage where available.

## Teams

- Development: coordinator, frontend, backend, QA, deployment when needed.
- YouTube: producer, scriptwriter, visual director, editor/audio, publisher, analyst.

Start with at most three concurrent workers across both teams as a suggested operating limit. Small tasks need only one worker. Keep separate queues and budgets for each product and channel.

The YouTube pilot proposes ten original Shorts over fourteen days and observation through day twenty-one. Day one is the first actual publication. Compare matching observation windows and record unavailable data as unknown. This is an early format test, not an earnings promise.

Example projects are fictional. Local task cards are ignored by git. Prompts are in Russian and can be translated or adapted.

See [contribution guidelines](CONTRIBUTING.md), [MIT License](LICENSE), and the Russian README for the full workflow. Third-party media rights are not granted by this license.
