# Jenkins

This set of documentation will walk you through the set up of the jenkins server all the way through learning advanced syntax for pipeline scripting. 

Index:
- [Jenkins Server Set Up](JenkinsSetUp.md)
- [Jenkins Pipeline Set Up](JenkinsPipeline.md)
- [Pipeline Approval Gates](PipelineApprovalGates.md)
- [Pipeline Quality Gates](PipelineQualityGates.md)
- Plugin Requirements for Jenkins(Terraform, Azure, Ansible, Packer, Artifactory, BitBucket, Docker, etc)
- Create a Jenkins Agent as a container
- Managed Identity auth



Azure DevOps Equivalents to manage pipeline execution, modification, access to Managed Identities, Approval Gates, Environments, etc.
    Reason: Want to insure that pipelines are governed, secured and dependable
    
    • Govern what pipeline(s) have access to what Azure Managed Identity or Service Principal Secret
    • Govern what Environments a pipeline can deploy too and provide mechanism for human or automated approval gates.
    • What is the process which Jenkins can use variables/tokens that are defined as "Design Time" vs. "Run Time"
    • What is Jenkins ability to create re-usable templates via "Shared Libraries"
    • How can required "Steps" be injected into a pipeline
How to run a pipeline that is triggered by a PR manually or from code in a different branch

