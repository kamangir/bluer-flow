# workflow

```bash
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
