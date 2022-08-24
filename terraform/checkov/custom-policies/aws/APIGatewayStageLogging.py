from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories

class APIGatewayStageLogging(BaseResourceCheck):
    def __init__(self):
        name = "Consider enabling execution logs for this API Gateway Production Stage.\nhttps://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/api_gateway_method_settings#logging_level"
        id = "CKV_IBT_010"
        supported_resources = ['aws_api_gateway_method_settings']
        # Look at checkov/common/models/enums.py for options
        categories = [CheckCategories.CONVENTION]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        """
        This checks and sees if execution logs are enabled for this API gateway which effects the log entries pushed to Amazon CloudWatch Logs.
        We will:
        Fail on OFF
        Pass but warn on INFO
        Pass on ERROR
        """
        if self.entity_type == 'aws_api_gateway_method_settings': 
            if 'settings' in conf.keys():  
                settings_block = conf['settings']
                if 'logging_level' in settings_block[0]:
                    logging_block = settings_block[0]['logging_level']
                    if logging_block in [['INFO']]:
                        self.name = "\"INFO\" for logs is sufficient, however \"ERROR\" might be more suitable for this API Gateway Production Stage."            
                        return CheckResult.PASSED
                    elif logging_block in [['ERROR']]:
                        self.name = "Consider enabling execution logs for this API Gateway Production Stage."  
                        return CheckResult.PASSED
                    else:
                        self.name = "logging_level must be \"INFO\" or \"ERROR\" your resource has specified " + logging_block + "\nhttps://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/api_gateway_method_settings#logging_level"
                        return CheckResult.FAILED
            return CheckResult.FAILED
        

scanner = APIGatewayStageLogging()