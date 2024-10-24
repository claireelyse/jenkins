# Jenkins Scripted Pipelines
Below we will walk through the below examples:

- How to do approval gates
- Quality gates
- Matrix Deployments
- Ring deployments (deploying applications to all regions and all landing zones - in azure devops by stages)
- Conditional logic
- Testing automation
- Build artifacts (do they have a store or is it stored on disk)
- Secrets

## Set up
If your repo is a private repo then you will need to create a Personal Access token.

#### Create the PAT
    Settings > Developer Settings > Personal Access Tokens > Classic

Then assign the PAT the below permissions
 - repo
 - workflow

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

## Quality Gates
For a quality gate we are going to set up a CodeQL action that is initiated by Jenkins. This is overly complicated but I want to test out how well Jenkins can work with external tools. 

#### Set up your CodeQL action in GitHub

Note: the .git files are hidden. if you want to set up vs code to show this folder then  follow the below notes. This is optional.
Set VS code so it shows the hidden git folders:
ctrl + Shift + P > Prefrences: Open Settings (JSON)

then add this to your settings profile
```Json
    "files.exclude": {
        "**/.git": false
     }
```

If the Repo is PRIVATE then you need to create a PAT

Create your CodeQL action file by creating the below directories and file:
.github/workflows/codeql-analysis.yml

Add the below code to your new file:

```YML
name: "CodeQL"

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  analyze:
    name: Analyze Code
    runs-on: ubuntu-latest
    strategy:
      matrix:
        language: ['javascript', 'python']  # Change to your project's language
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Initialize CodeQL
        uses: github/codeql-action/init@v2
        with:
          languages: ${{ matrix.language }}
          path: ['Code/**/*']

      - name: Perform CodeQL Analysis
        uses: github/codeql-action/analyze@v2
```
