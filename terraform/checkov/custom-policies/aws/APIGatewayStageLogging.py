from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories

class APIGatewayStageLogging(BaseResourceCheck):
    def __init__(self):
        name = "Evaluate enabling logs for this API Gateway Production Stage"
        id = "CKV_IBT_010"
        supported_resources = ['aws_api_gateway_method_settings']
        # Look at checkov/common/models/enums.py for options
        categories = [CheckCategories.CONVENTION]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        """
 
        """
        if self.entity_type == 'aws_api_gateway_method_settings': 
            if 'settings' in conf.keys():  
                settings_block = conf['settings']
                if 'logging_level' in settings_block[0]:
                    logging_block = settings_block[0]['logging_level']
                    #self.name = logging_block[0]
                    if logging_block in [['OFF'], ['INFO'], ['ERROR'], ['var.log_level']]:
                        return CheckResult.PASSED
        

scanner = APIGatewayStageLogging()