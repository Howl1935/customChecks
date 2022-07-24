# IBSCA-CLI Policies

This is the main repo where cloud infra at Ibotta will be able to manage policies and implementation for IBSCA.

## /language/package/config
If package supports a config, this is where we will find it.  This is our configuration for the package will run.  Instead of having our developers write extensive command line arguments they can use **ibsca run** which will load our config and execute the functionality the cloud-infra team deems necessary.  

For more information visit this [link](https://bridgecrew.io/blog/checkov-config-file-repeatably-support-multiple-environments/).

## /language/package/custom-policies
In this folder we will store our custom configurations.  We have added /aws so that this structure can scale comfortably to other services.
 These custom configurations are called when a developer runs **ibsca run**  It will first use the config.yaml from above and run against pre-written checkov checks and then run our custom policies. 
 
The policies are written in yaml and python.