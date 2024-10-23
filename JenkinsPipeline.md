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
