from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories


class APIGatewayLogging(BaseResourceCheck):
    def __init__(self):
        name = "Ensure RDS instances are configured for at least 3 AZs.  Also add at least one reader node for Aurora clusters."
        id = "CKV_IBT_010"
        supported_resources = ['aws_rds_cluster']
        # Look at checkov/common/models/enums.py for options
        categories = [CheckCategories.BACKUP_AND_RECOVERY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        """
            Ensure that RDS instances are configured with multi-az and add at least one reader node.
            To create a Multi-AZ RDS cluster, you must additionally specify the engine, storage_type, allocated_storage, iops and db_cluster_instance_class attributes.
            https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/rds_cluster
            https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html
        """
        if self.entity_type == 'aws_api_gateway_method_settings':
            if 'logging_level' in conf.keys():                
                log_level = conf["logging_level"]
                self.name = log_level
                return CheckResult.PASSED
            self.name = 'Ensure RDS instances are configured for Multi-AZ. See: https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/rds_cluster'
            return CheckResult.FAILED
scanner = APIGatewayLogging()