# 📜 bluer_flow

📜 `bluer_flow` for workflow management.

```bash
pip install bluer_flow
```

|   |   |   |   |   |
| --- | --- | --- | --- | --- |
| 📜 | [`a-bc-d`](./patterns/a-bc-d.dot) | [`hourglass`](./patterns/hourglass.dot) | [`map-reduce`](./patterns/map-reduce.dot) | [`map-reduce-large`](./patterns/map-reduce-large.dot) |
| [generic](./runners/generic.py) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-a-bc-d/workflow.gif?raw=true&random=hcqxc5a2akgbcbyt)](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-a-bc-d/workflow.gif?raw=true&random=hcqxc5a2akgbcbyt) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-a-bc-d/workflow.gif?raw=true&random=hcqxc5a2akgbcbyt) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-hourglass/workflow.gif?raw=true&random=2q19y8qlrmo0n1ku)](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-hourglass/workflow.gif?raw=true&random=2q19y8qlrmo0n1ku) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-hourglass/workflow.gif?raw=true&random=2q19y8qlrmo0n1ku) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-map-reduce/workflow.gif?raw=true&random=pbw339m6dzvu559z)](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-map-reduce/workflow.gif?raw=true&random=pbw339m6dzvu559z) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-map-reduce/workflow.gif?raw=true&random=pbw339m6dzvu559z) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-map-reduce-large/workflow.gif?raw=true&random=aswfvwxw77rwy08q)](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-map-reduce-large/workflow.gif?raw=true&random=aswfvwxw77rwy08q) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-map-reduce-large/workflow.gif?raw=true&random=aswfvwxw77rwy08q) |
| [local](./runners/local.py) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-local-a-bc-d/workflow.gif?raw=true&random=qdqgi8zdqq8gi1rj)](https://github.com/kamangir/assets/blob/main/bluer_flow-local-a-bc-d/workflow.gif?raw=true&random=qdqgi8zdqq8gi1rj) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-local-a-bc-d/workflow.gif?raw=true&random=qdqgi8zdqq8gi1rj) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-local-hourglass/workflow.gif?raw=true&random=sauw5zbz5u5gyym2)](https://github.com/kamangir/assets/blob/main/bluer_flow-local-hourglass/workflow.gif?raw=true&random=sauw5zbz5u5gyym2) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-local-hourglass/workflow.gif?raw=true&random=sauw5zbz5u5gyym2) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-local-map-reduce/workflow.gif?raw=true&random=imnyqutazvs61wbp)](https://github.com/kamangir/assets/blob/main/bluer_flow-local-map-reduce/workflow.gif?raw=true&random=imnyqutazvs61wbp) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-local-map-reduce/workflow.gif?raw=true&random=imnyqutazvs61wbp) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-local-map-reduce-large/workflow.gif?raw=true&random=plg8thsf2gfi3kns)](https://github.com/kamangir/assets/blob/main/bluer_flow-local-map-reduce-large/workflow.gif?raw=true&random=plg8thsf2gfi3kns) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-local-map-reduce-large/workflow.gif?raw=true&random=plg8thsf2gfi3kns) |
| [localflow](./runners/localflow.py) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-a-bc-d/workflow.gif?raw=true&random=46oz1inmyiat5pyi)](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-a-bc-d/workflow.gif?raw=true&random=46oz1inmyiat5pyi) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-a-bc-d/workflow.gif?raw=true&random=46oz1inmyiat5pyi) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-hourglass/workflow.gif?raw=true&random=pof62s0tmnk90vum)](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-hourglass/workflow.gif?raw=true&random=pof62s0tmnk90vum) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-hourglass/workflow.gif?raw=true&random=pof62s0tmnk90vum) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-map-reduce/workflow.gif?raw=true&random=yuiqmp1fvrzrgawv)](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-map-reduce/workflow.gif?raw=true&random=yuiqmp1fvrzrgawv) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-map-reduce/workflow.gif?raw=true&random=yuiqmp1fvrzrgawv) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-map-reduce-large/workflow.gif?raw=true&random=o66wse0hftq87id2)](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-map-reduce-large/workflow.gif?raw=true&random=o66wse0hftq87id2) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-map-reduce-large/workflow.gif?raw=true&random=o66wse0hftq87id2) |

💡 example use: [literature review using OpenAI API](https://github.com/kamangir/openai-commands/tree/main/openai_commands/literature_review).

# aliases

[localflow](./bluer_flow/docs/aliases/localflow.md), 
[workflow](./bluer_flow/docs/aliases/workflow.md).


---

> 🌀 [`blueflow`](https://github.com/kamangir/notebooks-and-scripts) for the [Global South](https://github.com/kamangir/bluer-south).

---


[![pylint](https://github.com/kamangir/bluer-flow/actions/workflows/pylint.yml/badge.svg)](https://github.com/kamangir/bluer-flow/actions/workflows/pylint.yml) [![pytest](https://github.com/kamangir/bluer-flow/actions/workflows/pytest.yml/badge.svg)](https://github.com/kamangir/bluer-flow/actions/workflows/pytest.yml) [![bashtest](https://github.com/kamangir/bluer-flow/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/bluer-flow/actions/workflows/bashtest.yml) [![PyPI version](https://img.shields.io/pypi/v/bluer-flow.svg)](https://pypi.org/project/bluer-flow/) [![PyPI - Downloads](https://img.shields.io/pypi/dd/bluer-flow)](https://pypistats.org/packages/bluer-flow)

built by 🌀 [`bluer README`](https://github.com/kamangir/bluer-objects/tree/main/bluer_objects/README), based on 📜 [`bluer_flow-5.38.1`](https://github.com/kamangir/bluer-flow).
