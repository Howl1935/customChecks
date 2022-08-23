# IBSCA-CLI Policies

This is the [enablement subgroup](https://ibotta.atlassian.net/wiki/spaces/TT/pages/453738711/Enablement+Subgroup) at Ibotta's launching point for customizing configs, checks and policies run by IBSCA-CLI.


## Overview
When ibsca cli is run by a user or a process it will pull this repo locally and use the data to run customized checks against the code.  This means that following the specified folder structure is necessary for the tool to successfully run.

### Folder Structure
    ├── ...
    ├── language                  	 
    │   ├── plugin              	
    │   	├── config              
	│   		├── config.yml      
	│   		├── README.md       
    │   	├── custom-policies  
    │   	└── ...           
    │   └── ...                 
    └── ...


## /language/plugin/config
If a plugin supports a config, this is where it is found.  This is the one source of truth for what checks are run by all users of IBSCA cli.   Instead of having our developers write extensive command line arguments they can use **ibsca run** which will load our config and execute the predefined checks.

Please reference the terraform/checkov folder and this [link](https://bridgecrew.io/blog/checkov-config-file-repeatably-support-multiple-environments/) for a general idea of how this works using checkov as an example.

## /language/package/custom-policies
In this folder we will store our custom configurations if the plugin allows this feature.  
Using terraform/checkov as an example:  These custom configurations are called when a developer runs **ibsca run**  It will first run the config.yml found in /terraform/checkov/config.  If there are custom checks available to the plugin they will be stored in this folder.  As a reference please see checkov's [custom policies overview](https://www.checkov.io/2.Basics/CLI%20Command%20Reference.html#) for more information about writing custom policies.
 
The policies are written in yaml and python.

# Contributing to Repo
## Add a new language
1. Create a new folder with the language name.  Continue to [Add a new plugin](#add-a-new-plugin)
## Add a new plugin
1. Create a new folder within the language of your choice.  Name this folder the title of the plugin in lowercase letters.
2. Add two folders: `config` and `custom-policies`
3. Within the config folder add your `config file`.  Also add a `README.md` and document any customizations you implement.
4. Within the custom-policies add any `custom policies` your plugin supports.  Also add a `README.md` and document any customizations you implement.
5. Commit and push changes.


