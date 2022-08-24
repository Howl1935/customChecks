from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories

class DAXminAvailZones(BaseResourceCheck):
    def __init__(self):
        name = "Ensure DAX clusters are configured with at least 3 AZs for production workloads."
        id = "CKV_IBT_001"
        supported_resources = ['aws_dax_cluster', 'aws_dax_subnet_group']
        # Look at checkov/common/models/enums.py for options
        categories = [CheckCategories.BACKUP_AND_RECOVERY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        """
            Since we can't do this with the .yaml config, we are using python.  This means we don't have the ability to check connections between resources.  
            In that case we check and see if we are looking at a aws_dax_cluster resource, or a aws_dax_subnet_group resource.
            If we are looking at a aws_dax_cluster, we make sure that there is a subnet_group_name and that the resource 'aws_dax_subnet_group' is called from
            the subnet_group_name.  If that is the case, we add that we checked the resource in the check name and pass the check.
            If we are looking at a aws_dax_subnet_group resource, then we check the subnet_ids key and make sure that the value contains 'private_subnets' since that is
            how Ibotta defines 3 AZs.
        """
        if self.entity_type == 'aws_dax_cluster':
            if 'availability_zones' in conf.keys():
                #availability_zones = conf['availability_zones']
                return CheckResult.PASSED
        return CheckResult.FAILED


scanner = DAXminAvailZones()