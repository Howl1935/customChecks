
## /Custom-Policies
In this folder we will store our custom configurations.  We have added /aws so that this structure can scale comfortably to other services.
 These custom configurations are called when a developer runs **ibsca run**  It will first use the config.yaml from above and run against pre-written checkov checks and then run our custom policies. 
 
The policies are written in yaml and python.

## More Information
Here are a few helpful links for more information on writing custom policies.
1. [Custom Policies Blog](https://bridgecrew.io/blog/creating-and-sharing-custom-policies-as-code-with-checkov/)
2. [From the docs](https://www.checkov.io/3.Custom%20Policies/Examples.html)