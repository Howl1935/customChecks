# IBSCA-CLI Policies

This is the main repo where cloud infra at Ibotta will be able to manage policies and implementation for the SECURE branch of ibsca-cli

## /Config
In this folder you will find a config.yaml file.  This is our configuration for how checkov will run.  Instead of having our developers write extensive command line arguments they will use **ibsca perform** which will load our config.yaml and execute the functionality the cloud-infra team deems necessary.  

For more information visit this [link](https://bridgecrew.io/blog/checkov-config-file-repeatably-support-multiple-environments/).

## /Custom-Policies
In this folder we will store our custom configurations.  We have added /aws so that this structure can scale comfortably to other services.
 These custom configurations are called when a developer runs **ibsca perform**  It will first use the config.yaml from above and run against pre-written checkov checks and then run our custom policies. 
 
The policies are written in yaml and python.