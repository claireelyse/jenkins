# Quality Gates
For a quality gate we are going to set up a CodeQL action that is initiated by Jenkins. This is overly complicated but I want to test out how well Jenkins can work with external tools. 

Note: If the Repo is PRIVATE then you need to change your repo to be public if you want to use codeQL. 


### Add permissions to token for CodeQL access
If you want to use CodeQL as your quality gate then you will need to Create/add the below permissions to your token.
    Settings > Developer Settings > Personal Access Tokens > Classic

Then assign the PAT the below permissions
 - repo
 - workflow



### Set up your CodeQL action in GitHub

Create your CodeQL action file by creating the below directories and file:
.github/workflows/codeql-analysis.yml

Add the below code to your new file changing the secrets.JENKIS line to be the name of your token created above:

```YML
name: "CodeQL"

on:
    workflow_dispatch:  # This allows manual triggering via the API
#  push:
#    branches: [main]
#  pull_request:
#    branches: [main]

permissions:
  contents: read  # Required to checkout the repository to the Actions runner
  security-events: write # Required for Code Scanning with CodeQL

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
        with:
          token: ${{ secrets.JENKINS }}

      - name: Initialize CodeQL
        uses: github/codeql-action/init@v2
        with:
          languages: ${{ matrix.language }}

      - name: Perform CodeQL Analysis
        uses: github/codeql-action/analyze@v2
```

### Add code to jenkins pipeline to call CodeQL remotely
To get credential Id go to the Jenkins server Manage Jenkins > Credentials and grab the ID for the credential you used to authenticate the Pipeline if Private. If not go back to the step "Create a Pipeline that will connect with your Source code repo in GitHub".

After getting the Id put it in the "credentialsId" value in the job step below

```yml
stage('Trigger CodeQL in GitHub Action') {
            steps {
                script {
                    // Use the existing 'Username with password' credential
                    withCredentials([usernamePassword(credentialsId: '3777c30a-0948-46fe-9901-ed688e8ca8d6', usernameVariable: 'GITHUB_USER', passwordVariable: 'GITHUB_TOKEN')]) {
                        sh """
                        curl -X POST \
                        -H "Accept: application/vnd.github.v3+json" \
                        -H "Authorization: Bearer ${GITHUB_TOKEN}" \
                        https://api.github.com/repos/claireelyse/jenkins/actions/workflows/codeql-analysis.yml/dispatches \
                        -d '{"ref":"main"}'
                        """
                    }
                }
            }
        }
```
