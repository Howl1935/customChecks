from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories


class KinesisStreams(BaseResourceCheck):
    def __init__(self):
        name = "Evaluate Kinesis On-Demand Streams and if shards, and retention time are accurate for given workload.  Default is 2 shards and 24hr retention."
        id = "CKV_IBT_005"
        supported_resources = ['aws_kinesis_stream']
        # Look at checkov/common/models/enums.py for options
        categories = [CheckCategories.BACKUP_AND_RECOVERY]
        super().__init__(name=name, id=id, categories=categories,
                         supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        """
            For this recommendation, we found a substantial amount of kinesis streams deployed using 4 shards with 72 hour retention.
            This may be more than necessary for a given workload.  This check will confirm the amount with the developer.

            https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/kinesis_stream
        """
        if self.entity_type == 'aws_kinesis_stream':
            if 'shard_count' in conf.keys() and 'retention_period' in conf.keys():
                return CheckResult.PASSED
            return CheckResult.FAILED


scanner = KinesisStreams()
