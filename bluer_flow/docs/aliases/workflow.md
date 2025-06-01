# workflow

```bash
@flow \
	build_README \
	[push]
 . build @flow/README.md.
@flow \
	pypi \
	browse \
	[token]
 . browse pypi/@flow.
@flow \
	pypi \
	build \
	[browse,install,~rm_dist,~upload]
 . build pypi/@flow.
@pypi \
	install
 . install pypi.
@flow \
	pylint \
	[ignore=<ignore>] \
	[<args>]
 . pylint @flow.
@flow \
	pytest \
	[list,dryrun,~log,show_warning,~verbose] \
	[filename.py|filename.py::test]
 . pytest @flow.
@flow \
	test \
	[what=all|<test-name>,dryrun] \
	[dryrun]
 . test @flow.
@flow \
	test \
	list
 . list @flow tests.
localflow \
	eval \
	[type=<cpu|gpu>,verbose] \
	<command-line>
 . <command-line> -> localflow
localflow \
	list \
	[status=<status>]
 . list localflow jobs.
localflow \
	rm \
	[status=<status>]
 . rm localflow jobs.
localflow \
	start \
	[exit_if_no_job]
 . start localflow
localflow \
	stop
 . stop localflow
workflow \
	create \
	[pattern=<pattern>,~upload] \
	[.|<job-name>] \
	[--publish_as <public-object-name>]
 . create a <pattern> workflow.
   pattern: a-bc-d | hourglass | map-reduce | map-reduce-large
workflow \
	monitor \
	[~download,node=<node>,~upload] \
	[.|<job-name>] \
	[<command-line>]
 . monitor <job-name>/workflow and run <command-line>.
workflow \
	submit \
	[~download,dryrun,to=<runner>,~upload] \
	[.|<job-name>]
 . submit workflow.
   runner: generic | local | localflow
```
