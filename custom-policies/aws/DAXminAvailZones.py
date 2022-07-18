from lark import Token

from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories


class DAXminAvailZones(BaseResourceCheck):
    def __init__(self):
        name = "Ensure DAX clusters are configured with at least 3 AZs for production workloads.!!!!!"
        id = "CKV_IBT_00231"
        supported_resources = ['aws_dax_cluster', 'aws_dax_subnet_group']
        # Look at checkov/common/models/enums.py for options
        categories = [CheckCategories.BACKUP_AND_RECOVERY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        """
            Looks for ACL configuration at aws_s3_bucket and Tag values:
            https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/dax_cluster
        :param conf: aws_s3_bucket configuration
        :return: <CheckResult>
        """
        if 'subnet_group_name' in conf.keys():
            subnet_block = conf['subnet_group_name'][0]
            if subnet_block == 'aws_dax_subnet_group.dax_subnet[0].id':
                if 'aws_dax_subnet_group' in conf.keys():
                    return CheckResult.FAILED
            return CheckResult.PASSED


scanner = DAXminAvailZones()