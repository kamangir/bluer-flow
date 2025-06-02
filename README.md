# 📜 bluer_flow

📜 `bluer_flow` for workflow management.

```bash
pip install bluer_flow
```

|   |   |   |   |   |
| --- | --- | --- | --- | --- |
| 📜 | [`a-bc-d`](./patterns/a-bc-d.dot) | [`hourglass`](./patterns/hourglass.dot) | [`map-reduce`](./patterns/map-reduce.dot) | [`map-reduce-large`](./patterns/map-reduce-large.dot) |
| [generic](./bluer_flow/workflow/runners/generic.py) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-a-bc-d/workflow.gif?raw=true&random=v5cg7ww1zz6jwhiz)](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-a-bc-d/workflow.gif?raw=true&random=v5cg7ww1zz6jwhiz) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-a-bc-d/workflow.gif?raw=true&random=v5cg7ww1zz6jwhiz) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-hourglass/workflow.gif?raw=true&random=lkvogpnbs220fifd)](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-hourglass/workflow.gif?raw=true&random=lkvogpnbs220fifd) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-hourglass/workflow.gif?raw=true&random=lkvogpnbs220fifd) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-map-reduce/workflow.gif?raw=true&random=kdcy6nah8d5hb3ty)](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-map-reduce/workflow.gif?raw=true&random=kdcy6nah8d5hb3ty) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-map-reduce/workflow.gif?raw=true&random=kdcy6nah8d5hb3ty) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-map-reduce-large/workflow.gif?raw=true&random=rw7xfkg5kwzcc3x8)](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-map-reduce-large/workflow.gif?raw=true&random=rw7xfkg5kwzcc3x8) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-map-reduce-large/workflow.gif?raw=true&random=rw7xfkg5kwzcc3x8) |
| [local](./bluer_flow/workflow/runners/local.py) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-local-a-bc-d/workflow.gif?raw=true&random=lmdjvyzc2itub25l)](https://github.com/kamangir/assets/blob/main/bluer_flow-local-a-bc-d/workflow.gif?raw=true&random=lmdjvyzc2itub25l) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-local-a-bc-d/workflow.gif?raw=true&random=lmdjvyzc2itub25l) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-local-hourglass/workflow.gif?raw=true&random=i6zu2vhpmbwvlpi2)](https://github.com/kamangir/assets/blob/main/bluer_flow-local-hourglass/workflow.gif?raw=true&random=i6zu2vhpmbwvlpi2) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-local-hourglass/workflow.gif?raw=true&random=i6zu2vhpmbwvlpi2) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-local-map-reduce/workflow.gif?raw=true&random=zhfjvbo74r6m71d2)](https://github.com/kamangir/assets/blob/main/bluer_flow-local-map-reduce/workflow.gif?raw=true&random=zhfjvbo74r6m71d2) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-local-map-reduce/workflow.gif?raw=true&random=zhfjvbo74r6m71d2) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-local-map-reduce-large/workflow.gif?raw=true&random=nqjr9ktjaxpkqnee)](https://github.com/kamangir/assets/blob/main/bluer_flow-local-map-reduce-large/workflow.gif?raw=true&random=nqjr9ktjaxpkqnee) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-local-map-reduce-large/workflow.gif?raw=true&random=nqjr9ktjaxpkqnee) |
| [localflow](./bluer_flow/workflow/runners/localflow/runner.py) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-a-bc-d/workflow.gif?raw=true&random=uo02wl4p9832uxk8)](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-a-bc-d/workflow.gif?raw=true&random=uo02wl4p9832uxk8) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-a-bc-d/workflow.gif?raw=true&random=uo02wl4p9832uxk8) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-hourglass/workflow.gif?raw=true&random=20k5buokgbtn6ns6)](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-hourglass/workflow.gif?raw=true&random=20k5buokgbtn6ns6) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-hourglass/workflow.gif?raw=true&random=20k5buokgbtn6ns6) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-map-reduce/workflow.gif?raw=true&random=zwm6dljd9os0qeyr)](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-map-reduce/workflow.gif?raw=true&random=zwm6dljd9os0qeyr) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-map-reduce/workflow.gif?raw=true&random=zwm6dljd9os0qeyr) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-map-reduce-large/workflow.gif?raw=true&random=e0pnd9v7gsg28iwr)](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-map-reduce-large/workflow.gif?raw=true&random=e0pnd9v7gsg28iwr) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-map-reduce-large/workflow.gif?raw=true&random=e0pnd9v7gsg28iwr) |

💡 example use: [literature review using OpenAI API](https://github.com/kamangir/openai-commands/tree/main/openai_commands/literature_review).

# aliases

[localflow](./bluer_flow/docs/aliases/localflow.md), 
[workflow](./bluer_flow/docs/aliases/workflow.md).


---

> 🌀 [`blueflow`](https://github.com/kamangir/notebooks-and-scripts) for the [Global South](https://github.com/kamangir/bluer-south).

---


[![pylint](https://github.com/kamangir/bluer-flow/actions/workflows/pylint.yml/badge.svg)](https://github.com/kamangir/bluer-flow/actions/workflows/pylint.yml) [![pytest](https://github.com/kamangir/bluer-flow/actions/workflows/pytest.yml/badge.svg)](https://github.com/kamangir/bluer-flow/actions/workflows/pytest.yml) [![bashtest](https://github.com/kamangir/bluer-flow/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/bluer-flow/actions/workflows/bashtest.yml) [![PyPI version](https://img.shields.io/pypi/v/bluer-flow.svg)](https://pypi.org/project/bluer-flow/) [![PyPI - Downloads](https://img.shields.io/pypi/dd/bluer-flow)](https://pypistats.org/packages/bluer-flow)

built by 🌀 [`bluer README`](https://github.com/kamangir/bluer-objects/tree/main/bluer_objects/README), based on 📜 [`bluer_flow-5.51.1`](https://github.com/kamangir/bluer-flow).
