from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories


class SFNLogging(BaseResourceCheck):
    def __init__(self):
        name = "Enable CloudWatch logging if needed for this step function."
        id = "CKV_IBT_009"
        supported_resources = ['aws_sfn_state_machine']
        # Look at checkov/common/models/enums.py for options
        categories = [CheckCategories.CONVENTION]
        super().__init__(name=name, id=id, categories=categories,
                         supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        """
This check examines a resource for the "logging_configuration" block.  It then checks if it contains "log_destination", 
"include_execution_data", and "level" attributes and that these attributes contain appropriate values.  One possible note 
to keep in mind is if this will work with a step function module.  I am having the same issue where it would be ideal to examine
 the created module’s input attributes and verify that a dev has input the correct values.
        """
        if self.entity_type == 'aws_sfn_state_machine':
            if 'logging_configuration' in conf.keys():
                logging_block = conf['logging_configuration'][0]
                if 'include_execution_data' in logging_block and logging_block['include_execution_data'][0]:
                    if 'level' in logging_block and logging_block['level'] in [["ALL"], ["ERROR"], ["FATAL"], ["OFF"]]:
                        if logging_block['level'][0] == 'OFF':
                            self.name = "Enable CloudWatch logging if needed for this step function: Please ensure logging is not set to \'OFF\'."
                            return CheckResult.FAILED
                        if 'log_destination' in logging_block:
                            return CheckResult.PASSED
                    self.name = "Please consider enabling Cloudwatch Logging for your state function and confirm that an appropriate \"level\" is set: https://docs.aws.amazon.com/step-functions/latest/dg/cw-logs.html and https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/sfn_state_machine#logging_configuration-configuration-block"
                    return CheckResult.FAILED
                self.name = logging_block['include_execution_data'][0] + " " + "Please consider enabling Cloudwatch Logging for your state function and confirm that logging_block attributes are correct: https://docs.aws.amazon.com/step-functions/latest/dg/cw-logs.html and https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/sfn_state_machine#logging_configuration-configuration-block"
                return CheckResult.FAILED
            self.name = "Please consider enabling Cloudwatch Logging for your state function: https://docs.aws.amazon.com/step-functions/latest/dg/cw-logs.html and https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/sfn_state_machine#logging_configuration-configuration-block"
            return CheckResult.FAILED


scanner = SFNLogging()
