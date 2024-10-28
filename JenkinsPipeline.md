# Jenkins Scripted Pipelines
Below we will walk through the below Pipeline examples:

- [Approval Gates](PipelineApprovalGates.md)
- [Quality Gates](PipelineQualityGates.md)
- Matrix Deployments
- Ring deployments (deploying applications to all regions and all landing zones - in azure devops by stages)
- [Conditional logic](PipelineConditionalLogic.md)
- Testing automation
- Build artifacts (do they have a store or is it stored on disk)
- Secrets

## Set up
If your repo is a private repo then you will need to create a Personal Access token.

#### Create the PAT for Jenkins
If your repo is private then you will need to create a PAT so that Jenkins can manage your repo
    Settings > Developer Settings > Personal Access Tokens > Classic

Then assign the PAT the below permissions
 - repo

#### Create a Pipeline that will connect with your Source code repo in GitHub
Create a pipeline Job and under Configure > Pipeline set the below settings
- Definition: Pipeline script from SCM
- SCM: Git
- Repositories: https://github.com/claireelyse/jenkins.git
- Credentials:
-- Add Credentials > Jenkins
--- Username: git username
--- Password: PAT Value
- Script Path: pipeline.yml

In the repository create a pipeline.yml file. This will hold the pipeline definition for Jenkins and should follow the basic structure:
```Yml
pipeline {
    agent any

    stages {
        }
    }
```


Note: the .git files are hidden. if you want to set up vs code to show this folder then  follow the below notes. This is optional.
Set VS code so it shows the hidden git folders:
ctrl + Shift + P > Prefrences: Open Settings (JSON)

then add this to your settings profile
```Json
    "files.exclude": {
        "**/.git": false
     }
```