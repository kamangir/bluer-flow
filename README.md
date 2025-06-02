# 📜 bluer_flow

📜 `bluer_flow` for workflow management.

```bash
pip install bluer_flow
```

|   |   |   |   |   |
| --- | --- | --- | --- | --- |
| 📜 | [`a-bc-d`](./patterns/a-bc-d.dot) | [`hourglass`](./patterns/hourglass.dot) | [`map-reduce`](./patterns/map-reduce.dot) | [`map-reduce-large`](./patterns/map-reduce-large.dot) |
| [generic](./runners/generic.py) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-a-bc-d/workflow.gif?raw=true&random=pfivnnflfj7xl4hn)](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-a-bc-d/workflow.gif?raw=true&random=pfivnnflfj7xl4hn) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-a-bc-d/workflow.gif?raw=true&random=pfivnnflfj7xl4hn) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-hourglass/workflow.gif?raw=true&random=ald4qsl6x3ocjqdh)](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-hourglass/workflow.gif?raw=true&random=ald4qsl6x3ocjqdh) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-hourglass/workflow.gif?raw=true&random=ald4qsl6x3ocjqdh) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-map-reduce/workflow.gif?raw=true&random=nuymmnvu8esnwibt)](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-map-reduce/workflow.gif?raw=true&random=nuymmnvu8esnwibt) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-map-reduce/workflow.gif?raw=true&random=nuymmnvu8esnwibt) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-map-reduce-large/workflow.gif?raw=true&random=6a6w2l2qinq5jri0)](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-map-reduce-large/workflow.gif?raw=true&random=6a6w2l2qinq5jri0) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-map-reduce-large/workflow.gif?raw=true&random=6a6w2l2qinq5jri0) |
| [local](./runners/local.py) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-local-a-bc-d/workflow.gif?raw=true&random=4zekouc01l40t89y)](https://github.com/kamangir/assets/blob/main/bluer_flow-local-a-bc-d/workflow.gif?raw=true&random=4zekouc01l40t89y) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-local-a-bc-d/workflow.gif?raw=true&random=4zekouc01l40t89y) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-local-hourglass/workflow.gif?raw=true&random=uj104l8hxivdposn)](https://github.com/kamangir/assets/blob/main/bluer_flow-local-hourglass/workflow.gif?raw=true&random=uj104l8hxivdposn) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-local-hourglass/workflow.gif?raw=true&random=uj104l8hxivdposn) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-local-map-reduce/workflow.gif?raw=true&random=dp66hptmj3kgqxiz)](https://github.com/kamangir/assets/blob/main/bluer_flow-local-map-reduce/workflow.gif?raw=true&random=dp66hptmj3kgqxiz) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-local-map-reduce/workflow.gif?raw=true&random=dp66hptmj3kgqxiz) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-local-map-reduce-large/workflow.gif?raw=true&random=dumg5gzm1xi8ni3u)](https://github.com/kamangir/assets/blob/main/bluer_flow-local-map-reduce-large/workflow.gif?raw=true&random=dumg5gzm1xi8ni3u) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-local-map-reduce-large/workflow.gif?raw=true&random=dumg5gzm1xi8ni3u) |
| [localflow](./runners/localflow.py) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-a-bc-d/workflow.gif?raw=true&random=jnsiqv5ru019k0hx)](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-a-bc-d/workflow.gif?raw=true&random=jnsiqv5ru019k0hx) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-a-bc-d/workflow.gif?raw=true&random=jnsiqv5ru019k0hx) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-hourglass/workflow.gif?raw=true&random=9ihobevyeg1i5ays)](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-hourglass/workflow.gif?raw=true&random=9ihobevyeg1i5ays) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-hourglass/workflow.gif?raw=true&random=9ihobevyeg1i5ays) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-map-reduce/workflow.gif?raw=true&random=hsm2rus3lv3mm0zx)](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-map-reduce/workflow.gif?raw=true&random=hsm2rus3lv3mm0zx) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-map-reduce/workflow.gif?raw=true&random=hsm2rus3lv3mm0zx) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-map-reduce-large/workflow.gif?raw=true&random=l3qxqxx5juje7vcs)](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-map-reduce-large/workflow.gif?raw=true&random=l3qxqxx5juje7vcs) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-map-reduce-large/workflow.gif?raw=true&random=l3qxqxx5juje7vcs) |

💡 example use: [literature review using OpenAI API](https://github.com/kamangir/openai-commands/tree/main/openai_commands/literature_review).

# aliases

[localflow](./bluer_flow/docs/aliases/localflow.md), 
[workflow](./bluer_flow/docs/aliases/workflow.md).


---

> 🌀 [`blueflow`](https://github.com/kamangir/notebooks-and-scripts) for the [Global South](https://github.com/kamangir/bluer-south).

---


[![pylint](https://github.com/kamangir/bluer-flow/actions/workflows/pylint.yml/badge.svg)](https://github.com/kamangir/bluer-flow/actions/workflows/pylint.yml) [![pytest](https://github.com/kamangir/bluer-flow/actions/workflows/pytest.yml/badge.svg)](https://github.com/kamangir/bluer-flow/actions/workflows/pytest.yml) [![bashtest](https://github.com/kamangir/bluer-flow/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/bluer-flow/actions/workflows/bashtest.yml) [![PyPI version](https://img.shields.io/pypi/v/bluer-flow.svg)](https://pypi.org/project/bluer-flow/) [![PyPI - Downloads](https://img.shields.io/pypi/dd/bluer-flow)](https://pypistats.org/packages/bluer-flow)

built by 🌀 [`bluer README`](https://github.com/kamangir/bluer-objects/tree/main/bluer_objects/README), based on 📜 [`bluer_flow-5.42.1`](https://github.com/kamangir/bluer-flow).
