# WorkAutomation:
<hr>



## To Set Up:
`python setup.py` - run the setup.py file and this will guide you through the setup.

<hr>
<hr>


## To Run:

<hr>

### To Create a new project:
`Create.py --reponame <reponame> --branchname <branchname> --language <language>`
you can use these options or not - please note that you will always need the --reponame option

<hr>

### To update a project:
`Update.py --steps <steps> --custom <custom>`
`--custom <custom>` is for a custom commit message not just "Updates x.y" - If this is present then it will ignore the --steps argument


`--steps <steps>` is for the number in "Updates x.y"

if set to `small` then the steps will go from 1.0 -> 1.1

if set to `big` then the steps will go from 1.0 -> 2.0


## [TODO](TODO)