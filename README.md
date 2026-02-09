# 📜 bluer_flow

📜 `bluer_flow` for workflow management.

```bash
pip install bluer_flow
```

|   |   |   |   |   |
| --- | --- | --- | --- | --- |
| 📜 | [`a-bc-d`](./patterns/a-bc-d.dot) | [`hourglass`](./patterns/hourglass.dot) | [`map-reduce`](./patterns/map-reduce.dot) | [`map-reduce-large`](./patterns/map-reduce-large.dot) |
| [generic](./bluer_flow/workflow/runners/generic.py) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-a-bc-d/workflow.gif?raw=true&random=zwp5moyeg84x1222)](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-a-bc-d/workflow.gif?raw=true&random=zwp5moyeg84x1222) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-a-bc-d/workflow.gif?raw=true&random=zwp5moyeg84x1222) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-hourglass/workflow.gif?raw=true&random=6a81gqmljytuguxv)](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-hourglass/workflow.gif?raw=true&random=6a81gqmljytuguxv) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-hourglass/workflow.gif?raw=true&random=6a81gqmljytuguxv) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-map-reduce/workflow.gif?raw=true&random=h0adfuyu1cuxmlur)](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-map-reduce/workflow.gif?raw=true&random=h0adfuyu1cuxmlur) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-map-reduce/workflow.gif?raw=true&random=h0adfuyu1cuxmlur) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-map-reduce-large/workflow.gif?raw=true&random=n7i0vsxhcmcsbsrv)](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-map-reduce-large/workflow.gif?raw=true&random=n7i0vsxhcmcsbsrv) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-generic-map-reduce-large/workflow.gif?raw=true&random=n7i0vsxhcmcsbsrv) |
| [local](./bluer_flow/workflow/runners/local.py) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-local-a-bc-d/workflow.gif?raw=true&random=f2etyr2ry54bcyb9)](https://github.com/kamangir/assets/blob/main/bluer_flow-local-a-bc-d/workflow.gif?raw=true&random=f2etyr2ry54bcyb9) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-local-a-bc-d/workflow.gif?raw=true&random=f2etyr2ry54bcyb9) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-local-hourglass/workflow.gif?raw=true&random=488gdj8ry1cahl8v)](https://github.com/kamangir/assets/blob/main/bluer_flow-local-hourglass/workflow.gif?raw=true&random=488gdj8ry1cahl8v) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-local-hourglass/workflow.gif?raw=true&random=488gdj8ry1cahl8v) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-local-map-reduce/workflow.gif?raw=true&random=v4ov0wlnf3nqxbgw)](https://github.com/kamangir/assets/blob/main/bluer_flow-local-map-reduce/workflow.gif?raw=true&random=v4ov0wlnf3nqxbgw) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-local-map-reduce/workflow.gif?raw=true&random=v4ov0wlnf3nqxbgw) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-local-map-reduce-large/workflow.gif?raw=true&random=1ulj3qclvjz0n16m)](https://github.com/kamangir/assets/blob/main/bluer_flow-local-map-reduce-large/workflow.gif?raw=true&random=1ulj3qclvjz0n16m) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-local-map-reduce-large/workflow.gif?raw=true&random=1ulj3qclvjz0n16m) |
| [localflow](./bluer_flow/workflow/runners/localflow/runner.py) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-a-bc-d/workflow.gif?raw=true&random=k3wvse275vhx4dil)](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-a-bc-d/workflow.gif?raw=true&random=k3wvse275vhx4dil) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-a-bc-d/workflow.gif?raw=true&random=k3wvse275vhx4dil) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-hourglass/workflow.gif?raw=true&random=u63w8pvk0ju8w3rz)](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-hourglass/workflow.gif?raw=true&random=u63w8pvk0ju8w3rz) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-hourglass/workflow.gif?raw=true&random=u63w8pvk0ju8w3rz) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-map-reduce/workflow.gif?raw=true&random=qsyd9izv5o62ia0a)](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-map-reduce/workflow.gif?raw=true&random=qsyd9izv5o62ia0a) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-map-reduce/workflow.gif?raw=true&random=qsyd9izv5o62ia0a) | [![image](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-map-reduce-large/workflow.gif?raw=true&random=0slfpnlx5dsq849l)](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-map-reduce-large/workflow.gif?raw=true&random=0slfpnlx5dsq849l) [🔗](https://github.com/kamangir/assets/blob/main/bluer_flow-localflow-map-reduce-large/workflow.gif?raw=true&random=0slfpnlx5dsq849l) |

💡 example use: [literature review using OpenAI API](https://github.com/kamangir/openai-commands/tree/main/openai_commands/literature_review).

# aliases

[localflow](./bluer_flow/docs/aliases/localflow.md), 
[workflow](./bluer_flow/docs/aliases/workflow.md).


---

> 🌀 [`blueflow`](https://github.com/kamangir/notebooks-and-scripts) for the [Global South](https://github.com/kamangir/bluer-south).

---


[![pylint](https://github.com/kamangir/bluer-flow/actions/workflows/pylint.yml/badge.svg)](https://github.com/kamangir/bluer-flow/actions/workflows/pylint.yml) [![pytest](https://github.com/kamangir/bluer-flow/actions/workflows/pytest.yml/badge.svg)](https://github.com/kamangir/bluer-flow/actions/workflows/pytest.yml) [![bashtest](https://github.com/kamangir/bluer-flow/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/bluer-flow/actions/workflows/bashtest.yml) [![PyPI version](https://img.shields.io/pypi/v/bluer-flow.svg)](https://pypi.org/project/bluer-flow/) [![PyPI - Downloads](https://img.shields.io/pypi/dd/bluer-flow)](https://pypistats.org/packages/bluer-flow)

built by 🌀 [`bluer README`](https://github.com/kamangir/bluer-objects/tree/main/bluer_objects/README), based on 📜 [`bluer_flow-5.58.1`](https://github.com/kamangir/bluer-flow).
