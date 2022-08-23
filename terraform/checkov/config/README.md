# IBSCA-CLI Config


## /Config
This is our configuration for how checkov will run.  Instead of having our developers write extensive command line arguments they will use **ibsca perform** which will load our config.yaml and execute the functionality the cloud-infra team deems necessary.  

For more information visit this [link](https://bridgecrew.io/blog/checkov-config-file-repeatably-support-multiple-environments/).

## Current Checks
To discover more checks visit [this link](https://www.checkov.io/5.Policy%20Index/terraform.html)
|                |Description                                                                        |
|----------------|-------------------------------|
|CKV_AWS_28|`Ensure Dynamodb point in time recovery (backup) is enabled`            			     |    
|CKV2_AWS_16|`Ensure that Auto Scaling is enabled on your DynamoDB tables`            			     |         
|CKV_AWS_66|`Ensure that CloudWatch Log Group specifies retention days`            			         |    
|CKV_AWS_228|`Verify Elasticsearch domain is using an up to date TLS policy`            			 |    
|CKV_AWS_250|`Ensure that RDS PostgreSQL instances use a non vulnerable version with the log_fdw extension (https://aws.amazon.com/security/security-bulletins/AWS-2022-004/)`            			                                             |    
|CKV_AWS_21|`Ensure all data stored in the S3 bucket have versioning enabled`            			 |    
|CKV_AWS_18|`Ensure the S3 bucket has access logging enabled`            			                 |    
## To Create a new config start here:

checkov -d . -c CKV_AWS_28,CKV2_AWS_16,CKV_AWS_66,CKV_AWS_228,CKV_AWS_250,CKV_AWS_16,CKV_AWS_21,CKV_AWS_18,CKV_AWS_96 --framework terraform terraform_plan --external-checks-dir ./customChecks/terraform/checkov/custom-policies/aws --download-external-modules DOWNLOAD_EXTERNAL_MODULES --quiet --create-config config.yml



## Helpful links
More information on checkov command line arguments[link] (https://www.checkov.io/2.Basics/CLI%20Command%20Reference.html)